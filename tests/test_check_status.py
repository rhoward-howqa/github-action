import responses
import pytest
from api import check_job_status

'''
Tests run against the check_job_status function in api.py
All tests are mocked 
'''


# Test to confirm that the Execution Id is returned from function when the status returned is 200
@responses.activate
def test_check_job_status_status_200():
    project_id = 'testProjectId'
    job_id = 'testJobId'
    auth_token = 'testAuthToken'
    execution_id = 'AslJNkX9jU8gV54Sn2cWq1'
    interval = '5'

    responses.add(responses.GET,
                  f'https://api.testproject.io/v2/projects/{project_id}/jobs/{job_id}/executions/{execution_id}/state',
                  json={"state": "Passed", "agent": "Ryan's Agent", "report": "https://testurl.com"}, status=200)

    state, response_code = check_job_status(project_id, job_id, execution_id, auth_token, interval)
    assert response_code == 200
    assert state == 'Passed'

# Test to confirm that the correct status is returned from function when the status returned is not 400
@responses.activate
@pytest.mark.parametrize('status_code', [400, 401, 412, 500])
def test_check_job_status_invalid_status_code(status_code):
    project_id = 'testProjectId'
    job_id = 'testJobId'
    auth_token = 'testAuthToken'
    execution_id = 'AslJNkX9jU8gV54Sn2cWq1'
    interval = '5'

    responses.add(responses.GET,
                  f'https://api.testproject.io/v2/projects/{project_id}/jobs/{job_id}/executions/{execution_id}/state',
                  status=status_code)

    state, response_code = check_job_status(project_id, job_id, execution_id, auth_token, interval)
    assert response_code == status_code
    assert state == "none"
