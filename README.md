# Google Takeout Timestamp Fixer

## Overview

If you've ever used Google Takeout to download your photos and videos, you may have noticed that the original photo/video files are separated from the accompanying metadata (in JSON format). This script helps you automatically update the **creation timestamp** of your photos and videos with the correct time from the associated JSON file.

### Problem:

- Google Takeout separates photos/videos and their metadata (JSON files).
- The file metadata includes the actual **"photo taken time"**, but this information isn't reflected in the file's timestamp.

### Solution:

This script will:

- Read the JSON file.
- Extract the correct **photo taken time** from the metadata.
- Update the **file's last modified and access time** with that timestamp.

This is especially useful for users who want to keep their photos and videos organized by date but are unable to easily do so after extracting files from Google Takeout.

---

## How to Use:

### Prerequisites:

- **Python** must be installed on your system. You can download it from [python.org](https://www.python.org/downloads/).
- Basic knowledge of using the command line.

### Steps:

1. Download the `google-takeout-timestamp-fixer` repository.
2. Extract your Google Takeout folder. Ensure it contains the .json files and their corresponding photo/video files organized together.
3. Open a command prompt or terminal.
4. Navigate to the folder where the script is located.
5. Run the script with one of the following commands:

**Option A: Process the current directory (default)**
```bash
python google_takeout_timestamp_fixer.py
```

**Option B: Process a specific directory**
```bash
python google_takeout_timestamp_fixer.py /path/to/Google/Takeout
```

Example:
```bash
python google_takeout_timestamp_fixer.py "/Users/YourName/Downloads/Takeout/Google Photos"
```

The script will:
- Process all .json files in the specified directory and its subdirectories (recursive)
- Extract the "photo taken time" from each JSON file
- Update the corresponding photo/video file with the correct timestamp

### Additional Information:

- The script uses **recursive processing**, so it will look for .json files in the specified directory and all subdirectories.
- The script looks for .json files and their associated photo/video files (same name, with extensions like .jpg, .mp4, etc.).
- The photoTakenTime in the JSON file is used to update the file's last modified and access timestamp.
- If no directory is specified, the script defaults to the current working directory.

### Troubleshooting:

- Ensure your Google Takeout files are organized with .json files and their corresponding media files in the same directory.
- If you encounter any issues with file paths, double-check that the path you're providing is correct and that the directory exists.
- If a media file is not found for a JSON metadata file, the script will display a warning but continue processing other files.

### License:

This project is licensed under the MIT License - see the LICENSE file for details.
