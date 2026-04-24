SELECT crop, AVG(price_per_kg) AS avg_price
FROM crop_prices
GROUP BY crop;

SELECT market, SUM(rainfall_mm) AS total_rainfall
FROM rainfall
GROUP BY market;