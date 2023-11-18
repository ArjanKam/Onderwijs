class Pin:
    IN  			 	= 0
    OUT 			 	= 1
    OPEN_DRAIN	 	= 2
    ALT			 	= 3
    ALT_OPEN_DRAIN 	= 4
    ANALOG			= 5
    
    PULL_UP 		= 0
    PULL_DOWN 	= 1
    PULL_HOLD	= 2
    
    IRQ_FALLING 		= 0
    IRQ_RISING 		= 1
    IRQ_LOW_LEVEL 	= 2
    IRQ_HIGH_LEVEL 	= 3
    
    DRIVE_0 = 1
    DRIVE_1 = 2
    DRIVE_2 = 3

    _value = 1
    
    def __init__(self, id, mode=-1, pull=-1, *, value=None, drive=0, alt=-1):
        self.id = id
        self.mode = mode
        self._pull = pull
        self._value = value
        self._drive = drive
        self._alt = alt
        if value == None:
            if self._pull == self.PULL_UP:
                self._value = 1
            elif self._pull == self.PULL_DOWN:
                self._value = 0
    
    def irq(self, handler=None, trigger=IRQ_FALLING | IRQ_RISING, *, priority=1, wake=None, hard=False):
        None
    
    def value(self):
        return self._value
    
    def low(self):
        self._value = 0
    
    def high(self):
        self._value = 1
        
    def on(self):
        self._value = 1
    
    def off(seld):
        self._value = 0