# Dice sum probability calculator
# Författare: Viktor Johansson nygren
# Datum: 2024/08/21

from collections import Counter

def main():
    dice_sum = []
    user_input = input("Skriv antal sidor av upp till 2st tärningar du vill kasta. Endast från 4 till 20 sidor är tillåtna\n").split(" ")
    if len(user_input) > 2:
        print("Max 2st tärningar får kastas")
        main()
    for i in user_input:
        x = 1
        try:
            i=int(i)
        except:
            print("Endast siffror")
            main()
        if i < 4:
            print("Endast tärningar med sidor från 4 till 20")
            main()
        elif i > 20:
            print("Endast tärningar med sidor från 4 till 20")
            main()
    for i in range(1, int(user_input[0])+1):       
        for y in range(1, int(user_input[1])+1):
            dice_sum.append(i+y)
    most_common = Counter(dice_sum).most_common(len(dice_sum))
    print(most_common)
    for i in range(len(most_common)-1):
        if int(most_common[0][1]) == int(most_common[i][1]):
            print(most_common[i][0])

if __name__ == "__main__":
    main()
