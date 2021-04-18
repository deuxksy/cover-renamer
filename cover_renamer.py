import datetime
import logging
import os

NEW_FILE_NAME = '00000'


def search(point):
    for (path, dir, files) in os.walk(point):
        if files :
            first_filename = files[0].split('.')[0]
            if NEW_FILE_NAME != first_filename:
                ext = files[-1].split('.')[-1].lower()
                if ext in ['png', 'jpg', 'jpeg']:
                    old = files[-1]
                    new = '{}.{}'.format(NEW_FILE_NAME, ext)
                    logging.debug('{},{},{}'.format(path, old, new))
                    os.replace(os.path.join(path, old), os.path.join(path, new))


if __name__ == '__main__':
    ROOT_FOLDER = 'Z:\Download'
    POINT = 'Z:\Download'

    logging.basicConfig(filename=os.path.join(ROOT_FOLDER, 'log.txt'), encoding='utf8', level=logging.DEBUG)
    logging.debug('--------------------------------------------------------------------------------')
    logging.debug('START:\t{}'.format(datetime.datetime.now()))
    search(POINT)
    logging.debug('END:\t\t{}'.format(datetime.datetime.now()))
