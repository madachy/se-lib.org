#!/usr/bin/env python3
"""
Sphinx to MkDocs Conversion Script for se-lib.org
Converts RST files to Markdown and sets up MkDocs structure
"""
import os
import re
import shutil
import subprocess
from pathlib import Path


class SphinxToMkDocsConverter:
    def __init__(self, source_dir='source', docs_dir='docs'):
        self.source_dir = Path(source_dir)
        self.docs_dir = Path(docs_dir)
        
    def convert_all(self):
        """Run all conversion steps"""
        print("=" * 60)
        print("Sphinx to MkDocs Conversion for se-lib.org")
        print("=" * 60)
        
        self.setup_structure()
        self.convert_rst_files()
        self.copy_assets()
        self.fix_links()
        self.fix_image_paths()
        self.create_mkdocs_yml()
        
        print("\n" + "=" * 60)
        print("Conversion Complete!")
        print("=" * 60)
        print("\nNext steps:")
        print("1. Review converted files in docs/")
        print("2. Test with: mkdocs serve")
        print("3. Build with: mkdocs build")
        print("4. Deploy with: mkdocs gh-deploy")
    
    def setup_structure(self):
        """Create MkDocs directory structure"""
        print("\n1. Setting up directory structure...")
        
        directories = [
            self.docs_dir,
            self.docs_dir / 'online',
            self.docs_dir / 'tutorials',
            self.docs_dir / 'about',
            self.docs_dir / 'assets',
        ]
        
        for directory in directories:
            directory.mkdir(parents=True, exist_ok=True)
            print(f"   Created: {directory}")
    
    def convert_rst_files(self):
        """Convert RST files to Markdown using pandoc"""
        print("\n2. Converting RST files to Markdown...")
        
        # Check if pandoc is installed
        try:
            subprocess.run(['pandoc', '--version'], 
                         capture_output=True, check=True)
        except (subprocess.CalledProcessError, FileNotFoundError):
            print("   WARNING: pandoc not found. Install with:")
            print("   - macOS: brew install pandoc")
            print("   - Ubuntu: sudo apt install pandoc")
            print("   - Windows: choco install pandoc")
            print("   Skipping RST conversion...")
            return
        
        if not self.source_dir.exists():
            print(f"   WARNING: Source directory '{self.source_dir}' not found")
            return
        
        rst_files = list(self.source_dir.glob('**/*.rst'))
        
        for rst_file in rst_files:
            rel_path = rst_file.relative_to(self.source_dir)
            md_file = self.docs_dir / rel_path.with_suffix('.md')
            
            md_file.parent.mkdir(parents=True, exist_ok=True)
            
            try:
                subprocess.run([
                    'pandoc',
                    str(rst_file),
                    '-f', 'rst',
                    '-t', 'markdown',
                    '--wrap=none',  # Don't wrap lines
                    '-o', str(md_file)
                ], check=True)
                print(f"   Converted: {rst_file.name} -> {md_file.name}")
            except subprocess.CalledProcessError as e:
                print(f"   ERROR converting {rst_file}: {e}")
    
    def copy_assets(self):
        """Copy images and static files"""
        print("\n3. Copying assets...")
        
        # Copy images
        source_images = self.source_dir / '_images'
        if source_images.exists():
            dest_assets = self.docs_dir / 'assets'
            dest_assets.mkdir(exist_ok=True)
            
            for image in source_images.glob('*'):
                if image.is_file():
                    shutil.copy2(image, dest_assets / image.name)
                    print(f"   Copied: {image.name}")
        
        # Copy static files
        source_static = self.source_dir / '_static'
        if source_static.exists():
            dest_assets = self.docs_dir / 'assets'
            for static_file in source_static.glob('*'):
                if static_file.is_file():
                    shutil.copy2(static_file, dest_assets / static_file.name)
                    print(f"   Copied: {static_file.name}")
    
    def fix_links(self):
        """Fix internal links from RST to MD format"""
        print("\n4. Fixing internal links...")
        
        for md_file in self.docs_dir.glob('**/*.md'):
            content = md_file.read_text(encoding='utf-8')
            original = content
            
            # Fix .rst links to .md
            content = re.sub(r'\]\(([^)]+)\.rst\)', r'](\1.md)', content)
            
            # Fix Sphinx :doc: references
            content = re.sub(r':doc:`([^`]+)`', r'[\1](\1.md)', content)
            
            # Fix :ref: references (convert to simple links)
            content = re.sub(r':ref:`([^`]+)`', r'[\1](#\1)', content)
            
            # Fix relative paths for links
            content = re.sub(r'\]\(\.\.\/([^)]+)\)', r'](\1)', content)
            
            if content != original:
                md_file.write_text(content, encoding='utf-8')
                print(f"   Fixed links in: {md_file.name}")
    
    def fix_image_paths(self):
        """Update image paths to use assets/ directory"""
        print("\n5. Fixing image paths...")
        
        for md_file in self.docs_dir.glob('**/*.md'):
            content = md_file.read_text(encoding='utf-8')
            original = content
            
            # Calculate relative path to assets from this file
            depth = len(md_file.relative_to(self.docs_dir).parts) - 1
            prefix = '../' * depth if depth > 0 else ''
            
            # Fix image paths
            content = re.sub(r'!\[(.*?)\]\(_images/([^)]+)\)', 
                           rf'![\1]({prefix}assets/\2)', content)
            content = re.sub(r'!\[(.*?)\]\(\.\./\_images/([^)]+)\)', 
                           rf'![\1]({prefix}assets/\2)', content)
            
            # Fix HTML img tags
            content = re.sub(r'<img src="_images/([^"]+)"', 
                           rf'<img src="{prefix}assets/\1"', content)
            
            if content != original:
                md_file.write_text(content, encoding='utf-8')
                print(f"   Fixed images in: {md_file.name}")
    
    def create_mkdocs_yml(self):
        """Create mkdocs.yml configuration file"""
        print("\n6. Creating mkdocs.yml...")
        
        config = """site_name: Systems Engineering Library (se-lib)
site_url: http://se-lib.org
site_description: Open source Python library for integrated systems modeling
site_author: se-lib Development Team

repo_url: https://github.com/se-lib/se-lib
repo_name: se-lib/se-lib

theme:
  name: material
  palette:
    - media: "(prefers-color-scheme: light)"
      scheme: default
      primary: indigo
      accent: indigo
      toggle:
        icon: material/brightness-7
        name: Switch to dark mode
    - media: "(prefers-color-scheme: dark)"
      scheme: slate
      primary: indigo
      accent: indigo
      toggle:
        icon: material/brightness-4
        name: Switch to light mode
  features:
    - navigation.tabs
    - navigation.sections
    - navigation.top
    - navigation.footer
    - search.suggest
    - search.highlight
    - content.code.copy
    - content.tabs.link

plugins:
  - search

markdown_extensions:
  - admonition
  - pymdownx.details
  - pymdownx.superfences
  - pymdownx.highlight:
      anchor_linenums: true
  - pymdownx.inlinehilite
  - pymdownx.snippets
  - attr_list
  - md_in_html
  - toc:
      permalink: true
  - tables

nav:
  - Home: index.md
  - Installation: installation.md
  - Function Reference: function_reference.md
  - Examples: examples.md
  - Playground:
      - SysML Scratchpad: online/scratchpad.md
      - Discrete Event Demo: online/discrete_event_modeling_demo.md
      - Playground: online/sysml.md
  - Tutorials:
      - System Dynamics: tutorials/sd_incose.md

copyright: Copyright &copy; 2025 se-lib Development Team
"""
        
        with open('mkdocs.yml', 'w') as f:
            f.write(config)
        
        print("   Created mkdocs.yml")


def main():
    converter = SphinxToMkDocsConverter()
    converter.convert_all()
    
    print("\n" + "=" * 60)
    print("IMPORTANT: Manual Review Needed")
    print("=" * 60)
    print("""
After running this script, please review:

1. Code blocks - ensure proper language tags
2. Tables - verify Markdown table formatting
3. Special directives - convert custom Sphinx directives manually
4. Math equations - add MathJax if needed
5. Cross-references - verify all internal links work

Test your site:
    mkdocs serve

Build for production:
    mkdocs build

Deploy to GitHub Pages:
    mkdocs gh-deploy
""")


if __name__ == '__main__':
    main()
