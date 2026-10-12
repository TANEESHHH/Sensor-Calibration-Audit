def read_offsets(filename):
    offsets = {}
    with open(filename, "r") as file:
        for line in file:
            key, val = line.strip().split(",")
            key = key.strip()
            val = val.strip()
            offsets[key] = int(val)      
    return offsets                

def process_day(input_name, output_name, offsets, totals, counts):
    counter = 0
    with open(input_name, "r") as ifile:
        with open(output_name, "w") as ofile:
            ofile.write("sensor_id,corrected\n")
            for line in ifile:
                sensor_id,reading = line.strip().split(",")
                sensor_id = sensor_id.strip()
                reading = int(reading.strip())
                corrected = reading + int(offsets[sensor_id])
                if 0 <= corrected <= 100:
                    ofile.write(f"{sensor_id},{corrected}\n")
                    counter += 1
                    totals[sensor_id] += corrected
                    counts[sensor_id] += 1
    return counter

def write_summary(filename, totals, counts):
    with open(filename, "w") as file:
        file.write("sensor_id,count,total\n")
        for sensor_id in totals:
            file.write(f"{sensor_id},{counts[sensor_id]},{totals[sensor_id]}\n")
    return

def main():
    offsets = read_offsets("calibration/offsets.txt")
    totals = {}
    for sensor_id in offsets:
        totals[sensor_id] = 0
    counts = {}
    for sensor_id in offsets:
        counts[sensor_id] = 0  
    day1count = process_day(
    "observations/day1/readings.txt",
    "reports/clean/day1.csv",
    offsets,
    totals,
    counts)
    day2count = process_day(
    "observations/day2/readings.txt",
    "reports/clean/day2.csv",
    offsets,
    totals,
    counts)
    write_summary("reports/summary/sensors.csv", totals, counts)
    print(f"Wrote {int(day1count) + int(day2count)} cleaned readings.")      
    pass

if __name__ == "__main__":
    main()