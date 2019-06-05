import unittest
from common import logger, get_res
from data.readexcel import ExcelUtil



data = ExcelUtil("publicparameter").dict_data()
class Token(unittest.TestCase):
    def setUp(self):
        self.log = logger.Log()
    def test_token(self):
        '''测试获取token'''
        resp = get_res.GetRes().get_res()
        self.log.info("--------test is start--------")
        self.log.info("响应内容为: %s" % resp.text)
        self.log.info("响应状态码为: %s" %resp.status_code)
        self.assertIn(data[0]["expect"],resp.text,msg="失败原因:%s not in %s"%(data[0]["expect"],resp.text))
        self.log.info("---------test is pass---------")
        self.log.info("---------end---------")

if __name__=="__main__":
    unittest.main()

