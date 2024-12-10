#!/usr/bin/python3

isWinner = __import__('0-prime_game').isWinner


print("Winner: {}".format(isWinner(3, [4, 5, 1])))
print("Winner: {}".format(isWinner(3, [4, 5, 6])))
print("Winner: {}".format(isWinner(3, [4, 5, 7])))
print("Winner: {}".format(isWinner(3, [4, 5, 8])))
print("Winner: {}".format(isWinner(3, [4, 5, 9])))
