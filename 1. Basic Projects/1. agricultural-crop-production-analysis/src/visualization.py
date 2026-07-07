"""
Visualization module for Agricultural Crop Production Analysis.
"""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]
INPUT_PATH = PROJECT_ROOT / "data" / "processed" / "crop_production_cleaned.csv"
FIGURE_DIR = PROJECT_ROOT / "outputs" / "figures"


def plot_selected_crop_trends(df: pd.DataFrame, crops: list[str]) -> None:
    """
    Plot production trends for selected crops.
    """
    plt.figure(figsize=(10, 6))

    for crop in crops:
        crop_df = df[df["crop"] == crop]
        plt.plot(crop_df["year"], crop_df["production_tonnes"] / 1000, marker="o", label=crop)

    plt.title("Production Trend by Selected Crops")
    plt.xlabel("Year")
    plt.ylabel("Production (thousand tonnes)")
    plt.legend()
    plt.tight_layout()
    plt.savefig(FIGURE_DIR / "production_trend_selected_crops_from_script.png", dpi=180)
    plt.close()


def plot_top_crops_latest_year(df: pd.DataFrame) -> None:
    """
    Plot top crops by production in the latest year.
    """
    latest_year = df["year"].max()
    latest_df = df[df["year"] == latest_year].copy()
    top_crops = latest_df.sort_values("production_tonnes", ascending=False).head(10)
    top_crops = top_crops.sort_values("production_tonnes")

    plt.figure(figsize=(10, 6))
    plt.barh(top_crops["crop"], top_crops["production_tonnes"] / 1000)
    plt.title(f"Top Crops by Production, {latest_year}")
    plt.xlabel("Production (thousand tonnes)")
    plt.tight_layout()
    plt.savefig(FIGURE_DIR / "top_crops_production_latest_year_from_script.png", dpi=180)
    plt.close()


def main() -> None:
    FIGURE_DIR.mkdir(parents=True, exist_ok=True)
    df = pd.read_csv(INPUT_PATH)

    selected_crops = ["Wheat", "Barley", "Vegetables", "Fruits and berries", "Potatoes"]
    plot_selected_crop_trends(df, selected_crops)
    plot_top_crops_latest_year(df)
    print(f"Figures saved to: {FIGURE_DIR}")


if __name__ == "__main__":
    main()
