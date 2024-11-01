
errors = '''
  /Users/owengometz/Desktop/CMU/Fall_2024/313/NodeBB Project/nodebb-f24-aawaa/public/src/modules/uploadHelpers.js:46:53: 'utils' is not defined. (no-undef)
  /Users/owengometz/Desktop/CMU/Fall_2024/313/NodeBB Project/nodebb-f24-aawaa/public/src/modules/uploadHelpers.js:46:72: '$' is not defined. (no-undef)
  /Users/owengometz/Desktop/CMU/Fall_2024/313/NodeBB Project/nodebb-f24-aawaa/public/src/modules/uploadHelpers.js:108:5: '$' is not defined. (no-undef)
  /Users/owengometz/Desktop/CMU/Fall_2024/313/NodeBB Project/nodebb-f24-aawaa/public/src/modules/uploadHelpers.js:135:28: 'utils' is not defined. (no-undef)
  /Users/owengometz/Desktop/CMU/Fall_2024/313/NodeBB Project/nodebb-f24-aawaa/public/src/modules/uploadHelpers.js:159:24: 'app' is not defined. (no-undef)
'''

from pathlib import Path
import re

# Regular expression to match lines with no-undef errors in the public directory
pattern = re.compile(r'\s*(/Users/owengometz/Desktop/CMU/Fall_2024/313/NodeBB Project/nodebb-f24-aawaa/public/[^:]+):\d+:\d+: \'([^\'\s]+)\' is not defined\. \(no-undef\)')

# Dictionary to store undefined variables for each file
file_undefined_vars = {}

# Iterate over each line in the errors string
for line in errors.splitlines():
    match = pattern.match(line)
    if match:
        print("hello")
        file_path_str = match.group(1)  # Extract file path
        undefined_var = match.group(2)  # Extract undefined variable

        # Initialize a set for undefined variables if this is the first time we encounter the file
        if file_path_str not in file_undefined_vars:
            file_undefined_vars[file_path_str] = set()

        # Add the undefined variable to the set if not already present
        file_undefined_vars[file_path_str].add(undefined_var)

# Add the global definitions to each file based on the collected undefined variables
for file_path_str, undefined_vars in file_undefined_vars.items():
    file_path = Path(file_path_str)
    
    # Check if file exists
    if file_path.is_file():
        # Read the current file content
        with file_path.open('r') as file:
            content = file.readlines()

        # Create the `/* global ... */` line with all undefined variables
        global_line = f"/* global {', '.join(undefined_vars)} */\n"

        # Insert the global line at the top if it's not already present
        if global_line not in content:
            content.insert(0, global_line)  # Add at the top

            # Write the updated content back to the file
            with file_path.open('w') as file:
                file.writelines(content)

print("Script finished processing files.")

