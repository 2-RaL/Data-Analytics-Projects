"""
Data cleaning module for Agricultural Crop Production Analysis.

This script converts a FAOSTAT-style long dataset into an analytical wide dataset.
The included demo data is synthetic, but the code is designed to work with
official FAOSTAT-style data after column mapping.
"""

from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]
RAW_PATH = PROJECT_ROOT / "data" / "raw" / "crop_production_raw_faostat_style_synthetic.csv"
OUTPUT_PATH = PROJECT_ROOT / "data" / "processed" / "crop_production_cleaned_from_script.csv"


def clean_column_names(df: pd.DataFrame) -> pd.DataFrame:
    """
    Standardize dataframe column names.

    Parameters
    ----------
    df:
        Input dataframe.

    Returns
    -------
    pandas.DataFrame
        Dataframe with cleaned column names.
    """
    cleaned_df = df.copy()
    cleaned_df.columns = (
        cleaned_df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_", regex=False)
        .str.replace("-", "_", regex=False)
    )
    return cleaned_df


def reshape_faostat_long_to_wide(df: pd.DataFrame) -> pd.DataFrame:
    """
    Reshape FAOSTAT-style long crop production data into analytical wide format.

    Expected long fields:
    country, iso3_code, year, crop, element, unit, value
    """
    required_columns = {"country", "iso3_code", "year", "crop", "element", "value"}
    missing_columns = required_columns.difference(df.columns)

    if missing_columns:
        raise ValueError(f"Missing required columns: {missing_columns}")

    value_map = {
        "Area harvested": "area_harvested_ha",
        "Yield": "yield_kg_per_ha",
        "Production": "production_tonnes",
    }

    filtered_df = df[df["element"].isin(value_map.keys())].copy()
    filtered_df["metric"] = filtered_df["element"].map(value_map)

    wide_df = (
        filtered_df
        .pivot_table(
            index=["country", "iso3_code", "year", "crop"],
            columns="metric",
            values="value",
            aggfunc="sum",
        )
        .reset_index()
    )

    wide_df.columns.name = None
    return wide_df


def validate_data(df: pd.DataFrame) -> None:
    """
    Run basic validation checks.
    """
    if df.empty:
        raise ValueError("The cleaned dataframe is empty.")

    if df.duplicated(subset=["country", "year", "crop"]).any():
        raise ValueError("Duplicate country-year-crop records detected.")

    numeric_columns = ["area_harvested_ha", "yield_kg_per_ha", "production_tonnes"]
    for column in numeric_columns:
        if column in df.columns and (df[column] < 0).any():
            raise ValueError(f"Negative values detected in {column}.")


def main() -> None:
    raw_df = pd.read_csv(RAW_PATH)
    raw_df = clean_column_names(raw_df)

    # Restore expected title-case element labels after column cleaning.
    cleaned_df = reshape_faostat_long_to_wide(raw_df)
    validate_data(cleaned_df)

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    cleaned_df.to_csv(OUTPUT_PATH, index=False)
    print(f"Cleaned data saved to: {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
