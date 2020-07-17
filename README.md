# Python Container Action Template

This is a GitHub actions for running a TestProject Job. It utilises the TestProject API to trigger the execution of a job. Once the job is executed the Check State API will be called at configured intervals to check if the status of the job.
Once the returned state of the Check State request is Failed, Passed, Skipped, Suspended, Error or Aborted the action will end.  

## Usage

Describe how to use your action here.

### Example workflow

```yaml
name: TpTest
on:
  push:
    branches: [ master ]
jobs:
  run_tp_tests:
    runs-on: ubuntu-latest
    steps:
    - uses: rhoward-howqa/TestProject-Run-Job@master
      with:
        project_id: 'TestProject-ProjectId'
        job_id: 'TestProject-JobId'
        authorisation_token: 'TestProject-API Authorisation Token'
        interval_time: '60'   
```

### Inputs

| Input                                             | Description                                        |
|------------------------------------------------------|-----------------------------------------------|
| `project_id`  | The id of the project your job resides in.   |
| `job_id`| The id of the project you want to run     |
| `authorisation_token`| The TestProject API authorisation token    |
| `interval_time`| The interval time in seconds between checking the state of the job  |

### Outputs

| Output                                             | Description                                        |
|------------------------------------------------------|-----------------------------------------------|


## Examples



### Using the inputs

This is how to use the optional input.

```yaml
      with:
        project_id: 'TestProject-ProjectId'
        job_id: 'TestProject-JobId'
        authorisation_token: 'TestProject-API Authorisation Token'
        interval_time: '60' 
```