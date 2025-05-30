import datetime
import psutil

def getTime():
    current_time = datetime.datetime.now()
    hr = int(current_time.hour)
    mnt = int(current_time.minute)
    
    if hr >= 12:
        bd_hr = abs(hr - 12)
    
    else:
        bd_hr = hr
        
    if hr >= 0 and hr < 12:
        tag = "AM"
    
    elif hr > 12 and hr <= 24:
        tag = "PM"
        
    telltime = f"Current time is {bd_hr} {mnt} {tag}"
    print(telltime)
    
    return telltime

class BatteryStatus:
    percentage = ""
    plug = ""
    
    def __init__(self):
        self.battery = psutil.sensors_battery()
        self.percentage = self.battery.percent
        self.plug = "Plugged in." if self.battery.power_plugged else "Not plugged in."
        
    def getBatteryStatus(self):
        if self.battery is None:
            print("No battery is found.")
            
        print(f"Battery is at {self.percentage}% power and {self.plug}")
        return f"Battery is at {self.percentage}% power and {self.plug}"
    
    
if __name__ == "__main__":
    getTime()
    BatteryStatus().getBatteryStatus()