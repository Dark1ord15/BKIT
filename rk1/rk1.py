from operator import itemgetter
class HardDrive:
    def __init__(self, id, model, size, computer_id):
        self.id = id
        self.model = model
        self.size = size
        self.computer_id = computer_id
        
class Computer:
    def __init__(self, id, processor):
        self.id = id
        self.processor = processor
        
class HDComp:
    def __init__(self, computer_id, hard_drive_id):
        self.computer_id = computer_id
        self.hard_drive_id = hard_drive_id
        
computers = [
    Computer(1, 'Intel Core i3-6100'),
    Computer(2, 'Intel Core i3-7300'),
    Computer(3, 'Intel Core i5-7400'),
    Computer(4, 'Intel Core i3-7100'),
    Computer(5, 'AMD Ryzen 3 3100'),
    Computer(6, 'Intel Core i5-6500'),
]
hard_drives = [
    HardDrive(1, 'Western Digital Blue WD10EZEX', 1024, 1),
    HardDrive(2, 'Seagate Barracuda ST500LM030', 500, 2),
    HardDrive(3, 'Western Digital Purple WD40PURX', 4096, 3),
    HardDrive(4, 'Seagate SkyHawk ST2000VX008', 2048, 3),
    HardDrive(5, 'Western Digital Blue WD5000LCPX', 500, 6),
    HardDrive(6, 'Western Digital Blue WD5000LCPX', 500, 4),
    HardDrive(7, 'Seagate SkyHawk ST2000VX008', 2048, 5),
]
hds_comps = [
    HDComp(1, 1),
    HDComp(2, 2),
    HDComp(3, 3),
    HDComp(3, 4),
    HDComp(3, 5),
    HDComp(4, 1),
    HDComp(5, 2),
    HDComp(6, 3),
    HDComp(6, 4),
    HDComp(6, 5),
]
def task1():
    #поиск 'Core i5' в названии процессора компьютера
    results = {}
    for Computer in computers:
        if 'Core i5' in Computer.processor:
            HD_data = []
            for HardDrive in hard_drives:
                if HardDrive.computer_id == Computer.id:
                    cur_HD_data = [HardDrive.model, HardDrive.size]
                    HD_data.append(cur_HD_data)
            results[Computer.processor]=HD_data
    return results

def task2():
    #сортировка по размеру жесткого диска
    results={}
    for Computer in computers:
        counter=0
        for HardDrive in hard_drives:
            if HardDrive.computer_id == Computer.id:
                counter+=1
                if Computer.processor in results:
                    results[Computer.processor]+=HardDrive.size
                else:
                    results[Computer.processor]=HardDrive.size
        if(results[Computer.processor]!=0):
            results[Computer.processor]/=counter
            results[Computer.processor]=round(results[Computer.processor], 2)
    return sorted(results.items(), key=itemgetter(1), reverse=True)

def task3():
    #поиск жесткого диска, название которого начинается с буквы 'S'
    results={}
    for HardDrive in hard_drives:
        if str(HardDrive.model)[0]=='S':
            for HDComp in hds_comps:
                if HDComp.hard_drive_id == HardDrive.id:
                    for Computer in computers:
                        if Computer.id == HDComp.computer_id:
                            results[HardDrive.model]=Computer.processor
    return results

def main():
    print('\tTask 1')
    print(task1())
    
    print('\tTask 2')
    print(task2())

    print('\tTask 3')
    print(task3())
if __name__ == "__main__":
    main()

            





















