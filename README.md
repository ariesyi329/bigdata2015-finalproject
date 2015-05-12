# bigdata2015-finalproject

Sample scripts to analyze taxi data on Amazon AWS

Pig join code:
======

1. Pick pig 0.12 instead of hadoop streaming before starting the cluster.
2. Use this arguments
        * s3://us-west-2.elasticmapreduce/libs/pig/pig-script --run-pig-script --pig-versions 0.12.0 --args -f s3://final-project-big-data/codes/join-only.pig

Rtree spatial index code:
======

1. Create an Amazon EMR cluster with the following configuration (the bootstrap action is very important -- please pay attention to that):

        * Termination protection: Yes
        * Logging: Enabled (remember to input your S3 bucket to store log file)
        * Hadoop distribution: Amazon AMI 3.3.1 (it has to be using this AMI Version
        * Bootstrap action: This is a very important step because the sample scripts 
        make use of python rtree library, but Amazon AMI 3.3.1 does not have rtree installed.
        Click 'Add bootstrap action' -> Custom action -> Configure and add -> 
        Put the following in 'S3 location': s3://dimas-rtree-test-zipcode/rtree.sh
        * Cluster Auto-terminate: No

2. Specify the input to thw 2013 fares and trips data. For example:


        * Input 1: s3://final-project-big-data/input/fare2013/
        * Input 2: s3://final-project-big-data/input/trip013/
        * Arguments: -D mapred.reduce.tasks=1 -files
        * s3://final-project-big-data/codes/mapper1.py,s3://final-project-big-data/codes/reduce1.py,
        * s3://final-project-big-data/codes/PostalBoundary.shp,
        * s3://final-project-big-data/codes/PostalBoundary.prj,
        * s3://final-project-big-data/codes/PostalBoundary.shp.xml,
        * s3://final-project-big-data/codes/PostalBoundary.shx,
        * s3://final-project-big-data/codes/PostalBoundary.dbf 
        * -files s3://final-project-big-data/codes/mapper1.py,s3://final-project-big-data/codes/reduce1.py 
        * -mapper mapper1.py -reducer reduce1.py 
        * -input s3://final-project-big-data/output/pig1-join-output/ -output

3. All the output is located under s3://final-project-big-data/output 
You can use aws s3 ls or cp to see the product.


Pig groupby codes:
======

1. Pick pig 0.12 instead of hadoop streaming before starting the cluster.
2. Use this arguments
        * s3://us-west-2.elasticmapreduce/libs/pig/pig-script --run-pig-script --pig-versions 0.12.0 --args -f s3://final-project-big-data/codes/group-only.pig


Pig groupby 2 codes:
======

1. Pick pig 0.12 instead of hadoop streaming before starting the cluster.
2. Use this arguments
        * s3://us-west-2.elasticmapreduce/libs/pig/pig-script --run-pig-script --pig-versions 0.12.0 --args -f s3://final-project-big-data/codes/group-per-zip.pig

**All the links above are made available for public, so you can test that with the link given above.


Contributors
============
1. Dimas Rinarso Putro
2. Yi Liu
3. Pan Ding
