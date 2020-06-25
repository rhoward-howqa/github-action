from api import run_job, check_job_status
import os

# project_id = 'jrKiet1cHEyKBTcZMmLoMg'
# job_id = 'heb20uUMlkSeTvaM8K8fFg'
# auth = 'wiaj2NlksX-SGf6VJctehppP1PLlYNZ5q4FNiQVY7wY1'

project_id = os.environ['INPUT_PROJECT_ID']
job_id = os.environ['INPUT_JOB_ID']
auth = os.environ['INPUT_AUTHORISATION_TOKEN']

# Call API to start TestProject job
start_job = run_job(project_id, job_id, auth)

print(start_job[1])
if start_job[1] == 200:
    check_job = check_job_status(project_id, job_id, start_job[0], auth)
    print('The current job status is {check_job}'.format(check_job=check_job))
else:
    print("something went wrong")
