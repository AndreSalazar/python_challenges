"""
Have the function LongestWord(sen) take the sen parameter being passed and return the longest
word in the string. If there are two or more words that are the same length, return the first
word from the string with that length. Ignore punctuation and assume sen will not be empty.
Words may also contain numbers, for example "Hello world123 567"
"""

def LongestWord(sen):
  # code goes here
  words = sen.split(' ')
  string_len = 0
  final_string = ""
  for string in words:
      if string.isalnum():
          if len(string) > string_len:
            string_len = len(string)
            final_string = string

  return final_string

# keep this function call here
print(LongestWord(input()))