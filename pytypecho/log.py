from logging import getLogger, StreamHandler, Formatter

fmt = Formatter('%(levelname)s: [%(asctime)s: %(message)s')
sh = StreamHandler()
sh.setFormatter(fmt)
logger = getLogger()
logger.addHandler(sh)
