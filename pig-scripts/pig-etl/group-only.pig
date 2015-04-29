-------------------------------------------------------------------------------
--
-- Big Data - Final Project
-- group-only.pig
-- Group by the combination of pickup zipcode and dropoff zipcode
-- contact: drp354@nyu.edu
--
-------------------------------------------------------------------------------

-- load the data
in1 = LOAD 'final-project/rtree-test/out-new-mod-tip-fixed/part-00000' 
USING PigStorage(',') 
AS (id:chararray,pickup_datetime:chararray,dropoff_datetime:chararray,trip_time_in_secs:float, trip_distance:float, fare_amount:float, tip_amount:float, tip_percentage:float,
    pickup_zipcode:int, dropoff_zipcode:int);

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
STORE in2 INTO 'final-project/join-test/output/outGROUP1' USING PigStorage (',');
