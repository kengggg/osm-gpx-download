import urllib2
import time

#Boundary Box
min_ln = "98.9311981"
min_lt = "18.7347042"
max_ln = "99.0335083"
max_lt = "18.8309158"

#Start downloading page
page = 0 

#Using OSM API V0.6
url = "http://api.openstreetmap.org/api/0.6/trackpoints?bbox="+min_ln+","+min_lt+","+max_ln+","+max_lt+"&page="+str(page)

print url

file_prefix = "download_"
file_suffix = ".gpx"

while True:
    try:
        file_name = file_prefix+str(page)+file_suffix
        u = urllib2.urlopen(url+str(page))
        f = open(file_name, 'wb')
        meta = u.info()
        file_size = int(meta.getheaders("Content-Length")[0])
        print "Downloading: %s Bytes: %s" % (file_name, file_size)

        file_size_dl = 0
        block_sz = 8192
        while True:
            buffer = u.read(block_sz)
            if not buffer:
                break

            file_size_dl += len(buffer)
            f.write(buffer)
            status = r"%10d  [%3.2f%%]" % (file_size_dl, file_size_dl * 100. / file_size)
            status = status + chr(8)*(len(status)+1)
            print status,

        f.close()
        
        page += 1
        time.sleep(60)
    except urllib2.HTTPError ,e:
        print "Download stopped; HTTP Error - %s" % e.code
        break
