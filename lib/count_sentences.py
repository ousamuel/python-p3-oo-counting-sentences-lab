#!/usr/bin/env python3

class MyString:
  def __init__(self, value=""):
    self.string = value

  def get_string(self):
    return self._string

  def set_string(self, value):
    if (type(value) == str):
      self._string = value
    else:
      print("The value must be a string.")

  value = property(get_string, set_string)

  def is_sentence(self):
    return (self.string.endswith("."))
  def is_question(self):
    return (self.string.endswith("?"))
  def is_exclamation(self):
    return (self.string.endswith("!"))

  def count_sentences(self):
    char_list = ["!", "?"]
    temp_string = self.string
    for char in char_list:
      temp_string = temp_string.replace(char, ".")

    split_string = temp_string.split(".")
    return len([string for string in split_string if string!= ""])

  pass
