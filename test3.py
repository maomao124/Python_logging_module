"""
 * Project name(项目名称)：Python_logging模块
 * Package(包名): 
 * File(文件名): test3
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/29 
 * Time(创建时间)： 12:12
 * Version(版本): 1.0
 * Description(描述)： 
 """

# 对日志系统进行基本配置。
import logging

logging.basicConfig(filename="error.log", encoding="UTF-8", level=logging.DEBUG,
                    format=' %(asctime)s -- %(levelname)s -->  %(message)s')

if __name__ == '__main__':
    logging.debug("hello")
    logging.info("hello")
    logging.warning("hello", )
    logging.error("hello")
    logging.critical("hello")
    for i in range(1, 11):
        logging.info("第" + str(i) + "次")
