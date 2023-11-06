import time

def getting_back():
    return 'You are back'

# First a welcoming message to the game
print('This is a game, you are a detective and your goal is to find the eyes of the victims.')
user_first_choice = input('Would you like to continue? (yes/no): ')

if user_first_choice.lower() == 'no':
    user_last_chance = input('Would you like to end the program? (yes/no): ')
    if user_last_chance.lower() == 'yes':
        print('You are out')
        exit()
    else:
        result_message = getting_back()
        print(result_message)

# Choosing the location
print('You are now at the police. You have three places to go: the graveyard, the killing scene, or the morgue.')
while True:
    user_location_choice = input("Enter your location choice (1 or 2 or 3 or 4): ")

    if user_location_choice == '1':
        print('You are now at the graveyard')
        time.sleep(2)
        print('There are two things here: a key and a note')
        time.sleep(2)
        print('The code of the key is (0129). You are going to need it later.')

    elif user_location_choice == '2':
        print('You are now at the killing scene. You are standing in a desert.')
        time.sleep(2)
        print('The location of the killing scene is (0987), and the code for the note is (0239)')
        time.sleep(3)
        user_grave_location = input('If you want to go anywhere else, write the location of it: ')

    elif user_location_choice == '3':
        print('You are now at the morgue, there is a glass. The code is (1235)')
        user_grave_location = input('If you want to go to anywhere else, write the location of it: ')

    elif user_location_choice == '4':
        print('You are now at the infinite world')
        print('You are seeing a board that requires three things')
        time.sleep(2)
        print('The Board: You have to enter the codes of the glass and the note and the key, Enter it!!!')
        time.sleep(3)
        The_master_code = input('The Board: Enter the code!!!: ')
        if The_master_code == '123502390129':
            print('Loading...')
            time.sleep(5)
            print('You have opened the board')
            time.sleep(2)
            print('Now you have the location of the killer')
            time.sleep(2.5)
            print('The location of the killer is 0000')
            user_killer_location = input('Enter the next location: ')
            if user_killer_location == '0000':
                time.sleep(2)
                print('You have found the killer')
                print('The game is over')
                break
    else:
        print('You have been kicked')
        break
