import unittest
from common import base,logger
from case.NWgame import get_res,get_key,get_gameurl
from data.readexcel import ExcelUtil


data = ExcelUtil("nwgame").dict_data()
class PlayGame(unittest.TestCase):
    def setUp(self):
        self.log = logger.Log()
        self.res = get_res.GetRes().get_res().text  # 调用get_res模块，获取包含token的响应
        self.token = eval(self.res)["data"]["token"]  # 获取token

    def test_play_game(self):
        '''获取游戏大厅url，进行跳转'''
        route = data[5]["route"]
        url = "".join(base.get_url(route))
        params = {"key":eval(get_key.GetKey().get_key().text)["data"]["key"]}
        headers = {"x-token":self.token}
        kwargs = {"params": params, "headers": headers}
        resp = get_gameurl.GameUrl().get_gameurl()
        self.log.info("----------test is start----------")
        self.log.info("请求的接口地址为: %s" % url)
        self.log.info("请求的参数为: %s" % kwargs)
        self.log.info("响应内容为: %s" % resp.text)
        self.log.info("响应状态码为: %s" % resp.status_code)
        self.assertIn(data[5]["expect"], resp.text, msg="失败原因为%s not in %s" % (data[5]["expect"], resp.text))
        self.log.info("----------test is pass----------")
        self.log.info("----------test is end----------")

if __name__ == "__main__":
    unittest.main()