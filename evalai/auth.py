import base64
import json
import os
import pickle
import requests


def login(username=None, password=None, domain="default"):
    """
    This is used for configuring the authentication details the initial time the user
    logs in. We can also configure the domain to do the requests to. After the initial
    setup the user need not have to log in again.
    """

    if domain == "default":
        url = "http://localhost:8000/api/auth/login"

    auth_details = {
            "username": username,
            "password": password
    }

    response = requests.post(url, auth_details)

    if response.status_code == requests.codes.ok:
        print("You're now logged-in!")
    else:
        print("Something went wrong, please check your connection.")

    token = response.text
    json_token = json.loads(token)
    hashed_token = base64.b64encode(json_token["token"])

    __location__ = os.path.realpath(os.path.join(os.getcwd(),
                                    os.path.dirname(__file__)))
    outputFile = '.data'
    file_path = os.path.join(__location__, outputFile)
    with open(file_path, 'wb') as fw:
        pickle.dump({'Token': hashed_token}, fw)
