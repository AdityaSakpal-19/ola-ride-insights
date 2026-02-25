SELECT customer_id,
       COUNT(*) AS total_rides
FROM OLA_RIDES
GROUP BY customer_id
ORDER BY total_rides DESC
FETCH FIRST 5 ROWS ONLY;