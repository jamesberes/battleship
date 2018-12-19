from random import randint
import random #Need this b/c below line doesn't work 
#from random import choice

board = [] #player's board
board_p2 = [] #computer's board

for x in range(0, 10):
  board.append(["O"] * 10)
  board_p2.append(["O"] * 10)

def print_board(board):
  for row in board:
    print " ".join(row)

#--- Start New Code ----#
def start_script():
  print """Hello and welcome to Battlehsip.
  
   ----Instructions----
  A) You will be given 5 ships consisting of: 
    1 Aircraft Carrier (5 blocks long)
    1 Battleship (4 blocks long)
    1 Destroyer (3 blocks long)
    1 Submarine (3 blocks long)
  	-- and --
    1 Patrol Boat (2 blocks long)
  
  B) Then, you and the computer place your ships.
     Note: Ships cannot be placed diagonally
     Note: The board is 10 x 10

  C) Finally, both teams will take turns firing at the enemy grid until only one fleet is left standing!
  """
  
#---- Ship dictionary ----#  
ships = {
  "Aircraft Carrier": 5,
  "Battleship": 4,
  "Destroyer": 3,
  "Submarine": 3,
  "Patrol Boat": 2}

#---- Ship list used to iterate over dictionary with matching keys ----#
ship_list = [
  "Aircraft Carrier",
  "Battleship",
  "Destroyer",
  "Submarine",
  "Patrol Boat"]

#---- Create a list containing pieces left for each player. Will be used to check if game is over ----#
player_pieces = []
computer_pieces = []
for i in range(0, len(ship_list)):
  player_pieces.append(ships[ship_list[i]])
  computer_pieces.append(ships[ship_list[i]])

#---- Player 1 Boat Placement ----#
def place_ships(boat_list, dictionary): #Places all boats in dictionary on battleship board. Uses key values for size
  i = 0
  while i < len(boat_list): #until each item in boat_list has been placed...
    print "Let's place the %s" % boat_list[i] #Informs user which iteration (boat) we're on.
    direc = str(raw_input("Would you like the place the ship vertically (enter v) or horizontally (enter h): ")) 
    direc = direc.lower()
    if direc == "vertical" or direc == "v": #When the boat is placed vertically...
      print "Your %s will be placed vertically." % boat_list[i]
      # Choose a column that is an integer
      v_col_check = False 
      while not v_col_check: 
        try:
          choose_col = int(raw_input("Choose Column 1-10: ")) - 1 
          v_col_check = True 
        except ValueError: 
          print "Non numerical entry. Try again." 
      # Ensure the column chosen is within range
      if choose_col not in range(0, len(board[0])): #Ensure column is within acceptable range
        print "You did not choose a column between 1 and 10"
      else: #Choose row that is an integer 
        v_row_check = False 
        while not v_row_check: 
          try:
            choose_row = int(raw_input("Choose Row 1-10: ")) - 1 
            v_row_check = True 
          except ValueError: 
            print "Non numerical entry. Try again." 
        # Ensure the row chosen is within range
        if choose_row not in range (0, len(board) - dictionary[boat_list[i]] + 1): #Make sure there's room 
          print "Row %s won't work. The %s needs %s spaces." % (choose_row + 1, boat_list[i], dictionary[boat_list[i]])
          print " "
        else: #Place letters
          availability = True #initialize availability check
          for boat_size in range (0, dictionary[boat_list[i]]): #From 0 to length of ship
            if board[choose_row + boat_size][choose_col] != "O": #If there's ever a space besides "O"pen water 
              availability = False #This selection is unavailable
            
          if availability == False:
            print "There was a boat in the way. Choose again."
          else: #If there were only O's found 
            for boat_size in range (0, dictionary[boat_list[i]]):
              board[choose_row + boat_size][choose_col] = boat_list[i][0]
            print_board(board)
            i += 1
      
    elif direc == "horizontal" or direc == "h": #When the boat is placed horizontally...
      print "Your %s will be placed horizontally." % boat_list[i]  
      #choose row that is an integer
      h_row_check = False
      while not h_row_check: 
          choose_row = 0 
          try:
            choose_row = int(raw_input("Choose Row 1-10: ")) - 1 
            h_row_check = True 
          except ValueError: 
            print "Non numerical entry. Try again." 
      #ensure validity of the row chosen.
      if choose_row not in range(0, len(board)): #Ensure row is within acceptable range
        print "You did not choose a row between 1 and 10"
      else: #choose column that is an integer
        h_col_check = False
        while not h_col_check: 
          choose_col = 0 
          try:
            choose_col = int(raw_input("Choose Column 1-10: ")) - 1 
            h_col_check = True 
          except ValueError: 
            print "Non numerical entry. Try again." 
        if choose_col not in range(0, len(board[0]) - dictionary[boat_list[i]] + 1): #Make sure there's room
          print "Column %s won't work. The %s needs %s spaces." % (choose_col + 1, boat_list[i], dictionary[boat_list[i]])
          print " "
        else: #Place Letters
          availability = True #Initialize availability check 
          for boat_size in range (0, dictionary[boat_list[i]]): #From 0 to length of ship 
            if board[choose_row][choose_col + boat_size] != "O": #If there's ever a space besides "O"pen water
              availability = False #This selection is unavailable 
              
          if availability == False:
            print "There was a boat in the way. Choose again." 
          else: #If there were only O's found 
            for boat_size in range (0, dictionary[boat_list[i]]):
              board[choose_row][choose_col + boat_size] = boat_list[i][0]
            print_board(board)
            i += 1
      
    else:
      print "something went wrong"
      print " "
  print "-------------------------"

