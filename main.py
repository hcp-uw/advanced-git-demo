def foo(num, double_sided=False):
    for i in range(num):
        print('*'*(i+1))
    if double_sided:
        for i in range(num-1, 0, -1):
            print('*'*i)

def main():
    amount = int(input('Amount: '))
    double_sided = input('Double Sided(Y/N): ')

    print()
    foo(amount, double_sided.lower()=='y')
    
if __name__ == "__main__":
    main()