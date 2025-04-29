//(Create this file inside tests/ folder)
//What this test does:
//	•	Loads the query from file
//	•	Sends it to server
//	•	Checks if the response has data, expenseDetails, and totalCount
//•	Checks if totalCount is an integer


def load_query(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def test_expense_details_total_count(gql_client):
    # Step 1: Load query from file
    query = load_query("graphql_queries/expense_details_query.graphql")
    
    # Step 2: Send the query
    response = gql_client.execute(query)

    # Step 3: Assertions
    assert 'data' in response, "Response should contain 'data'"
    assert 'expenseDetails' in response['data'], "'data' should contain 'expenseDetails'"
    assert 'totalCount' in response['data']['expenseDetails'], "'expenseDetails' should contain 'totalCount'"

    # Optional extra check
    total_count = response['data']['expenseDetails']['totalCount']
    assert isinstance(total_count, int), "'totalCount' should be an integer"
