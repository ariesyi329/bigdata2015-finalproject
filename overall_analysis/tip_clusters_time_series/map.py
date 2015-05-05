#!/usr/bin/python
import sys
#import pickle

#clusters = pickle.loads(open('cluster_results_zipcode', 'r').read())

cluster_a = [10026, 10035, 10458, 10467, 11205, 11232, 10027, 10459, 10468, 11206, 11224, 11233, 10037, 10451, 10460, 10469, 11207, 11216, 11225, 10002, 10029, 10452, 11208, 11226, 10030, 10039, 10453, 10462, 11236, 10031, 10040, 10454, 10463, 10472, 11237, 10032, 10455, 10473, 11220, 11238, 10033, 10456, 10474, 11203, 11212, 11221, 11239, 10034, 10457, 10466, 10475, 11213]

cluster_b = [10017, 10044, 10009, 10018, 10036, 11215, 10001, 10010, 10019, 10028, 10280, 10011, 10038, 10065, 10128, 11217, 10003, 10012, 10021, 10075, 10004, 10013, 10022, 11201, 10005, 10014, 10023, 11211, 10006, 10024, 10007, 10016, 10025, 11222, 11231]

cluster_c = [10305, 10314, 11214, 11223, 10306, 10307, 11234, 10308, 10461, 10470, 11235, 10309, 10471, 11209, 11218, 10301, 10310, 11210, 11219, 11228, 10302, 10464, 11229, 10303, 10312, 10465, 11230, 10304, 11204]


for line in sys.stdin:
    cluster = -1
    line = line.strip()
    values = line.split(',')
    if values[0]:
        tip_perc = values[-3]
        pickup_time = values[2]
        pickup_zipcode = values[-2]
        try:
            pickup_zipcode = int(pickup_zipcode)
            date, time = pickup_time.split(' ')
            time = time[:2]
        except:
            pass
        if pickup_zipcode in cluster_a:
            cluster = 0
        elif pickup_zipcode in cluster_b:
            cluster = 1
        elif pickup_zipcode in cluster_c:
            cluster = 2
        else:
            cluster = -1

        print "%d,%s\t%s" % (cluster,time,tip_perc)
