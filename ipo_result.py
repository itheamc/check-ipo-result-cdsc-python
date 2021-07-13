import json
import requests as requests
from urls import FETCH_COMPANY_URL, IPO_CHECK_URL

# Ipo result Class to handle all the tasks needed to check the ipo results
class IpoResult:
    def __init__(self):
        pass

    # Static method to fetch the companies
    @staticmethod
    def fetch_companies():
        return requests.request('get', url=FETCH_COMPANY_URL).text

    # Function to check the ipo results
    @staticmethod
    def check_ipo_results(company_id, boid):
        headers = {'Content-Type': 'application/json', 'Accept': 'application/json, text/plain, */*'}
        payload = {'companyShareId': company_id, 'boid': boid}
        return requests.request('post', url=IPO_CHECK_URL, data=json.dumps(payload), headers=headers).text
