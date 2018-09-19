from getContent import *
from getData import *
from writeDate import *
if __name__ == '__main__':
     url = 'http://www.weather.com.cn/weather/101210101.shtml'
     html = getContent(url)  # 调用获取网页信息
     result = getData(html)  # 解析网页信息，拿到需要的数据
     writeData(result, 'E:/project/python/Reptilian/weather.csv')  # 数据写入到 csv文档中
     print('my frist python file')