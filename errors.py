def error_message(status_code):
    response_dict = {
        400: 'Job failed to start, status code returned was 400. Check the Job Id is correct.',
        401: 'Job failed to start, status code returned was 401.'
             'Check The Project Id and Authorisation code are correct.',
        412: 'Job failed to start, status code returned was 412. Check that your agent is running.'
    }
    message = response_dict.get(status_code, f'An Unknown Error Occurred. Status Code returned was {status_code}.')

    return message
