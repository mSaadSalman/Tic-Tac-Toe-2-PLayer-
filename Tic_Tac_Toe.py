#Milestone 1
import random

def welcome():
    print("Welcome to...........")

    print (" ________                     ________                      ________       ______     ")
    print (" |__  __| _______             |__  __|    ___               |__  __|  __   | ___|     ")
    print ("   |  |  |__  ___|   ___        |  |     /   \     ___        |  |   /  \  | |__      ")
    print ("   |  |     | |     / __)       |  |    / /_\ \   / __)       |  |  / /\ \ | ___|   ")      
    print ("   |  |   __| |__  (  (         |  |   / /___\ \ (  (         |  | ( (__) )| |__    ")
    print ("   |__|  |_______|  \__\        |__|  /_/     \_\ \__\        |__|  \____/ |____| ")
                                                                    
    print ("\n")


def display_board(board):
    
    
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    
test_board = ['#','X','O','X','O','X','O','X','O','X']
#display_board(test_board)

def player_input():
    marker = "FILLER"

    
    while marker not in ["X","O"]:
        marker = input("Player 1 choose X or O: ")
        

        if marker not in ["X","O"]:
            print ("Sorry please select a valid choice ")

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

#player_input()

def place_marker(board, marker, position):

    #positon = input("Enter which position number you will like to set: ")

    board[position]=marker 


    return marker

#place_marker(test_board,"%",4)
#display_board(test_board)

def win_check (board, mark):

    if (mark == board[1]==board[2]==board[3]) or (mark == board[4]==board[5]==board[6]) or(mark == board[7]==board[8]==board[9]) or (mark == board[1]==board[4]==board[7]) or (mark == board[2]==board[5]==board[8]) or(mark == board[3]==board[6]==board[9]) or (mark == board[1]==board[5]==board[9]) or(mark == board[3]==board[5]==board[7]):
        print("Team ", mark, "has won!")
        return True 
    else:
        pass
#win_check(test_board,'X')

def choose_first():
    ran = (random.randint(1,2))

    if ran == 1:
        return "Player 1"

    else:
        return "Player 2"

def space_check(board, position):

    return board[position] == " "

def full_board_check(board):

   if (board[1]==" ")or (board[2]==" ")or (board[3]==" ")or (board[4]==" ")or (board[5]==" ")or (board[6]==" ")or(board[7]==" ")or(board[8]==" ")or(board[9]==" ") :
       return False
   else:
        return True

#full_board_check(test_board)

def player_choice(board):
    position = 0
    
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Choose your next position: (1-9) '))
        
    return position

def replay ():

    choice = "asasa"

    while choice not in ["Y","N"]:

        choice = input("Keep playing? (Y or N): ")

        if choice not in ["Y","N"]:
            print ("Sorry, invalid choice! ")

    if choice == "Y":
        return True

    else:
        False
#----------------------------------------------------------




welcome() 

while True:
    board = [" "] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print (turn, " will go first")

    game_on = input("Are you ready to play? Yes or No ")
    if game_on == "Yes" or "yes":
        game_on= True

    else:
        game_on= False 

    while game_on==True :
        if turn == "Player 1":
            display_board(board)
            position = player_choice(board)
            place_marker(board,player1_marker, position)

            if win_check(board, player1_marker)==True:
                display_board(board)
                print('Congratulations! You have won the game!')
                game_on = False

            else:
                if full_board_check(board):
                    display_board(board)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'

        else:
            display_board(board)
            position = player_choice(board)
            place_marker(board,player2_marker, position)

            if win_check(board, player2_marker):
                display_board(board)
                print('Congratulations! You have won the game!')
                game_on = False

            else:
                if full_board_check(board):
                    display_board(board)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 1'

            
                

    if not replay():
        break
            
            
            
            
        
        
        

   

    

    






    
