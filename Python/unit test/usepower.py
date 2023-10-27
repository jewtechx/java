from powerr import square
import sys
def main():

    num = int(input('Enter your number here '))
    res = square(num)
    if num:
        print(f'The square of {num} is {res}')
    else:
        print('Add an argv value')

if __name__ == "__main__":
    main()