from tanks.tank import Tank, TankFinder

from managers.main_manager import Manager


def main():
    tank1 = Tank(10)
    manager = Manager()
    manager.tanks.append(tank1)
    print(manager.tanks)
    manager.pour_in_water(tank1, 11)
    print(tank1.current)
    manager.pour_in_water(tank1, 8)
    print(tank1.current)
    print(tank1.free_capacity)
    manager.pour_out_water(tank1, 7)
    print(tank1.current)
    print(manager.operations)


if __name__ == "__main__":
    main()
