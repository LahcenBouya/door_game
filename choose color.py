print("welcome to my game")
asking=input('choose a door for playing this small  game\n red or blue\n').lower()
if asking=="red":
    choose=input('that is\'t than choose an other rool white or green\n').lower()
    if choose=="white":
        print('you are the best man')
    elif choose=="green":
        print('the green is for sake just try again')
    else:
        print('invalid choice')
elif asking=="blue":
    print('again mr')
else:
    print('invalid choice')
