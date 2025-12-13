```
pip install -r requirements.txt
# Install Pandoc via conda
conda install -c conda-forge pandoc -y
cd /workspaces/se-lib.org
python convert_to_mkdocs.py
python -m mkdocs build
python -m mkdocs serve

# if good
git add .
git commit -m "Complete Sphinx to MkDocs conversion"
git push
```

at main branch to pull in merge the updated branch
Click "Pull requests"
Click "New pull request"
Select dec_25 → main
Click "Create pull request"
Click "Merge pull request"


GitHub UI steps:

Go to your repo: github.com/madachy/se-lib.org
Click "Pull requests" tab
Click green "New pull request" button
Set: base: main ← compare: dec_25
Click "Create pull request"
Add title/description (optional)
Click "Create pull request" again
Click "Merge pull request"
Click "Confirm merge"
Done! Optionally delete dec_25 branch
