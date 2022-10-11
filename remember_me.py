import json
#Load the username, if it has been stored previously.
#otherwise, prompt for username and store it.
def get_stored_username():
    """Get stored username if available"""
    file_name = 'username.json'   
    try:
        with open(file_name) as f:
          username = f.read()
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """Prompt for new username"""
    username = input("what is your username? ")
    file_name = 'username.json'
    with open(file_name, 'w') as f:
        json.dump(username, f)
    return username

def greet_user():
    """Greet user by name"""
    username = get_stored_username()
    if username:
        print(f"Welcome back, {username}!")
    else:
       username = get_new_username()
       print(f"We will remember you when you come back, {username}!")    
greet_user()



    

