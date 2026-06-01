from pathlib import Path

folder = Path("pyfolder")
folder.mkdir(exist_ok=True)

print(f"Folder '{folder}' is ready.")