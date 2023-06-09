from tank import Tank, TankFinder

from manager import Manager


def main():
    tank1 = Tank(10)
    manager = Manager()
    manager.tanks.append(tank1)
    print(manager.tanks)
    

if __name__=='__main__':
    main()