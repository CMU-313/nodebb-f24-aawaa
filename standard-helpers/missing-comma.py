
# sample error
errors = '''
/Users/owengometz/Desktop/CMU/Fall_2024/313/NodeBB Project/nodebb-f24-aawaa/public/src/modules/userFilter.js
  71:40  error  Missing trailing comma  comma-dangle

/Users/owengometz/Desktop/CMU/Fall_2024/313/NodeBB Project/nodebb-f24-aawaa/public/src/sockets.js
   23:31  error  Missing trailing comma  comma-dangle
   24:6   error  Missing trailing comma  comma-dangle
  172:26  error  Missing trailing comma  comma-dangle
  212:23  error  Missing trailing comma  comma-dangle
  239:12  error  Missing trailing comma  comma-dangle
  253:10  error  Missing trailing comma  comma-dangle

/Users/owengometz/Desktop/CMU/Fall_2024/313/NodeBB Project/nodebb-f24-aawaa/public/src/utils.common.js
   12:16  error  Missing trailing comma  comma-dangle
  272:17  error  Missing trailing comma  comma-dangle
  353:15  error  Missing trailing comma  comma-dangle
  399:31  error  Missing trailing comma  comma-dangle
  723:4   error  Missing trailing comma  comma-dangle

'''

import re
from pathlib import Path

file_pattern = re.compile(r'^(/Users[^\n]+)')
error_pattern = re.compile(r'^\s+(\d+):\d+\s+error\s+Missing trailing comma')

files_with_errors = {}
current_file = None

for line in errors.splitlines():
    file_match = file_pattern.match(line)
    error_match = error_pattern.match(line)
    
    if file_match:
        current_file = Path(file_match.group(1))
        files_with_errors[current_file] = []
    elif error_match and current_file:
        line_number = int(error_match.group(1)) - 1
        files_with_errors[current_file].append(line_number)

for file_path, line_numbers in files_with_errors.items():
    if file_path.is_file():
        with file_path.open('r') as file:
            content = file.readlines()
        
        for line_number in line_numbers:
            line = content[line_number]
            if line.rstrip() and not line.rstrip().endswith(','):
                content[line_number] = line.rstrip() + ',\n'
        
        with file_path.open('w') as file:
            file.writelines(content)

print("Script finished processing files.")
