import os
import pyperclip

input_file = r"subtitles.txt"
output_file = r"output.txt"

if not os.path.exists(input_file):
    print(f"The file {input_file} does not exist.")
else:
    with open(input_file, 'r') as infile:
        lines = infile.readlines()
        
        start_index = 0 
        end_index = len(lines)  

        # Modify lines in memory
        for i in range(start_index, end_index):
            lines[i] = lines[i][12:].strip()  # Trim the first 12 characters
            # print(lines[i])
    
    with open(output_file, 'w') as outfile:
        outfile.writelines(lines)
    
    print("File has been updated and saved to output.txt.")

    # Read the contents of output.txt to copy to clipboard
    with open(output_file, 'r') as outfile:
        output_content = outfile.read()
    
    # Copy to clipboard
    pyperclip.copy(output_content)
    print("Contents of output.txt have been copied to the clipboard.")

print("done")