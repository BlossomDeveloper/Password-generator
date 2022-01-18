# This is a password generator using random

import random

password_len = int(input('Please enter the length of the password: '))

all_w_s = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"

password = "".join(random.sample(all_w_s, password_len))

print(password)

