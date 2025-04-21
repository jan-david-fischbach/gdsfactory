import json
import os


# This file is needed due to sphinx-ext-mystmd writing code blocks without language specification
# it traverses all .myst.json files in the specified folders
# and puts a "lang": "python" specification in all "code" blocks that do not have a specified language
def add_lang(filepath: str) -> None:
    with open(filepath, encoding="utf-8") as f:
        data = json.load(f)

    def process(obj: object) -> None:
        if isinstance(obj, dict):
            if obj.get("type") == "code" and "lang" not in obj:
                obj["lang"] = "python"
            for v in obj.values():
                process(v)
        elif isinstance(obj, list):
            for item in obj:
                process(item)

    process(data)

    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def traverse_and_add_lang(root_dirs: list) -> None:
    for root_dir in root_dirs:
        for dirpath, _, filenames in os.walk(root_dir):
            for filename in filenames:
                if filename.endswith(".myst.json"):
                    filepath = os.path.join(dirpath, filename)
                    add_lang(filepath)


if __name__ == "__main__":
    # Define the folders to process
    folders = ["api/myst", "routing-api/myst"]
    traverse_and_add_lang(folders)
    print("Replacement completed.")
