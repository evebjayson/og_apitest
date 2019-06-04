from common import base
from case.NWgame import get_res
from data.readexcel import ExcelUtil


data = ExcelUtil("nwgame").dict_data()

class GetGameID(object):

    def get_gameid(self):
        '''获取gameid响应'''
        route = data[2]["route"]
        url = "".join(base.get_url(route))
        Method = data[2]["method"]
        headers = {"x-token": eval(get_res.GetRes().get_res().text)['data']['token']}
        kwargs = {"headers":headers}
        resp = base.get_response(url,Method,**kwargs)
        return resp


