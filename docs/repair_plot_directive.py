import os

# This file is needed due to an incompatibility between
# matplotlib.sphinxext.plot_directive and sphinx-ext-mystmd
# it replaces all instances of the dynamic file extension matching
# .* with hardcoded .png file endings (compatible with mystmd)
# further it modifies the path to not include the top level "myst" folder


def replace_in_file(filepath: str, search_replace_pairs: list) -> None:
    with open(filepath, encoding="utf-8") as file:
        content = file.read()
    original_content = content
    for search, replace in search_replace_pairs:
        content = content.replace(search, replace)
    if content != original_content:
        with open(filepath, "w", encoding="utf-8") as file:
            file.write(content)


def traverse_and_replace(root_dirs: list, search_replace_pairs: list) -> None:
    for root_dir in root_dirs:
        for dirpath, _, filenames in os.walk(root_dir):
            for filename in filenames:
                if filename.endswith(".myst.json"):
                    filepath = os.path.join(dirpath, filename)
                    replace_in_file(filepath, search_replace_pairs)


if __name__ == "__main__":
    # Define the folders to process
    folders = ["api/myst", "routing-api/myst"]
    # Define the search and replace pairs
    search_replace_pairs = [(".*", ".png"), ("myst/plot", "plot")]
    traverse_and_replace(folders, search_replace_pairs)
    print("Replacement completed.")
