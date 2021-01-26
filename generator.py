# Imports here 
import string
import random

# Config
amount = 10000
allowed_chars = string.ascii_lowercase + string.ascii_uppercase + string.digits
prefix = "RPG-"
postfix = "-APS01"
output_path = "generated_codes.csv"

# Code array 
generated_codes = []

# Generator function 
def generate(length = 16, char = allowed_chars ):
    return prefix + ''.join(random.choice( char) for x in range(length)) + postfix

# write new line to csv
def write_to_csv(line):
    f = open(output_path,'a')
    f.write(line + '\n')
    f.close()            

# Loop and generate codes
i = 0
while i <= amount:
    code = generate()
    # Ensure the code is unique
    if code not in generated_codes:
        generated_codes.append(code)
        write_to_csv(code)
        i += 1
    else:
        continue    

