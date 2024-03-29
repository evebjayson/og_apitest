import unittest
from common import base, logger, get_res
from data.readexcel import ExcelUtil



data = ExcelUtil("nwgame").dict_data()
class OutBalance(unittest.TestCase):
    def setUp(self):
        self.log = logger.Log()
        self.res = get_res.GetRes().get_res().text  # 调用get_res模块，获取包含token的响应
        self.token = eval(self.res)["data"]["token"]  # 获取token
    def test_out_balance(self):
        '''测试会员转账（out）'''
        route = data[7]["route"]
        url = "".join(base.get_url(route))
        Method = data[7]["method"]
        headers = {
            "x-token": self.token
        }
        json = eval(data[7]["data"])
        kwargs = {"json": json, "headers": headers}
        resp = base.get_response(url, Method, **kwargs)
        self.log.info("----------test is start----------")
        self.log.info("请求的接口为: %s" % url)
        self.log.info("请求的参数为: %s" % kwargs)
        self.log.info("响应内容为: %s" % resp.text)
        self.log.info("响应状态码为: %s" % resp.status_code)
        self.assertIn(data[7]["expect"], resp.text, msg="失败原因为%s not in %s" % (data[7]["expect"], resp.text))
        self.log.info("----------test is pass----------")
        self.log.info("----------test is end----------")

if __name__ == "__main__":
    unittest.main()