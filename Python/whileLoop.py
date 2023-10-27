i = 0
while(i < 500):
    if i % 2 == 0:
     print("# # # #")
    elif i % 2 == 1:
        print(" # # # ")
    i += 1

while True:
    try:
       num = int(input('How many times to you wanna print meow ? '))
       if num > 0:
            i = 0
            while i < num:
                print('meow')
                i += 1
            break #break out of loop since user entered a valid num
        
       else:
            print('Don\'t enter a negative number')
            continue #continue to loop over and over again
    except ValueError:
         print("Don\'t enter a letter or any other thing apart from a number")
    
    