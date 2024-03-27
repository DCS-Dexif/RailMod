import hashlib
import json


# This function reads the hash information of mod files to check for duplicates
def compute_file_hash(file_path):
    """Compute the SHA-256 hash of a file's content."""
    sha256_hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    return sha256_hash.hexdigest()


# This function reads mod information from a JSON file to display on main window
def read_mod_info(mod_folder_path):
    mod_info_file_path = f"{mod_folder_path}/mod.json"
    try:
        with open(mod_info_file_path, 'r') as file:
            mod_info = json.load(file)
        return mod_info
    except FileNotFoundError:
        print(f"mod.json not found in {mod_folder_path}")
        return None
