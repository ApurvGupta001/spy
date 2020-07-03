def display_mat(a):
    for row in a:
        print(row)
 
 
def decide_position(a, pos, ch):
    if pos == 1 and a[0][0] == '1':
        a[0][0] = ch
        return a
    elif pos == 2 and a[0][1] == '2':
        a[0][1] = ch
        return a
    elif pos == 3 and a[0][2] == '3':
        a[0][2] = ch
        return a
    elif pos == 4 and a[1][0] == '4':
        a[1][0] = ch
        return a
    elif pos == 5 and a[1][1] == '5':
        a[1][1] = ch
        return a
    elif pos == 6 and a[1][2] == '6':
        a[1][2] = ch
        return a
    elif pos == 7 and a[2][0] == '7':
        a[2][0] = ch
        return a
    elif pos == 8 and a[2][1] == '8':
        a[2][1] = ch
        return a
    elif pos == 9 and a[2][2] == '9':
        a[2][2] = ch
        return a
    else:
        return False
 
 
def check(a):
    if a[0][0] == a[0][1] == a[0][2] == '0' or a[1][0] == a[1][0] == a[1][2] == '0' or a[2][0] == a[2][1] == a[2][
        2] == '0' or a[0][0] == a[1][0] == a[2][0] == '0' or a[0][1] == a[1][1] == a[2][1] == '0' or a[0][2] == a[1][
        2] == a[2][2] == '0' or a[0][0] == a[1][1] == a[2][2] == '0' or a[0][2] == a[1][1] == a[2][0] == '0':
        return 1
    elif a[0][0] == a[0][1] == a[0][2] == 'X' or a[1][0] == a[1][0] == a[1][2] == 'X' or a[2][0] == a[2][1] == a[2][
        2] == 'X' or a[0][0] == a[1][0] == a[2][0] == 'X' or a[0][1] == a[1][1] == a[2][1] == 'X' or a[0][2] == a[1][
        2] == a[2][2] == 'X' or a[0][0] == a[1][1] == a[2][2] == 'X' or a[0][2] == a[1][1] == a[2][0] == 'X':
        return 0
    else:
        return -1
 
 
