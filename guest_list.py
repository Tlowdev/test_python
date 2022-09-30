guest_list = ['Bob', 'John', 'Batman']
print(f"Welcome {guest_list[0]} we invite you to a dinner at the ball.")
print(f"Welcome {guest_list[1]} we invite you to a dinner at the ball.")
print(f"Welcome {guest_list[2]} we invite you to a dinner at the ball.")

guest_na = 'Batman'
print(f"It's unfortunate but {guest_na} will not be able to attend.")

guest_list.remove(guest_na)
guest_list.append('Alfred')

print(f"Welcome {guest_list[0]} we invite you to a dinner at the ball.")
print(f"Welcome {guest_list[1]} we invite you to a dinner at the ball.")
print(f"Welcome {guest_list[2]} we invite you to a dinner at the ball.")

print("Excuse me, we have found a bigger table with more seats")

guest_list.insert(0, 'Prince')
guest_list.insert(2, 'Woman')
guest_list.append('Invisible man')

print(f"Welcome {guest_list[0]} we invite you to a dinner at the ball.")
print(f"Welcome {guest_list[1]} we invite you to a dinner at the ball.")
print(f"Welcome {guest_list[2]} we invite you to a dinner at the ball.")
print(f"Welcome {guest_list[3]} we invite you to a dinner at the ball.")
print(f"Welcome {guest_list[4]} we invite you to a dinner at the ball.")
print(f"Welcome {guest_list[5]} we invite you to a dinner at the ball.")

print("I'm sorry to inform you but the table won't arrive on time and we can only have two guests.")

popped_guest1 = guest_list.pop()
print(f"I'm sorry {popped_guest1} but there is no more space at the moment.")

popped_guest2 = guest_list.pop()
print(f"I'm sorry {popped_guest2} but there is no more space at the moment.")

popped_guest3 = guest_list.pop()
print(f"I'm sorry {popped_guest3} but there is no more space at the moment.")

popped_guest4 = guest_list.pop()
print(f"I'm sorry {popped_guest4} but there is no more space at the moment.")

print(f"Sorry for the inconvinence, {guest_list} welcome to the ball.")