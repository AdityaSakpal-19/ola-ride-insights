SELECT booking_id,
       vehicle_type,
       incomplete_rides_reason
FROM OLA_RIDES
WHERE incomplete_rides = 'Yes';