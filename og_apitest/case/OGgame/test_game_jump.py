from case.OGgame import get_gameurl
from common import logger, base, get_res
from data.readexcel import ExcelUtil
import unittest


data = ExcelUtil("oggame").dict_data()
class GameJump(unittest.TestCase):
    def setUp(self):
        self.log = logger.Log()
        self.res = get_res.GetRes().get_res().text  # 调用get_res模块，获取包含token的响应
        self.token = eval(self.res)["data"]["token"]  # 获取token
        self.url = get_gameurl.GameUrl().get_gameurl().url


    def test_game_jump(self):
        '''测试游戏跳转,用响应状态码来判断是否跳转成功，返回200则表示成功，其他则跳转失败'''
        Method = data[3]["method"]
        resp = base.get_response(self.url,Method)
        self.log.info("----------test is start----------")
        self.log.info("跳转连接为：%s" % self.url)
        self.log.info("响应状态码为: %s" % resp.status_code)
        self.assertEqual(data[3]["expect"],resp.status_code,msg="失败原因为: %s != %s" %(data[3]["expect"],resp.status_code))
        self.log.info("----------test is pass----------")
        self.log.info("----------test is end----------")


if __name__ == "__main__":
    unittest.main()