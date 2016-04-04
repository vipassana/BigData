#!/usr/bin/python

import sys
import os

for line in sys.stdin:

    line = line.strip().split(',')

    if len(line) == 11: # fare
        medallion, hack_license, vendor_id, pickup_datetime, payment_type, fare_amount, surcharge, mta_tax, tip_amount, tolls_amount, total_amount = line
        print ('%s,%s,%s,%s,%s&%s,%s,%s,%s,%s,%s,%s' % (medallion, hack_license, vendor_id, pickup_datetime,os.environ['mapreduce_map_input_file'], payment_type, fare_amount, surcharge, mta_tax, tip_amount, tolls_amount, total_amount))
    elif len(line) == 14: # trip
        medallion, hack_license, vendor_id, rate_code, store_and_fwd_flag, pickup_datetime, dropoff_datetime, passenger_count, trip_time_in_secs, trip_distance, pickup_longitude, pickup_latitude, dropoff_longitude, dropoff_latitude = line
        print ('%s,%s,%s,%s,%s&%s,%s,%s,%s,%s,%s,%s,%s,%s,%s' % (medallion, hack_license, vendor_id, pickup_datetime,os.environ['mapreduce_map_input_file'], rate_code, store_and_fwd_flag, dropoff_datetime, passenger_count, trip_time_in_secs, trip_distance, pickup_longitude, pickup_latitude, dropoff_longitude, dropoff_latitude))
