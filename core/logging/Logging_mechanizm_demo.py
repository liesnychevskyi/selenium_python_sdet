import logging

logging.basicConfig(filename="C://Users//User//PycharmProjects//selenium_sdet//core//logg_files//test.log",
                    format='%(asctime)s: %(levelname)s: %(message)s',
                    datefmt='%m/%d/%Y/ %I:%M:%S %p', level=logging.DEBUG)

logging.debug("This is debug message")
logging.info("This is info message")
logging.warning("Thia is warning message")
logging.error("This is error message")
logging.critical("This is critical message")
