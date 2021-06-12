def get_input():
    try:       
        guess = input("FIND THE TREASURE, enter a number between 1 and 100!: ")
        guess = int(guess)
        return guess
        
    except ValueError: 
        print("ARGHH! That ain't a number, try again matey!")

#def test_get_input():
#    assert callable(get_input)
#    assert isinstance(get_input(guess), int)
#    assert isinstance(get_input('hello'), str)
    


    
def outta_bounds(guess):
    if type(guess) != int:
        return ("ARGHH! That ain't a number, try again matey!")
    elif guess < 0 or guess > 100:
        return ("ARRGH, MATEY!! Yer outta bounds! Choose a number between 1 and 100!")

def test_outta_bounds():
    assert callable(outta_bounds)
    assert outta_bounds(-1) == "ARRGH, MATEY!! Yer outta bounds! Choose a number between 1 and 100!"
    assert outta_bounds(101) == "ARRGH, MATEY!! Yer outta bounds! Choose a number between 1 and 100!"


    

#def user_guess(guess, random_number):
#    if type(guess) != int: #new
#        return ("ARGHH! That ain't a number, try again matey!") #new
#    elif guess < random_number:
#        print("AVAST YE! Guess higher!")
#    elif guess > random_number:
#        print("AVAST YE! Guess lower!")
#    return 

#def test_user_guess():
#    assert callable(user_guess)
#    assert isinstance(user_guess(guess, random_number), int)
#    assert user_guess(guess < random_number) == "AVAST YE! Guess higher!" #NEW
#    assert user_guess(guess > random_number) == "AVAST YE! Guess lower!"  #NEW
    
   
 
    
#def user_win(guess, random_number):
#    import random
#    statements = ["YO HO HO!! Ye plunder yields fifty gold pieces!", 
#                  "YO HO HO!! Ye plunder yields twenty gold pieces!", 
#                  "YO HO HO!! Ye plunder yields ten gold pieces!"]
#    plunder = random.choice(statements)
    
#    if guess == random_number:
#        print("SHIVER ME TIMBERS! Ye found the treasure!") 
#        print(plunder) #returns one of three prize statements
#        return False #the game ends here with a win

#def test_user_win():
#    assert callable(user_win)
#    assert isinstance(user_win(guess, random_number), int)
#    assert user_win(guess == random_number) == "SHIVER ME TIMBERS! Ye found the treasure!"
#    assert user_win(guess == random_number) == random.choice(statements)

    


def user_loss(guess, random_number):
    while guess != random_number:
        out_loss = "YARRGH! Ye didn’t find tha booty this time. The treasure number was " + str(random_number) + "." + " Try again, matey!"
        return out_loss
    
#def test_user_loss():
#    assert callable(user_loss)
#    assert isinstance(user_loss(guess, random_number), int)
#    assert user_loss(guess != random_number) == "YARRGH! Ye didn’t find tha booty this time. The treasure number was " + #str(random_number) + "." + " Try again, matey!"




def treasure_hunt():
    import random
    tries = 0
    random_number = random.randint(1, 100)
    
    while tries < 10:
        
        guess = get_input()
        tries = tries + 1 
        
        bounds = outta_bounds(guess)
        
        statement = user_guess(guess, random_number)

        break_loop = user_win(guess, random_number)
        if break_loop == False:
            return
        
    loss = user_loss(guess, random_number)
    return loss

def test_treasure_hunt():
    assert callable(treasure_hunt)
    assert isinstance(treasure_hunt(), int)
    
# END UNIT TEST