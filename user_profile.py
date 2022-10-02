def build_user(first_name, last_name, **user_info):
    """Build a dictionary containing info about the user"""
    user_info['first'] = first_name
    user_info['last']  = last_name
    return user_info

users_profile = build_user(
    'Scooby', 'Doo',
    age = 7,
    hair = 'brown',
    eye = 'brown'

)
print(users_profile)