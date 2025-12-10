'''
Title: Rolling Dice Function with Error Handling
Description: This script defines a function to roll dice, ensuring that the inputs are integers. If not, it raises a ValueError with a descriptive message.
Author: Guy Friley
Date: 12/10/2025
'''

# This is not working. Will need to revisit later. Committing for now. For reference.
def roll_dice(n, d):
    num_dice = int(n)
    dice_type = int(d)

    if not isinstance(num_dice, int):
        raise ValueError("Number of Dice is not a number!")
    if not isinstance(dice_type, int):
        raise ValueError("Dice Type is not a number!")
    
roll_dice(2, 6)
roll_dice('two', 6)