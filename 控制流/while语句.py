
number = 23
running = True

while running:
    guess = int(input('Enter an interger:'))

    if guess == number:
        print('Congreatulations, you guessed it.')
        # 这将导致 while 循环终止
        running = False
    elif guess < number:
        print('No, it is a little lower than that.')
    else:
        print('No, it is a little higher than that.')
else:
    print('The while loop is over.')
    # 在这里你可以做你想做的任何事情

print('Done')
