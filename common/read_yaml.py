# encoding: utf-8
# @Time    : 2021/6/3 7:22 下午
# @Author  : Sail
# @File    : read_yaml.py
# @Software: PyCharm
import os
import yaml


class ReadYaml():

    def __init__(self):
        current_path = os.path.abspath(__file__)
        father_path = os.path.abspath(os.path.dirname(current_path) + os.path.sep + "..")
        datafile="data/saas_interface_data/yapi.yaml"
        file=os.path.join(father_path,datafile)
        self.file=file

    def getYaml(self):
        with open(self.file, "r", encoding="utf-8")as f:
            return yaml.load(f,Loader=yaml.FullLoader)



    def write_yaml(self,date):
        """
        提供一个公共方法，将python数据格式写入yaml文件
        直接在yaml文件写符合格式的数据太容易出错了
        :return:
        """
        with open(self.file, 'w') as outfile:
            yaml.dump(date, outfile, default_flow_style=False,allow_unicode=True
)


if __name__ == '__main__':

    date = {"list_date": [("http://qq/api/project/list?group_id=417&page=1&limit=10", "417", 1,10),
                          ("http://11.3imx.cn/api/project/list?group_id=417&page=1&limit=10", "417", 2,10)
                          ]}
    ReadYaml().write_yaml(date)