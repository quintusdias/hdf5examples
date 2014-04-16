"""
This example code illustrates how to access and visualize LAADS MODIS swath
file in Python. 
If you have any questions, suggestions, comments  on this example, please use
the HDF-EOS Forum (http://hdfeos.org/forums). 
If you would like to see an  example of any other NASA HDF/HDF-EOS data
product that is not listed in the HDF-EOS Comprehensive Examples page
(http://hdfeos.org/zoo), 
feel free to contact us at eoshelp@hdfgroup.org or post it at the
HDF-EOS Forum (http://hdfeos.org/forums).
"""

import os
import sys

#import mpl_toolkits.basemap
import matplotlib.pyplot as plt
import netCDF4 as nc4

#def run(data_root='.'):
data_root = '/opt/data/hdfeos'
FILE_NAME = os.path.join(data_root,
                         'MOD07_L2.A2010001.0000.005.2010004001518.hdf')
SWATH_NAME='mod07'

# Opening the HDF-EOS2 Swath File
ncid = nc4.Dataset(FILE_NAME)

DATAFIELD_NAME = 'Retrieved_Moisture_Profile'
data1 = ncid.variables['Retrieved_Moisture_Profile'][:]

#file_id = hdfsw('open', FILE_NAME, 'rdonly')
## Open swath
#swath_id = hdfsw('attach', file_id, SWATH_NAME)
#
#%Reading Data from a Data Field
#DATAFIELD_NAME='Retrieved_Moisture_Profile'
#
#[data1, fail] = hdfsw('readfield', swath_id, DATAFIELD_NAME, [], [], [])
#
#%Reading lat and lon data
lon = ncid.variables['Longitude'][:]
lat = ncid.variables['Latitude'][:]

# Convert M-D data to 2-D data
#data=squeeze(data1(:,:,6))
data = data1[5,:,:]

#%Convert the data to double type for plot
#data=double(data)
#lon=double(lon)
#lat=double(lat)
#
#%Reading attributes from the data field
#FILE_NAME='MOD07_L2.A2010001.0000.005.2010004001518.hdf'
#SD_id = hdfsd('start',FILE_NAME, 'rdonly')
#DATAFIELD_NAME='Retrieved_Moisture_Profile'
#
#sds_index = hdfsd('nametoindex', SD_id, DATAFIELD_NAME)
#
#sds_id = hdfsd('select',SD_id, sds_index)
#
#
# Reading filledValue from the data field
#fillvalue_index = hdfsd('findattr', sds_id, '_FillValue')
#[fillvalue, status] = hdfsd('readattr',sds_id, fillvalue_index)
fillvalue = ncid.variables['Retrieved_Moisture_Profile']._FillValue
#
#%Reading units from the data field
#units_index = hdfsd('findattr', sds_id, 'units')
#[units, status] = hdfsd('readattr',sds_id, units_index)
units = ncid.variables['Retrieved_Moisture_Profile'].units

#%Reading scale_factor from the data field
#scale_index = hdfsd('findattr', sds_id, 'scale_factor')
#[scale, status] = hdfsd('readattr',sds_id, scale_index)
scale = ncid.variables['Retrieved_Moisture_Profile'].scale_factor
#
#%Reading add_offset from the data field
#offset_index = hdfsd('findattr', sds_id, 'add_offset')
#[offset, status] = hdfsd('readattr',sds_id, offset_index)
offset = ncid.variables['Retrieved_Moisture_Profile'].add_offset
#
#%Terminate access to the corresponding data set
#hdfsd('endaccess', sds_id)
#%Closing the File
#hdfsd('end', SD_id)
#
#%Replacing the filled value with NaN
#data(data==fillvalue) = NaN
#
#%Multiplying scale and adding offset, the equation is scale *(data-offset).
data = scale * (data - offset)
#data = scale*(data-offset)
#
#%Plot the data using contourfm and axesm
#pole=[-90 0 0]
#latlim=[-90,ceil(max(max(lat)))]
#lonlim=[floor(min(min(lon))),ceil(max(max(lon)))]
#min_data=floor(min(min(data)))
#max_data=ceil(max(max(data)))
#
#% create the graphics figure -- 'visible'->'off' = off-screen rendering
#figure_handle=figure('Name', ...
#'MOD07_L2.A2010001.0000.005.2010004001518_Retrieved_Moisture_Profile_Pressure_Leve5', 'visible','on')
#% if 'visible'->'on', figure_handle is undefined
#
#whitebg('w')
#axesm('MapProjection','stereo','MapLatLimit', latlim, 'MapLonLimit',lonlim, ...
#      'Origin',pole,'Frame','on','Grid','on', ...
#      'MeridianLabel','on','ParallelLabel','on')
#coast = load('coast.mat')
#
#% surfacem is faster than contourfm
#% contourfm(lat, lon, data, 'LineStyle','none')
#surfacem(lat, lon, data)
#colormap('Jet')
#caxis([min_data max_data]) 
#colorbar('YTick', min_data:0.2:max_data)
#
#plotm(coast.lat,coast.long,'k')
#
#title({'MOD07\_L2.A2010001.0000.005.2010004001518'['Retrieved Moisture Profile at Pressure\_Level=5, units: ',units]}, 'FontSize',16,'FontWeight','bold')
#
#scrsz = get(0,'ScreenSize')
#if ishghandle(figure_handle)
#  set(figure_handle,'position',scrsz,'PaperPositionMode','auto')
#
#  saveas(figure_handle, ...
#  'MOD07_L2.A2010001.0000.005.2010004001518_Retrieved_Moisture_Profile_Pressure_level5_Polar.m.jpg')
#end
#
#m = basemap.Basemap(projection='spstere', boundinglat=-70)
#m.drawcoastlines()
#m.drawparallels(np.arange(-80., 81., 20.))
#m.drawmeridians(np.arange(-180., 181., 20.))
plt.imshow(lon, lat, data)

# fontsize?
ax = plt.gca()
titlestr = 'MOD07\_L2.A2010001.0000.005.2010004001518\nRetrieved Moisture Profile at Pressure\_Level=5, units: {0}'.format(units)
plt.title(titlestr)

#if __name__ == "__main__":
#    if len(sys.argv) > 1:
#        dataroot = sys.argv[1]
#    else:
#        dataroot = '.'
#    run(dataroot)
