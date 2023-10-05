# import random
import random


def rolld6():
    d6 = [1, 2, 3, 4, 5, 6]
    d6_result = random.choice(d6)
    return d6_result


def rolld4():
    d4 = [1, 2, 3, 4]
    d4_result = random.choice(d4)
    return d4_result


def rolld8():
    d8 = [1, 2, 3, 4, 5, 6, 7, 8]
    d8_result = random.choice(d8)
    return d8_result


def rolld10():
    d10 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    d10_result = random.choice(d10)
    return d10_result


def roll4xd6():
    results = []
    for d in range(1, 5):
        d = rolld6()
        results.append(d)
    return results


def get_character_stat(lista):
    highest_scores = []
    # print("Minimum is: %s" % str(min(lista)))
    # print("Removing the smallest element: %s" % str(min(lista)) )
    lista.remove(min(lista))
    highest_scores = lista
    # print("Remaining scores: %s" % highest_scores)
    attribute = sum(highest_scores)
    return attribute



# def main():
#    print("Rolling D&D stats")
#    dice_rolls = roll4xd6()
#    print("Rolled 4D6: %s" % str(dice_rolls))
#    selected_rolls = select_highest(dice_rolls)
#    # print(selected_rolls)
#    print("Stat #1: %s" % str(sum(selected_rolls)))
