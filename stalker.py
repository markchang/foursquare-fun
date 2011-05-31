#!/usr/bin/env python
#
# stalks a foursquare friend
# checks their checkins every 360 seconds
# and copies it
# you must be friends with them to see their checkin details

import json
import urllib
import urllib2
import base64
import time

username = "[YOUR USERNAME]"
password = "[YOUR PASSWORD]"
checkin_url = 'https://api.foursquare.com/v1/checkin'
stalkee_url = "https://api.foursquare.com/v1/user.json?uid=[UID # HERE]"

# encode auth
base64string = base64.encodestring('%s:%s' % (username,password))[:-1]

venue_id = last_venue_id = 0
while 1:
  # get stalkee's json
  req = urllib2.Request(stalkee_url)
  req.add_header('Authorization', "Basic %s" % base64string)
  
  response = urllib2.urlopen(req)
  response_json = response.read()
  response.close()
  stalkee = json.loads(response_json)

  venue_id = stalkee['user']['checkin']['venue']['id']
  venue_name = stalkee['user']['checkin']['venue']['name']
  venue_lat = stalkee['user']['checkin']['venue']['geolat']
  venue_long = stalkee['user']['checkin']['venue']['geolong']

  print "Stalkee's last checkin: "
  print venue_name + " (" + str(venue_id) + ") @" + str(venue_lat) + ", " + str(venue_long)
  
  # do the checkin if new
  if venue_id != last_venue_id:
    print "Stalking at " + venue_name
    last_venue_id = venue_id
    values = {'vid':venue_id, 
              'geolat':str(venue_lat), 
              'geolong':str(venue_long), 
              'private':'0' }
    data = urllib.urlencode(values)
    req = urllib2.Request(checkin_url,data)
    req.add_header('Authorization', "Basic %s" % base64string)
    response = urllib2.urlopen(req)
  
  print "Sleeping..."
  time.sleep(360)
