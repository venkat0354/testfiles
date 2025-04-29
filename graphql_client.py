//(Create this file graphql_client.py inside utils folder)
//👉 This class sends queries to your API and gets the response.


import requests

class GraphQLClient:
    def __init__(self, endpoint):
        self.endpoint = endpoint  # API endpoint

    def execute(self, query, variables=None, headers=None):
        payload = {
            'query': query,
            'variables': variables or {}
        }
        response = requests.post(self.endpoint, json=payload, headers=headers)
        return response.json()
