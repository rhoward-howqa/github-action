import requests
import time


def run_job(project_id, job_id, authorisation):
    try:
        headers = {"Authorization": authorisation}
        url = 'https://api.testproject.io/v2/projects/{project_id}/jobs/{job_id}/run'.format(project_id=project_id,
                                                                                             job_id=job_id)
        r = requests.post(url, headers=headers)
        body = r.json()

        job_id = body['id']
        print("Job id is: {}".format(job_id))

        return job_id, r.status_code
    except:
        return "No job ID", r.status_code


#running the TestProject state check to see the results of the test
def check_job_status(project_id, job_id, execution_id, authorisation):
    try:
        print("Checking the status of the job")
        headers = {"Authorization": authorisation}
        url = 'https://api.testproject.io/v2/projects/{project_id}/jobs/{job_id}/executions/{execution_id}/state' \
            .format(project_id=project_id, job_id=job_id, execution_id=execution_id)

        run_state = ""
        while run_state not in ("Passed", "Failed"):
            r = requests.get(url, headers=headers)
            if r.status_code == 200:
                body = r.json()
                run_state = body['state']
                print(run_state)
            else:
                print("response code not 200")

            time.sleep(5)

        return run_state, r.status_code
    except:
        return "No state", r.status_code
        exit(1)

