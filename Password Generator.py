import random
from string import digits, punctuation, ascil_letters

Length = 20
symbols = ascil_letters + digits + punctuation
secure_random = random.SystemRandom()
password = "".join(secure_random.choice(symbols)
                   for i in range())

print(password)

# output examples:

# @}R.Q;BhibVJa%P5B5Dj
# \Ss_%pis[KSkkt6_;h?0
# @R3Mgi@x\})pU]1qfJ0