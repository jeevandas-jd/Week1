
def isPalindrome(string):
    """Check if a string is a palindrome.
    loop through half the string and compare characters
    from the start and end of the string.
    """
    for i in range(len(string) // 2):
        # Compare characters from the start and end of the string
        # If they are not equal, return False
        if string[i] != string[-(i + 1)]:
            return False
    return True

def main():
    # Test the isPalindrome function
    flag=input("Enter a string: ")
    if isPalindrome(flag):
        print(f"{flag} is a palindrome")
    else:
        print(f"{flag} is not a palindrome")

if __name__ == "__main__":
    main()