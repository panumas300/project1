"""
import random

HEADS = 1
TAILS = 2
TOSSES = 10

def main():
  for toss in range(TOSSES):
    if random.randint(HEADS, TAILS) == HEADS:
      print('Heads')
    else:
      print('Tails')

main()

"""
import random

HEADS = 1
TAILS = 2
TOSSES = 20
total_heads = 0
total_tails = 0
total_toss = 0

def main():
  global total_heads
  global total_tails
  global total_toss
  for toss in range(TOSSES):
    if random.randint(HEADS, TAILS) == HEADS:
      print('Heads')
      total_heads = total_heads + 1
      total_toss = total_toss + 1
    else:
      print('Tails')
      total_tails = total_tails + 1
      total_toss = total_toss + 1
  print('Total of Heads : ',total_heads)
  print('Total of Tails : ',total_tails) 
  print('Total of Toss : ',total_toss)


main()