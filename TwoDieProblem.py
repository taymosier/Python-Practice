#This program will calculate the probability of rolling a certain number when rolling two x-sided die

number_of_sides_first_dice = list(range(6))
number_of_sides_second_dice = list(range(6))
total_roll_combinations_equal_to_target = 0
target_number = 9

for x in number_of_sides_first_dice:
    for y in number_of_sides_second_dice:
        if (x+1)+ (y+1) == target_number:
            total_roll_combinations_equal_to_target = total_roll_combinations_equal_to_target + 1

total_number_of_possible_combinations = len(number_of_sides_first_dice)*len(number_of_sides_second_dice)

possibility_of_rolling_target_number = (total_roll_combinations_equal_to_target/total_number_of_possible_combinations)*100

print(str(possibility_of_rolling_target_number))