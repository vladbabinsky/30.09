from abc import ABC, abstractmethod
from abc import abstractmethod

class Robot(ABC):
    def __init__(self, name, model, power_level):
        self.name = name
        self.model = model
        self.power_level = power_level
    
    def show_info(self):
        return f"{self.name} (Model: {self.model}, Power Level: {self.power_level})"
    
    @abstractmethod
    def perform_task(self):
        pass
    
    def charge(self, amount):
        self.power_level += amount
        if self.power_level > 100:
            self.power_level = 100

class WorkerRobot(Robot):
    def __init__(self, name, model, power_level, tool):
        super().__init__(name, model, power_level)
        self.tool = tool
    
    def perform_task(self):
        if self.power_level >= 10:
            self.power_level -= 10
            return f"{self.name} is using {self.tool}."
        return f"{self.name} has low power."

class DefenseRobot(Robot):
    def __init__(self, name, model, power_level, weapon):
        super().__init__(name, model, power_level)
        self.weapon = weapon
    
    def perform_task(self):
        if self.power_level >= 15:
            self.power_level -= 15
            return f"{self.name} is activating {self.weapon}."
        return f"{self.name} has low power"

class ServiceRobot(Robot):
    def __init__(self, name, model, power_level, service_type):
        super().__init__(name, model, power_level)
        self.service_type = service_type
    
    def perform_task(self):
        if self.power_level >= 5:
            self.power_level -= 5
            return f"{self.name} is providing {self.service_type}."
        return f"{self.name} has low power."

worker_bot = WorkerRobot("Bob", "X1", 80, "Wrench")
defense_bot = DefenseRobot("Defender", "Z3", 90, "Laser")
service_bot = ServiceRobot("Helper", "$2", 60, "Cleaning")

robots = [worker_bot, defense_bot, service_bot]

for robot in robots:
    print(robot.show_info(), robot.perform_task())
    robot.charge(20)
    print(robot.show_info(), "\n")

