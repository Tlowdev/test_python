#Start a list of designs to be printed.
unprinted_designs = ['picture frame', 'key chain', 'phone case']
printed_designs = []

#Simulate printing design, until none are left.
#Move each design into printed_designs after printing.
while unprinted_designs:
    current_design = unprinted_designs.pop()
    print(f'Printing: {current_design}')
    printed_designs.append(current_design)

#display printed_designs
print('\nThe following models have been printed:')
for completed in printed_designs:
    print(completed)

