from dagster import job, op


@op
def smoke_test_op1(context):
    return "Successfully ran smoketest"


@op
def smoke_test_op2(context, string_to_log):
    context.log.info(string_to_log)


@job
def nira_smoke_test_job():
    smoke_test_op2(smoke_test_op1())
