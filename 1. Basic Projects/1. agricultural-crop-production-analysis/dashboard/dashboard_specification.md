# Power BI Dashboard Specification

## Dashboard Name
Agricultural Crop Production Performance Dashboard

## Target Users
- Agricultural policy analysts
- BI analysts
- Food security teams
- Ministry reporting teams

## Pages

### Page 1: Executive Overview
KPI cards:
- Total production
- Total harvested area
- Weighted yield
- Latest year
- Top crop by production

Charts:
- Total production trend
- Top crops by latest-year production
- Production share by crop

### Page 2: Crop Performance
Slicers:
- Year
- Crop

Charts:
- Production trend by crop
- Yield trend by crop
- Harvested area trend by crop
- YoY growth table

### Page 3: Risk and Volatility
Charts:
- Volatility by crop
- YoY production growth heatmap
- Area vs production scatter plot

## Recommended Measures
```DAX
Total Production = SUM(crop_production[production_tonnes])

Total Area = SUM(crop_production[area_harvested_ha])

Weighted Yield =
DIVIDE([Total Production] * 1000, [Total Area])

Production Share =
DIVIDE([Total Production], CALCULATE([Total Production], ALL(crop_production[crop])))

YoY Production Growth =
VAR CurrentProduction = [Total Production]
VAR PreviousProduction =
    CALCULATE([Total Production], DATEADD('Date'[Date], -1, YEAR))
RETURN
DIVIDE(CurrentProduction - PreviousProduction, PreviousProduction)
```
