
import re
from pathlib import Path

# Multi-line string holding all errors
errors = '''
/Users/owengometz/Desktop/CMU/Fall_2024/313/NodeBB Project/nodebb-f24-aawaa/Gruntfile.js:57:11: Identifier 'styleUpdated_Client' is not in camel case. (camelcase)
/Users/owengometz/Desktop/CMU/Fall_2024/313/NodeBB Project/nodebb-f24-aawaa/test/utils.js:471:3: 'it' is not defined. (no-undef)
/Users/owengometz/Desktop/CMU/Fall_2024/313/NodeBB Project/nodebb-f24-aawaa/test/user.js:1280:5: 'it' is not defined. (no-undef)
/Users/owengometz/Desktop/CMU/Fall_2024/313/NodeBB Project/nodebb-f24-aawaa/test/user/uploads.js:150:5: 'it' is not defined. (no-undef)
/Users/owengometz/Desktop/CMU/Fall_2024/313/NodeBB Project/nodebb-f24-aawaa/test/uploads.js:426:7: 'it' is not defined. (no-undef)
...
'''

# Define the line to add if conditions are met
line_to_add = '/* eslint-env mocha */\n'

# Loop over each line of the errors string
for match in re.finditer(r'(/Users/owengometz/Desktop/CMU/Fall_2024/313/NodeBB Project/nodebb-f24-aawaa/test/[^:]+):\d+:\d+: .* \(no-undef\)', errors):
    file_path = Path(match.group(1))

    # Check if file exists
    if file_path.is_file():
        # Read the current file content
        with file_path.open('r') as file:
            content = file.readlines()

        # Locate 'use strict' and check if '/* eslint-env mocha */' is already present
        for i, line in enumerate(content):
            if 'use strict' in line:
                if line_to_add not in content:
                    content.insert(i + 1, line_to_add)  # Insert after 'use strict'
                break

        # Write the updated content back to the file if modified
        with file_path.open('w') as file:
            file.writelines(content)

print("Script finished processing files.")