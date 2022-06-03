"""
日志级别，输出add（），file_name输出文件名，format输出格式，级别，level只会输出级别高于设置级别的日志
格式化

"""
from loguru import logger
logger.add('a.log',format="{time:YYYY-MM-DD at HH:MM:SS} | {level} | {message}",level="DEBUG")
logger.info("这是一条普通日志")
logger.debug("只是一条调试日志")
logger.warning("这是一条警告日志")
logger.success("这是一条成功日志")
logger.error("这是一条错误日志")
logger.info("If you're using Python {},prefer {feature} of course!", 3.6, feature="f-strings")
logger.add('file_logger',format="{}")
