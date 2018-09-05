# coding: utf-8
#
# # MPL115A2 Temperature and Pressure sensor
#

import smbus
import time, datetime



CHANNEL = 1

class MPL115A2:
    _I2C_ADDRESS = 0x60
    COEF_DATA = 0x04
    COEF_REQ = 0x04
    CONV_REQ = 0x12
    HPA_DATA = 0x00
    _COMMAND_START_CONVERSION = 0x12
    _COEFFICIENT_START_ADDRESS = 0x04
    _COEFFICIENT_BLOCK_LENGTH = 8
    _SENSOR_DATA_BLOCK_LENGTH = 4


    def __init__(self, bus):
        self.bus = bus
        # Coefficients for compensation calculations - will be set on first
        # attempt to read pressure or temperature
        self.a0 = None
        self.b1 = None
        self.b2 = None
        self.c12 = None

    def __exit__(self, type, value, traceback):
        self.bus.close()

    def __enter__(self):
        return self

    def getTimeStamp(self):
        datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S').replace(":" , "").replace("-","").replace(" ","")

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

    def pressure(self, times=10):
        sum = 0
        for run in range(times):
            sum += self.read_pressure()
        return round(sum / times, 1)

    def read_pressure(self):
        """Starts sensor conversion, retrieves raw pressure and temperature data and
        calculates barometric pressure in kPa from sensor readings and coefficients.
        Retrieves coefficients if neccessary.
        Note that this call blocks for 5 ms to allow the sensor to return the data.
        """
        if self.a0 is None:
            self.read_coefficients()
        rp = self.read_raw_pressure()
        rt = self.read_raw_temperature()
        compensated = (((self.b1 + (self.c12 * rt)) * rp) + self.a0) + (self.b2 * rt)
        return round((compensated * (65.0 / 1023.0)) + 50.0, 1)

    def read_coefficients(self):
        """Coefficients reflect the individual sensor calibration. Differs from sensor to sensor.
        Only needs to be read once per session.
        """
        block = self.bus.read_i2c_block_data(self._I2C_ADDRESS,
                                             self._COEFFICIENT_START_ADDRESS,
                                             self._COEFFICIENT_BLOCK_LENGTH)
        self.a0 = float(self.parse_signed(block[0], block[1])) / 8.0
        self.b1 = float(self.parse_signed(block[2], block[3])) / 8192.0
        self.b2 = float(self.parse_signed(block[4], block[5])) / 16384.0
        self.c12 = float(self.parse_signed(block[6], block[7]) >> 2) / 4194304.0

    def parse_signed(self, msb, lsb):
        """Helper function for processing raw sensor readings.
        """
        combined = msb << 8 | lsb
        negative = combined & 0x8000
        if negative:
            combined ^= 0xffff
            combined *= -1
        return combined
    def read_raw_temperature(self):
        """Retrieves msb and lsb from the sensor and calculates the raw sensor temperature reading.
        """
        self.bus.write_byte_data(self._I2C_ADDRESS,
                                 self._COMMAND_START_CONVERSION,
                                 0x02)
        time.sleep(0.005)
        rt = self.bus.read_i2c_block_data(self._I2C_ADDRESS,
                                          0x02,
                                          2)
        return int((rt[0] << 8 | rt[1]) >> 6)

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

    def read_raw_pressure(self):
        """Retrieves msb and lsb from the sensor and calculates the raw sensor pressure reading.
        """
        self.bus.write_byte_data(self._I2C_ADDRESS, self._COMMAND_START_CONVERSION, 0x00)
        time.sleep(0.005)
        rp = self.bus.read_i2c_block_data(self._I2C_ADDRESS,self.HPA_DATA,2)
        return int((rp[0] << 8 | rp[1]) >> 6)

    def read_hpa(self,coef):
        self.bus.write_byte_data(self._I2C_ADDRESS, self.CONV_REQ, 0x01)

        time.sleep(0.003)

        self.bus.write_byte_data(self._I2C_ADDRESS, self.HPA_DATA, 0x00)
        adata = self.bus.read_i2c_block_data(self._I2C_ADDRESS, self.HPA_DATA, 4)

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
            print " hpa = " , ( mpl115a2.pressure() )
            print " temp = " , ( data['temp'] )

    except IOError, e:
        print e
        print 'Error creating connection to i2c.'

