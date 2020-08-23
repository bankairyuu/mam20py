import logging

# create logger
logger = logging.getLogger('root')
logger.setLevel(logging.DEBUG)

# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# add formatter to ch
ch.setFormatter(formatter)

# add ch to logger
logger.addHandler(ch)

# # 'application' code
# self.logger.debug('debug message')
# self.logger.info('info message')
# self.logger.warning('warn message')
# self.logger.error('error message')
# self.logger.critical('critical message')
