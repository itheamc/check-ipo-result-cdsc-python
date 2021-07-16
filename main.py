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


# Creating function to process the response and convert on dictionary type
def process_response(res):
    _res = res
    if 'true' in _res:
        _res = _res.replace("true", "True")
    if 'false' in _res:
        _res = _res.replace("false", "False")
    if 'null' in _res:
        _res = _res.replace("null", "None")
    try:
        _res = ast.literal_eval(_res)
    except SyntaxError as se:
        _res = {'message': se.msg}
    return _res


while True:
    # Getting input from the user
    comp_id = input('\n[+] Enter Here_    ')
    user_boid = input('[+] Enter BOID_    ')

    # Checking whether share is allotted or not and processing the response to convert in dict
    res = IpoResult.check_ipo_results(comp_id, user_boid)
    _proceed_res = process_response(res)

    print(f"\n\t\t_______ {_proceed_res['message']} _______")
