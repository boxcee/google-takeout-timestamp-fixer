import os
import json
import sys
from datetime import datetime, timezone


def modify_file_timestamp(json_file, photo_file):
    # Load the JSON data from the file
    with open(json_file, "r") as f:
        data = json.load(f)

    # Extract the photoTakenTime (Unix timestamp)
    photo_taken_timestamp = int(data["photoTakenTime"]["timestamp"])

    # Convert the Unix timestamp to a tuple for os.utime()
    timestamp = datetime.fromtimestamp(photo_taken_timestamp, timezone.utc).timetuple()

    # Set the file's last modified and access time to the new timestamp
    os.utime(photo_file, (photo_taken_timestamp, photo_taken_timestamp))

    print(
        f"Modified {photo_file} to the timestamp {datetime.fromtimestamp(photo_taken_timestamp, timezone.utc)}"
    )


def process_directory(directory):
    # Loop through all files in the directory
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        
        # Recursively process subdirectories
        if os.path.isdir(file_path):
            process_directory(file_path)
        
        # If the file is a JSON file
        elif filename.endswith(".json"):
            json_file_path = file_path

            # Load the JSON data and get the corresponding photo/video file title
            with open(json_file_path, "r") as f:
                data = json.load(f)
                title = data.get("title")

                if title:
                    # Find the corresponding photo/video file in the directory
                    photo_file_path = os.path.join(directory, title)

                    # Check if the photo/video file exists
                    if os.path.exists(photo_file_path):
                        # Modify the timestamp of the corresponding file
                        modify_file_timestamp(json_file_path, photo_file_path)
                    else:
                        print(
                            f"Warning: The file {title} does not exist in the directory."
                        )
                else:
                    print(f"Warning: No 'title' found in JSON file {filename}.")


if __name__ == "__main__":
    # Use provided directory path or default to current directory
    directory_path = sys.argv[1] if len(sys.argv) > 1 else os.getcwd()
    
    # Validate that the directory exists
    if not os.path.isdir(directory_path):
        print(f"Error: Directory '{directory_path}' does not exist.")
        sys.exit(1)
    
    print(f"Processing directory: {directory_path}")
    process_directory(directory_path)
    print("Done!")
