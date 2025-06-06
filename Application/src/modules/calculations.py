import re
import math

pat_lower = r'(?=.*[a-z])'
pat_upper = r'(?=.*[A-Z])'
pat_special = r'(?=.*[@$!%*?&])'
pat_num = r'(?=.*\d)'

def possible_combinations(password):
  possible_chars = 0
  length = len(password)

  if re.search(pat_lower, password):
    possible_chars += 26
  if re.search(pat_upper, password):
    possible_chars += 26
  if re.search(pat_special, password):
    possible_chars += 7
  if re.search(pat_num, password):
    possible_chars += 10

  combinations = pow(possible_chars, length)

  return combinations

def get_entropy(combinations):
  entropy = math.log2(combinations)
  return round(entropy,2)

def possible_passwords(entropy):
  num_passwords = pow(2, entropy)
  return num_passwords

def get_time(possible_passwords, guess_per_second):
  time = float(possible_passwords) / float(guess_per_second)
  if time < 60:
    return f"{time:.2f} seconds"
  elif time < 3600:
    minutes = time / 60
    return f"{minutes:.2f} minutes"
  elif time < 86400:
    hours = time / 3600
    return f"{hours:.2f} hours"
  else:
    days = time / 86400
    return f"{days:.2f} days"
  
  
def get_expected_time(possible_passwords, guess_per_second):
  time = float(possible_passwords) / (float(guess_per_second) * 2)
  if time < 60:
    return f"{time:.2f} seconds"
  elif time < 3600:
    minutes = time / 60
    return f"{minutes:.2f} minutes"
  elif time < 86400:
    hours = time / 3600
    return f"{hours:.2f} hours"
  else:
    days = time / 86400
    return f"{days:.2f} days"