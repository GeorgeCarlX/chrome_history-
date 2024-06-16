# chrome_history-
川大网安法的学子啊，证据法与数字取证的期末设计，前辈决定帮帮，等待有缘人哦
Chrome 历史记录提取工具
这个工具允许你从 Chrome 浏览器的历史记录中提取并保存信息到 Excel 表格中。
你可以根据日期范围、关键词和目的 IP 地址来筛选历史记录，并可选择是否使用第三方 API 获取 IP 地址的地理位置信息。

安装依赖
确保安装了 Python 3 和以下依赖：

pip install xlsxwriter

使用方法
命令行参数说明
运行 main.py 文件时，可以使用以下命令行参数来执行不同的操作：

-h, --help: 帮助信息
-c, --create: 创建 Excel 表格并保存 Chrome 历史记录到 chrome_history.xlsx。
-s, --screen: 筛选 Chrome 历史记录，并将结果保存到 filtered_chrome_history.xlsx。
以下是-s的参数
-d, --date YYYY/MM/DD-YYYY/MM/DD: 指定日期范围筛选历史记录。
-k, --keyword KEYWORD: 指定关键词用于筛选 URL。
--dip IP_ADDRESS: 指定目的 IP 地址用于筛选历史记录。
--country COUNTRY: 指定国家用于筛选 IP 地理位置。
--city CITY: 指定城市用于筛选 IP 地理位置。

示例
1.创建包含所有历史记录的 Excel 文件：  

python main.py -c  

这将从 Chrome 历史记录中提取所有记录，并保存到 chrome_history.xlsx 文件中。

2.筛选特定日期范围的历史记录：

python main.py -s -d 2024/01/01-2024/06/30

这将筛选出从 2024 年 1 月 1 日到 2024 年 6 月 30 日的历史记录，并保存到 filtered_chrome_history.xlsx 文件中。

3.根据关键词筛选历史记录：

python main.py -s -k example

这将筛选包含关键词 "example" 的 URL 的历史记录，并保存到 filtered_chrome_history.xlsx 文件中。

4.根据目的 IP 地址筛选历史记录：

python main.py -s --dip 192.168.1.1

这将筛选出所有目标 IP 地址为 192.168.1.1 的历史记录，并保存到 filtered_chrome_history.xlsx 文件中。

5.根据国家和城市筛选历史记录：

python main.py -s --country China --city Beijing

这将筛选出目的 IP 地址所在国家为 "China"，城市为 "Beijing" 的历史记录，并保存到 filtered_chrome_history.xlsx 文件中。

注意事项
(1)如果 Chrome 历史记录文件的路径与默认路径不同，需要修改 main.py 中的 original_history_path 变量。
(2)确保在运行前已经关闭 Chrome 浏览器，以免历史记录文件被锁定而无法复制和读取。
(3)由于会查询目的ip的城市（http://ip-api.com/），可能会运行较慢，在数据量大时比较明显
(4)保存的 Excel 文件将位于与 main.py 文件相同的目录中。在脚本运行后，会在当前工作目录中生成以下文件：
chrome_history.xlsx：包含所有 Chrome 历史记录。
filtered_chrome_history.xlsx：包含筛选后的 Chrome 历史记录。

错误处理
如果遇到问题，请检查控制台输出和 error.log 文件中的日志记录，以获取更多错误信息和帮助。

结束语
这个工具可以帮助你方便地从 Chrome 浏览器的历史记录中提取信息，并以 Excel 表格的形式保存，希望对你有帮助！
请根据你的实际情况和文件结构进行调整和测试，确保所有的路径和参数能够正确地运行。
这个 README 文档可以帮助用户了解如何使用你的工具，同时也提供了一些示例命令供参考。
