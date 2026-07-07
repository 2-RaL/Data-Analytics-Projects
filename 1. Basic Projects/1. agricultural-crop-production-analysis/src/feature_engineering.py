"""
Feature engineering module for crop production analysis.
"""

from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]
INPUT_PATH = PROJECT_ROOT / "data" / "processed" / "crop_production_cleaned_from_script.csv"
FALLBACK_INPUT_PATH = PROJECT_ROOT / "data" / "processed" / "crop_production_cleaned.csv"
OUTPUT_PATH = PROJECT_ROOT / "data" / "processed" / "crop_production_features.csv"


def add_growth_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Add year-over-year growth features.
    """
    feature_df = df.sort_values(["crop", "year"]).copy()
    feature_df["production_yoy_growth_pct"] = (
        feature_df.groupby("crop")["production_tonnes"].pct_change() * 100
    )
    feature_df["yield_yoy_growth_pct"] = (
        feature_df.groupby("crop")["yield_kg_per_ha"].pct_change() * 100
    )
    feature_df["area_yoy_growth_pct"] = (
        feature_df.groupby("crop")["area_harvested_ha"].pct_change() * 100
    )
    return feature_df


def add_share_and_rank_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Add production share and annual rank features.
    """
    feature_df = df.copy()
    total_by_year = feature_df.groupby("year")["production_tonnes"].transform("sum")
    feature_df["production_share_pct"] = feature_df["production_tonnes"] / total_by_year * 100
    feature_df["yield_tonnes_per_ha"] = feature_df["yield_kg_per_ha"] / 1000
    feature_df["production_rank_by_year"] = (
        feature_df.groupby("year")["production_tonnes"]
        .rank(method="dense", ascending=False)
        .astype(int)
    )
    feature_df["yield_rank_by_year"] = (
        feature_df.groupby("year")["yield_kg_per_ha"]
        .rank(method="dense", ascending=False)
        .astype(int)
    )
    return feature_df


def add_volatility_feature(df: pd.DataFrame) -> pd.DataFrame:
    """
    Add crop-level volatility score based on YoY production growth.
    """
    feature_df = df.copy()
    volatility = (
        feature_df.groupby("crop")["production_yoy_growth_pct"]
        .std()
        .rename("volatility_score")
        .reset_index()
    )
    return feature_df.merge(volatility, on="crop", how="left")


def main() -> None:
    input_path = INPUT_PATH if INPUT_PATH.exists() else FALLBACK_INPUT_PATH
    df = pd.read_csv(input_path)

    feature_df = add_growth_features(df)
    feature_df = add_share_and_rank_features(feature_df)
    feature_df = add_volatility_feature(feature_df)

    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    feature_df.to_csv(OUTPUT_PATH, index=False)
    print(f"Feature dataset saved to: {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
