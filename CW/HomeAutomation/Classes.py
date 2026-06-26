from abc import ABC, abstractmethod
class Event:
    def __init__(self, event_type, value):
        self.event_type = event_type
        self.value = value
        
class Observer(ABC):
    @abstractmethod
    def update(self, message):
        pass
    
class Subject():
    def __init__(self):
        self._observers = []
        
    def attach(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)
    
    def detach(self, observer):
        if observer in self._observers:
            self._observers.remove(observer)
            
    def notify(self, event):
        for observer in self._observers:
            observer.update(event)
            
class Device:
    def __init__(self, name, UUID):
        self.name = name
        self.UUID = UUID
        
    def display(self):
        print(f"Device Name: {self.name}, UUID: {self.UUID}")
        
class Light(Device, Observer):
    def __init__(self, name, UUID, initial_brightness=50, state="off"):
        super().__init__(name, UUID)
        self.brightness = initial_brightness
        self.state = state
        
    def update(self, event):
        if event.value == True:
            self.turnOn()
        elif event.value == False:
            self.turnOff()
        elif type(event.value) == int:
            self.setBrightness(event.value)
    
    def setBrightness(self, brightness):
        self.brightness = brightness
        print(f"{self.name} brightness set to {self.brightness}%")
        
    def turnOn(self):
        if self.state != "on":
            self.state = "on"
            print(f"{self.name} turned on")
        else:
            print(f"{self.name} is already on")
            
    def turnOff(self):
        if self.state != "off":
            self.state = "off"
            print(f"{self.name} turned off")
        else:
            print(f"{self.name} is already off")
        
class Sensor(Device, Subject):
    def __init__(self, name, UUID):
        Device.__init__(self, name, UUID)
        Subject.__init__(self)
        
    def trigger(self, event_type, value):
        event = Event(event_type, value)
        print(f"[EVENT] - {self.name} triggered with event: {event.event_type}, value: {event.value}")
        self.notify(event)
        
class Heating(Device, Observer):
    def __init__(self, name, UUID, state="off"):
        super().__init__(name, UUID)
        self.state = state
        
    def update(self, event):
        if event.value == True:
            self.turnOn()
        elif event.value == False:
            self.turnOff()
    
    def turnOn(self):
        if self.state != "on":
            self.state = "on"
            print(f"{self.name} turned on")
        else:
            print(f"{self.name} is already on")
    
    def turnOff(self):
        if self.state != "off":
            self.state = "off"
            print(f"{self.name} turned off")
        else:
            print(f"{self.name} is already off")
            
class Lock(Device, Observer):
    def __init__(self, name, UUID, state="locked"):
        super().__init__(name, UUID)
        self.state = state
        
    def update(self, event):
        if event.value == True:
            self.lock()
        elif event.value == False:
            self.unlock()
    
    def lock(self):
        if self.state != "locked":
            self.state = "locked"
            print(f"{self.name} locked")
        else:
            print(f"{self.name} is already locked")
    
    def unlock(self):
        if self.state != "unlocked":
            self.state = "unlocked"
            print(f"{self.name} unlocked")
        else:
            print(f"{self.name} is already unlocked")

class HomeAutomation:
    def __init__(self):
        self.devices = []
        
    def add_device(self, device):
        self.devices.append(device)
    
    def remove_device(self, device):
        self.devices.remove(device)
        
    def display_devices(self):
        for device in self.devices:
            device.display()
            
    def link_device_sensor(self, device, sensor):
        if isinstance(device, Observer) and isinstance(sensor, Subject):
            sensor.attach(device)

    def demo(self):
        #creating objects
        motion_sensor = Sensor("Motion Sensor", "UUID-1234")
        dimmer = Sensor("Dimmer", "UUID-4321")
        thermostat = Sensor("Thermostat", "UUID-4321")
        keypad = Sensor("Keypad", "UUID-8765")
        door_lock = Lock("Front Door Lock", "UUID-3456")
        light = Light("Living Room Light", "UUID-5678")
        heating = Heating("Heating", "UUID-9012")

        #Adding devices
        self.add_device(keypad)
        self.add_device(door_lock)
        self.add_device(motion_sensor)
        self.add_device(thermostat)
        self.add_device(light)
        self.add_device(heating)
        
        #test light and motion sensor
        self.link_device_sensor(light, motion_sensor)
        self.link_device_sensor(light, dimmer)
        motion_sensor.trigger("motion_detected", True)
        motion_sensor.trigger("motion_detected", False)
        dimmer.trigger("brightness_changed", 75)
        dimmer.trigger("Dimmer turned on", True)
        dimmer.trigger("Dimmer turned off", False)

        #test heating and thermostat
        self.link_device_sensor(heating, thermostat)
        thermostat.trigger("Lower temperature threshold crossed", True)
        thermostat.trigger("Higher temperature threshold crossed", False)
        
        #test lock and keypad
        self.link_device_sensor(door_lock, keypad)
        keypad.trigger("unlock", False)
        keypad.trigger("lock", True)
        keypad.trigger("lock", True)
        