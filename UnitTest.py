import TestCodeScript

#def test_get_input(): #This test requires mock - unsure how to run
#    assert callable(get_input)
#    assert isinstance(get_input(guess), int)
#    assert isinstance(get_input('hello'), str)
    
def test_outta_bounds():
    assert callable(outta_bounds)
    #assert isinstance(outta_bounds(guess), int)
    assert outta_bounds(-1) == "ARRGH, MATEY!! Yer outta bounds! Choose a number between 1 and 100!"
    assert outta_bounds(101) == "ARRGH, MATEY!! Yer outta bounds! Choose a number between 1 and 100!"
    
#def test_user_guess():
#    assert callable(user_guess)
#    assert isinstance(user_guess(guess, random_number), int)
#    assert user_guess(guess < random_number) == "AVAST YE! Guess higher!" #NEW
#    assert user_guess(guess > random_number) == "AVAST YE! Guess lower!"  #NEW
    
#def test_user_win():
#    assert callable(user_win)
#    assert isinstance(user_win(guess, random_number), int)
#    assert user_win(guess == random_number) == "SHIVER ME TIMBERS! Ye found the treasure!" #NEW EDIT 
#    assert user_win(guess == random_number) == random.choice(statements) #NEW EDIT
    
#def test_user_loss():
#    assert callable(user_loss)
#    assert isinstance(user_loss(guess, random_number), int)
#    assert user_loss(guess != random_number) == "YARRGH! Ye didn’t find tha booty this time. The treasure number was " + str(random_number) + "." + " Try again, matey!"
    
#def test_treasure_hunt(): #This test requires mock - unsure how to run
#    assert callable(treasure_hunt)
#    assert isinstance(treasure_hunt(), int) #new
#   assert 
    
#END UNIT TEST