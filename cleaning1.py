###############################################################################
##
## Big Data - Final Project
## cleaning1.py
## Join fares and trips and search the zipcodes using rtree
## contact: drp354@nyu.edu
##
###############################################################################

import csv,sys,os
import numpy
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib.path import Path
from datetime import date,datetime
from rtree import index as rtree
import shapefile  
from pyproj import Proj, transform

def dataInit():
    filename_fares = 'input/fares_sunday.csv'
    filename_trips = 'input/trips_sunday.csv'
    df_fares = pd.read_csv(filename_fares)
    df_trips = pd.read_csv(filename_trips)
    df_alltaxi = pd.merge(df_fares, df_trips, how='inner', on=['medallion','hack_license','vendor_id','pickup_datetime'])
    return df_alltaxi

def findNeighborhood(location, index, neighborhoods):
    match = index.intersection((location[0], location[1], location[0], location[1]))
    for a in match:
        if any(map(lambda x: x.contains_point(location), neighborhoods[a][1])):
            return a
    return -1

def readNeighborhood(shapeFilename, index, neighborhoods):
    sf = shapefile.Reader(shapeFilename)
    for sr in sf.shapeRecords():
        if sr.record[0].strip() not in ['New York', 'Staten Island', 'Queens', 'Bronx','Brooklyn']:
            continue
        paths = map(Path, numpy.split(sr.shape.points, sr.shape.parts[1:]))
        bbox = paths[0].get_extents()
        map(bbox.update_from_path, paths[1:])
        index.insert(len(neighborhoods), list(bbox.get_points()[0])+list(bbox.get_points()[1]))
        neighborhoods.append((sr.record[3], paths))
    neighborhoods.append(('UNKNOWN', None)) 


def geocode(longitude,latitude):
    if not latitude or not longitude:
        print("Error reading longitude/latitude")
        sys.exit()

    index = rtree.Index()
    neighborhoods = []
    agg = {}

    readNeighborhood('zip_codes_shp/PostalBoundary.shp', index, neighborhoods)

    #convert to projected
    inProj = Proj(init='epsg:4326')
    outProj = Proj(init='epsg:26918')
    outx,outy = transform(inProj,outProj,longitude,latitude)
    pickup_location = (outx,outy)

    resultMap = findNeighborhood(pickup_location, index, neighborhoods)
    if resultMap!=-1:
        zipcode_result = neighborhoods[resultMap][0]
        return zipcode_result
    else:
        print("Unable to convert lat-lon: %f %f"%(float(latitude),float(longitude)))
        return -1


def main():

    df = dataInit()

    for index, row in df.iterrows():
        df.loc[index,'zipcode_pickup'] = geocode(row['pickup_longitude'], row['pickup_latitude'])
        df.loc[index,'zipcode_dropoff'] = geocode(row['dropoff_longitude'], row['dropoff_latitude'])

    df.to_csv('out.csv')
            
if __name__ == '__main__':
    main()