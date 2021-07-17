# Importing the required packages internally and from the external library
from ipo_result import IpoResult


# -----------------------------------------------------------
# Below codes are for printing information on the console
# -----------------------------------------------------------

# Printing the Header
print(
    '------------------------------------------------------------------------------------\n\t\t------------------------ CHECK IPO RESULTS -----------------------\n------------------------------------------------------------------------------------')
# Getting the list of companies from the server
companies = IpoResult.get_company_list()
# Printing the companies name as a option for the user
for company in companies:
    print(f"[✓] Enter __ {company['id']} __ for {company['name']}")

while True:
    # Getting input from the user
    comp_id = input('\n[+] Enter Here_    ')
    user_boid = input('[+] Enter BOID_    ')

    # Checking whether share is allotted or not and printing on the console
    res = IpoResult.get_ipo_result(company_id=comp_id, boid=user_boid)
    print(f"\n\t\t_______ {res['message']} _______")
