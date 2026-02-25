SELECT MAX(driver_ratings) AS max_rating,
       MIN(driver_ratings) AS min_rating
FROM OLA_RIDES
WHERE vehicle_type = 'Prime Sedan';