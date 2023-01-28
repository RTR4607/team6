import logging
logging.basicConfig(filename="log.txt",level=logging.WARNING)
print("log Demo")
logging.debug("Debugging Information")
logging.info("Info information")
logging.warning("Warning information")
logging.error("Error information")
logging.critical("Critical information")