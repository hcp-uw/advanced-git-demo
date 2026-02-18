def foo(num, double_sided=False, char='*'):
    for i in range(num):
        print(char*(i+1))
    if double_sided:
        for i in range(num-1, 0, -1):
            print(char*i)

def main():
    amount = int(input('Amount: '))
    double_sided = input('Double Sided(Y/N): ')
    char = input("Character: ")
    if (len(char) < 1):
        char = '*'
    else:
        char = char[0]

    print()
    foo(amount, double_sided.lower()=='y', char)
    
if __name__ == "__main__":
    main()