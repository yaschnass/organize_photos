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
python3 photo_organizer.py
```

## Functions

- **`make_place_directories(places)`**: Creates directories for each unique place.
- **`extract_place(filename)`**: Extracts the place from the filename by splitting it at underscores.
- **`organize_photos(directory)`**: Organizes photos in the specified directory by moving them into folders based on the extracted place.

## Notes

- Ensure that filenames follow the expected format: `prefix_place_suffix.ext`.
- This script will overwrite files in directories if files with the same name exist.

