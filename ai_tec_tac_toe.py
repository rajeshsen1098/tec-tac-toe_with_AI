def analyseboard(board):
  c=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
  for i in range (0,8):
    if(board[c[i][0]]!=0 and board[c[i][0]]== board[c[i][1]] and board[c[i][1]]== board[c[i][2]]):
      return board[c[i][0]]
  return 0


def ConstBoard(board):
  print("The Current State of The Board : \n")
  for i in range(0,9):
    if(i !=0 and i%3==0):
      print("\n")
    if(board[i]==0):
      print("_",end=' ')
    if(board[i]==1):
      print("O",end=' ')
    if(board[i]==-1):
      print("X",end=' ')
  print("\n")


def User1Turn(board):
  pos = int(input("Enter 'X' position [1-9]:"))
  if(board[pos-1]!=0):
    print("Wrong Move")
    exit(0)
  board[pos-1]=-1


def User2Turn(board):
  pos = int(input("Enter 'O' position [1-9]:"))
  if(board[pos-1]!=0):
    print("Wrong Move")
    exit(0)
  board[pos-1]=1

  
def minmax(board,player):
  x=analyseboard(board)
  
  if(x!=0):
    return (x*player)
  pos= -1
  value= -2
  for i in range(0,9):
    if(board[i]==0):
      board[i]=player
      score= (-1)*minmax(board,player*-1)
      board[i]=0
      if(score>value):
        value=score
        pos=i
  if(pos==-1):
    return 0
  return value


def CompTurn(board):
  pos=-1;
  value=-2
  for i in range(0,9):
    if(board[i]==0):
      board[i]=1
      score = (-1)*minmax(board,-1)
      board[i]=0
      if(score>value):
        value=score
        pos=i
  board[pos]=1





def main():
  choice=int(input("1| for Play With AI\n2| for Play with Friend\n"))

  board=[0,0,0,0,0,0,0,0,0]

  if(choice==1):
    print("Single Player Game")                                    #new
    print("Computer O vs You X\n")                                #new
    player=int(input("Enter to play 1st('1') or 2nd('2'):"))      #new

    for i in range(0,9):              #new
        if(analyseboard(board)!=0):   #new
          break                       #new
        if(i+player)%2==0:
          CompTurn(board)
        else:
          ConstBoard(board)
          User1Turn(board)
    ConstBoard(board)

  elif(choice==2):
    for i in range(0,9):
        if(analyseboard(board)!=0):
          break

        if(i%2==0):
          ConstBoard(board)
          User1Turn(board)

        else:
          ConstBoard(board)
          User2Turn(board)

    ConstBoard(board)

    if(analyseboard(board)==0):
        print("Draw")

    elif(analyseboard(board)==-1):
        print("Player 1,has Won")

    elif(analyseboard(board)==1):
        print("Player 2,has Won")
    # ConstBoard(board)

  else:
      print("______WRONG INPUT______\n")
      con=input("Want to continue.press'y' for YES,another key for exit\n")
      if(con=='y'):
        main()
      exit(0)


main()
