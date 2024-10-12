def print_in_green(text,clean=0):
    green_text = f"\033[92m{text}\033[0m"
    
    if (clean==0):
        print(green_text)
    if (clean!=0):
        return(green_text)

def printnlist(list):
    print("[")
    for i in list:
        print(f" {print_in_green("-",1)} {i}" )
    print(f"] : {len(list)} ")