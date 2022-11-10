from dagster import job

from pipeline.interview_job.ops.add_gw_available_column import add_gw_available_column
from pipeline.interview_job.ops.concat_transformed_buses import concat_transformed_buses
from pipeline.interview_job.ops.filter_buses import filter_buses
from pipeline.interview_job.ops.get_mw_available_for_each_bus_very_slow import (
    get_mw_available_for_each_bus_very_slow,
)
from pipeline.interview_job.ops.get_already_computed_buses import get_already_computed_buses
from pipeline.interview_job.ops.raw_buses_to_run import raw_buses_to_run
from pipeline.interview_job.output.output_interview_job import output_interview_job


@job
def interview_job():
    df_raw_buses_to_run = raw_buses_to_run()
    df_get_already_computed_buses = get_already_computed_buses()
    
    df_filtered_raw_buses = filter_buses(
        df_raw_buses_to_run,
        df_get_already_computed_buses,
    )

    df_buses_with_calculation = get_mw_available_for_each_bus_very_slow(
        df_filtered_raw_buses
    )

    df_buses_with_calculation_transformed = add_gw_available_column(
        df_buses_with_calculation
    )

    df_all_busses = concat_transformed_buses(
        df_get_already_computed_buses, df_buses_with_calculation_transformed
    )

    output_interview_job(df_all_busses)
