import logging

logging.basicConfig(filename="C://Users//User//PycharmProjects//selenium_sdet//core//logg_files//test.log",
                    format='%(asctime)s: %(levelname)s: %(message)s',
                    datefmt='%m/%d/%Y/ %I:%M:%S %p')

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

logger.debug("This is debug message")
logger.info("This is info message")
logger.warning("Thia is warning message")
logger.error("This is error message")
logger.critical("This is critical message")
