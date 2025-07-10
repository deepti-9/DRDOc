import os

EXCLUDED_DIRS = {'venv', '__pycache__', '.git', '.idea', '.mypy_cache', '.vscode', '.pytest_cache'}
MAX_DEPTH = 4

def print_tree(path, prefix='', depth=0):
    if depth > MAX_DEPTH:
        return

    try:
        items = sorted(os.listdir(path))
    except PermissionError:
        return

    items = [item for item in items if item not in EXCLUDED_DIRS]

    for index, item in enumerate(items):
        full_path = os.path.join(path, item)
        is_last = index == len(items) - 1
        connector = '└── ' if is_last else '├── '

        print(f"{prefix}{connector}{item}")

        if os.path.isdir(full_path):
            extension = '    ' if is_last else '│   '
            print_tree(full_path, prefix + extension, depth + 1)

# Run the function
print(".")
print_tree(".")


