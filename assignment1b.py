# This program calculates the number of poker chips
# given with user input

# Recall what Poker chips colors and values are there:
# Yellow = $1000, Purple = $500, Black = $100
# Blue = $50, Green = $25, Red = $5, White = $1

# function to output the results of the distribution of chips
def output(money, y, p, bk, bl, g, r, w):
    print()
    print("Cash: $" + str(money))
    print("yellow chips: " + str(y))
    print("purple chips: " + str(p))
    print("black chips: " + str(bk))
    print("blue chips: " + str(bl))
    print("green chips: " + str(g))
    print("red chips: " + str(r))
    print("white chips: " + str(w))


# function to calculate the number of chips possible in cash
def calculateChips(cash, chipVal):
    # check possible case where cash is less than value that can fit
    if cash < chipVal:
        return 0
    # calculate the number of chips that fit in cash value
    chips = 0
    while cash >= chipVal:
        cash = cash - chipVal
        chips += 1
    return chips


# function to obtain user input for amount of cash to use
def getCash():
    print("This program calculates the number of chips present in a given cash value.")
    cash = int(input("Enter a positive number (amount of money) to calculate with: "))
    while cash < 0:
        cash = int(input("Please enter a positive value: "))
    return cash


# function to drive the program
def main():
    cash = getCash()
    # make a separate and modifiable cash variable for calculation
    c = cash
    # As the program calculates the chips that fit in cash value, reduce cash
    # value to fit in more chips as needed as a little as possible
    ychip = calculateChips(c, 1000)
    c -= (1000 * ychip)
    pchip = calculateChips(c, 500)
    c -= (500 * pchip)
    bkchip = calculateChips(c, 100)
    c -= (100 * bkchip)
    blchip = calculateChips(c, 50)
    c -= (50 * blchip)
    gchip = calculateChips(c, 25)
    c -= (25 * gchip)
    rchip = calculateChips(c, 5)
    c -= (5 * rchip)
    wchip = calculateChips(c, 1)
    c -= (1 * wchip)
    # print out the results
    output(cash, ychip, pchip, bkchip, blchip, gchip, rchip, wchip)


# call main to run the program
main()
