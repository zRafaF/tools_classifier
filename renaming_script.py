import os
import re

# Directory where your images are stored
directory = "unprocessed_data_set/cropped"

# Regular expression pattern to match the filenames
pattern = re.compile(r"^(\d+)-(\d+)-(V\d+)-(W|B)\.png$")

# Iterate over all files in the directory
for filename in os.listdir(directory):
    # Match the filename against the pattern
    match = pattern.match(filename)
    if match:
        # Extract parts of the filename
        first_number = match.group(1)
        version = match.group(3)
        color = match.group(4)

        # Construct new filename with second number as '01'
        new_filename = f"{first_number}-01-{version}-{color}.png"

        # Full paths to the old and new files
        old_file = os.path.join(directory, filename)
        new_file = os.path.join(directory, new_filename)

        # Rename the file
        os.rename(old_file, new_file)
        print(f"Renamed '{filename}' to '{new_filename}'")
