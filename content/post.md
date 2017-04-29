Title:Geo-Locate Internet Protocol (IP) Traffic With Python
Date:21/04/2017
Author:Piyush Singh
Category:Python
Tags:Forensic DataInvestigation
Head:WHERE IS THAT IP TRAFFIC HEADED?—A PYTHON ANSWER

![Alt Text]({filename}/images/1.jpg)

To begin with, we must how to correlate an Internet Protocol (IP) address to a physical
location. To do this, we will rely on a freely available database from MaxMind, Inc. 
While MaxMind offers several precise commercial products, its open-source GeoLiteCity
database available at http://www.maxmind.com/ app/geolitecity offers us enough fidelity to
correlate IP addresses to cities. Once the database has been downloaded, we need to
decompress it and move it to a location such as /opt/GeoIP/Geo.dat.

>analyst# wget http://geolite.maxmind.com/download/geoip/database/ GeoLiteCity.dat.gz


>2012-03-17 09:02:20-- http://geolite.maxmind.com/download/geoip/database/GeoLiteCity.dat.gz


>Resolving geolite.maxmind.com... 174.36.207.186


>Connecting to geolite.maxmind.com|174.36.207.186|:80... connected. 


>HTTP request sent, awaiting response... 200 OK


>Length: 9866567 (9.4M) [text/plain]


>Saving to: 'GeoLiteCity.dat.gz'


>100%[================================================ ==================================================== ==================================================>] 9,866,567 724K/s in 15s k





>2012-03-17 09:02:36 (664 KB/s) – 'GeoLiteCity.dat.gz' saved [9866567/9866567]


>analyst#gunzip GeoLiteCity.dat.gz analyst#mkdir /opt/GeoIP


>analyst#mv GeoLiteCity.dat /opt/GeoIP/Geo.dat


With the GeoCityLite database, we can correlate an IP address to a state, postal code, 
country name, and general latitude and longitude coordinates. 
All of this will prove useful in analyzing IP traffic.

##Using PyGeoIP to Correlate IP to Physical Locations##

Jennifer Ennis produced a pure Python library to query the GeoLiteCity data- base. Her 
library can be downloaded from [pygeoip](http://code.google.com/p/pygeoip/) and installed prior to 
importing it into a Python script. Note that we will first instantiate a GeoIP class with 
the location of our uncompressed database. Next we will query the database for a specific 
record, specifying the IP address. This returns a record containing fields for city, 
region_name, postal_code, coun- try_name, latitude and longitude, among other 
identifiable information.

CODE Below:


    :::python
    import pygeoip
    gi = pygeoip.GeoIP('/opt/GeoIP/Geo.dat') def printRecord(tgt):
    rec = gi.record_by_name(tgt) city = rec['city']
    region = rec['region_name'] country = rec['country_name'] long = rec['longitude']
    lat = rec['latitude']
    print '[*] Target: ' + tgt + ' Geo-located. '
    print '[+] '+str(city)+', '+str(region)+', '+str(country) print '[+] Latitude: '
    +str(lat)+ ', Longitude: '+ str(long)
    tgt = '173.255.226.98' printRecord(tgt)
    
    
Running the script, we see that it produces output showing the target IP’s physical 
location in Jersey City, NJ, US, with latitude 40.7245 and longitude −74.0621. Now that 
we are able to correlate an IP to a physical address, let’s begin writing our analysis 
script.

    :::python
    analyst# python printGeo.py
    [*] Target: 173.255.226.98 Geo-located. [+] Jersey City, NJ, United States
    [+] Latitude: 40.7245, Longitude: −74.0621
    
Thanking You
Do Share this efforts.
