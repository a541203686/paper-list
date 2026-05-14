import sys
import os

# Add project root to path
sys.path.append(os.getcwd())

from utils.json_tools import json_to_md

json_file = './docs/data'
md_file = 'README.md'
show_badge = True

if os.path.exists(json_file):
    json_to_md(json_file, 'README_EN.md', task='Update Readme EN', show_badge=show_badge, split_to_docs=True, lang='en')
    json_to_md(json_file, 'README.md', task='Update Readme ZH', show_badge=show_badge, split_to_docs=True, lang='zh')
    print("Regenerated README.md, README_EN.md and split docs.")
else:
    print(f"Error: {json_file} not found.")
