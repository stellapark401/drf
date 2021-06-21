import json
import pandas as pd
import googlemaps
from rest_framework.cctv_prediction.common.abstract import PrinterBase, ReaderBase


class CommonServices(PrinterBase, ReaderBase):

    def dframe(self, df):
        print('*' * 50)
        print(f'Data type: {type(df)}이다.')
        print(f'Data column\n|->{df.columns}이다.')
        print(f"Data 상위 5개\n {df.head()}")
        print(f'Data null 갯수\n{df.isnull().sum()}개')
        print('*' * 50)

    def csv(self) -> object:
        return pd.read_csv(self.new_file(), encoding='UTF-8', thousands=',')

    def xls(self) -> object:
        return pd.read_excel(self.new_file(), header=2, usecols='B, D, G, J, N')

    def json(self) -> object:
        return json.load(open(self.new_file(), encoding='UTF-8'))

    def gmaps(self):
        return googlemaps.Client(key='AIzaSyBvIDK8Cn0nhO3N7TuSE4TlvWiNOViPqOs')

    def setting_context(self, payload1, payload2):
        self.context = payload1
        self.f_name = payload2

    def new_file(self) -> str:
        return self.context + self.f_name
