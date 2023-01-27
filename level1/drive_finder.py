import os
class SystemDriveFinder:
    def __init__(self):
        pass
    def find_drives(self):
        print("This is the find drives method of system Drive Finder class")
        drives=[]
        for i in range(65,91):
            if os.path.exists(chr(i)+":"):
                drives.append(chr(i))
        return drives
sdf=SystemDriveFinder()
print(sdf.find_drives())