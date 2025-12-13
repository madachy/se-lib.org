```
pip install -r requirements.txt
# Install Pandoc via conda
conda install -c conda-forge pandoc -y
cd /workspaces/se-lib.org
python convert_to_mkdocs.py
python -m mkdocs build
python -m mkdocs serve
```
