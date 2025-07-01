from unrar import rarfile

def list_contents(archive_path):
    return rarfile.RarFile(archive_path).namelist()
