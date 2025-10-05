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

def main(): #main function
    user_input = input("Enter letters: ").strip()
    print(rle_encode(user_input))

if __name__ == "__main__":
    main() #calls main function