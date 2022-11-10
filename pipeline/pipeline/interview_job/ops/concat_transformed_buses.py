from dagster import op
import pandas as pd


@op
def concat_transformed_buses(
    df_old_buses: pd.DataFrame, df_new_buses: pd.DataFrame
) -> pd.DataFrame:
    return pd.concat([df_old_buses, df_new_buses])
