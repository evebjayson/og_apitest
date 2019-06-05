from common import base, get_res
from data.readexcel import ExcelUtil


data = ExcelUtil("nwgame").dict_data()

class GetGameID(object):

    def get_gameid(self):
        '''获取providers信息'''
        route = data[1]["route"]
        url = "".join(base.get_url(route))
        Method = data[1]["method"]
        headers = {"x-token": eval(get_res.GetRes().get_res().text)['data']['token']}
        kwargs = {"headers":headers}
        resp = base.get_response(url,Method,**kwargs)
        return resp


res = GetGameID().get_gameid()
print(res.json())

