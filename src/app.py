from tanks.tank import Tank
from tanks.tank_finder import TankFinder

from managers.main_manager import Manager


def main():
    tank1 = Tank(90)
    tank2 = Tank(11)
    tank3 = Tank(9)
    print(tank1)
    manager = Manager()
    manager.tanks.append(tank1)
    manager.tanks.append(tank2)
    manager.tanks.append(tank3)
    manager.pour_in_water(tank2, 4)
    manager.pour_in_water(tank1, 66)
    print(manager.tanks)
    #manager.pour_in_water(tank1, 11)
    #print(tank1.current)
    #manager.pour_in_water(tank1, 8)
    #print(tank1.current)
    #print(tank1.free_capacity)
    #manager.pour_out_water(tank1, 7)
    #print(tank1.current)
    manager.transfer_water(tank2, tank1, 1)
    
    #manager.pour_out_water(tank1, 2)
    print(manager.sourcer.operations)
    print(manager.tanks)
    print(manager.tankfinder.max_water())

if __name__ == "__main__":
    main()
