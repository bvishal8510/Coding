str = input('Enter string \n')
if len(str) < 3:
    pass
elif len(str) >= 3:
    if str[-3:] == 'ing':
        str = str + 'ly'
    else:
        str = str + 'ing'
    print(str)
