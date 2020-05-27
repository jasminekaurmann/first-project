import random
money = 100

def coin_flip(guess, bet):
    global money
    #Bet should be greater than 0
    if bet <= 0:
        print("Your bet needs to exceed 0 to play.")
        return 0

    result=random.choice(['heads', 'tails'])
    is_correct = (guess == result)

    if is_correct :
        money = money + bet
        print(f"You guessed {guess} and the coin landed on {result}. You won ${bet}, now you have ${money}.")
    else:
        money = money - bet
        print(f"You guessed {guess} and the coin landed on {result}. You lost ${bet}, now you have ${money} loser:p.")

while True:

    user_guess = input("Heads or Tails?")
    user_guess = user_guess.lower()
    user_guess = user_guess.strip()

    user_bet = input(f"You have ${money}. How much are you willing to bet?")
    user_bet = int(user_bet)

    coin_flip(user_guess, user_bet)
