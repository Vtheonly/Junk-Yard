import os
import pyperclip
input_file  = r"C:\Users\merse\OneDrive\Documents\Projects\Junk Yard\Get trasncribtions\subtitles.txt"
output_file = r"C:\Users\merse\OneDrive\Documents\Projects\Junk Yard\Get trasncribtions\output.txt"


def getPureText(mode="site"):
    if not os.path.exists(input_file):
        print(f"The file {input_file} does not exist.")
    else:
        with open(input_file, 'r') as infile:
            lines = infile.readlines()
            start_index = 0 
            end_index = len(lines)  
            big_text=""
            if(mode=="site"):
                for i in range(start_index, end_index):
                    lines[i] = lines[i][12:].strip()  # Trim the first 12 characters
            elif(mode=="js"):
                for i in range(start_index, end_index):
                    big_text+= str(lines[i])[0:-1]+" " if i%2==0 else "" # delete the the /n
                
                lines.clear()
                lines.append(big_text)        

        with open(output_file, 'w') as outfile:
            outfile.writelines(" ".join(lines))

        print("File has been updated and saved to output.txt")

        with open(output_file, 'r') as outfile:
            output_content = outfile.read()

        pyperclip.copy(output_content)
        print("Contents of output.txt have been copied to the clipboard.")
        

# getPureText(mode="js")
# getPureText(mode="site")