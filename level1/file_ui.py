from level1.search_file import SearchFile
import time
filename=input("ENter the file Name with extension:")
drive=input("Enter the Drive")
obj=SearchFile() # Creating an object for the SearchFile class
print(obj.find_file(filename,drive)) # Calling the find_file function through the object and printing
if __name__=='__main__':
    st=time.time()
    #obj=SearchFile()
    print(obj.find_file('one.txt','C:\\'))
    et=time.time()
    print(et-st)