from pathlib import Path
root = Path().cwd()/"images"
from jmd_imagescraper.core import * # dont't worry, it's designed to work with import *
duckduckgo_search(root, "Lorem Ipsum", "Lorem Ipsum", max_results=100)
