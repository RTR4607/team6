import logging
logging.basicConfig(filename="log.txt",level=logging.INFO)
logging.info("A new  Log came")
try:
    n1=int(input("Enter the vale"))
    n2=int(input("Enter the vale"))
    print(n1/n2)
except ZeroDivisionError as e:
    print("Can't Divided by zero")
    logging.exception(e)
logging.info("Log is recorded")