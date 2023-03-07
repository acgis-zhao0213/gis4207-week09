import sys
def main():
    global arcpy
    if len(sys.argv) != 2:
        print('Usage: cursor02.py <prov_abbrev>')
        sys.exit()
    # Check prov_abbrev is ON, QC, ...
    prov_name = ['ON','QC','NB','NS']
    if sys.argv[1] in prov_name:
        import arcpy
        ws = r'..\..\..\..\data\Canada'
        prov = sys.argv[1].upper()
        fields=['NAME','PROV']
        field = arcpy.AddFieldDelimiters(ws, 'PROV')
       
        where_clause = f"{field} = '{prov}'"
    
        arcpy.env.workspace = ws
        fc = 'Can_Mjr_Cities.shp'
        
        with arcpy.da.SearchCursor(fc, fields, where_clause) as cursor:
            for row in cursor:
    
                print(row)

if __name__ == "__main__":
    main()