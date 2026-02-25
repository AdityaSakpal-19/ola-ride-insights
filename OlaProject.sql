DROP TABLE OLA_RIDES PURGE;

CREATE TABLE ola_ride (
    date_col              VARCHAR2(50),
    time_col              VARCHAR2(20),
    booking_id            VARCHAR2(50),
    booking_status        VARCHAR2(50),
    customer_id           VARCHAR2(50),
    vehicle_type          VARCHAR2(50),
    pickup_location       VARCHAR2(100),
    drop_location         VARCHAR2(100),
    v_tat                 NUMBER(10,2),
    c_tat                 NUMBER(10,2),
    canceled_rides_by_customer VARCHAR2(200),
    canceled_rides_by_driver   VARCHAR2(200),
    incomplete_rides      VARCHAR2(10),
    incomplete_rides_reason VARCHAR2(200),
    booking_value         NUMBER(10,2),
    payment_method        VARCHAR2(50),
    ride_distance         NUMBER(10,2),
    driver_ratings        NUMBER(3,2),
    customer_rating       NUMBER(3,2),
    vehicle_images        VARCHAR2(500)
);