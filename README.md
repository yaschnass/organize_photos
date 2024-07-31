### `README.md`

```markdown
# Photo Organizer

This Python script organizes photos into directories based on their filenames. It assumes that filenames are formatted in a specific way where the place is indicated as the second part of the filename when split by an underscore (`_`).

## Features

- Creates directories for each unique place extracted from filenames.
- Moves files into their corresponding directories based on the extracted place.

## Usage

1. Ensure you have Python 3 installed.
2. Update the `organize_photos` function call with the path to your photos directory.

### Example

Update the path in the `__main__` section:

```python
if __name__ == "__main__":
    organize_photos("path_to_your_photos_directory")
```

Run the script:

```bash
python3 org_photos.py
```

## Functions

- **`make_place_directories(places)`**: Creates directories for each unique place.
- **`extract_place(filename)`**: Extracts the place from the filename by splitting it at underscores.
- **`organize_photos(directory)`**: Organizes photos in the specified directory by moving them into folders based on the extracted place.

## Unittest

- Unittest-file in the tests folder.

### Example


Update the `test_filename` and `folder` in `test_org_photos.py`:

```python
test_file_1 = "2018-01-03_Scotland_21_51_57.jpg"
folder_1 = "Scotland"
```

Run the script:

```bash
pytest test_org_photos.py
```
## Notes

- Ensure that filenames follow the expected format: `prefix_place_suffix.ext`.
- This script will overwrite files in directories if files with the same name exist.
  
