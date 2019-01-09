from random import randint

def print_winner(element):
    if(element=="X"):
        print "-->congratulations,you win"
    else:
        print "-->sorry,you lose"
        
def print_board(board):
    print "-->current board condition is \n"
    i=0
    while(i<=6):
        print(board[i]+"\t"+board[i+1]+"\t"+board[i+2]+"\n")
        i+=3
        
def player(board):
    print "-->please enter a position"
    test=False
    while(test==False):
        pos=input()
        pos=pos-1
        if(board[pos]=="*"):
            test=True
            board[pos]="X"
        else:
            print "-->please enter a valid value"
    return board

def robot(board):
    print "-->now it's the computer's turn"
    test=False
    pos=0
    while(test==False):
        pos=randint(0,8)
        if(board[pos]=="*"):
            board[pos]="O"
            test=True
    return board
        

def checkwin(board):
    i=0
    state=False
    while(i<3):
        if(board[i]==board[i+3] and board[i+3]==board[i+6] and board[i]!="*"):
            state=True
            print_winner(board[i])
            break
        else:
            state=False
        
        if(board[i]==board[i+1] and board[i+1]==board[i+2] and board[i]!="*"):
            print_winner(board[i])
            state=True
            break
        else:
            state=False
        i+=1
    if(board[0]==board[4] and board[4]==board[8] and board[0]!="*"):
        print_winner(board[0])
        state=True
    if(board[2]==board[4] and board[4]==board[6] and board[4]!="*"):
        print_winner(board[2])
        state=True
    return state
        
user=True
state=False
board=[]
print "-->the positions on the board are:"
print "1\t2\t3\n4\t5\t6\n7\t8\t9\n"
print "-->the first turn is yours"
for i in range(0,9):
    board.append("*")
print_board(board)
while(state==False):
    if(user==True):
        board=player(board)
        print_board(board)
    else:
        board=robot(board)
        print_board(board)
    state=checkwin(board)
    user=not user
    