def computer_chance(a):
    #print("ONE")
    if ((a[0][1] == '0' and a[0][2] == '0') or (a[1][0] == '0' and a[2][0] == '0') or a[1][1] == a[2][2] == '0') and \
            a[0][0] == '1':
        #print("1")
        a[0][0] = '0'
        return a
    elif ((a[0][0] == '0' and a[0][2] == '0') or (a[1][1] == '0' and a[2][1] == '0')) and a[0][1] == '2':
        a[0][1] = '0'
        #print("2")
        return a
    elif ((a[0][0] == '0' and a[0][1] == '0') or (a[1][2] == '0' and a[2][2] == '0') or a[1][1] == a[2][0] == '0') and \
            a[0][2] == '3':
        #print("3")
        a[0][2] = '0'
        return a
    elif ((a[0][0] == '0' and a[2][0] == '0') or (a[1][1] == '0' and a[1][2] == '0')) and a[1][0] == '4':
        #print("4")
        a[1][0] = '0'
        return a
    elif ((a[1][0] == '0' and a[1][2] == '0') or (a[0][1] == '0' and a[2][1] == '0') or a[0][0] == a[2][2] == '0') and \
            a[1][1] == '5':
        #print("5")
        a[1][1] = '0'
        return a
    elif ((a[1][0] == '0' and a[1][1] == '0') or (a[0][2] == '0' and a[2][2] == '0')) and a[1][2] == '6':
        #print("6")
        a[1][2] = '0'
        return a
    elif ((a[0][0] == '0' and a[1][0] == '0') or (a[2][1] == '0' and a[2][2] == '0') or (a[0][2] == '0' and a[1][1] == '0')) and \
            a[2][0] == '7':
        #print("7")
        a[2][0] = '0'
        return a
    elif ((a[0][1] == '0' and a[1][1] == '0') or (a[2][0] == '0' and a[2][2] == '0')) and a[2][1] == '8':
        a[2][1] = '0'
        #print("8")
        return a
    elif ((a[0][2] == '0' and a[1][2] == '0') or (a[2][0] == '0' and a[2][1] == '0') or a[0][0] == a[1][1] == '0') and \
            a[2][2] == '9':
        #print("9")
        a[2][2] = '0'
        return a
    elif a[0][0] == a[2][2] and a[1][1] == '5':
        a[0][1] = '0'
        return a
    elif a[0][2] == a[2][0] and a[1][1] == '5':
        a[2][1] = '0'
        return a
    elif ((a[0][1] == 'X' and a[0][2] == 'X') or (a[1][0] == 'X' and a[2][0] == 'X') or a[1][1] == a[2][2] == 'X') and \
            a[0][0] == '1':
        a[0][0] = '0'
        return a
    elif ((a[0][0] == 'X' and a[0][2] == 'X') or (a[1][1] == 'X' and a[2][1] == 'X')) and a[0][1] == '2':
        a[0][1] = '0'
        return a
    elif ((a[0][0] == 'X' and a[0][1] == 'X') or (a[1][2] == 'X' and a[2][2] == 'X') or a[1][1] == a[2][0] == 'X') and \
            a[0][2] == '3':
        a[0][2] = '0'
        return a
    elif ((a[0][0] == 'X' and a[2][0] == 'X') or (a[1][1] == 'X' and a[1][2] == 'X')) and a[1][0] == '4':
        a[1][0] = '0'
        return a
    elif ((a[1][0] == 'X' and a[1][2] == 'X') or (a[0][1] == 'X' and a[2][1] == 'X') or a[0][0] == a[2][2] == 'X') and \
            a[1][1] == '5':
        print("HEY")
        a[1][1] = '0'
        return a
    elif ((a[1][0] == 'X' and a[1][1] == 'X') or (a[0][2] == 'X' and a[2][2] == 'X')) and a[1][2] == '6':
        a[1][2] = '0'
        return a
    elif ((a[0][0] == 'X' and a[1][0] == 'X') or (a[2][1] == 'X' and a[2][2] == 'X') or (a[0][2] == 'X' and a[1][1] == 'X')) and \
            a[2][0] == '7':
        print("May")
        a[2][0] = '0'
        return
    elif ((a[0][1] == 'X' and a[1][1] == 'X') or (a[2][0] == 'X' and a[2][2] == 'X')) and a[2][1] == '8':
        a[2][1] = '0'
        return
    elif ((a[0][2] == 'X' and a[1][2] == 'X') or (a[2][0] == 'X' and a[2][1] == 'X') or a[0][0] == a[1][1] == 'X') and \
            a[2][2] == '9':
        print("NEW")
        a[2][2] = '0'
        return
    else:
        print("REached here")
        for i in range(3):
            for j in range(3):
                if a[i][j] != "X" and a[i][j] != '0':
                    a[i][j] = '0'
                    return
                break
 
 
a = [
    ['1', '2', '3'],
    ['4', '5', '6'],
    ['7', '8', '9']
]
 
# actual code starts here
print('''
          THIS IS A CLASSICAL TIC TAC TOE GAME ( ZERO - KAATA )
          ENTER THE POSITION OF 'X' BY PRESSING THE NUMBER AGAINST THAT POISITION (1-9)
 
''')
display_mat(a)
choice = int((input("Enter the position: ")))
a = decide_position(a, choice, 'X')
try:
    display_mat(a)
 
    if a[1][1] == 'X':
        a[0][0] = '0'
    else:
        a[1][1] = '0'
    print("After computer's chance")
    display_mat(a)
 
    chance = 1
    while chance <= 3:
        choice = int((input("Enter the position: ")))
        a = decide_position(a, choice, 'X')
        try:
            display_mat(a)
            if check(a) == 1:
                print("Computer Wins")
                break
            elif check(a) == 0:
                print("you win")
                break
            computer_chance(a)
            print("After computer's chance")
            display_mat(a)
            if check(a) == 1:
                print("Computer Wins")
                break
            elif check(a) == 0:
                print("you win")
                break
            chance += 1
 
        except TypeError:
            print("Wrong Choice")
            chance = 6
 
    if chance == 4:
        print("Reached here")
        choice = int((input("Enter the position: ")))
        a = decide_position(a, choice, 'X')
        display_mat(a)
        if check(a) == 1:
            print("Computer Wins")
        elif check(a) == 0:
            print("you win")
        else:
            print("Match Draw")
 
except TypeError:
    print("Wrong Choice")
