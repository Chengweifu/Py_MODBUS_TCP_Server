# MODBUS TCP Simulator V1.0 (20200415)
import sys
import modbus_tk
import modbus_tk.modbus_tcp as modbus_tcp
import modbus_tk.defines as mtk
import time
import random
# import modbus_tk.modbus
logger = modbus_tk.utils.create_logger('console')
# import string
print('MODBUS TCP Simulator V1.0 (20200415)')
print('Polls  /  4X  /  0X  ')

try:
    server = modbus_tcp.TcpServer(port=502, address='127.0.0.1', timeout_in_sec=3)
    master = modbus_tcp.TcpMaster('127.0.0.1',502)
    master.set_timeout(3.0)
    server.start()
    slaveID1 = server.add_slave(2)
    slaveID1.add_block('block1', mtk.HOLDING_REGISTERS, 0, 6)
    slaveID2 = server.add_slave(3)
    slaveID2.add_block('block2', mtk.COILS, 0, 6)
    logger.info('MODBUS TCP Server Start!')
    count=0
    while True:
        time.sleep(1)
        count +=1
        HV001 = random.randint(0,65535)
        HV002 = random.randint(0,65535)
        HV003 = random.randint(0,65535)
        slaveID1.set_values("block1", 0, HV001)
        slaveID1.set_values("block1", 1, HV002)
        slaveID1.set_values("block1", 2, HV003)
        CV001 = random.randint(0,1)
        CV002 = random.randint(0,1)
        CV003 = random.randint(0,1)
        slaveID2.set_values("block2", 0, CV001)
        slaveID2.set_values("block2", 1, CV002)
        slaveID2.set_values("block2", 2, CV003)
        H_value = master.execute(2, mtk.READ_HOLDING_REGISTERS, 0, 6)
        C_value = master.execute(3, mtk.READ_COILS, 0, 6)
        print('{} 4X={} , 0X={}'.format(count, H_value, C_value))

except:
    print('Value Error')
finally:
    print('====Stop===')
    server.stop()
