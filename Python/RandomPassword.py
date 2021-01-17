import random

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers ="0123456789"
symbols ="[]{}()*;/,._-"

together = lower + upper + numbers + symbols

length= 17
password = "".join(random.sample(together, length))
print("Your new password is:", password)
