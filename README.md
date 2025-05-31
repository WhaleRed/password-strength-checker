# Password Strength Checker

A basic password strength checker with a GUI.<br>



## Goals

1. Learn Regex for pattern matching  
2. Understand basic cryptographic principles


## Formulas
1. Entropy(bits) = log<sub>2</sub>(possible combinations)
2. Possible combinations = (Number of possible characters) ^ (Password length)
3. Possible Passwords = 2 ^ Entropy
4. Time(Worst Case) = Possible Passwords / Guesses per second
5. Expected Time ≈ Time / 2
