#Simple password generator and tester
import random
import string
import re
lenght = int(input('Enter the lenght of your password:'))
upper = string.ascii_uppercase
lower = string.ascii_lowercase
digits = string.digits
punc = string.punctuation
char = upper + lower + digits + punc
print(char)
def create_pwd():
    pwd_list = random.choices(char , k= lenght)
    pwd =  "".join(pwd_list)
    return pwd
def check_password_strength(pwd):
    # Criteria definitions
    length_error = len(pwd) < 8
    digit_error = re.search(r"\d", pwd) is None 
    uppercase_error = re.search(r"[A-Z]", pwd) is None 
    lowercase_error = re.search(r"[a-z]", pwd) is None 
    symbol_error = re.search(r"[ !@#$%^&*(),.?\":{}|<>]", pwd) is None
    errors = {
        "Too short": length_error,
        "Missing digit": digit_error,
        "Missing uppercase": uppercase_error,
        "Missing lowercase": lowercase_error,
        "Missing symbol": symbol_error,
    }
    problem_list = []
    for msg , failed in errors.items():
        if failed:
            problem_list.append(msg)
    return problem_list
gen_pwd = create_pwd()
print(f"Your new pwd is {gen_pwd}")
results = check_password_strength(gen_pwd)
if not results:
    print("Your pwd is safe.")
else:
    print(f"Weakness found {results}")

