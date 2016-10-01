# coding: utf-8
#
# # MPL115A2 Temperature and Pressure sensor
#

import smbus
import time



CHANNEL = 1

class MPL115A2:
    _I2C_ADDRESS = 0x60
    COEF_DATA = 0x04
    COEF_REQ = 0x04
    CONV_REQ = 0x12
    HPA_DATA = 0x00

    def __init__(self, bus):
        self.bus = bus

    def conv_coef(self, msb, lsb, total, fractional, zero):
        data = (msb << 8) | lsb
        rate = float(1 << 16 - total + fractional + zero)

        if (msb >> 7) == 0:
            result = float(data / rate)
        else:
            result = -float(((data ^ 0xFFFF) + 1) / rate)

        return result

    def conv_adc(self, msb, lsb):
        data = ( (msb << 8) | lsb ) >> 6
        return data

    def read_coef(self):
        self.bus.write_byte_data(self._I2C_ADDRESS, self.COEF_REQ, 0x01)
        data = self.bus.read_i2c_block_data(self._I2C_ADDRESS, self.COEF_DATA, 12)

        a0  = self.conv_coef(data[0],  data[1],  16,  3, 0)
        b1  = self.conv_coef(data[2],  data[3],  16, 13, 0)
        b2  = self.conv_coef(data[4],  data[5],  16, 14, 0)
        c12 = self.conv_coef(data[6],  data[7],  14, 13, 9)
        c11 = self.conv_coef(data[8],  data[9],  11, 10, 11)
        c22 = self.conv_coef(data[10], data[11], 11, 10, 15)

        return {"a0": a0, "b1": b1, "b2": b2, "c12": c12, "c11": c11, "c22": c22}

    def read_hpa(self,coef):
        self.bus.write_byte_data(self._I2C_ADDRESS, self.CONV_REQ, 0x01)

        time.sleep(0.003)

        self.bus.write_byte_data(self._I2C_ADDRESS, self.HPA_DATA, 0x00)
        adata = bus.read_i2c_block_data(self._I2C_ADDRESS, self.HPA_DATA, 4)

        padc = self.conv_adc(adata[0], adata[1])
        tadc = self.conv_adc(adata[2], adata[3])

        pcomp = coef['a0'] + ( coef['b1'] + coef['c11'] * padc + coef['c12'] * tadc ) \
            * padc + ( coef['b2'] + coef['c22'] * tadc ) * tadc
        hpa = pcomp * 650 / 1023 + 500
        temp = 25 - (tadc - 472) / 5.35;

        return {"hpa": hpa, "temp": temp}

if __name__ == "__main__":
    try:
        bus = smbus.SMBus(CHANNEL)
        with MPL115A2(bus) as mpl115a2:
            coef = mpl115a2.read_coef()
            data = mpl115a2.read_hpa(coef)
            print " hpa = " , ( data['hpa'] )
            print " temp = " , ( data['temp'] )

    except IOError, e:
        print e
        print 'Error creating connection to i2c.'

