"""
 * Project name(项目名称)：Python_logging模块
 * Package(包名): 
 * File(文件名): test1
 * Author(作者）: mao
 * Author QQ：1296193245
 * GitHub：https://github.com/maomao124/
 * Date(创建日期)： 2022/3/29 
 * Time(创建时间)： 11:57
 * Version(版本): 1.0
 * Description(描述)： basicConfig:

 def basicConfig(*,
                filename: str | PathLike[str] | None = ...,
                filemode: str = ...,
                format: str = ...,
                datefmt: str | None = ...,
                style: str = ...,
                level: int | str | None = ...,
                stream: SupportsWrite[str] | None = ...,
                handlers: Iterable[Handler] | None = ...) -> None

对日志系统进行基本配置。
如果根记录器已经配置了处理程序，则此函数不执行任何操作，除非关键字参数force设置为True 。这是一种方便的方法，旨在由简单的脚本使用来对日志包进行一次性配置。
默认行为是创建一个写入 sys.stderr 的 StreamHandler，使用 BASIC_FORMAT 格式字符串设置格式化程序，并将处理程序添加到根记录器。
可以指定许多可选的关键字参数，它们可以改变默认行为。
文件名 指定创建一个 FileHandler，使用指定的
文件名，而不是 StreamHandler。
filemode 指定打开文件的模式，如果指定了文件名
（如果未指定文件模式，则默认为“a”）。
format 为处理程序使用指定的格式字符串。 datefmt 使用指定的日期/时间格式。 style 如果指定了格式字符串，则使用它来指定
 格式字符串的类型（可能的值 '%'、'{'、'$'，用于 %-formatting、str.format 和string.Template - 默认为 '%'）。
level 将根记录器级别设置为指定级别。 stream 使用指定的流来初始化 StreamHandler。笔记
 该参数与“文件名”不兼容 - 如果两者都存在，则忽略“流”。
handlers 如果指定，这应该是已经创建的可迭代
处理程序，这将被添加到根处理程序。列表中未分配格式化程序的任何处理程序都将分配在此函数中创建的格式化程序。
force 如果将此关键字指定为 true，则任何现有的处理程序
在执行其他参数指定的配置之前，附加到根记录器的内容将被删除并关闭。
encoding 如果与文件名一起指定，则将此编码传递给
创建的 FileHandler，使其在文件打开时使用。
errors 如果与文件名一起指定，则此值将传递给
创建了 FileHandler，使其在以文本模式打开文件时使用。如果未指定，则默认值为backslashreplace 。
 """

import logging
# 对日志系统进行基本配置。
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s -- %(levelname)s -->  %(message)s')
logging.debug('Start of program')


def factorial(n):
    logging.debug('Start of factorial(%s%%)' % n)
    total = 1
    for i in range(n + 1):
        total *= i
        logging.debug('i is ' + str(i) + ', total is ' + str(total))
    logging.debug('End of factorial(%s%%)' % (n))
    return total


if __name__ == '__main__':
    print(factorial(5))
    logging.debug('End of program')
