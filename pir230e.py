from pymodbus.client.sync import ModbusTcpClient as ModbusClient    # библиотека для работы по протоколу Modbus
from datetime import datetime
import time
import csv

a = 'Сумма цифр числа Фибоначчи №164'
b = 'Сумма цифр числа Фибоначчи №100'
c = 'Сумма цифр числа Фибоначчи №137'
d = 'Сумма цифр числа Фибоначчи №89'

x = 'Число високосных лет от 2020 и 10000 включительно'


client = ModbusClient('159.93.112.94', port=1936)                           # создание объекта client класса ModbusClient
status = client.connect()                                           # вызов функции подключения к устройству
# t = client.read_input_registers(0, 1, unit=1)                      # вызов функции чтения пяти регистров (начиная с 0) с устройства
# print(t.registers)                                                 # вывод считанных регистров в консоль

filename = round(time.time())

while True:
    row = {}
    time_now = datetime.now()
    t = client.read_input_registers(0, 1, unit=1).registers

    row['time'] = time_now
    row['t'] = t[0]/100
    print(row)
    with open(f'{filename}.csv', 'a') as csv_file:
        writer = csv.DictWriter(csv_file, delimiter=";", fieldnames=['time', 't'], lineterminator='\n')
        writer.writerow(row)

    time.sleep(10)


