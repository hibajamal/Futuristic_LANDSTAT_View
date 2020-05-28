from osgeo import gdal
import matplotlib.pyplot as plt

ds = gdal.Open('try2.tif').ReadAsArray()
ds = ds.reshape((ds.shape[1], ds.shape[2], 3))
print(ds.shape)

plt.imshow(ds)
plt.show()
