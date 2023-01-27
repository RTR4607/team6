import os # To communicate operating system
class SearchFile:
    def __init__(self):
        pass
    def find_file(self,filename,filepath):
        self.filename=filename
        self.filepath=filepath
        files=[]
        for root,dir,file in os.walk(filepath):
            if filename in file:
                files.append(os.path.join(root,filename))

        return files
# obj=SearchFile()
# print(obj.find_file('one.txt','C:/'))

