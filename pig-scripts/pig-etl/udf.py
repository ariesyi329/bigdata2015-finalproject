#!/usr/bin/env python
###############################################################################
##
## Big Data - Final Project
## udf.py
## Find zipcodes as PIG udf
## contact: drp354@nyu.edu
##
###############################################################################

from pig_util import outputSchema

def findNeighborhood(location, index_rtree, neighborhoods):
    match = index_rtree.intersection((location[0], location[1], location[0], location[1]))
    for a in match:
        if any(map(lambda x: x.contains_point(location), neighborhoods[a][1])):
            return a
    return -1

def readNeighborhood(shapeFilename, index_rtree, neighborhoods):
    sf = shapefile.Reader(shapeFilename)
    for sr in sf.shapeRecords():
        if sr.record[0].strip() not in ['New York', 'Staten Island', 'Queens', 'Bronx','Brooklyn']:
            continue
        paths = map(Path, numpy.split(sr.shape.points, sr.shape.parts[1:]))
        bbox = paths[0].get_extents()
        map(bbox.update_from_path, paths[1:])
        index_rtree.insert(len(neighborhoods), list(bbox.get_points()[0])+list(bbox.get_points()[1]))
        neighborhoods.append((sr.record[3], paths))
    neighborhoods.append(('UNKNOWN', None)) 

def geocode(longitude,latitude,index_rtree,neighborhoods):
    if not latitude or not longitude:
        #print("Error reading longitude/latitude")
        return -1

    #convert to projected
    inProj = Proj(init='epsg:4326')
    outProj = Proj(init='epsg:26918')
    outx,outy = transform(inProj,outProj,longitude,latitude)
    pickup_location = (outx,outy)

    resultMap = findNeighborhood(pickup_location, index_rtree, neighborhoods)
    if resultMap!=-1:
        zipcode_result = neighborhoods[resultMap][0]
        return zipcode_result
    else:
        #print("Unable to convert lat-lon: %f %f"%(float(latitude),float(longitude)))
        return -1

# the output schema is zipcode
@outputSchema("id:chararray")
def findzip(pickup_longitude,pickup_latitude,dropoff_longitude,dropoff_latitude):

    #load packages
    import csv,sys,os
    os.environ['MPLCONFIGDIR'] = '/tmp'
    import numpy
    from matplotlib.path import Path
    from rtree import index as rtree
    import shapefile  
    from pyproj import Proj, transform
    from pig_util import outputSchema
    #main process
    index_rtree = rtree.Index()
    neighborhoods = []
    agg = {}
    readNeighborhood('PostalBoundary.shp', index_rtree, neighborhoods)
    
    try:
        #attributes for geocoding       
        pickup_location = (float(pickup_longitude), float(pickup_latitude))
        dropoff_location = (float(dropoff_longitude), float(dropoff_latitude))
        pickup_zipcode = geocode(pickup_location[0], pickup_location[1],index_rtree,neighborhoods)
        dropoff_zipcode = geocode(dropoff_location[0], dropoff_location[1],index_rtree,neighborhoods)
        if (pickup_zipcode!=-1) and (dropoff_zipcode!=-1): 
            return str(pickup_zipcode)+'^'+str(dropoff_zipcode)
    except:
        pass


# the output schema is zipcode
@outputSchema("id:chararray")
def test():
    return "hello"
