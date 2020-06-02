from osgeo import gdal

filepath = r"try2.tif"

# Open the file:
raster = gdal.Open(filepath)

# Check type of the variable 'raster'
print(type(raster))
