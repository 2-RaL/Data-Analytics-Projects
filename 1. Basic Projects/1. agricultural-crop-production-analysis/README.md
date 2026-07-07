# Agricultural Crop Production Analysis

## Project Type
Basic Data Analytics Portfolio Project

## Sector
Agriculture, Food Security, Public Policy

## Important Data Note
This repository contains a **synthetic demo dataset** structured in a FAOSTAT-style crop production format. It is included so the project can run end-to-end without internet access. The methodology, code, data cleaning pipeline, KPIs, visualizations, and reporting structure are designed so the synthetic data can later be replaced with official FAOSTAT, Our World in Data, World Bank, or Azerbaijan State Statistical Committee data.

## Business Problem
Agricultural decision-makers need to understand whether crop production growth is driven by more harvested area or by productivity improvements. This project analyzes crop production, harvested area, yield, year-over-year growth, production shares, and volatility to identify priority crops for policy, productivity improvement, and food security planning.

## Business Questions
1. Which crops have the highest production volume?
2. Which crops show the strongest growth trend over time?
3. Is production growth driven by area expansion or yield improvement?
4. Which crops have the highest volatility and therefore higher planning risk?
5. Which products should be prioritized for agricultural policy and productivity support?

## Tools Used
- Python
- Pandas
- NumPy
- Matplotlib
- Excel
- Markdown
- SQL

## Repository Structure
```text
agricultural-crop-production-analysis/
├── data/
│   ├── raw/
│   └── processed/
├── notebooks/
├── src/
├── outputs/
│   ├── figures/
│   └── tables/
├── reports/
├── dashboard/
├── sql/
├── docs/
├── README.md
├── requirements.txt
└── .gitignore
```

## Main KPIs
- Total production, tonnes
- Harvested area, hectares
- Yield, kg/ha
- Production share, %
- Year-over-year growth, %
- Volatility score

## Key Findings from the Demo Dataset
- Wheat is the largest crop by production volume in the latest year.
- Vegetables and potatoes have high production values due to higher yields per hectare.
- Cotton has a high growth profile but also higher volatility.
- Production growth should be interpreted together with yield and harvested area to avoid misleading conclusions.

## How to Run
```bash
pip install -r requirements.txt
python src/data_cleaning.py
python src/feature_engineering.py
python src/visualization.py
```

## Replace Synthetic Data with Official Data
Use `src/download_real_data_template.py` as a guide. Recommended data sources:
- FAOSTAT: https://www.fao.org/faostat/en/#data/QCL
- FAO bulk downloads: https://bulks-faostat.fao.org/production/datasets_E.xml
- Our World in Data grapher API: https://ourworldindata.org/grapher/wheat-production
- World Bank Agriculture & Rural Development: https://data.worldbank.org/topic/agriculture-and-rural-development
- Azerbaijan State Statistical Committee Agriculture: https://www.stat.gov.az/source/agriculture/

## Portfolio Deliverables
- Cleaned analytical dataset
- Excel dashboard workbook
- Word report
- PDF report
- Python scripts
- Jupyter notebooks
- SQL queries
- Chart images
- README documentation

## Limitations
The included dataset is synthetic and is not suitable for official policy decisions. It is intended for portfolio demonstration, teaching, code review, and methodology development. For production use, replace the data with official source data.
