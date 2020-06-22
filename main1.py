import requests
import time
import os


def run_tests():
    project_id = os.environ["ProjectId"]
    job_id = os.environ["JobId"]
    auth = os.environ["AuthorisationToken"]

    #project_id = 'jrKiet1cHEyKBTcZMmLoMg'
    #job_id = 'heb20uUMlkSeTvaM8K8fFg'
    #auth = 'wiaj2NlksX-SGf6VJctehppP1PLlYNZ5q4FNiQVY7wY1'

def run_job(project_id, job_id, authorisation):
    headers = {"Authorization": authorisation}
    url = 'https://api.testproject.io/v2/projects/{project_id}/jobs/{job_id}/run'.format(project_id=project_id,
                                                                                         job_id=job_id)
    r = requests.post(url, headers=headers)
    body = r.json()
    print(body)

    job_id = body['id']
    print(job_id)

    return job_id


def check_job_status(project_id, job_id, execution_id, authorisation):
    print("now in check job status")
    headers = {"Authorization": authorisation}
    url = 'https://api.testproject.io/v2/projects/{project_id}/jobs/{job_id}/executions/{execution_id}/state'.format(project_id=project_id,
                                                                                         job_id=job_id, execution_id=execution_id)
    status = ""
    while status not in ("Passed", "Failed"):
        r = requests.get(url, headers=headers)
        body = r.json()
        print(body)

        status = body['state']
        print(status)
        time.sleep(2)

    return status




start_job = run_job(project_id, job_id, auth)

print("id is: " + start_job)

check_job = check_job_status(project_id, job_id, start_job, auth)

print('the job status is {check_job}'.format(check_job=check_job))


