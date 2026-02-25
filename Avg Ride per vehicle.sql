SELECT vehicle_type,
       AVG(ride_distance) AS avg_ride_distance
FROM OLA_RIDES
GROUP BY vehicle_type
ORDER BY avg_ride_distance DESC;