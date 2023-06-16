import random

MAX_LINES = 3 #max rows to bet on

MIN_BET= 1
MAX_BET= 100

ROWS_LINES=3 #3x3 slot machine
COLUMNS_REELS=3

symbol_reel={  #Number of symbols on each reel
    "A":2,
    "B":4,
    "C":6,
    "D":8
}

line_multiplier={  #Multiplier of each symbol if line is made. 
                   #low freq = rare = higher multiplier 
    "A":10,
    "B":7,
    "C":5,
    "D":3
}

"""
Functions defined: 

slotmachine_spin
print_slotmachine } **core logic of project** >> dont mug >> to implement this matrix problem visualize in A4 sheet and write the necessary algo and then code
check_winnings

deposit
get_no_of_lines } getting the desired whole number input from users
get_bet

spin >> to run code multiple times and call the relevant functions
main >> to call all the functions

"""






def slotmachine_spin(rows,cols,symbols): #implement slot machine and make it spin >> **core logic**, rows and cols show the visible 3x3 slot machine
    all_symbols=[] # using below loop to make list [A,A,B,B,B,B.......] ie the possible items in the reel
    for symbol,symbol_count in symbols.items(): #*dict iteration using items()
        for _ in range(symbol_count):           #* using _ instead if i as dont need index of iteration
            all_symbols.append(symbol)




    columns=[] #a nested list/matrix is made up of multiple rows but here we will use it for multiple columns indicating visible reel

    """
__
Reels >> columns[]
A    =  [[A,B,C],[A,A,D],.....]
B
C
__

    """
    for _ in range(cols): #making the ramdom reel after spin
        column=[]
        current_symbols=all_symbols[:] #*always copy lists like this else it leads to reference and update on one leads to update on other since it stores multi Data >> DS
        for _ in range(rows):
            value=random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)           # We are generating vertical columns here
        columns.append(column)             # Storing these columns as rows  

    return columns

def print_slotmachine(columns):
    
    for row in range(len(columns[0])): #transposing the matrix >> i j made j i
        for i,column in enumerate(columns):
            
            if i != len(columns)-1:    #printing in slot machine fashion
                print(column[row], "|", end="")
            else:
                print(column[row])


def check_winnings(columns,lines, bet, multiplier):
    winnings=0
    winning_lines=[]
    for line in range(lines):
        symbol=columns[0][line] # first element of row
        for column in columns:
            symbol_to_check=column[line]
            if  symbol != symbol_to_check:
                break #*breaks the inner loop >> else not executed
        else:#* this is executed only if loop runs without breaking  
                winnings +=multiplier[symbol]*bet
                winning_lines.append(line+1)
    
    return winnings,winning_lines










def deposit():
    while True:   #Using While True and break so that loop runs till we get the desired input which is value > 0
        amount=input("What would you like to deposit? $")       
        if amount.isdigit():                                   
            amount=int(amount)
            if amount > 0:
                break
            else:    
                print("Amount must be greater than 0.")
        else:
            print("Please enter a valid amount")
    return amount

def get_no_of_lines():
    while True:   
        lines=input("Enter the number of lines to bet on (1-"+str(MAX_LINES)+")? : ")    
        if lines.isdigit():                                   
            lines=int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:    
                print("Number of lines should be between 1 and "+str(MAX_LINES))
        else:
            print("Please enter a valid number")
    return lines

def get_bet():
    while True:   
        bet=input("Enter the amount you want to bet on each line ")    
        if bet.isdigit():                                   
            bet=int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:    
                print(f"The bet should be between ${MIN_BET} - ${MAX_BET}")
        else:
            print("Please enter a valid amount")
    return bet










def spin(balance): # main functions shifted here to run the program multiple times till we want

    lines=get_no_of_lines()
   
    while True:
        bet=get_bet()
        total_bet= lines*bet
        if total_bet>balance:
            print("You dont have sufficient balance")
        else:
            break

    print(f"You are betting ${bet} on {lines} lines so your total bet is {total_bet}")

    slots=slotmachine_spin(ROWS_LINES,COLUMNS_REELS,symbol_reel)
    print_slotmachine(slots)

    winnings, winning_lines= check_winnings(slots,lines,bet, line_multiplier)
    print(f"You won ${winnings}.")
    print(f"You won on lines: ", *winning_lines) #* slash op >> removes list [ ] ,  and print values 
    return winnings-total_bet




def main(): #to call all the functions
    balance= deposit()

    while True:
        print(f"Your current balance is ${balance}.")
        start=input("Press ENTER to play (q to quit).")
        if start == "q" or balance<=0:
            break
        balance +=spin(balance)
        

    print(f"Your checkout balance is ${balance}")





main()    


