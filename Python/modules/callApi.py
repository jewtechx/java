import sys
from fetchhApi import fetchApi
from fetchhApi import letCowSay

def main():
    if len(sys.argv) == 2:
        print(sys.argv[1])
    elif len(sys.argv) == 3:
        print(letCowSay(sys.argv[1]))
        
    else:
        print(fetchApi("https://jsonplaceholder.typicode.com/users"))

# Move the call to main() outside of its definition
# if __name__ == "__main__":
main()
