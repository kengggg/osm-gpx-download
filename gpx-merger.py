from bs4 import BeautifulSoup
import glob
import time
import os
import errno

#Output file name
output_file_name = "trace-out.gpx"
#Output file directory
output_directory = "output"

#Check whether output directory exists?
def make_sure_path_exists(path):
    try:
        os.makedirs(path)
    except OSError as exception:
        if exception.errno != errno.EEXIST:
            raise

make_sure_path_exists(output_directory)

fo = open(output_directory+"/"+output_file_name, "w")
fo.write('<?xml version="1.0" encoding="UTF-8"?>')
fo.write('<gpx version="1.0" creator="OpenStreetMap.org" xmlns="http://www.topografix.com/GPX/1/0">')

gpx_list = glob.glob('*.gpx')

for gpx_file_name in gpx_list:
    print "Parsing "+gpx_file_name+" ..."

    fi = open(gpx_file_name,"r")
    gpx_trace = fi.read()
    fi.close()

    soup = BeautifulSoup(gpx_trace)
    fo.write(soup.trk.prettify())
    
    time.sleep(1)
    
fo.write('</gpx>')
fo.close()
