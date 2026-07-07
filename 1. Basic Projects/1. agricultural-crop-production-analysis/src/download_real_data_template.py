"""
Template for replacing the synthetic demo dataset with official data.

Recommended sources:
1. FAOSTAT Crops and Livestock Products:
   https://www.fao.org/faostat/en/#data/QCL

2. FAOSTAT bulk download metadata:
   https://bulks-faostat.fao.org/production/datasets_E.xml

3. Our World in Data Grapher API example:
   https://ourworldindata.org/grapher/wheat-production.csv?v=1&csvType=full&useColumnShortNames=false

Important:
- This script is a template because source schemas and URLs may change.
- Always verify units before analysis: tonnes, hectares, kg/ha.
- Do not mix production, yield, and harvested area without checking the "element" and "unit" fields.
"""

from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parents[1]
RAW_DIR = PROJECT_ROOT / "data" / "raw"


def download_owid_wheat_production() -> pd.DataFrame:
    """
    Example of how to download one OWID/FAOSTAT-derived chart.

    This requires internet access.
    """
    url = (
        "https://ourworldindata.org/grapher/wheat-production.csv"
        "?v=1&csvType=full&useColumnShortNames=false"
    )
    return pd.read_csv(url)


def main() -> None:
    RAW_DIR.mkdir(parents=True, exist_ok=True)

    # Example:
    # wheat_df = download_owid_wheat_production()
    # wheat_df.to_csv(RAW_DIR / "owid_wheat_production.csv", index=False)

    print("Template ready. Uncomment download code after confirming source URL and schema.")


if __name__ == "__main__":
    main()
