import tiktok
import proxies
import creator
import account
import time 
import json

# Load configuration from config.json
with open('config.json') as f:
    config = json.load(f)

# Import necessary functions/classes from modules
from tiktok import accounts 
from account import email, password, username 

# Creating accounts 
def accountCreator():
    x = creator.newAccount(tiktok, email, password, username) 
    x.append()
    x.changeAvatar(RandomPictureNet) 
    x.subTo(MostFolloweds) 

# Sub to your accountdef subBot(x):
    if x.banned:
        print('Account is banned')
    elif x.doesNotExist:
        print('Skipped account')
    else:
        x.subTo(config['acc'])
        x.pass_and_return()  # Corrected syntax for calling a function
        print('x.followers + 1') 

# Call functions
accountCreator()
subBot(x)
