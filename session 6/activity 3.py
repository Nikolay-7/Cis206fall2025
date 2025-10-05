def rle_encode(s):
    if not s:
        return "Invalid input"
    
    result = "##00"
    count = 1
    

    for i in range(1, len(s) + 1):
        if i < len(s) and s[i] == s[i - 1]:
            #checks if to continue the run of the string
            count += 1
        else:
            chara = s[i - 1]
            
            #applies escape sequence then appends the count
            if chara == '#':
                result += "##" + (str(count) if count > 1 else "")
            elif chara.isdigit():
                result += "#" + chara + (str(count) if count > 1 else "")
            else:
                #normal character, followed by count
                result += chara + (str(count) if count > 1 else "")
            
            #resets the count
            count = 1
    
    return result


def rle_decode(s):
    #validation check for ##
    if not s or not s.startswith("##00"):
        return "Invalid input (Missing ##00)"
    
    #removes ##
    s = s[4:]
    result = ""
    i = 0
    
    #decoding loop
    while i < len(s):
        
        #identifies character
        if s[i] == '#':
            if i + 1 >= len(s):
                return "Invalid input"
            
            if s[i + 1] == '#':
                chara = '#' #ex: ## to #
                i += 2
            elif s[i + 1].isdigit():
                chara = s[i + 1] #ex: #N to N
                i += 2
            else:
                return "Invalid input"
        else:
            chara = s[i]
            i += 1
            
        num = ""
        #subsequent digits for the count
        while i < len(s) and s[i].isdigit():
            num += s[i]
            i += 1
            
        #expands character by the count
        result += chara * (int(num) if num else 1)
        
    return result


def main():
    #gets user input
    user_input = input("Enter a string: ").strip()
    
    #decodes if ##, otherwise encodes
    if user_input.startswith("##00"):
        print(f"Decoded: {rle_decode(user_input)}")
    else:
        print(f"Encoded: {rle_encode(user_input)}")

  #calls main function
if __name__ == "__main__":
    main() 
