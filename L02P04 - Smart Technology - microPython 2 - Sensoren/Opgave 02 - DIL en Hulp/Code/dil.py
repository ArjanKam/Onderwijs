from machine import Pin
TXT_UNKNOWN = "UNKNOWN"
TXT_AND = "AND"
TXT_OR  = "OR"
TXT_XOR = "XOR"
TXT_NAND= "NAND"
TXT_NOR = "NOR"
TXT_NXOR= "NXOR"

RESULT_AND  = (0,0,0,1)
RESULT_OR   = (0,1,1,1)
RESULT_XOR  = (0,1,1,0)
RESULT_NAND = (1,1,1,0)
RESULT_NOR  = (1,0,0,0)
RESULT_NXOR = (1,0,0,1)
ERROR       = (0,0,0,0)
CHECK       = ((0,0),(0,1),(1,0),(1,1))

DilTypes = {RESULT_AND : "74HC00",
            RESULT_OR  : "74HC01",
            RESULT_XOR : "74HC02",
            RESULT_NAND: "74HC03",
            RESULT_NOR : "74HC04",
            RESULT_NXOR: "74HC05"
           }

class Dil():
    """
        name : name of the DIL
        vcc  : port number for vcc
        gnd  : port number for vcc
        port1 : tuple of (pinInA, pinInB, pinOUT) : pinIn in of type machine.Pin(..., Pin.IN)
        port2 : tuple of (pinInA, pinInB, pinOUT)
        port3 : tuple of (pinInA, pinInB, pinOUT)
        port4 : tuple of (pinInA, pinInB, pinOUT)
    """
    def __init__(self, port1=None, port2=None, port3=None, port4=None, vcc:int=14, gnd:int=7, debugResult=None ):
        self._vcc  = vcc
        self._gnd  = gnd
        self._port1 = port1
        self._port2 = port2
        self._port3 = port3
        self._port4 = port4
        self._debugResult = debugResult
        
        self._result = self.checkAllPorts()
        self._same = self._allSame(self._result)
        
        self._setDilName()        
            
    def _allPorts(self):
        ports = []
        if self._port1 != None:
            ports += self._port1
        if self._port2 != None:
            ports += self._port2
        if self._port3 != None:
            ports += self._port3
        if self._port4 != None:
            ports += self._port4
        return ports
    
    def print(self):
        print(f"Name : ", self.name)
        print("Ports same : ", self._same, ". Result = ", self._result)
        print(f"Vcc  : {self._vcc}")
        print(f"Gnd  : {self._gnd}")
        for x in self._allPorts():
            print(f"GP{x.id:2} -> {self._getModeName(x.mode)}")
        print("-------------------")
    
    def _getModeName(self, mode):
        if mode == Pin.IN:
            return "IN"
        else:
            return "OUT"
        
    def _getType(self, result:tuple) -> str:
        if result == RESULT_AND:
            return TXT_AND
        if result == RESULT_OR:
            return TXT_OR
        if result == RESULT_XOR:
            return TXT_XOR
        if result == RESULT_NAND:
            return TXT_NAND
        if result == RESULT_NOR:
            return TXT_NOR
        if result == RESULT_NXOR:
            return TXT_NXOR
        return TXT_UNKNOWN
    
    def _setDilName(self):
        if len(self._result) == 0 or self._same == False or self._result[0] not in DilTypes:
            self.name = TXT_UNKNOWN
        else:
            self.name = DilTypes[self._result[0]]
        
    def checkAllPorts(self):
        result = []
        for pinSet in (self._port1, self._port2, self._port3, self._port4):
            if pinSet != None:
                result.append(self.getWaarheidstabel(pinSet[0],pinSet[1],pinSet[2]))
        return result
    
    def getWaarheidstabel(self, pinA: Pin, pinB: Pin, pinOut : Pin):
        result = []
        for x, check in enumerate(CHECK):
            pinA.value = check[0]
            pinB.value = check[1]
            
            if self._debugResult != None:
                pinOut._value = self._debugResult[x]
            
            result.append( pinOut.value() )
        return tuple(result)

    def _allSame(self, lst: tuple):
        return all([x == lst[0] for x in lst])
     
 
