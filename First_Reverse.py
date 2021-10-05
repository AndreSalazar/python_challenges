"""
First Reverse.

Have the function FirstReverse(str) take the str parameter being passed and return the string
in reversed order. For example: if the input string is "Hello World and Coders" then your
program should return the string sredoC dna dlroW olleH.
"""

def FirstReverse(strParam):

  # code goes here
  counter = 0
  final = ""
  for x in strParam:
    final = x + final
    counter += 1

  return final


# keep this function call here
print(FirstReverse(input()))