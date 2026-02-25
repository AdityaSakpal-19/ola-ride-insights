SELECT COUNT(*) AS total_cancelled_by_customers
FROM OLA_RIDES
WHERE booking_status = 'Canceled by Customer';