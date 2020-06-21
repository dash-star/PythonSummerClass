##
# INSTRUCTIONS:
# 1. DO NOT rename the function names or change the parameters
# 2. Feel free to write helper functions in the HELPER FUNCTIONS area
# 3. DO NOT write new classes to help solve the problems
# 4. Make use of 'sandbox.py' to test/debug your code
# 5. I will test your code using my user generated files
# 6. Make use of the group chat & ask questions in the group chat
#
#
#


# IMPORTS
import math

# HELPER FUNCTIONS
# part1 helper function
def isOddFactor(num1, num2):
    # do we have a one? if so, return false, else do comparison
    if num1 == 1 or num2 == 1:
        return False
    return num1 % 2 == 1 or num2 % 2 == 1


# part2 helper function 1
# returns a roman numeral based on numbers
# from the tens place and base
def baseTenRomanNum(num):
    if num == 10:
        return "X"
    elif num == 9:
        return "IX"
    elif num == 8:
        return "VIII"
    elif num == 7:
        return "VII"
    elif num == 6:
        return "VI"
    elif num == 5:
        return "V"
    elif num == 4:
        return "IV"
    elif num == 3:
        return "III"
    elif num == 2:
        return "II"
    else:  # num == 1
        return "I"


# part2 helper function 2
# returns a roman numeral based on numbers
# from the hundreds and tens place
def baseHundredRomanNum(num):
    if num >= 100:
        return "C"
    elif num >= 90:
        return "XC"
    elif num >= 80:
        return "LXXX"
    elif num >= 70:
        return "LXX"
    elif num >= 60:
        return "LX"
    elif num >= 50:
        return "L"
    elif num >= 40:
        return "XL"
    elif num >= 30:
        return "XXX"
    elif num >= 20:
        return "XX"
    else:  # num >= 10
        return "X"


# part2 helper function 3
# returns a roman numeral based on numbers
# from the thousands and hundreds place
def baseThousandRomanNum(num):
    if num >= 1000:
        return "M"
    elif num >= 900:
        return "CM"
    elif num >= 800:
        return "DCCC"
    elif num >= 700:
        return "DCC"
    elif num >= 600:
        return "DC"
    elif num >= 500:
        return "D"
    elif num >= 400:
        return "CD"
    elif num >= 300:
        return "CCC"
    elif num >= 200:
        return "CC"
    else:  # num >= 100
        return "C"


# part3 helper function
# returns a number that encodes the letter passed to parameter
def charToNum(char):
    if char == 'a' or char == 'b' or char == 'c':
        return "2"
    elif char == 'd' or char == 'e' or char == 'f':
        return "3"
    elif char == 'g' or char == 'h' or char == 'i':
        return "4"
    elif char == 'j' or char == 'k' or char == 'l':
        return "5"
    elif char == 'm' or char == 'n' or char == 'o':
        return "6"
    elif char == 'p' or char == 'q' or char == 'r' or char == 's':
        return "7"
    elif char == 't' or char == 'u' or char == 'v':
        return "8"
    elif char == 'w' or char == 'x' or char == 'y' or char == 'z':
        return "9"
    else:  # char is a space character
        return "0"


##
# write a function that adds the numbers between x and y inclusive
# return the sum of those numbers
# #
def part0(x, y):
    # check precondition: only +ve nums and 0
    if x < 0 or y < 0:
        return -1
    # find out which number is larger to perform with for
    # getting all numbers in range in order
    num1 = int
    num2 = int
    if x < y:
        num1 = x
        num2 = y
    else:
        num1 = y
        num2 = x
    # perform the operation of getting all numbers between x and y
    sum = 0
    for i in range(num1, num2 + 1):
        sum += i
    return sum


##
# write a function that checks if a  number is a perfect even
# this means that the number has no odd factors except 1
# returns True/False
def part1(num):
    # is num an even number and a non-negative?
    # if zero, return false since zero is not a perfect even
    if num % 2 != 0 or num <= 0:
        return False
    # check what factors there are by starting at number and 1
    # use variables to loop through all possible factors
    lowfact = 1
    highfact = num
    # calculate all possible factors until we reach a number already covered
    # or until we hit an odd numbered factor
    while lowfact < highfact:
        # is this a perfect division? Perfect div Means a factor is present, no remainder
        if num % lowfact == 0:
            # A factor! Get product and check if product or low factor is an odd factor
            product = num / lowfact
            if isOddFactor(lowfact, product):
                # Odd factor present! Return false
                return False
            else:
                # either a 1 in factor or both are even. Increment lowfact and set
                # product as the highest factorial to compare for looping
                lowfact += 1
                highfact = product
        else:
            # Remainder occured. Skip this number and move on to the next
            lowfact += 1
    # Got through all the factors and were all even
    return True


