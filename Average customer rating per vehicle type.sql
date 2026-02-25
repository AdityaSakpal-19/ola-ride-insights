SELECT vehicle_type,
       AVG(customer_rating) AS avg_customer_rating
FROM OLA_RIDES
GROUP BY vehicle_type
ORDER BY avg_customer_rating DESC;