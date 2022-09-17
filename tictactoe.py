

def game_board(board):
    print('\n' *50)
    horizontal = ('----------')

    print(board[7],'|',board[8],'|',board[9])
    print(horizontal)
    print(board[4],'|',board[5],'|',board[6])
    print(horizontal)
    print(board[1],'|',board[2],'|',board[3])


def x_or_o():
    print('\n')

    icon = ''

    while icon != 'X' and icon != 'O':

       icon = input('Player 1, select X or O: ').upper()
        

       if icon =='X':
           return('X','O')
        
       else:
           return('O','X')

icon1,icon2 = x_or_o()

def place_icon(board,icon,square):
    board[square]= icon




def win_check(board,icon):

    return ((board[7]==board[8]==board[9]==icon) or (board[4]==board[5]==board[6]==icon)
            or (board[1]==board[2]==board[3]==icon) or (board[7]==board[4]==board[1]==icon)
            or (board[8]==board[5]==board[2]==icon) or (board[9]==board[6]==board[3]==icon)
            or (board[7]==board[5]==board[3]==icon) or (board[9]==board[5]==board[1]==icon))


import random

def choose_starter():

    if random.randint(0,1) ==0:
        return 'Player 2'
    else:
        return 'Player 1'
    

def open_square(board,square):
    return board[square] ==' '

def board_full_check(board):
    for s in range (1,10):
        if open_square(board,s):
            return False

    return True


def player_choice(board):
    print('\n')

    square = 0

    while square not in [1,2,3,4,5,6,7,8,9] or not open_square(board,square):
        square = int(input('where would you like to place next? (1-9) '))
       

    return square


def replay():
    print('\n')
    choice = input('Do you want to play again, yes or no?: ')
    if choice =='yes':
        return True

    else:
        game_on=False


print(" \nWelcome to Tic Tac Toe  (programmed by Amin Ambike)")

while True:

    myboard=[' ']*10
   

    move = choose_starter()
    print(move, 'will go first')

    start=input('Press y to start game')

    if start.lower()[0] =='y':
        game_on = True
    else:
        game_on = False

    while game_on:

        if move == 'Player 1':

            game_board(myboard)
            square = player_choice(myboard)
            place_icon(myboard,icon1,square)

            if win_check(myboard,icon1):
                game_board(myboard)
                print('Player 1 has won the game')
                game_on=False
            else:
                if board_full_check(myboard):
                    game_board(myboard)
                    print('TIE!')
                    game_on=False
                else:
                    move ='Player 2'

        else:
            game_board(myboard)
            square = player_choice(myboard)
            place_icon(myboard,icon2,square)

            if win_check(myboard,icon2):
                game_board(myboard)
                print('Player 2 has won the game')
                game_on = False
            else:
                if board_full_check(myboard):
                    game_board(myboard)
                    print('TIE!')
                    game_on = False
                else:
                    move = 'Player 1'


    if not replay():
        break




    


        

    
    
        

                
            
             

