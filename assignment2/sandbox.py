from assignment2.challenges import *

# function to test part 0
def test0():
    print("*****  Testing Part 0 *****")
    print("Test 1, 1-2. Output: " + str(part0(1, 2)))  # Expect 3
    print("Test 2 1-5. Output: " + str(part0(1, 5)))  # Expect 15
    print("Test 3, 1-10. Output: " + str(part0(1, 10)))  # Expect 55
    print("Test 4, 1-100. Output: " + str(part0(1, 100)))  # Expect 5050
    print("Test 5, 1-3. Output: " + str(part0(0, 3)))  # Expect 6
    print("Test 6, 0-0. Output: " + str(part0(0, 0)))  # Expect 0
    # what about negative numbers? No negative numbers, only 0 and above
    print("Test 7, (-4)-(0). Output: " + str(part0(-4, 0)))  # Expect 0
    print()


# function to test part 1
def test1():
    print("*****  Testing Part 1 *****")
    print("Test 1, number 2, output: " + str(part1(2)))  # expected res: true
    print("Test 2, number 4, output: " + str(part1(4)))  # expected res: true
    print("Test 3, number 6, output: " + str(part1(6)))  # expected res: false
    print("Test 4, number 8, output: " + str(part1(8)))  # expected res: true
    print("Test 5, number 12, output: " + str(part1(12)))  # expected res: false
    print("Test 6, number 24, output: " + str(part1(24)))  # expected res: false
    # check for negative and odds
    print("Test 7, number -8, output: " + str(part1(-8)))  # expected res: false
    print("Test 8, number 5, output: " + str(part1(5)))  # expected res: false
    print()


# function to test part 2
def test2():
    print("*****  Testing Part 2 *****")
    print(part2(1))
    print(part2(5))
    print(part2(10))
    print(part2(999))
    print(part2(100))
    print()


# function to test part 3
def test3():
    print("*****  Testing Part 3 *****")
    print(part3("alan"))
    print()


# function to test part 4
def test4():
    print("*****  Testing Part 4 *****")
    print("Test 1, 'paper' and 'title'. Output: " + str(part4("paper", "title")))
    print()


# function to test part 5
def test5():
    print("*****  Testing Part 5 *****")
    print("Test 1, 'car'. Output: " + str(part5("car")))
    print("Test 2, 'Bob'. Output: " + str(part5("Bob")))
    print("Test 1, 'RACECAR'. Output: " + str(part5("RACECAR")))


# function to test part 6
def test6():
    pass


# function to test part 7
def test7():
    pass


# main function to test the challenge code
def main():
    # print("DO NOT delete the import statement")
    test0()
    test1()
    test2()
    test3()
    test4()
    test5()
    test6()
    test7()


# # call to main function
# main()
