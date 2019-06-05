from common import base
from data.readexcel import ExcelUtil


data = ExcelUtil("publicparameter").dict_data()
class GetRes(object):

    def get_res(self):
        '''获取token响应'''
        route = data[0]["route"]
        url = "".join(base.get_url(route))
        Method = data[0]["method"]
        headers = eval(data[0]["header"])
        kwargs = {"headers": headers}
        res = base.get_response(url, Method, **kwargs)
        return res



