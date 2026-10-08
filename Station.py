from abc import ABC, abstractmethod
from typing import List, Dict
from datetime import datetime

class Observer(ABC):
    @abstractmethod
    def update(self, station):
        pass

class Station:
    def __init__(self):
        self.observers: List[Observer] = []
    
    def attach(self, observer: Observer):
        if observer not in self.observers:
            self.observers.append(observer)
    
    def detach(self, observer: Observer):
        if observer in self.observers:
            self.observers.remove(observer)
    
    def notify(self):
        for observer in self.observers:
            observer.update(self)
        

class Center(Station):
    def __init__(self, x: float = 0, y: float = 0):
        super().__init__()
        self._x = x
        self._y = y
    
    @property
    def x(self):
        return self._x
    
    @property
    def y(self):
        return self._y
    
    @x.setter
    def x(self, val: float):
        if self._x != val:
            self._x = val
            self.notify()
    
    @y.setter
    def y(self, val:float):
        if self._y != val:
            self._y = val
            self.notify()
    
class Follower(Observer):
    def __init__(self, station: Station):
        self.notification = 0
        self._station = station
        self._data: Dict[int, tuple] = {}
        station.attach(self)
        self.update(station)
    
    def update(self, command: Station):
        if command is self._station:
            self._data[self.notification] = (command.x, command.y)
            self.notification += 1
    
    def get_data(self):
        return dict(self._data)
            
if __name__ == "__main__":
    command = Center()
    observer = Follower(command)
    
    for i in range (2):
        for j in range (3):
            command.x = i
            command.y = j + i
    print (observer.get_data())