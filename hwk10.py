# Name:  - your name (and your partners name) <br>
# Peers:  - names of CSC252 students who you consulted or ``N/A'' <br>
# References:  - URL of resources used <br>
from random import randint

### Part 1: Lumber Mill
def lumberSelection(prices:list, n:int) -> float:
	return 0.0

### Part 2: Cash Register
def calcPermutations(val:int) -> None:
    pass

def getNumberOfWays(change_amount:int, bill_list:list) -> int:
	return 0



def main():
    """ This function drives the program and will call each of your functions.
    """
    lumber_prices = [0.25, 1.45, 0, 3.58, 0, 4.4, 0, 5.18, 0, 6.58, 0, 8.28]
    size = randint(1,len(lumber_prices))
    print("The max value for " + str(size) + " feet is $" + str(lumberSelection(lumber_prices, size)))
    
    bills = [1, 2, 5, 10, 20, 50, 100]
    change = randint(1, 100)
    print("For $" + str(change) + " there are " + str(getNumberOfWays(6, bills)) + " combinations.")

if __name__ == '__main__': 
    main()

