# lesson 1
"""
I have a lot of boxes of eggs in my fridge and I want to calculate how many omelettes I can
make. Write a program to calculate this.
Assume that a box of eggs contains six eggs and I need four eggs for each omelette, but I should be
able to easily change these values if I want. The output should say something like "You can make 9
omelettes with 6 boxes of eggs".
"""
eggs_in_a_box = input("How many eggs a box has?")
boxes_in_the_fridge = input(" How many boxes of eggs are in the fridge?")
eggs_for_an_omlette = input("How many eggs do you need to cook an omlette?")
number_of_omlettes = int(eggs_in_a_box) * int(boxes_in_the_fridge) / int(eggs_for_an_omlette)
print("You can cook {} omlettes with {} boxes of eggs".format(number_of_omlettes, boxes_in_the_fridge))