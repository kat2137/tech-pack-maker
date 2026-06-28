import os
import re

DATA_DIR = './data'

# Set to False to actually rename. While True, the script only prints
# what it *would* do so you can review before committing.
DRY_RUN = False

# Screenshots in data/ are garment flats too, so include them in the sequence.
SKIP_SCREENSHOTS = False

IMAGE_EXTS = {'.jpg', '.jpeg', '.png', '.webp'}

# Files already following the convention, e.g. image_42.jpg or image100.jpg
LABELED_PATTERN = re.compile(r'^image_?\d+\.', re.IGNORECASE)
# Captures the numeric index of an already-labeled file
INDEX_PATTERN = re.compile(r'^image_?(\d+)\.', re.IGNORECASE)


def get_file_extension(file_name) -> str:
    return os.path.splitext(file_name)[1]


def is_image(file_name) -> bool:
    return get_file_extension(file_name).lower() in IMAGE_EXTS


def current_max_index(files) -> int:
    """Highest N among files already named image_<N>.<ext>."""
    max_idx = 0
    for f in files:
        match = INDEX_PATTERN.match(f)
        if match:
            max_idx = max(max_idx, int(match.group(1)))
    return max_idx


def rename_image(source_path, new_path):
    os.rename(source_path, new_path)


def main():
    files = sorted(os.listdir(DATA_DIR))
    next_index = current_max_index(files) + 1

    to_rename = [
        f for f in files
        if is_image(f)
        and not LABELED_PATTERN.match(f)
        and not (SKIP_SCREENSHOTS and f.lower().startswith('screenshot'))
    ]

    if not to_rename:
        print('Nothing to rename.')
        return

    for f in to_rename:
        ext = get_file_extension(f)
        old_path = os.path.join(DATA_DIR, f)
        new_name = f'image_{next_index}{ext}'
        new_path = os.path.join(DATA_DIR, new_name)
        print(f'{"[dry-run] " if DRY_RUN else ""}{f}  ->  {new_name}')
        if not DRY_RUN:
            rename_image(old_path, new_path)
        next_index += 1

    print(f'\n{len(to_rename)} file(s) {"to rename" if DRY_RUN else "renamed"}, '
          f'starting at image_{current_max_index(files) + 1}.')


if __name__ == '__main__':
    main()
