//(Create this file directly inside the root folder)
//👉 Here we are creating the GraphQL client once and reusing it for all tests.


import pytest
from utils.graphql_client import GraphQLClient

@pytest.fixture(scope="session")
def gql_client():
    endpoint = "https://lv-sub-inv-dev-appsvc.azurewebsites.net/subinvapi/graphql/"
    return GraphQLClient(endpoint)
