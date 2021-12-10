from capitals import states
import random
print(states)

random.shuffle(states)


user_input = input('Welcome to this terrible capitals game. Would you like to play? y/n: ')
print('you chose: '+ user_input)

if user_input == 'y':
    random_state= states
    def game():
        correct = 0
        incorrect = 0
        for i in states:
            answer = input(f'What is the capital of '+ i['name'] + '?')
            if answer.lower() == i['capit2al'].lower():
                correct += 1
                print('Nice, your score is now: ' + str(correct))
            else:
                incorrect += 1
                print('Good effort. Your total correct is: ' + str(correct) + ' incorrect is: ' + str(incorrect))
            play_again = input('Wanna play again?')
            if play_again == 'y':
                user_input()
    game()
else:
    print('okay bye dont come back')