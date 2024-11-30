from us_visa.logger import logging
from  us_visa.exception import USVisaException
logging.info("check this")

try: 
    1/0

except USVisaException as e:
    logging.error(e)