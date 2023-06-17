from managers.main_manager import Manager
from tanks.tank import Tank


def main():
    tank1 = Tank(18)
    tank2 = Tank(11)
    tank3 = Tank(9)
    print(tank1)
    manager = Manager()
    manager.tanks.append(tank1)
    manager.pour_in_water(tank1, 19)
    manager.tanks.append(tank2)
    manager.tanks.append(tank3)
    manager.tanks.append(Tank(10))
    manager.tanks.append(Tank(9))

    print(manager.tanks)
    manager.pour_in_water(tank2, 1)
    # print(tank1.current)
    # manager.pour_in_water(tank1, 8)
    # print(tank1.current)
    # print(tank1.free_capacity)
    # manager.pour_out_water(tank1, 7)
    # print(tank1.current)
    manager.transfer_water(tank2, tank1, 1)
    print(manager.sourcer.operations)
    manager.pour_out_water(tank1, 10)
    print(manager.tanks)
    print(manager.tankfinder.max_water())
    water_levels = [tank.water_level for tank in manager.tanks]
    print(water_levels)
    print(manager.analyze_tank(tank1))


if __name__ == "__main__":
    main()
