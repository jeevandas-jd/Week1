

def celsius_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit."""
    return (celsius * 9/5) + 32
def main():
    """Main function to run the temperature conversion."""
    try:
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = celsius_to_fahrenheit(celsius)
        print(f"{celsius}°C is equal to {fahrenheit}°F")
    except ValueError:
        print("Please enter a valid number.")
if __name__ == "__main__":
    main()