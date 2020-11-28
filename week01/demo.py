import logging

logging.basicConfig(filename='test.log', level=logging.DEBUG,
                    datefmt='%Y-%m-%d %H:%M:%S',
                    format='%(asctime)s %(name)-8s %(levelname)-8s [line: %(lineno)d] %(message)s'
                    )

logging.debug('debug message')
logging.info('info message')
logging.warning('warning message')
logging.error('error message')
logging.critical('critical message')