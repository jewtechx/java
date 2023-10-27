def main():
    def sum(num):
        if num > 0:
            return num + sum(num - 1)
        else:
            return 0

    number = sum(200)
    print(number)
    
if __name__ == "__main__":
    main()