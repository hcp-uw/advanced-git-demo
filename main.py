def foo(num):
    for i in range(num):
        print('*'*(i+1))

def main():
    amount = int(input('Number? '))
    foo(amount)
    
if __name__ == "__main__":
    main()