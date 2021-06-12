def get_input(): #asks user for an input guess
    """ Get user input.
    Parameters
    ----------
    guess: int
        user guess
    Returns
    -------
    guess: int
        user guess
    """   
    #returns an error stament if an input is not an integer
    try:
        guess = input("FIND THE TREASURE! enter a number between 1 and 100: ")
        guess = int(guess) 
        return guess
        
    except ValueError: 
        print("ARGHH! That ain't a number, try again matey!")



def outta_bounds(guess):
    """ Determines if user guess is < 0 or > 100.
    Parameters
    ----------
        guess: int
            user guess
    Returns
    -------
        guess: boolean
            if guess is <0 or >100
    """
    
    #returns an error if input is < 0 or > 100 
    if type(guess) != int: 
        return ("ARGHH! That ain't a number, try again matey!")
    elif guess < 0 or guess > 100:
        print("ARRGH, MATEY!! Yer outta bounds! Choose a number between 1 and 100!")
        return True 
        
 
 
def user_guess(guess, random_number):
    """ Gives feedback to the user based on their guess.
    Parameters
    ----------
        guess: int
            user guess
        random_number: int
            number to guess
    Returns
    -------
        NONE
    """
    
    #prompts the player to adjust their input
    if type(guess) != int:
        return ("ARGHH! That ain't a number, try again matey!")
    elif guess < random_number:
        print("AVAST YE! Guess higher!")
    elif guess > random_number:
        print("AVAST YE! Guess lower!")
    #return breaks the loop
    return 
    


def user_win(guess, random_number):
    """ Determine user win.
    Parameters
    ----------
        guess: int
            user guess
        random_number: int
            number to guess
    Returns
    -------
        plunder: str
            one of three win statements
        guess: boolean
            user guess
    """
    
    #returns a win statement and prize statement if random number is guessed
    import random
    statements = ["YO HO HO!! Ye plunder yields fifty gold pieces!", 
                  "YO HO HO!! Ye plunder yields twenty gold pieces!", 
                  "YO HO HO!! Ye plunder yields ten gold pieces!"]
    plunder = random.choice(statements)
    
    if guess == random_number:
        print("SHIVER ME TIMBERS! Ye found the treasure!") 
        #returns one of three prize statements
        print(plunder)
        #the game ends here with a win
        return False
        
  
  
def user_loss(guess, random_number):
    """ Determine user loss.
    Parameters
    ----------
        guess: int
            user guess
        random_number: int
            number to guess
    Returns
    -------
        out_loss: str
            loss statement
    """
    
    #returns a loss statemnt if random number is not guessed
    while guess != random_number:
        out_loss = "YARRGH! Ye didn’t find tha booty this time. The treasure number was " + str(random_number) + "." + " Try again, matey!"
        #the game ends here with a loss
        return out_loss 
        

#module to run the guessing game
def treasure_hunt():
    """function to run game
    Parameters
    ----------
        guess: int
            user guess
    Return
    ------
        plunder: str
        loss: str
    """
    
    import random
    tries = 0
    random_number = random.randint(1, 100)
    
    while tries < 10:
        
        #get input guess from user
        guess = get_input()
        tries = tries + 1 #This line was moved here from previous function in a collab w/ Caitlin C. Uses one try for each input
        
        
        #check if guess is within bounds
        bounds = outta_bounds(guess)
        

        #if guess is not random_number
        statement = user_guess(guess, random_number)

        
        #if guess is random_number
        break_loop = user_win(guess, random_number) #this code line was created in a collab w/ Caitlin C.
        if break_loop == False:
            #return win - loop ends game
            return 
        
        
    #outside while-loop #if user does not guess the number within 10 tries
    loss = user_loss(guess, random_number)
    return loss