#---- Computer Boat Placement ----#
def place_computer_ships(boat_list, dictionary): #Places all boats in dictionary on battleship board. Uses key values for size
  i = 0
  directions = ['v', 'h']
  while i < len(boat_list): #until each item in boat_list has been placed
    direc = random.choice(directions) #choose random direction from list "directions"
    
    if direc == 'v': #If random direction was vertically
    	#Place Letters Vertically
      rand_row = randint(0, len(board) - dictionary[boat_list[i]] - 1) #Ensures enough room for entire boat
      rand_col = randint(0, len(board[0]) - 1) #Choose any column
      availability = True #initialize availability check
      
      for boat_size in range (0, dictionary[boat_list[i]]): #From 0 to length of ship
        if board_p2[rand_row + boat_size][rand_col] != "O": #If there's ever a space besides "O"pen water
          availability = False #This selection is unavailable
          
      if availability == True: #If there were only O's found
        for boat_size in range (0, dictionary[boat_list[i]]): #From 0 to length of ship
          board_p2[rand_row + boat_size][rand_col] = boat_list[i][0] #Print first letter of that ship
        i += 1 #On to the next one
      
    elif direc == 'h': #Boat is randomly placed horizontally
      #Place Letters Horizontally
      rand_row = randint(0, len(board) - 1) #Choose any row
      rand_col = randint(0, len(board[0]) - dictionary[boat_list[i]] - 1) #Ensure enough room for entire boat
      availability = True #Initialize availability check
      
      for boat_size in range (0, dictionary[boat_list[i]]): #From 0 to length of ship
        if board_p2[rand_row][rand_col + boat_size] != "O": #If there's ever a space besides "O"pen water
          availability = False #This selection is unavailable

      if availability == True:#If there were only O's found
        for boat_size in range (0, dictionary[boat_list[i]]): #From 0 to length of ship
          board_p2[rand_row][rand_col + boat_size] = boat_list[i][0] #Print first letter of that ship
        i += 1 #On to the next one
    else:
      print "Orientation Selection Error"
  #print_board(board_p2)

#---- Coin toss for who goes first ----#
def coin_toss():
  print "A coin toss will select who goes first..."
  print "The results are in... "
  coin = randint(0,1)
  if coin == 0:
    return "computer"
  else:
    return "player"

#---- Begin firing ----#  
def begin_firing():
  game_on = True
  turn = coin_toss()
  print "The %s will go first" % turn
  while game_on:
    # Check if game is over
    if player_pieces == [0,0,0,0,0]:
        print "The computer has sunk your fleet. You've lost!"
        game_on = False
        break
    if computer_pieces == [0,0,0,0,0]:
        print "You've sunk the enemy fleet. Contrats. You've won!"
        game_on = False
        break
        
    if turn == 'player':
      print "Player's Turn: "
      # Player's Turn
      guess_row = int(raw_input("Guess Row: ")) - 1
      guess_col = int(raw_input("Guess Col: ")) - 1
      
      if board_p2[guess_row][guess_col] not in ['O','X','-',]:
        print "Hit!"
        for i in range(0, len(ship_list)):
          if board_p2[guess_row][guess_col] == ship_list[i][0]:
            computer_pieces[i] -= 1
            if computer_pieces[i] == 0:
              print "%s: Sunk!" % ship_list[i]
        board_p2[guess_row][guess_col] = "X"
        print_board(board)
        print "------------------------------"
        #print_board(board_p2)
        print " "
        turn = 'computer'
        
      elif board_p2[guess_row][guess_col] in ['X', '-']:
        print "Miss! You've already shot here!"
        print_board(board)
        print "------------------------------"
        #print_board(board_p2)
        print " "
        turn = 'computer'
      else: 
        print "Miss!"
        board_p2[guess_row][guess_col] = "-"
        print_board(board)
        print "------------------------------"
        #print_board(board_p2)
        print " "
        turn = 'computer'
        
    else:
      #Computer's Turn
      print "Computer's Turn:"
      guess_row = randint(0, len(board) - 1)
      guess_col = randint(0, len(board[0]) - 1)
      
      if board[guess_row][guess_col] not in ['O','X','-',]:
        print "Hit!"
        for i in range(0, len(ship_list)):
          if board[guess_row][guess_col] == ship_list[i][0]:
            player_pieces[i] -= 1
            if player_pieces[i] == 0:
              print "%s: Sunk!" % ship_list[i]
        board[guess_row][guess_col] = "X"
        print_board(board)
        print "------------------------------"
        #print_board(board_p2)
        print " "
        turn = 'player'
        
      elif board[guess_row][guess_col] in ['X', '-']:
        turn = 'computer'
        
      else: 
        print "Miss!"
        board[guess_row][guess_col] = "-"
        print_board(board)
        print "------------------------------"
        #print_board(board_p2)
        print " "
        turn = 'player'
    
#----------------------------- 
start_script()
# -> Prints instructions
#-----------------------------
place_ships(ship_list, ships)
# -> Places player's ships onto board
#-----------------------------
place_computer_ships(ship_list, ships) 
# -> Places computer's ships onto board_p2
#-----------------------------
begin_firing()
# -> Fires until a fleet is defeated
# -> Calls coin_toss() inside
#---------------------------------

#Changes:
# The computer has a board, but I don't want to see it. 
# The player takes shots, but prints them to the computer's board, which is hidden
#   - Need to have a blank board that shows player's shots and misses
