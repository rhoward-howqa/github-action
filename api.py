import requests
import time

job_states = ["Failed", "Passed", "Skipped", "Suspended", "Error", "Aborted"]
base_url = 'https://api.testproject.io/v2/'

'''
Run the TestProject Job using the supplied values
Project Id
Job Id
Authorisation Token

If http 200 response returned get the execution Id from response body and call the 'Get State' TestProject API to check 
the status 
'''


def run_job(project_id, job_id, authorisation):
    headers = {"Authorization": authorisation}
    url = f'{base_url}projects/{project_id}/jobs/{job_id}/run'
    try:
        # Call the Test Project API to Run the Job
        r = requests.post(url, headers=headers, timeout=5)
        # Raiseexception for status code other than 200 range
        r.raise_for_status()
        # Get Execution Id from Response body
        body = r.json()
        execution_id = body['id']
        print(f'Execution id is {execution_id}')
        # return execution Id and status code
        return execution_id, r.status_code
    except requests.exceptions.HTTPError as error:
        print(str(error))
        return "none", r.status_code
    except requests.exceptions.ConnectionError as error:
        print(str(error))
    except requests.exceptions.Time as error:
        print(str(error))


'''
Run the TestProject 'Get State' API using the supplied values
Project Id
Job Id
Authorisation Token
Execution ID (Returned from the Run job API Response

API is called every 5 seconds until a Failed or Passed job status is returned in Response Body
'''


def check_job_status(project_id, job_id, execution_id, authorisation, interval):
    print('Checking the status of the job')
    headers = {'Authorization': authorisation}
    url = f'{base_url}projects/{project_id}/jobs/{job_id}/executions/{execution_id}/state'
    try:
        run_state = ""
        # while ste state returned in the response body is not passed or failed continue to call Get State
        while run_state not in job_states:
            r = requests.get(url, headers=headers)
            # Raiseexception for status code other than 200 range
            r.raise_for_status()
            body = r.json()
            # Get the state from the Response Body
            run_state = body['state']
            print(run_state)
            time.sleep(int(interval))
        return run_state, r.status_code
    except requests.exceptions.HTTPError as error:
        print(str(error))
        return 'none', r.status_code
    except requests.exceptions.ConnectionError as error:
        print(str(error))
    except requests.exceptions.Time as error:
        print(str(error))