##
# convert a number to a roman numeral string
# the number should be in range [0, 1000]
#
# returns uppercase string roman numeral string representation of num
# https://www.britannica.com/topic/Roman-numeral
# RECALL (from Britannica):
# Roman numeral, any of the symbols used in a system of numerical notation based on the ancient Roman system.
# The symbols are I, V, X, L, C, D, and M, standing respectively for 1, 5, 10, 50, 100, 500, and 1,000
# in the Hindu-Arabic numeral system. A symbol placed after another of equal or greater value adds its value;
# e.g., II = 2 and LX = 60. A symbol placed before one of greater value subtracts its value; e.g., IV = 4, XL = 40,
# and CD = 400. A bar placed over a number multiplies its value by 1,000.
def part2(num):
    # check preconditions and special cases
    if num < 0 or num > 1000:
        return "NaN"
    elif num == 0:
        return ""
    # # base cases, are they needed?
    # elif num == 1 or num == 5 or num == 10 or num == 50 or num == 100 or num == 500 or num == 1000:
    #     return getBaseRomanNumeral(num)
    # find what roman numeral this number is
    # make n variable for easy modification
    result = str("")
    n = num
    # check for the following places: thousands, hundreds, base 10, in order
    # if present, assign the roman numeral to an equivalent base 10 value
    if (n / 100) >= 1.0:
        # check for thousands place
        result += baseThousandRomanNum(n)
        tho = n / 100
        tho = math.floor(tho)
        n -= tho * 100
    if (n / 10) >= 1.0:
        # check for hundreds place
        result += baseHundredRomanNum(n)
        hun = n / 10
        hun = math.floor(hun)
        n -= hun * 10
    # check for tens place and/or base place if non zero exist at end of number
    if n > 0:
        result += baseTenRomanNum(n)
    return result


##
# Write a T9 Encryption method that takes a string parameter
# and converts it to a numerical value using a phone keypad as a cypher
# @par
# abc -> 2
# def -> 3
# ghi -> 4
# jkl -> 5
# mno -> 6
# pqrs -> 7
# tuv -> 8
# wxyz -> 9
# <space> ->0
# needs to return a encoded string
# Ex: part3("alan") = 2526
def part3(original):
    # make lowercase for ease of workability
    lowercase = str.lower(original)
    result = str("")
    # loop through the entire string and send the character from position i to encoder
    for i in range(0, len(lowercase)):
        result += charToNum(lowercase[i])
    # convert result string to a number sequence and return the result
    result = int(result)
    return result


##
# Check if 2 texts are isomorphic (each letter maps to another)
# ex: paper and title are isomorphic
# p -> t
# a -> i
# p -> t
# e -> l
# r -> e
# returns True/False
def part4(text1, text2):
    # check the lengths of the words.
    # if lengths are equal, they are possibly isomorphic, else return false
    if len(text1) != len(text2):
        return False
    # get array to map each letter to another. Based on mapping of text1
    list = dict()
    for i in range(0, len(text1)):
        char1 = text1[i]
        char2 = text2[i]
        # does char1 (text1 letter) already have a mapping?
        if char1 in list:
            # exists in the dictionary/pair. Is this one matching?
            if list.get(char1) != char2:
                # different mapping! return false
                return False
        else:
            # new letter! add it to dictionary to signify a mapping
            list[char1] = char2
    # if code is here, that means that word set is isomorphic, so return true
    return True


##
# check if a string is a palindrome: (spelt the same both ways)
# ignore the case
# part5(car): False
# part5(bob): True
# returns True/False
#
# ##
def part5(text):
    # Note: palindrome check is case sensitive
    # loop through lowercase text in front and use int variable to loop backwards as well
    # decrement length by one to avoid index out of bounds error
    backPos = len(text) - 1
    for i in range(0, len(text)):
        if text[backPos] != text[i]:
            return False
        else:
            backPos -= 1
    return True


##
# write the combination formula
# c(n, k) = n! / ((n-k)! * k!)
# returns the combination of 2 number
# needs to work for large numbers and cannot timeout
# ##
def part6(n, k):
    # precondition statement
    if k > n:
        return -1
    # do math
    numerator = math.factorial(n)
    denominator = math.factorial(n - k) * math.factorial(k)
    return numerator / denominator


##
# write the permutation formula
# p(n, k) = n! / ((n-k)!)
# returns the permutation of 2 number
# needs to work for large numbers and cannot timeout
# ##
def part7(n, k):
    # precondition statement
    if k > n:
        return -1
    # do math
    numerator = math.factorial(n)
    denominator = math.factorial(n - k)
    return numerator / denominator
