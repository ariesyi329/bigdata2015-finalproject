-------------------------------------------------------------------------------
--
-- Big Data - Final Project
-- join-only.pig
-- Join fares and trips with eliminating rows when zipcodes are not available
-- contact: drp354@nyu.edu
--
-------------------------------------------------------------------------------

-- register rtree udf file
Register 'udf.py' using streaming_python as udf;
register 'test.py' using org.apache.pig.scripting.streaming.python.PythonScriptEngine as udf;

outtest = FOREACH fares
GENERATE udf.square(3)
;



-- load the data
fares = LOAD 'final-project/join-test/input/fares_wednesday.csv' 
USING PigStorage(',') 
AS (medallion,hack_license,vendor_id,pickup_datetime:chararray,payment_type:chararray,fare_amount:float,surcharge,mta_tax,tip_amount:float,tolls_amount,total_amount);

trips = LOAD 'final-project/join-test/input/trips_wednesday.csv' 
USING PigStorage(',') 
AS (medallion,hack_license,vendor_id,rate_code,store_and_fwd_flag,pickup_datetime:chararray,dropoff_datetime:chararray,passenger_count,trip_time_in_secs:float,trip_distance:float,
    pickup_longitude:long,pickup_latitude:long,dropoff_longitude:long, dropoff_latitude:long);

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
GENERATE 
--         udf.findzip(trips::pickup_longitude,trips::pickup_latitude,trips::dropoff_longitude,trips::dropoff_latitude),
         udf.test(trips::pickup_longitude,trips::pickup_latitude,trips::dropoff_longitude,trips::dropoff_latitude),
         trips::pickup_datetime AS pickup_datetime,
         trips::dropoff_datetime AS dropoff_datetime,
         trips::trip_time_in_secs AS trip_time_in_secs, 
         trips::trip_distance as trip_distance, 
         fares::fare_amount AS fare_amount, 
         fares::tip_amount AS tip_amount,
         ((fares::tip_amount/fares::fare_amount)*100) AS tip_percentage
;

-- group by pickup_zipcode^dropoff_zipcode (id)
in2 = FOREACH (GROUP in1 BY id)
      GENERATE
             (INT) AVG(in1.pickup_zipcode) AS pickup_zipcode,
             (INT) AVG(in1.dropoff_zipcode) AS dropoff_zipcode,
             AVG(in1.trip_time_in_secs) AS trip_time_in_secs,
             AVG(in1.trip_distance) AS trip_distance,
             AVG(in1.fare_amount) AS fare_amount,
             AVG(in1.tip_amount) AS tip_amount,
             AVG(in1.tip_percentage) AS tip_percentage;


-- store the data
STORE min_alltable INTO 'final-project/join-test/output/outJOIN2' USING PigStorage (',');



