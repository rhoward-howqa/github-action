from api import run_job, check_job_status
import os

os.environ["INPUT_PROJECT_ID"] = 'jrKiet1cHEyKBTcZMmLoMg'
os.environ["INPUT_JOB_ID"] = 'heb20uUMlkSeTvaM8K8fFg'
os.environ["INPUT_AUTHORISATION_TOKEN"] = \
    'wiaj2NlksX-SGf6VJctehppP1PLlYNZ5q4FNiQVY7wY1'

project_id = os.environ['INPUT_PROJECT_ID']
job_id = os.environ['INPUT_JOB_ID']
auth = os.environ['INPUT_AUTHORISATION_TOKEN']

# Call API to start TestProject job
start_job = run_job(project_id, job_id, auth)

response_code = start_job[1]

if response_code == 200:
    check_job = check_job_status(project_id, job_id, start_job[0], auth)
    check_response_code = check_job[1]
    if check_response_code == 200:
        print('The current job status is {check_job}'
              .format(check_job=check_job[0]))
    elif check_response_code == 412:
        print("Job failed to start, status code returned was {}. "
              "Check that your agent is running".format(response_code))
        exit(1)
    elif check_response_code == 401:
        print("Job failed to run, status code returned was {}. "
              "Check The Project Id and Authorisation code are correct".format(response_code))
        exit(1)
    elif check_response_code == 400:
        print("Job failed to run, status code returned was {}. "
              "Check The Job Id is correct".format(response_code))
        exit(1)
    else:
        print("Error running job, status code returned was {}."
              .format(response_code))
        exit(1)

elif response_code == 412:
    print("Job failed to start, status code returned was {}. "
          "Check that your agent is running".format(response_code))
    exit(1)
elif response_code == 401:
    print("Job failed to run, status code returned was {}. "
          "Check The Project Id and Authorisation code are correct".format(response_code))
    exit(1)
elif response_code == 400:
    print("Job failed to run, status code returned was {}. "
          "Check The Job Id is correct".format(response_code))
    exit(1)
else:
    print("Error running job, status code returned was {}."
          .format(response_code))
    exit(1)
