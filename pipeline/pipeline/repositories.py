from dagster import repository

from pipeline.interview_job.interview_job import interview_job
from pipeline.smoke_test_job.smoke_test_job import nira_smoke_test_job


@repository
def nira_interview_repository():
    return [nira_smoke_test_job, interview_job]
