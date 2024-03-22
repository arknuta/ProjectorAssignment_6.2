import csv
from convector import temperature, distance


def convert_temperature(reading, covert_to_temp):
    temperature_value = float(reading[:-2])
    if reading.endswith("°C") and covert_to_temp == "F":
        return temperature.cel_to_fahr(temperature_value)
    elif reading.endswith("°F") and covert_to_temp == "C":
        return temperature.fahr_to_cel(temperature_value)
    else:
        return temperature_value


def covert_distance(reading, convert_to_dist):
    distance_value = float(reading[:-2])
    if reading.endswith("m") and convert_to_dist == "ft":
        distance_value = float(reading[:-1])
        return distance.meters_to_feet(distance_value)
    elif reading.endswith("ft") and convert_to_dist == "m":
        return distance.feet_to_meters(distance_value)
    elif reading.endswith("ft"):
        return float(reading[:-2])
    elif reading.endswith("m"):
         return float(reading[:-1])


def main(input_file, output_file, convert_to_temp, convert_to_dist):
    with open(input_file, "r") as input_f, open(output_file, "w", newline = "") as output_f:
        reader = csv.DictReader(input_f)

        writer = csv.DictWriter(output_f, fieldnames=reader.fieldnames)
        writer.writeheader()

        for row in reader:
            converted_temperature = convert_temperature(row["Reading"], convert_to_temp)
            converted_distance = covert_distance( row["Distance"], convert_to_dist)
            row["Reading"] = f"{converted_temperature}°{convert_to_temp}"
            row["Distance"] = f"{converted_distance}{convert_to_dist}"
            writer.writerow(row)


if __name__ == "__main__":
    main("input.csv", "output.csv", "C", "ft")

















