from dagster import repository

from pipeline.caiso.jobs.get_caiso_model_data_job.get_caiso_model_data_job import (
    get_caiso_model_data_job,
)
from pipeline.combine_all_regions.jobs.combine_all_regions_job import (
    combine_all_regions_job,
)
from pipeline.miso.jobs.eris_fcitc.all_regions_2021_phase_one_eris_fcitc_job import (
    all_regions_2021_phase_one_eris_fcitc_job,
)
from pipeline.miso.jobs.eris_fcitc.atc_2020_phase_two_eris_fcitc_job import (
    atc_2020_phase_two_eris_fcitc_job,
)
from pipeline.miso.jobs.eris_fcitc.central_2020_phase_one_eris_fcitc_job import (
    central_2020_phase_one_eris_fcitc_job,
)
from pipeline.miso.jobs.eris_fcitc.itc_2020_phase_two_eris_fcitc_job import (
    itc_2020_phase_two_eris_fcitc_job,
)
from pipeline.miso.jobs.eris_fcitc.south_2020_phase_two_eris_fcitc_job import (
    south_2020_phase_two_eris_fcitc_job,
)
from pipeline.miso.jobs.eris_fcitc.west_2020_phase_two_eris_fcitc_job import (
    west_2020_phase_two_eris_fcitc_job,
)
from pipeline.miso.jobs.get_branch_data_per_year_phase import (
    get_branch_data_per_year_phase,
)
from pipeline.miso.jobs.historical_facility_costs_job import (
    historical_facility_costs_job,
)
from pipeline.miso.jobs.miso_post_process_job import miso_post_process_job
from pipeline.miso.jobs.nris_flowgate_analysis.all_regions_2021_phase_one_nris_flowgate_analysis_job import (
    all_regions_2021_phase_one_nris_flowgate_analysis_job,
)
from pipeline.miso.jobs.nris_flowgate_analysis.atc_2020_phase_two_nris_flowgate_analysis_job import (
    atc_2020_phase_two_nris_flowgate_analysis_job,
)
from pipeline.miso.jobs.nris_flowgate_analysis.central_2020_phase_one_nris_flowgate_analysis_job import (
    central_2020_phase_one_nris_flowgate_analysis_job,
)
from pipeline.miso.jobs.nris_flowgate_analysis.itc_2020_phase_two_nris_flowgate_analysis_job import (
    itc_2020_phase_two_nris_flowgate_analysis_job,
)
from pipeline.miso.jobs.nris_flowgate_analysis.south_2020_phase_two_nris_flowgate_analysis_job import (
    south_2020_phase_two_nris_flowgate_analysis_job,
)
from pipeline.miso.jobs.nris_flowgate_analysis.west_2020_phase_two_nris_flowgate_analysis_job import (
    west_2020_phase_two_nris_flowgate_analysis_job,
)
from pipeline.miso.jobs.nris_flowgate_screen.all_regions_2021_phase_one_flowgate_screen_job import (
    all_regions_2021_phase_one_flowgate_screen_job,
)
from pipeline.miso.jobs.nris_flowgate_screen.atc_2020_phase_two_flowgate_screen_job import (
    atc_2020_phase_two_flowgate_screen_job,
)
from pipeline.miso.jobs.nris_flowgate_screen.central_2020_phase_one_flowgate_screen_job import (
    central_2020_phase_one_flowgate_screen_job,
)
from pipeline.miso.jobs.nris_flowgate_screen.itc_2020_phase_two_flowgate_screen_job import (
    itc_2020_phase_two_flowgate_screen_job,
)
from pipeline.miso.jobs.nris_flowgate_screen.south_2020_phase_two_flowgate_screen_job import (
    south_2020_phase_two_flowgate_screen_job,
)
from pipeline.miso.jobs.nris_flowgate_screen.west_2020_phase_two_flowgate_screen_job import (
    west_2020_phase_two_flowgate_screen_job,
)
from pipeline.pjm.graphs.flowgate_screen_graph import flowgate_screen_job
from pipeline.pjm.graphs.model_file_creation_graph_job import (
    model_file_creation_graph_job,
)
from pipeline.pjm.graphs.post_processing_job import post_processing_job
from pipeline.pjm.graphs.run_flowgate_analysis_job import run_flowgate_analysis_job
from pipeline.shared_data.velocity_suite.jobs.shared_data_velocity_suite_job import (
    shared_data_velocity_suite_job,
)


@repository
def caiso_pipeline():
    return [get_caiso_model_data_job]


@repository
def pjm_pipeline():
    """
    The repository definition for this pipeline Dagster repository.

    For hints on building your Dagster repository, see our documentation overview on Repositories:
    https://docs.dagster.io/overview/repositories-workspaces/repositories
    """

    jobs = [
        post_processing_job,
        model_file_creation_graph_job,
        flowgate_screen_job,
        run_flowgate_analysis_job,
    ]

    return jobs


@repository
def miso_pipeline():
    jobs = [
        historical_facility_costs_job,
        miso_post_process_job,
        get_branch_data_per_year_phase,
        central_2020_phase_one_eris_fcitc_job,
        central_2020_phase_one_flowgate_screen_job,
        central_2020_phase_one_nris_flowgate_analysis_job,
        west_2020_phase_two_eris_fcitc_job,
        west_2020_phase_two_flowgate_screen_job,
        west_2020_phase_two_nris_flowgate_analysis_job,
        south_2020_phase_two_eris_fcitc_job,
        south_2020_phase_two_flowgate_screen_job,
        south_2020_phase_two_nris_flowgate_analysis_job,
        itc_2020_phase_two_eris_fcitc_job,
        itc_2020_phase_two_flowgate_screen_job,
        itc_2020_phase_two_nris_flowgate_analysis_job,
        atc_2020_phase_two_eris_fcitc_job,
        atc_2020_phase_two_flowgate_screen_job,
        atc_2020_phase_two_nris_flowgate_analysis_job,
        all_regions_2021_phase_one_eris_fcitc_job,
        all_regions_2021_phase_one_flowgate_screen_job,
        all_regions_2021_phase_one_nris_flowgate_analysis_job,
    ]

    return jobs


@repository
def non_region_specific_pipeline():
    jobs = [
        shared_data_velocity_suite_job,
        combine_all_regions_job,
    ]

    return jobs
