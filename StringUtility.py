class StringUtility:
  def __init__(self,string):
    " String is a parameter and is stored as variable, self: str, string"
    self.string = string
  def __str__(self):
    " returns string, self: str, string, return: str, return string"
    return self.string

  def vowels(self):
    "counts number of vowels"
    vowels = "aeiouAEIOU"
    count = 0
    for character in self.string:
      if character in vowels:
        count = count +1
    if count >=5:
      return "many"
    return str(count)

    
  def bothEnds(self):
    "returns a string made of first and last two charactes of string"
    string = self.string
    if len(string) <= 2:
      return ""
    return string[0] + string[1] + string[-2] + string[-1]
  def fixStart(self):
      "returns string where first characters have been changed to * besides the actual character"
      string = self.string
      if len(string) <= 1:
        return string
      return string[0]+ string[1:].replace(string[0],"*")
  def asciiSum(self):
    "returns integer that is a sumof all ascii values in string"
    ascii = 0
    for character in self.string:
      ascii = ord(character) + ascii
    return (ascii)

  def cipher(self):
    "returns string by incrementing all leters by length of string"
    ciphered = ""
    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    space = " "
    for character in self.string:
      if character in uppercase:
        changedcharacter = chr(((ord(character)+ len(self.string)- 65) % 26) + 65)
        print(character,":",changedcharacter)
        ciphered = ciphered + changedcharacter 
      if character in lowercase:
        changedcharacter = chr(((ord(character)+len(self.string)- 97) % 26) + 97)
        print(character,":",changedcharacter)
        ciphered = ciphered + changedcharacter
      if character in space:
        ciphered = ciphered + character 
    return ciphered 
