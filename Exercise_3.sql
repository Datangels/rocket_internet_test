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


SELECT cities.city_name, DAYNAME(events._ts),
(sum(CASE WHEN events.event_name = 'sign_up_success' THEN 1 ELSE 0 END) / COUNT(events.event_name)) as ratio
FROM deliveries
    JOIN events
        ON deliveries.rider_id = events.rider_id
    JOIN cities
        ON events.city_id = cities.city_id
WHERE cities.city_name = 'Singapore' or cities.city_name = 'Bangkok'
AND deliveries.status = 'completed'
AND events._ts BETWEEN STR_TO_DATE('01/01/2016', '%m/%d/%Y') AND STR_TO_DATE('07/01/2016', '%m/%d/%Y')
AND deliveries.actual_eta <= STR_TO_DATE('14/01/2016', '%m/%d/%Y');
