from common import base, get_res
from data.readexcel import ExcelUtil



data = ExcelUtil("oggame").dict_data()
class GetKey(object):

    def get_key(self):
        '''获取key，用到后面获取游戏跳转的URL'''
        route = data[0]["route"]
        url = "".join(base.get_url(route))
        Method = "get"
        headers = {"x-token":eval(get_res.GetRes().get_res().text)['data']['token']}
        params = eval(data[0]["params"])
        kwargs = {"params": params,"headers":headers}
        res = base.get_response(url, Method, **kwargs)
        return res



