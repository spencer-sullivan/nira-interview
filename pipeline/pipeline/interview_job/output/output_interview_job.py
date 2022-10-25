from dagster import op


@op
def output_interview_job(context, df_with_all_columns):
    output_file_path = f"pipeline/interview_job/output/{context.run_id}.csv"
    df_with_all_columns.to_csv(
        output_file_path, index=False, line_terminator="\n", encoding="utf-8"
    )
