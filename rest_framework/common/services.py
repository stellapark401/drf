import json
import pandas as pd
import googlemaps
from rest_framework.common.abstract import PrinterBase, ReaderBase, ScrapperBase
from selenium import webdriver


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
        return pd.read_excel(self.new_file(), header=2, usecols=None)

    def json(self) -> object:
        return json.load(open(self.new_file(), encoding='UTF-8'))

    def gmaps(self):
        return googlemaps.Client(key='AIzaSyBvIDK8Cn0nhO3N7TuSE4TlvWiNOViPqOs')

    def setting_context(self, payload1, payload2):
        self.context = payload1
        self.f_name = payload2

    def new_file(self) -> str:
        return self.context + self.f_name


class Scrapper(ScrapperBase):

    def __init__(self):
        self.url = ''

    def chrome_driver(self) -> object:

        options = webdriver.ChromeOptions()
        # options.add_argument('headless')
        # options.add_experimental_option('useAutomationExtension', False)
        options.add_argument('window-size=1920x1080')
        options.add_argument('--disable-gpu')
        options.add_argument('lang=ko_KR')

        # options.add_argument('Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) HeadlessChrome/60.0.3112.50 Safari/537.36')

        options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) "
                             "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")

        return webdriver.Chrome('../common/chromedriver', chrome_options=options)
