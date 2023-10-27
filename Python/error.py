def main():
    x = get_age('What is your car number ')
    print(x)
def get_age(question):
    while True:
        try:
            return int(input(question))
        except ValueError:
            raise ValueError("input not a number")
            continue
        finally:
            print("Everything done")
main() 