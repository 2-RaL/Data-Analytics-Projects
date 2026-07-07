-- Agricultural Crop Production Analysis
-- Basic SQL analysis queries

-- 1. Top crops by latest year production
SELECT
    crop,
    year,
    production_tonnes,
    area_harvested_ha,
    yield_kg_per_ha
FROM crop_production
WHERE year = (SELECT MAX(year) FROM crop_production)
ORDER BY production_tonnes DESC;

-- 2. Yearly total production
SELECT
    year,
    SUM(production_tonnes) AS total_production_tonnes,
    SUM(area_harvested_ha) AS total_area_harvested_ha,
    SUM(production_tonnes) * 1000.0 / NULLIF(SUM(area_harvested_ha), 0) AS weighted_yield_kg_per_ha
FROM crop_production
GROUP BY year
ORDER BY year;

-- 3. Crop production share in latest year
SELECT
    crop,
    production_tonnes,
    production_tonnes * 100.0 / SUM(production_tonnes) OVER () AS production_share_pct
FROM crop_production
WHERE year = (SELECT MAX(year) FROM crop_production)
ORDER BY production_share_pct DESC;

-- 4. Crop-level volatility proxy
SELECT
    crop,
    AVG(production_yoy_growth_pct) AS avg_yoy_growth_pct,
    AVG(volatility_score) AS volatility_score
FROM crop_production
WHERE production_yoy_growth_pct IS NOT NULL
GROUP BY crop
ORDER BY volatility_score DESC;
