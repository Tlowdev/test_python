
def print_models(unprinted_designs, printed_designs):
    """
    Simulate printing design, until none are left.
    Move each design into printed_designs after printing.
    """
    while unprinted_designs:
        current_design = unprinted_designs.pop()
        print(f'Printing: {current_design}')
        printed_designs.append(current_design)

def completed_models(printed_designs):
    """display printed_designs"""
    print('\nThe following models have been printed:')
    for completed in printed_designs:
        print(completed)

#Start a list of designs to be printed.
unprinted_designs = ['picture frame', 'key chain', 'phone case']
printed_designs: list[str] = []

#Call the function
print_models(unprinted_designs, printed_designs)
completed_models(printed_designs) 