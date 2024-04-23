from replit import clear
clear()
def bill_clac():
    sum = 0
    finished = False
    while not finished:
        rate = input("Enter the price of the item (press q to quit the program) \n").lower()
        
        if rate == "q":
            finished = True
            print(f"The total bill is {sum}")
            restart = input("Do you want to restart the program?(yes/no) ").lower()
            if restart == "yes":
                clear()
                bill_clac()
        elif not rate == "q":
            sum = sum+int(rate)
            print(f"Your bill so far has been {sum}. Thanks for shopping with us.")
bill_clac()