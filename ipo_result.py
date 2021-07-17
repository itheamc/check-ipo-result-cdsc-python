import ast
import json
import requests as requests
from urls import FETCH_COMPANY_URL, IPO_CHECK_URL


# Ipo result Class to handle all the tasks needed to check the ipo results
class IpoResult:
    def __init__(self):
        pass

    # Function to fetch the companies
    @staticmethod
    def __fetch_companies():
        return requests.request('get', url=FETCH_COMPANY_URL).text

    # Function to check the ipo results
    @staticmethod
    def __check_ipo_results(company_id, boid):
        res = None
        try:
            headers = {'Content-Type': 'application/json', 'Accept': 'application/json, text/plain, */*'}
            payload = {'companyShareId': company_id, 'boid': boid}
            res = requests.request('post', url=IPO_CHECK_URL, data=json.dumps(payload), headers=headers).text
        except Exception as e:
            res = {'message': e.msg}

        return res

    # Creating function to process the company list
    @staticmethod
    def get_company_list():
        _res = IpoResult.__fetch_companies()
        if 'true' in _res:
            _res = _res.replace("true", "True")
        if 'false' in _res:
            _res = _res.replace("false", "False")

        _res = ast.literal_eval(_res)
        return _res['body']

    # Creating function to process the response and convert on dictionary type
    @staticmethod
    def get_ipo_result(company_id, boid):
        _res = IpoResult.__check_ipo_results(company_id=company_id, boid=boid)
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

