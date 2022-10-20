def get_formatted_name(first, last, middle = None):
    if middle:
        full_name = f"{first} {middle} {last}"
    else:
        full_name = f"{first} {last}" 
    return full_name.title()
    #formatted_name = full_name.title()
    #print(formatted_name)

