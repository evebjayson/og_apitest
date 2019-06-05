from common import base, get_res
from case.OGgame import get_key
from data.readexcel import ExcelUtil


data = ExcelUtil("oggame").dict_data()
class GameUrl(object):
    def get_gameurl(self):
        '''获取游戏大厅url，进行跳转'''
        res = get_res.GetRes().get_res().text  # 调用get_res模块，获取包含token的响应
        token = eval(res)["data"]["token"]  # 获取token
        route = data[2]["route"]
        url = "".join(base.get_url(route))
        Method = data[2]["method"]
        params = {"key":eval(get_key.GetKey().get_key().text)["data"]["key"]}
        headers = {"x-token":token}
        kwargs = {"params": params, "headers": headers}
        resp = base.get_response(url,Method,**kwargs)

        return resp




