import random
import time
import tkinter as tk
minimum = 1
maximum = 6

# ------ Global variables---------
roll_again = True

def tui():
    while roll_again:
      print("Rolling dice .... ")
      time.sleep (random.randint (1,4))#wait between 1 to 4 seconds randomly
      result = random.randint(minimum, maximum)
      print(result)
      roll_again = False
      repeater = input("Do you want to roll again :(yes or no) ? : ").lower()
      while repeater not in ["yes", "no"]:repeater = input("Invalid Input. Please try again : ").lower()
      if repeater == "yes":
        roll_again = True
      elif repeater == "no":
        roll_again = False
      print("Have a good day.")

def gui():
    root = tk.Tk()
    label = tk.Label(root, text= "Random Number")
    label.pack()
    def roll():
        while roll_again:
            time.sleep (random.randint (1,4))#wait between 1 to 4 seconds randomly
            random_number = random.randint(minimum, maximum)
            label.config(text= random_number)

            root.update()

    roll()
    # root.after(0, roll)
    # root.mainloop()

gui()
