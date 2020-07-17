import responses
import pytest
from api import run_job

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

    responses.add(responses.GET,
                  'https://api.testproject.io/v2/projects/{project_id}/jobs/{job_id}/executions/{execution_id}/state'
                  .format(project_id=project_id, job_id=job_id, execution_id=execution_id),
                  json={"state": "Executing", "agent": "Ryan's Agent", "report": "https://testurl.com"}, status=200)

    state, response_code = run_job(project_id, job_id, auth_token)
    assert response_code == 200
    assert state == execution_id

# Test to confirm that the correct status is returned from function when the status returned is not 400
@responses.activate
@responses.activate
@pytest.mark.parametrize('status_code', [400, 401, 412, 500])
def test_check_job_status_invalid_status_code(status_code):
    project_id = 'testProjectId'
    job_id = 'testJobId'
    auth_token = 'testAuthToken'

    responses.add(responses.POST,
                  'https://api.testproject.io/v2/projects/{project_id}/jobs/{job_id}/run'.format(project_id=project_id,
                                                                                                 job_id=job_id),
                  status=status_code)

    state, response_code = run_job(project_id, job_id, auth_token)
    assert response_code == status_code
    assert state == "none"
