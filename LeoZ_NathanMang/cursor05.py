from lxml import etree
import arcpy
import os
# Check prov_abbrev is ON, QC, ...
prov_name = ['ON','QC','NB','NS']
ws = r'..\..\..\..\data\Canada\Canada.gdb'
fields=['NAME','PROV','SHAPE@X','SHAPE@Y','UTM_MAP']
arcpy.env.workspace = ws
fc = 'MajorCities'
# create KML document
kml_doc = etree.Element("kml", xmlns="http://www.opengis.net/kml/2.2")
doc = etree.SubElement(kml_doc, "Document")
with arcpy.da.SearchCursor(fc, fields) as cursor:
    for row in cursor:
        name = row[0] + ", " + row[1]
        url = "http://www.canmaps.com/topo/nts50/map/{}.htm".format(row[4])
        coordinates = "{},{}".format(row[2],row[3]) 
        placemark = etree.SubElement(doc, "Placemark")
        etree.SubElement(placemark, "name").text = name
        etree.SubElement(placemark, "description").text = url
        point = etree.SubElement(placemark, "Point")
        etree.SubElement(point, "coordinates").text = coordinates

parent_dir = os.path.abspath(os.path.join(os.getcwd(), ".."))
output_path = os.path.join(parent_dir, "output","Cities.kml")

# write KML document to file
with open(output_path, "wb") as f:
    f.write(etree.tostring(kml_doc, pretty_print=True))