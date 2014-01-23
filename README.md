osm-gps-trace-download.py
======================

A Python script for downloading OSM's GPS traces from given boundary box. 

There are 2 parts of variables that you should adjust to match your need.


```python
#These variables should be adjusted to meet your requirements, 
#see http://wiki.openstreetmap.org/wiki/API_v0.6#Retrieving_GPS_points for more information
#Boundary Box
min_ln = "98.9311981"
min_lt = "18.7347042"
max_ln = "99.0335083"
max_lt = "18.8309158"

#Start downloading page
page = 0 
```

Simply run `python osm-gps-trace-download.py`

gpx-merger.py
======================

A Python script for merging OSM's GPX files.

There are 2 parts of variables that you should adjust to match your need.

```python
#Output file name
output_file_name = "trace-out.gpx"
#Output file directory
output_directory = "output"
```

Simply run `python gpx-merger.py`. You output file should be in `output/trace-out.gpx` by default.

Todo
======================

* Resumable GPX file download
* Merged GPX file noise reduction