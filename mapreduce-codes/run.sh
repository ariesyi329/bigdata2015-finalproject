hjs -D mapreduce.job.reduces=1 -file mapper1.py -mapper mapper1.py -file reduce1.py -reducer reduce1.py -file PostalBoundary.* -file PostalInventory.* -input final-project/rtree-test/input  -output final-project/rtree-test/out1

hjs -D mapreduce.job.reduces=1 -files mapper1.py,reduce1.py,PostalBoundary.dbf,PostalBoundary.prj,PostalBoundary.sbn,PostalBoundary.sbx,PostalBoundary.shp,PostalBoundary.shp.xml,PostalBoundary.shx -mapper mapper1.py  -reducer reduce1.py  -input final-project/rtree-test/input  -output final-project/rtree-test/outFINAL4
