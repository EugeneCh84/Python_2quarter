from random import randint

def input_dat(player):
    x = int(input(f"{player}, Enter number of candies, from 1 till 28: "))
    while x < 1 or x > 28:
        x = int(input(f"{player}, Enter correct number of candies: "))
    return x


def p_print(player, k, counter, candies):
    print(f"Turn {player}, he has {counter} candies.  {candies} left.")

player1 = input("Enter player 1 name: ")
player2 = input("Enter player 2 name: ")

flag = randint(0,2) # флаг очередности
if flag:
    print(f"First turn is {player1}")
else:
    print(f"First turn is {player2}")

counter1 = 0 
counter2 = 0
candies = 2021
while candies > 28:
    if flag:
        k = input_dat(player1)
        counter1 += k
        candies -= k
        flag = False
        p_print(player1, k, counter1, candies)
    else:
        k = input_dat(player2)
        counter2 += k
        candies -= k
        flag = True
        p_print(player2, k, counter2, candies)

if flag:
    print(f"{player1}  is a Winner")
else:
    print(f"{player2}  is a Winner")