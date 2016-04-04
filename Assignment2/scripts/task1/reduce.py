#!/usr/bin/python

import sys
cnt = 0

for line in sys.stdin:

    k, v = line.strip().split('&')
    if k != "medallion,hack_license,vendor_id,pickup_datetime":
        if 'trips' in v:
            trip_v = v
        else: # fare
            if k != "medallion,hack_license,vendor_id,pickup_datetime":
                trip_v = trip_v.strip(',trips_sunday')
                trip_v = trip_v.strip(',trips_wednesday')
                v = v.strip(',fares_sunday')
                v = v.strip(',fares_wednesday')
                print ("%s%s" % (k, (trip_v + ',' + v)))
