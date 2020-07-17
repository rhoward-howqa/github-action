import pytest
from errors import error_message

'''
Tests run against the error message function in error.py

'''


# Test to confirm that the correct Error message is returned from function

@pytest.mark.parametrize('status_code', [400, 401, 412, 500])
def test_get_error_message(status_code):
    response_dict = {
        400: 'Job failed to start, status code returned was 400. Check the Job Id is correct.',
        401: 'Job failed to start, status code returned was 401.'
             'Check The Project Id and Authorisation code are correct.',
        412: 'Job failed to start, status code returned was 412. Check that your agent is running.',
        500: 'An Unknown Error Occurred. Status Code returned was 500.'
    }

    message = error_message(status_code)

    assert message == response_dict.get(status_code)
