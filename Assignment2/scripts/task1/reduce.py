#!/usr/bin/python

import sys

cnt = 0

for line in sys.stdin:

    k, v = line.strip().split('&')
    cnt += 1

    if cnt % 2 == 1: # trip - 1st
        trip_v = v
    else: # fare
        if k != "medallion,hack_license,vendor_id,pickup_datetime":
            print ("%s	%s" % (k, (trip_v + ',' + v)))
