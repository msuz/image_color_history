from logging import getLogger, StreamHandler, DEBUG
logger = getLogger(__name__)
handler = StreamHandler()
handler.setLevel(DEBUG)
logger.setLevel(DEBUG)
logger.addHandler(handler)
logger.propagate = False

import os

from classes.ich import ImageColorHistory

def main():
    logger.debug('pixel.py')
    ich = ImageColorHistory()
    ich.load_image_data('./image/001/*.png')
    bgr_list = ich.get_pixcel_bgr_list(80, 80)
    print(bgr_list.T)

if __name__ == '__main__':
	main();