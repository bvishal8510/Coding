def hangman():
    print '    ___________\n          |\n          |\n          |\n         (_)\n       _____\n      ||    ||\n      ||    ||\n        -------',
    print '\n      ||    ||\n        |    |\n        -------\n        |    |\n        |    |\n        |    |\n        |    |\n-----------------------'
def hanged():
    print '    ___________\n          |\n          |\n          |\n          |\n         (_)\n         ____\n       /|    |\ \n     /  |    |  \  ',
    print '\n   /     ------     \ \n /      |    |      \  \n        |    |          \n         ------\n        |    |\n        |    |\n        |    |\n        |    |'

name=['MITHUN CHACRAVARTHI','FIVE POINT SOMEONE ','DANIEL VITTORI','STEVE JOBS','ATIF ASALAM',]


while(1):
    print '\n'
    print 'Hey friends! Lets start the hangman game.The rules are gona be simple. I will be showing you a name as blank spaces'
    print 'and you are going to guess it letter by letter. If you guessed it right within 5 turns then you will save hangman'
    print 'otherwise he will be hanged. For each right guess you will get an extra guess for the number of letters you guessed '
    print 'right. You should not enter a single alphabet twice otherwise you will be responsible for the conseqences.'
    print 'I hope you understood the rules. Lets start the game.'
    sc=0
    hangman()
    
    for i in range(0,5):
        print 'Your score is = ',sc
        rn=list(name[i])
        if(i==0):
            print ' So Lets play hangman to save hangman from hanging. In first stage you are going to guess the name',
            print 'of famous film star of bollywood'
        elif(i==1):
            print ' Welcome to second stage. Here you are going to guess the name of famous Novel'
        elif(i==2):
            print ' Welcome to third stage. Here you are going to guess the name of famous baller'
        elif(i==3):
            print ' Welcome to fourth stage. Here you are going to guess the name of famous businessman'
        elif(i==4):
            print ' Welcome to fifth stage. Here you are going to guess the name of famous singer'
        
        alp=list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        gn=list()
        print 'LETS PLAY'
        c2=-1
        
        for x in rn:
            if(x==' '):
                print ' ',
                gn.append(' ')
            else:
                gn.append('_')
                print '_',
                continue
                
        c1=1
        ch1=''
        print ''
        while(c1<=5):
            print 'You have ',6-c1,'chances left wih you.'
            c1+=1
            print 'Enter a letter from the alphabets given below'
            print alp
            ch1=raw_input("Enter the letter of your guess  :")
            ch1=ch1.upper()

            if(ch1 in alp):
                alp.remove(ch1)
            elif(ch1==''):
                print '\n'
                print 'Please do not enter nothing'
                c1-=1
                continue
            elif(ch1==' '):
                print '\n'
                print 'Please do not enter a space. They are already shown to you.'
                c1-=1
                continue
            else:
                print '\n'
                print 'You have already entered this letter. Please enter your guess again.'
                c1-=1
                continue

            chk=0
            c2=-1
            for x in rn:
                c2+=1
                if(x==ch1):
                    chk=5
                    print ch1,
                    c1-=1
                    gn[c2]=ch1
                else:
                    print gn[c2],
                    continue
            print ''
            if(rn==gn):
                    print 'Yes, the right answer is ',name[i]
                    print 'You won this part of game. Lets continue to next part of game'
                    sc+=100 
                    break    
            elif(chk==5):
                print 'You guessed it right'
                continue
            else:
                print ' OOPS! you guessed it wrong'
                continue
        if(c1>=5):
                print 'You lost this part of game'
                print 'The right anwser is ',name[i]
                print 'Lets continue to next part of game'
        print '\n'
    
    if(sc<=400):
        print 'You lost the game. You could not save hangman from hanging'
        hanged()
    elif(sc>400):
        print 'You won the game.You saved hangman'
        print 'Your score is =',sc
        hangman()
        print 'Congratulations! you have successfully completed the game and saved hangman.'
    ch2=raw_input("Do you want to play again.Type y for yes and anything else for no   :")
    if(ch2=='Y' or ch2=='y'):
        continue
    else:
        break
