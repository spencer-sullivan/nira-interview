from dagster import op
import pandas as pd


@op
def filter_buses(
    context, df_raw_buses: pd.DataFrame, df_existing_buses: pd.DataFrame
) -> pd.DataFrame:
    new_buses = df_raw_buses[
        ~df_raw_buses.bus_number.isin(df_existing_buses.bus_number)
    ]
    context.log.info(f"Found {df_existing_buses.shape[0]} existing busses and {new_buses.shape[0]} new buses")
    return new_buses
