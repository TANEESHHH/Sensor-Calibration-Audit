My Programme does this jobs
• Write reports/clean/day1.csv and reports/clean/day2.csv, each beginning with
sensor_id,corrected, followed by sensor_id,corrected_value rows.
• Across both days, write reports/summary/sensors.csv. It begins with
sensor_id,count,total. Its rows follow the order of offsets.txt; for each sensor, count
and total use only retained corrected readings. Include a sensor even when its count is zero.
• Print exactly Wrote X cleaned readings., where X is the total number of retained readings.
