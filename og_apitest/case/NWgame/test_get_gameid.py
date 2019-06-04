from case.NWgame import get_gameid
from data.readexcel import ExcelUtil
from common import logger
import unittest


data = ExcelUtil("nwgame").dict_data()
class GameID(unittest.TestCase):

    def setUp(self):
        self.log = logger.Log()
    def test_get_gameid(self):
        '''测试获取gameid是否正确'''
        resp = get_gameid.GetGameID().get_gameid()
        self.log.info("----------test is start----------")
        self.log.info("请求接口为: %s" %resp.url)
        self.log.info("响应状态码为: %s" %resp.status_code)
        self.assertIn(data[2]["expect"],resp.text,msg="失败原因为: %s is not in %s" %(data[2]["expect"],resp.text))
        self.log.info("----------test is pass----------")
        self.log.info("----------test is end----------")


if __name__ == "__main__":
    unittest.main()
