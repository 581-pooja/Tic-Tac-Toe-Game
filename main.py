'''
board
x o x
_ _ o
x _ o
1. Board
2. User Input -> from 1 to 9 Validate it 
3. Add the number x and o ( get row and columns i.e. coords to add x & o)
4. To check and Every turns which user wins (iswin) Function
5. iswin 3 possiblity
6. Declare win or if 9 turns over there is tie
'''

board = [
    ["-","-","-"],
    ["-","-","-"],
    ["-","-","-"]
]

user = True # If user true then x otherwise o
turns = 0

# Function for printing board
def print_board():
    for row in board:
        for slot in row:
            print(f"{slot} ",end="")
        print()

# Function for quit from game
def quit(user_inputs):
    if user_inputs.lower() == "q":
        print("Thanks for playing!!")
        return True
    else:
        return False

# Function for checking inputs 1. It is number 2. In range of 1 to 9
def check_inputs(user_inputs):
    # If it is a number
    if not isnum(user_inputs):  # If isnum is false then stop here and print
        return False 
    user_inputs = int(user_inputs)
    # If it is 1 to 9
    if not bounds(user_inputs):
        return False
    return True

# Function is input a number?
def isnum(user_inputs):              # If user-inputs is not numeric return False
    if not user_inputs.isnumeric():  # If user-inputs is numeric return True 
        print("There is invalid number!!")
        return False
    else:
        return True

# Function is input in range (1 to 9)?
def bounds(user_inputs):
    if user_inputs > 9 or user_inputs < 1:
        print("These number is out of bounds")
        return False
    else:
        return True

# Function for checking is position required is taken 
def istaken(coords, board):
    row = coords[0]
    col = coords[1]
    if board[row][col] != "-":
        print("This position is already taken.")
        return True
    else:
        return False

# Co-ordinates for row and columns to get
def coordinates(user_inputs):
    row = int(user_inputs / 3)
    col = user_inputs
    if col > 2:
        col = int(col % 3)
    return (row,col)

# Function to add x or o to board
def add_to_board(coords,board,active_user):
    row = coords[0]
    col = coords[1]
    board[row][col] = active_user

# Function to get current user
def current_user(user):  # Simple if user is true return 'x' or user is false return  'o'
    if user:
        return "x"
    else:
        return"o"

# Function to see win player
def iswin(user,board):
    if check_row(user,board):
        return True
    if check_col(user,board):
        return True
    if check_diag(user,board):
        return True
    return False

# Function to check is any wins in row
def check_row(user, board):
    for row in board:
        complete_row = True
        for slot in row:
            if slot!= user:
                complete_row = False
                break
        if complete_row:
            return True
    return False

# Function to check is any wins in col
def check_col(user, board):
    for col in range(3):  
        complete_col = True
        for row in range(3):  
            if board[row][col] != user:
                complete_col = False
                break
    if complete_col : return True 
    return False

# Function to check is any wins in diagonal
def check_diag(user,board):
    if board[0][0] == user and board[1][1]== user and board[2][2] == user:
        return True
    elif board[0][2] == user and board[1][1] == user and board[2][0] == user:
        return True
    return False


while turns<9:
    active_user = current_user(user)
    print_board() 
    user_inputs = input("Please Enter position from 1 to 9 or enter q for Quit: ")
    # print(user_inputs) # For Testing

    if quit(user_inputs): 
        break # If quit(user_inputs) is true then break

    if not check_inputs(user_inputs):
        print("Please Try again")
        continue

    user_inputs = int(user_inputs) - 1  # Since using values 0,1,2 since arrays start from 0
    coords = coordinates(user_inputs)  # In coords we store the coordinates passes as row and col
    # board[0][0] = 'x'

    if istaken(coords,board):
        print("Please try again")
        continue

    add_to_board(coords,board,active_user)

    if iswin(active_user,board):
        print(f"{active_user.upper()} Wins!\n")
        break

    turns += 1
    if turns == 9:
        print("There is a Tie! Game Over!\nBetter Luck Next Time!")
    user = not user
