# Dice sum probability calculator
# Författare: Viktor Johansson nygren
# Datum: 2024/08/21

from collections import Counter

def main():
    dice_sum = []
    user_input = input().split(" ")
    for i in range(1, int(user_input[0])+1):       
        for y in range(1, int(user_input[1])+1):
            dice_sum.append(i+y)
    most_common = Counter(dice_sum).most_common(len(dice_sum))
    for i in range(len(most_common)-1):
        if int(most_common[0][1]) == int(most_common[i][1]):
            print(most_common[i][0])

if __name__ == "__main__":
    main()
