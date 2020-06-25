import requests
import time


def run_job(project_id, job_id, authorisation):
    try:
        headers = {"Authorization": authorisation}
        url = 'https://api.testproject.io/v2/projects/{project_id}/jobs/{job_id}/run'.format(project_id=project_id,
                                                                                         job_id=job_id)
        r = requests.post(url, headers=headers)
        body = r.json()
        print(body)

        job_id = body['id']
        print("Job id is: {}".format(job_id))

        return job_id, r.status_code
    except:
        print("Job failed to start, status code returned was {}. Check that your agent is running".format(r.status_code))
        exit(0)
        return "No job ID", r.status_code


def check_job_status(project_id, job_id, execution_id, authorisation):
    try:
        print("Checking the status of the job")
        print("now in check job status")
        headers = {"Authorization": authorisation}
        url = 'https://api.testproject.io/v2/projects/{project_id}/jobs/{job_id}/executions/{execution_id}/state'.format(
            project_id=project_id,
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
    except:
        "ooops"
        exit(1)
