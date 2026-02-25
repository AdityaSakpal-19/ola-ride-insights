SELECT SUM(booking_value) AS total_successful_revenue
FROM OLA_RIDES
WHERE booking_status = 'Success';