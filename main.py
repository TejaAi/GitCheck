def even_or_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
    
if __name__ == "__main__":
    number = int(input("Enter a number: "))
    result = even_or_odd(number)
    print(f"The number {number} is {result}.")