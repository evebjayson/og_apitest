import unittest
from common import base,logger
from case.NWgame import get_res


class GetBalance(unittest.TestCase):
    def setUp(self):
        self.log = logger.Log()
        self.res = get_res.GetRes().get_res().text  # 调用get_res模块，获取包含token的响应
        self.token = eval(self.res)["data"]["token"]  # 获取token
    def test_get_balance(self):
        '''测试查询会员余额'''
        url = 'http://api01.oriental-game.com:8085/game-providers/34/balance'
        Method = "get"
        headers = {
            "Content-Type": "application/json",
            "x-token": self.token
        }
        params = {"username":"marsqc01"}
        kwargs = {"params": params, "headers": headers}
        resp = base.get_response(url,Method,**kwargs)
        self.log.info("----------test is start----------")
        self.log.info("请求的接口地址为: %s" % url)
        self.log.info("请求的参数为: %s" % kwargs)
        self.log.info("响应内容为: %s" % resp.text)
        self.log.info("响应状态码为: %s" % resp.status_code)
        self.assertIn("success", resp.text, msg="失败原因为%s not in %s" % ("success", resp.text))
        self.log.info("----------test is pass----------")
        self.log.info("----------test is end----------")

if __name__ == "__main__":
    unittest.main()