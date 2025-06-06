import re
import math

pat_lower = r'(?=.*[a-z])'
pat_upper = r'(?=.*[A-Z])'
pat_special = r'(?=.*[@$!%*?&])'

def possible_combinations(password):
  possible_chars = 0
  length = len(password)

  if re.search(pat_lower, password):
    possible_chars += 26
  if re.search(pat_upper, password):
    possible_chars += 26
  if re.search(pat_special, password):
    possible_chars += 7

  combinations = pow(possible_chars, length)

  return combinations

def get_entropy(combinations):
  entropy = math.log2(combinations)
  return entropy

def possible_passwords(entropy):
  num_passwords = pow(2, entropy)
  return num_passwords

def get_time(possible_passwords, guess_per_second):
  time = possible_passwords / guess_per_second
  return time