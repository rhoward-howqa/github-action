from api import run_job, check_job_status
from errors import error_message
import os

project_id = os.environ['INPUT_PROJECT_ID']
job_id = os.environ['INPUT_JOB_ID']
auth = os.environ['INPUT_AUTHORISATION_TOKEN']
interval = os.environ['INPUT_INTERVAL_TIME']


# Call API to start TestProject job
execution_id, response_code = run_job(project_id, job_id, auth)


if response_code == 200:
    state, response_code = check_job_status(project_id, job_id, execution_id, auth, interval)
    if response_code == 200:
        print(f'The final run status of the Job is {state}')
        if state != 'Passed':
            exit(1)
    else:
        print(error_message(response_code), f'Error running job status code returned was {response_code}.')
        exit(1)
else:
    print(error_message(response_code))
    exit(1)

