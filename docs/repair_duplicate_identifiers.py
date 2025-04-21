import json
import os


# This file is needed due to sphinx-ext-mystmd writing duplicate identifiers
# it traverses all .myst.json files in the specified folders
# and removes the identifier field if an equal label field is present
def remove_duplicate_identifier(filepath: str) -> None:
    with open(filepath, encoding="utf-8") as f:
        data = json.load(f)

    def process(obj: object) -> None:
        if isinstance(obj, dict):
            if "identifier" in obj and obj["identifier"] == obj.get("label"):
                del obj["identifier"]
            for v in obj.values():
                process(v)
        elif isinstance(obj, list):
            for item in obj:
                process(item)

    process(data)

    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def traverse_and_remove_dupe_ids(root_dirs: list) -> None:
    for root_dir in root_dirs:
        for dirpath, _, filenames in os.walk(root_dir):
            for filename in filenames:
                if filename.endswith(".myst.json"):
                    filepath = os.path.join(dirpath, filename)
                    remove_duplicate_identifier(filepath)


if __name__ == "__main__":
    # Define the folders to process
    folders = ["api/myst", "routing-api/myst"]
    traverse_and_remove_dupe_ids(folders)
    print("duplicate Identifiers removed.")
