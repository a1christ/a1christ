#!/usr/bin/env python
# coding: utf-8

# Description:
# "Treasure Hunt" - a number guessing game with a limit of 10 tries. 
# The user recieves a series of prompts based on their input number, either to increase or decrease the value of their guess. If the user enters a number below 0 or above 100, they will recieve an out-of-bounds error message. A unique message will appear based on if the user guessses the correct number within 10 tries, or if they do not.
# 
#                     "Arghh, matey! Are ye ready to set course for the treasure number?
#                                 Find the treasure and collect your loot"

# IMPORT AND RUN THE CODE:

# In[1]:


from TestCodeScriptDOC import get_input
from TestCodeScriptDOC import outta_bounds
from TestCodeScriptDOC import user_guess
from TestCodeScriptDOC import user_win
from TestCodeScriptDOC import user_loss
from TestCodeScriptDOC import treasure_hunt
import random


# In[2]:


treasure_hunt()


# In[3]:


get_ipython().system('pytest CodeUnitTest.py')

Extra Credit:
1) background - one failed coding course, no prior experience!
2) In my code, I used six separate functions to properly run an exciting guessing game! The outputs for a win are unique everytie, by making use of the "random" function. Needless to say, I'm proud of the code I've written and creativity to make it fun and engaging.  
# #Credits: Given to Caitlin Connolly for helping me understand the importance of returns in functions, and debugging errors in code.
