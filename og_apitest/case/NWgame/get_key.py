from common import base
from case.NWgame import get_res
from data.readexcel import ExcelUtil



data = ExcelUtil("nwgame").dict_data()
class GetKey(object):

    def get_key(self):
        '''获取key，用到后面游戏跳转'''
        route = data[1]["route"]
        url = "".join(base.get_url(route))
        Method = "get"
        headers = {"x-token":eval(get_res.GetRes().get_res().text)['data']['token']}
        params = eval(data[1]["params"])
        kwargs = {"params": params,"headers":headers}
        res = base.get_response(url, Method, **kwargs)
        return res



