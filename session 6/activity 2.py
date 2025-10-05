def rle_encode(s):
    #data and parameter validation
    if not s or not s.isalpha(): 
        return "Invalid input"

    #core rle
    result = ""
    count = 1
    for i in range(1, len(s) + 1):
        #checks if we continue the run of the string
        if i < len(s) and s[i] == s[i - 1]:
            count += 1
        else:
            #outputs the result and resets the count
            result += s[i - 1] + (str(count) if count > 1 else "")
            count = 1
            
    return result


def rle_decode(s):
    if not s:
        return "Invalid input"
    
    result = ""
    i = 0
    #decoding loop
    while i < len(s):
        #checks if the current character is a letter
        if not s[i].isalpha():
            return "Invalid input"
        
        char = s[i]
        i += 1
        num = ""
        
        #reads the subsequent digits
        while i < len(s) and s[i].isdigit():
            num += s[i]
            i += 1
        #expands the character by the count
        result += char * (int(num) if num else 1)
    
    return result


def main():
    #gets user input
    user_input = input("Enter a string: ").strip()
    
    #checks for digits to decide between encoding and decoding
    if any(c.isdigit() for c in user_input):
        print(rle_decode(user_input))
    else:
        print(rle_encode(user_input))

        #main function
if __name__ == "__main__":
    main()