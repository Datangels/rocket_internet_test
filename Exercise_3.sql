SELECT cities.city_name,
PERCENTILE_CONT(0.9) WITHIN GROUP (ORDER BY deliveries.predicted_eta - deliveries.actual_eta) AS _90_percentile
FROM deliveries
    JOIN events
        ON deliveries.rider_id = events.rider_id
    JOIN cities
        ON events.city_id = cities.city_id
WHERE cities.city_name = 'Singapore' or cities.city_name = 'Bangkok'
AND deliveries.status = 'completed'
AND DATE_FORMAT(deliveries.actual_eta, '%m/%d/%Y') BETWEEN NOW() - INTERVAL 30 DAY AND NOW();