"""
 * Project name(项目名称)：Python_logging模块
 * Package(包名): 
 * File(文件名): test2
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/29 
 * Time(创建时间)： 12:03
 * Version(版本): 1.0
 * Description(描述)：
 级别	对应的函数	描述
DEBUG	logging.debug()	最低级别，用于小细节，通常只有在诊断问题时，才会关心这些消息。
INFO 	logging.info()	用于记录程序中一般事件的信息，或确认一切工作正常。
WARNING 	logging.warning()	用于表示可能的问题，它不会阻止程序的工作，但将来可能会。
ERROR 	logging.error()	用于记录错误，它导致程序做某事失败。
CRITICAL	logging.critical()	最高级别，用于表示致命的错误，它导致或将要导致程序完全停止工作。
 """

# 对日志系统进行基本配置。
import logging

logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s -- %(levelname)s -->  %(message)s')

if __name__ == '__main__':
    logging.debug("hello")
    logging.info("hello")
    logging.warning("hello")
    logging.error("hello")
    logging.critical("hello")
    # 禁用所有严重级别为“级别”及以下的日志记录调用。
    logging.disable()
    logging.debug("hello")
    logging.info("hello")
    logging.warning("hello")
    logging.error("hello")
    logging.critical("hello")
    logging.disable(logging.INFO)
    logging.debug("hello")
    logging.info("hello")
    logging.warning("hello")
    logging.error("hello")
    logging.critical("hello")
