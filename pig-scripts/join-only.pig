-------------------------------------------------------------------------------
--
-- Big Data - Final Project
-- join-only.pig
-- Join fares and trips with eliminating rows when zipcodes are not available
-- contact: drp354@nyu.edu
--
-------------------------------------------------------------------------------

-- load the data
fares = LOAD 'final-project/input-1-month/trip_fare_12.csv' 
USING PigStorage(',') 
AS (medallion,hack_license,vendor_id,pickup_datetime,payment_type,fare_amount,surcharge,mta_tax,tip_amount,tolls_amount,total_amount);

trips = LOAD 'final-project/input-1-month/trip_data_12.csv' 
USING PigStorage(',') 
AS (medallion,hack_license,vendor_id,rate_code,store_and_fwd_flag,pickup_datetime,dropoff_datetime,passenger_count,trip_time_in_secs,trip_distance,pickup_longitude,pickup_latitude,dropoff_longitude,dropoff_latitude);

-- join operation
alltable = JOIN fares BY (medallion,hack_license,vendor_id,pickup_datetime), trips BY (medallion,hack_license,vendor_id,pickup_datetime);

-- remove null coordinates
min_alltable= FOREACH 
(FILTER alltable
       BY ((trips::pickup_longitude IS NOT NULL) AND 
           (trips::pickup_latitude IS NOT NULL) AND 
           (trips::dropoff_longitude IS NOT NULL) AND 
           (trips::dropoff_latitude IS NOT NULL) AND 
           (fares::payment_type == 'CRD'))
)
GENERATE 	trips::pickup_datetime,
	 	trips::dropoff_datetime,
	 	trips::passenger_count,
		trips::trip_time_in_secs, 
		trips::trip_distance, 
		trips::pickup_longitude, 
		trips::pickup_latitude, 
		trips::dropoff_longitude, 
		trips::dropoff_latitude,
         	fares::fare_amount, 
		fares::tip_amount,
		fares::total_amount
;

-- store the data
STORE min_alltable INTO 'final-project/join-test/output/out-1-month' USING PigStorage (',');
