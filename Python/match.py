#Get input from user
while True:
    name = input('Enter character name').lower()
    match name:
        case 'john' | 'master chief' | 'halo king':
            print('He was the commander of the army')
        case 'kai':
            print('She was John\'s close friend')
        case 'halsey':
            print('Dr. Halsey was the chief scientist and the initiator of the whole spartan program')
        case 'miranda':
            print('She was Dr. Halsey\'s daughter and a scientist too')
        case _:
            print('Character not found!!!')