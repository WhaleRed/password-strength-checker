# Password Strength Checker

A basic password strength checker with a GUI.<br>
Shows how strong your password is.<br>
Shows the expected time it takes to brute force your password on offline attacks.<br>
Shows the longest time it takes to brute force your password on offline attacks.<br>


## Goals

1. Learn Regex for pattern matching  
2. Understand basic cryptographic principles


## Formulas
1. Entropy(bits) = log<sub>2</sub>(possible combinations)
2. Possible combinations = (Number of possible characters)<sup>(Password length)</sup>
3. Possible Passwords = 2<sup>Entropy</sup>
4. Time(best Case) = <sup>Possible Passwords</sup> / <sub>Guesses per second</sub>
5. Expected Time ≈ <sup>Time</sup> / <sub>2</sub>
