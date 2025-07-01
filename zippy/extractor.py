# zippy/extractor.py
from unrar import rarfile

def list_contents(archive_path):
    return rarfile.RarFile(archive_path).namelist()

def extract(archive_path, out_dir):
    with rarfile.RarFile(archive_path) as rf:
        rf.extractall(path=out_dir)
