import random
import requests


# A game where a random Harry Potter character is selected for you and an opponent.
# The program then asks the user to enter a feature of the character which will then be used to see if the feature matches the opponents.
# The program will then record and enter scores in a .txt file.

def game():
    url = 'http://hp-api.herokuapp.com/api/characters'

    response = requests.get(url)
    harry_potter = response.json()

    user_stat = input(
        'Choose a feature of your Harry Potter character: (name, species, house, gender, alive, student, staff):')

    computer_generated = (random.choice(harry_potter))
    print('The computer has selected:')
    print(computer_generated['name'])
    print(computer_generated['species'])
    print(computer_generated['gender'])
    print('Living? {}'.format(computer_generated['alive']))
    print(computer_generated['house'])
    print('Hogwarts student? {}'.format(computer_generated['hogwartsStudent']))
    print('Hogwarts staff? {}'.format(computer_generated['hogwartsStaff']))

    user_generated = (random.choice(harry_potter))
    print('Your randomly selected Harry Potter Character is:')
    print(user_generated['name'])
    print(user_generated['species'])
    print(user_generated['gender'])
    print('Living? {}'.format(user_generated['alive']))
    print(user_generated['house'])
    print('Hogwarts student? {}'.format(user_generated['hogwartsStudent']))
    print('Hogwarts staff? {}'.format(user_generated['hogwartsStaff']))

    winner = 'Congrats your stat has matched the opponents!!'

    name_winner = user_generated['name'] == computer_generated['name']
    species_winner = user_generated['species'] == computer_generated['species']
    gender_winner = user_generated['gender'] == computer_generated['gender']
    alive_winner = user_generated['alive'] == computer_generated['alive']
    house_winner = user_generated['house'] == computer_generated['house']
    student_winner = user_generated['hogwartsStudent'] == computer_generated['hogwartsStudent']
    staff_winner = user_generated['hogwartsStaff'] == computer_generated['hogwartsStaff']

    if user_stat == 'name' and name_winner:
        print('You have selected name as your stat')
        print(winner)
        print('You win 100 points!')

    elif user_stat == 'species' and species_winner:
        print('You have selected species as your stat')
        print(winner + '30 points')

    elif user_stat == 'gender' and gender_winner:
        print('You have selected gender as your stat')
        print(winner + '20 points')

    elif user_stat == 'alive' and alive_winner:
        print('You selected alive as your stat')
        print(winner + '20 points')

    elif user_stat == 'house' and house_winner:
        print('You have selected house as your stat')
        print(winner + '50 points')

    elif user_stat == 'student' and student_winner:
        print('You have chosen student as your stat to match')
        print(winner + '20 points')

    elif user_stat == 'staff' and staff_winner:
        print('You have chosen staff as your stat to match')
        print(winner + ' 20 points')

    else:
        print('The chosen stat ({}) did not match, You have lost!'.format(user_stat))




game()

