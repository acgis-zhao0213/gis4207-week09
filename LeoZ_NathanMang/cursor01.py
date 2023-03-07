import sys
import arcpy
ws = r'..\..\..\..\data\Canada'
arcpy.env.workspace = ws
fc = 'Can_Mjr_Cities.shp'

fields=['NAME','PROV']
with arcpy.da.SearchCursor(fc,fields) as cursor:
    count=0
    for row in cursor:
        count+=1
print(row)
