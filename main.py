# Importing the required packages internally and from the external library
import ast
from ipo_result import IpoResult

# Getting the list of companies from the server and proceeds the response
response = IpoResult.fetch_companies()
response = response.replace('true', 'True')
response = ast.literal_eval(response)
companies = response['body']

# Printing the Header
print(
    '------------------------------------------------------------------------------------\n\t\t------------------------ CHECK IPO RESULTS -----------------------\n------------------------------------------------------------------------------------')
# Printing the companies name as a option for the user
for company in companies:
    print(f"[✓] Enter __ {company['id']} __ for {company['name']}")

while True:
    # Getting input from the user
    comp_id = input('\n[+] Enter Here_    ')
    user_boid = input('[+] Enter BOID_    ')

    # Checking whether share is allotted or not and processing the response to convert in dict
    final_res = IpoResult.check_ipo_results(comp_id, user_boid)
    final_res = final_res.replace("true", "True")
    final_res = final_res.replace("false", "False")
    final_res = final_res.replace("null", "None")
    final_res = ast.literal_eval(final_res)

    print(f"\n\t\t_______ {final_res['message']} _______")
