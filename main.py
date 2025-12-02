# The "Memory" (Index 0 is unused)
board = ["#", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
winning_combinations = [
     [1,2,3],[4,5,6],[7,8,9], #rows
     [1,4,7],[2,5,8],[3,6,9], #columns
     [1,5,9],[3,5,7] #diagonals
]

#creating the game grid
def display_board(board):
    print("\n")
    # range(start, stop, step) -> 1, 4, 7
    for i in range(1, 10, 3): 
        print(f"  {board[i]}  |  {board[i+1]}  |  {board[i+2]}")
        
        if i < 7:
            print("-----|-----|-----")
    print("\n")

display_board(board)

#getting player markers
def user_marker():
    marker = ''
    
    while marker != 'X' and marker != 'O':
        marker = input("Player 1: Choose X or O: ").upper()
    if marker == 'X':
        return ('X', 'O') # Return a tuple: (Player 1, Player 2)
    else:
        return('O', 'X')
    
player1_marker, player2_marker = user_marker()

print(f"Player 1 is {player1_marker}")
print(f"Player 2 is {player2_marker}")



#game logic
turn = player1_marker
count = 0
game_on = True
while count < 9 and game_on:
    display_board(board)
    position = int(input(f"Player{turn}, place your move (1-9): "))

    if board[position] != 'X' and board[position] != 'O':
        board[position] = turn
        count += 1

        # Check winning combinations
        for combo in winning_combinations:
            if board[combo[0]] == board[combo[1]] == board[combo[2]] == turn:
                display_board(board)
                print(f"Game over! {turn} wins!")
                game_on = False
                break   
           
       
            

        if turn == player1_marker:
            turn = player2_marker
        else:
            turn = player1_marker
    else:
        print("That spot is already taken! Try again!")


#Game tie logic
if game_on:
    display_board(board)
    print("It's a Tie!")