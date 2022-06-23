import logging
import time
logging.basicConfig(filename='log.txt',
                    filemode='a',
                    format='%(asctime)s, %(levelname)s | %(msg)s',
                    datefmt='%H:%M:%S',
                    level=logging.DEBUG)
count = 0

while True:
    logging.info(f"Logging into the File {count}")
    time.sleep(2)
    count += 1
