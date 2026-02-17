def foo(num, char='*'):
    for i in range(num):
        print(char*(i+1))

def main():
    amount = int(input('Amount: '))
    char = input("Character: ")
    if (len(char) < 1):
        char = '*'
    else:
        char = char[0]

    print()
    foo(amount, char)
    
if __name__ == "__main__":
    main()