import unittest
import traceback
from common import readExcelData
from common import configHTTP
from common import readDBData
from common import log
import ddt


@ddt.ddt
class TestLogin(unittest.TestCase):
    i_excel = readExcelData.ConfigExcel()
    i_http = configHTTP.ConfigHTTP()
    # self.i_db = configDB.Operate_DB()
    excel_result = i_excel.get_data_from_excel()
    print(excel_result)

    # url = excel_result[0]['url']
    # method = excel_result[0]['method']
    # data = excel_result[0]['data']
    # sql = excel_result[0]['sql']
    # headers = excel_result[0]['headers']
    @classmethod
    def setUpClass(cls):
        print('开始执行')

    # def setParams(self):
    #     self.i_excel = configExcel.ConfigExcel()
    #     # self.i_http = configHTTP.ConfigHTTP()
    #     # self.i_db = configDB.Operate_DB()
    #     self.excel_result = self.i_excel.get_data_from_excel()
    #     print(self.excel_result)
    #     self.url = self.excel_result[0]['url']
    #     self.method = self.excel_result[0]['method']
    #     self.data = self.excel_result[0]['data']
    #     self.sql = self.excel_result[0]['sql']
    #     self.headers = self.excel_result[0]['headers']

    @ddt.data(*excel_result)
    def testLogin(self, data):
        print(type(self.excel_result))
        print(data)
        self.url = data['url']
        self.method = data['method']
        self.data = data['data']
        self.sql = data['sql']
        self.headers = data['headers']
        http_result = self.i_http.http_connect(url=self.url, method=self.method, data=self.data,
                                               headers=self.headers)  # 获取接口返回数据
        self.assertEqual(http_result['code'], data['except_code'])

    @classmethod
    def tearDownClass(cls):
        print('执行结束')


if __name__ == '__main__':
    unittest.main()



