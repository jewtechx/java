import re
while True:
    username = input("Enter your preferred username ")
    if re.search(r'^[0-9].*',username) or len(username) < 3:
        print("Invalid username")
        continue
    else:
        while True:
            email = input('Enter your email').strip()
            if re.search(r'^\w+@(\w+\.)?\w+\.(com|net|org|co|gh)$', email, re.IGNORECASE):
                print("Thanks for signing up to our news letter box")
                break
            else :
                 print("Invalid email")
                 continue
    break