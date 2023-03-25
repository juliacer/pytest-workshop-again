import random


def is_valid_play(play):
    return play in ['rock', 'paper', 'scissors']


def computer_play():
    return random.choice(['rock',
                          'paper',
                          'scissors'])


def determine_game_result(human, computer):
    if human == computer:
        return 'tie'
    if human + computer in 'rockpaperscissorsrock':
        return 'computer'
    return 'human'


def main():
    human = input('rock, paper or scissors? ')

    while not is_valid_play(human):
        human = input('rock, paper or scissors? ')

    computer = computer_play()

    print(computer)

    result = determine_game_result(human, computer)

    if result == 'tie':
        print('it\'s a tie!')
    elif result == 'computer':
        print('you loose')
    else:
        print('you win')


if __name__ == '__main__':
    main()
