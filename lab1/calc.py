
def print_separator():
    print('---------------------------')


def print_menu():
    print('[1] Add')
    print('[2] Subtract')
    print('[3] Multiply')
    print('[4] Divide')
    print('[5] Exponential')
    print('[x] Close System')

#instructions

opc = ''
while(opc != 'x'):
     print("\n\n\n")
    print_menu()

    opc = input('Please choose an option: ')
    print("User choose: " + opc)

    num1 = float(input('First number: '))
    num2 = float(input('Second number: '))

    if(opc == '1'):
        res = num1 + num2
        print('Res: ' + str(res))

    elif(opc == '2'):
        res = num1 - num2
        print('Res: ' + str(res))

    elif(opc == '3'):
        res = num1 * num2
        print('Res: ' + str(res))

    elif(opc == '4'):
        res = num1 / num2
        print('Res: ' + str(res))

    elif(opc == '5'):
        res = num1 ** num2
        print('Res: ' + str(res))

    input('Press Enter to Continue...')

print_separator()