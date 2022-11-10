from pathlib import Path
from typing import Optional

import pandas as pd
from dagster import op


def existing_output_path() -> Optional[Path]:
    matching_files = [f for f in Path("pipeline/interview_job/output/").glob("*.csv")]
    assert len(matching_files) == 1, "There should be only one output CSV file"

    return matching_files[0]


@op
def get_already_computed_buses(context) -> pd.DataFrame:
    existing_path = existing_output_path()
    
    return pd.read_csv(
        existing_path,
        index_col=None,
        encoding="utf-8",
    )
