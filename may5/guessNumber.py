def guessNumber(intervel):
    
    mid = (intervel[0] + intervel[1]) // 2

    user=input(f"is number is {mid}")
    if user == 'yes':
        return mid
    else:
        user=input(f"Is number greater than {mid}")
        if user == 'yes':
            return guessNumber([mid+1, intervel[1]])
        else:
            return guessNumber([intervel[0], mid-1])
def main():
    print("Welcome to the guess number game!")
    print("Think of a number between 1 and 100.")
    print("I will try to guess it.")
    print("Please answer with 'yes' or 'no'.")
    
    result = guessNumber([1, 100])
    print(f"Your number is: {result}")
if __name__ == "__main__":
    main()