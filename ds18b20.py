# подключаем модуль времени
import time
import csv
from datetime import datetime
# подключаем модуль для работы с датчиком DS18B20
from w1thermsensor import W1ThermSensor
# создаём объект для работы с сенсором
sensor = W1ThermSensor()
filename = round(time.time()) 
while (True):
    row = {}
    time_now = datetime.now()
    
    # считываем данные с датчика
    t = sensor.get_temperature()
    # выводим значения в консоль каждую секунду
    
    row["time"] = time_now
    row["t"] = t
    print(row)
    with open(f'{filename}.csv',"a") as csv_file:
        writer = csv.DictWriter(csv_file, delimiter=";", fieldnames = ['time', 't'], lineterminator = '\n')
        writer.writerow(row)
    time.sleep(10)