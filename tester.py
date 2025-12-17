import Strength_Checker
import characters_list
import random
import json
from pathlib import Path
import plotly.express as px

parent_folder = Path(__file__).parent
json_file = parent_folder / "tested_passwords.json"



with open(json_file, 'w') as f:
    json.dump('', f)



def create_password():
    random_password = []
    password = ""
    random_length = random.randint(1, 20) 
    while len(random_password) < random_length:
        random_selection = characters_list.select_random_char()
        random_password.append(random_selection)
        password = "".join(random_password)
    return password

data = []

blank_return = Strength_Checker.main("")
data.append({'Password': "", "Score": blank_return})

for i in range(1000):
    passkey_to_test = None
    result = None
    passkey_to_test = create_password()
    result = Strength_Checker.main(passkey_to_test)
    data.append({'Password': passkey_to_test, "Score": result})

with open(json_file, 'w') as f:
    json.dump(data, f, indent = 2)
    print(f'The data was saved to folder existing at {json_file} .')