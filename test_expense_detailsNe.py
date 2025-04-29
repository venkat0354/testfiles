def test_invalid_field_error(gql_client):
    bad_query = """
    query {
        expenseDetails {
            nonExistentField  # This field does not exist
        }
    }
    """
    response = gql_client.execute(bad_query)

    # GraphQL should return an 'errors' section
    assert 'errors' in response, "Expected errors in response for invalid query"
    assert "nonExistentField" in response['errors'][0]['message'], "Error message should mention 'nonExistentField'"
