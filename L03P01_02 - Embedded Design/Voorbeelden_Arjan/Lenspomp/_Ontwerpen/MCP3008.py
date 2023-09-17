# I am using the MCP3008, which works perfectly for up to 8 analog inputs
# using the SPI pins (~2$).
# You could also use the MCP3004, I think, but it only has 4 analog inputs.
# I wrote a simple driver (mcp3008.py):

# The layout of the MCP3008 can be found on the internet (e. g. here).
# You will have to make the follwing connections (MCP3004/8 <-> ESP8266):

#    V_dd <-> 3.3V
#    V_ref <-> 3.3V
#    AGND <-> GND
#    CLK <-> SCK (14)
#    D_out <-> MISO (12)
#    D_in <-> MOSI (13)
#    CS <-> 15
#    DGND <-> GND

# Then you can read values from the different channels that can be addressed using integers 0 to 7.
# Example:
#    from mcp3008 import MCP3008
#    mcp = MCP3008()
#    print("Value on CH0:", mcp.read(0))    

# You can change the pins in the constructor if you like
# (e. g. CS pin can be any pin you like).
# If you need more than 8 extra ADC inputs, you can probably (not tested)
# simply connect multiple MCP3008 (on the same three SPI pins),
# but use a different CS pin for each MCP.

from machine import Pin

class MCP3008:
    def __init__(self, clk=14, mosi=13, miso=12, cs=15):
        self._clk = Pin(clk, Pin.OUT)
        self._mosi = Pin(mosi, Pin.OUT)
        self._miso = Pin(miso, Pin.IN)
        self._cs = Pin(cs, Pin.OUT)

    def read(self, channel):
        # """ Reads an analog value from the given channel (0-7) and returns it. """
        if channel not in range(0, 8):
            raise ValueError("channel must be 0-7")

        self._cs(1)  # negative edge
        self._cs(0)
        self._clk(0)

        send_cmd = channel
        send_cmd |= 0b00011000  # 0x18 (start bit + single/ended)

        # send bits (only 5 bits considered)
        for i in range(5):
            self._mosi(bool(send_cmd & 0x10))  # check bit on index 4
            self._clk(1)  # negative edge
            self._clk(0)
            send_cmd <<= 1

        # receive value from MCP
        v = 0
        for i in range(11):
            self._clk(1)  # negative edge
            self._clk(0)
            v <<= 1
            if self._miso():
                v |= 0x01

        return v