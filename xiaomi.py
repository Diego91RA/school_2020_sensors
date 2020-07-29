#!/usr/bin/env python3

from btlewrap import BluepyBackend
from mitemp_bt.mitemp_bt_poller import MiTempBtPoller, MI_TEMPERATURE
from datetime import datetime
import time
import csv


def poll():
    """Poll data from the sensor."""
    backend = BluepyBackend
    poller = MiTempBtPoller("4c:65:a8:d1:da:d9", backend)
    print("Getting data from Mi Temperature and Humidity Sensor")
    print("Temperature: {}".format(poller.parameter_value(MI_TEMPERATURE)))

    filename = round(time.time())

    while True:
        try:
            row = {}
            time_now = datetime.now()
            t = poller.parameter_value(MI_TEMPERATURE)

            row['time'] = time_now
            row['t'] = t
            print(row)
            with open(f'{filename}.csv', 'a') as csv_file:
                writer = csv.DictWriter(csv_file, delimiter=";", fieldnames=['time', 't'], lineterminator='\n')
                writer.writerow(row)
            time.sleep(10)
        except:
            print('Sensor is not available')


def main():
    poll()


if __name__ == '__main__':
    main()
