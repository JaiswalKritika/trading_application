import datetime
from apps.home.MyTOTP import Mypyotp
from apps.home.kite_trade import KiteApp, get_enctoken
from tinydb import TinyDB,Query
import pandas as pd



class kiteInit:
    def __init__(self):
        # Inputdb=TinyDB('Inputdb.json')
        # inputs = Inputdb.table("inputs")
        # q = Query()
        # self.data = inputs.search(q.id==1)
        # self.data = self.data[0]


        #=============================================
        StrategyDb = TinyDB("StrategyDb.json")
        strategies = StrategyDb.table("strategies")
        data = strategies.all()
        data1 = data[0]
        self.generic_params = data1["generic_params"]
        self.nifty_params = data1["nifty_params"]
        self.banknifty_params = data1["banknifty_params"]
        self.finnifty_params = data1["finnifty_params"]
        self.applicable_scripts = data1['applicable_scripts']

        # from_datetime=self.data.get("from_datetime")
        # x=from_datetime.replace("T"," ")+":00"
        # print(self.data)
        # db=TinyDB('db.json')
        # q = Query()
        # self.input_params = db.search(q.id==1)[0]
    def generic_params(self,key):
        return self.generic_params.get(key)
    
    def nifty_params(self,key):
        return self.nifty_params.get(key)
    
    def banknifty_params(self,key):
        return self.banknifty_params.get(key)
    
    def finnifty_params(self,key):
        return self.finnifty_params.get(key)
    
    def getdata(self,key):
        return self.data.get(key)
    
    def dataAuth(self, request):
        mtp=Mypyotp()
        otp=mtp.generate("ZR4FASMFK6VNZ5ZV3V3OSG4OXFL3376L")
        enctoken = get_enctoken(userid="RH6017",password='9454597201',twofa=otp)
        request.session["enctoken"]=enctoken

    def historicalData(self,request,ttoken,from_datetime,to_datetime,interval):
        enc=request.session["enctoken"]
        kite = KiteApp(enctoken=enc)
        historical_data = pd.DataFrame(kite.historical_data(ttoken, from_datetime, to_datetime, interval, continuous=False, oi=False))
        return historical_data
    
    def get_ltp(self,request,instruments):
        enc=request.session["enctoken"]
        kite = KiteApp(enctoken=enc)
        last_traded_price = kite.ltp(instruments)
        return last_traded_price


    def breakoutCandle(self,request,orb_range_start_time,or_breakout_candle_time):
        to_datetime= datetime.datetime.now()
        instrument_token= 256265
        enc=request.session["enctoken"]
        kite = KiteApp(enctoken=enc)
        breakout_data = kite.historical_data(instrument_token, orb_range_start_time, to_datetime, or_breakout_candle_time, continuous=False, oi=False)
        # print("breakout candle data start from here")
        # print(breakout_data)
        return breakout_data
    
    # def moving_average_high(self,request, high_window_size):
    #     from_datetime=self.data.get("from_datetime")
    #     x=from_datetime.replace("T"," ")+":00"
    #     ORB_candle_data = self.breakoutCandle(request=request,orb_range_start_time = x, ORB_candle_time = (self.data.get("ORB_candle_time")+"minute"))
    #     # print(historical_data)
    #     high_data = []
    #     for x in ORB_candle_data:
    #         data = x
    #         for i in data:
    #             high_data.append(data['high']) 
    #             # print(high_data)
    #     MA_H_result = []
    #     tem=high_data[:high_window_size]
    #     moving_sum = sum(tem)
    #     MA_H_result.append(moving_sum/high_window_size)
    #     for i in range(len(high_data)-high_window_size):
    #         moving_sum += (high_data[i + high_window_size] - high_data[i])
    #         MA_H_result.append(moving_sum / high_window_size)
    #     # print("MA-H start from here")
    #     # print(MA_H_result)
    #     return MA_H_result
    

    # def moving_average_low(self , request, low_window_size, ):
    #     ORB_candle_data = self.breakoutCandle(request=request,from_datetime = self.data.get("from_datetime"), ORB_candle_time = self.data.get("ORB_candle_time"))
    #     low_data = []
    #     for x in ORB_candle_data:
    #         data = x
    #         for i in data:
    #             low_data.append(data['low'])
    #     MA_L_result = []
    #     tem=low_data[:low_window_size]
    #     moving_sum = sum(tem)
    #     MA_L_result.append(moving_sum/low_window_size)
    #     for i in range(len(low_data)-low_window_size):
    #         moving_sum += (low_data[i + low_window_size] - low_data[i])
    #         MA_L_result.append(moving_sum / low_window_size)
    #     # print("MA-l Start friom here")
    #     # print(MA_L_result)
    #     return MA_L_result
    
    # def top_range_breakout(self,request):
    #     from_datetime=self.data.get("orb_range_start_time")
    #     x=from_datetime.replace("T"," ")+":00" 
    #     historical_data = self.historicalData(request=request,from_datetime=x, interval=(self.data.get("orb_range_candle_time")+"minute"))
    #     print(historical_data)
    #     opening_candle_data = historical_data[0]
    #     top_range = float(opening_candle_data['high']) 
    #     bottom_range = float(opening_candle_data['low'])
    #     first_candle_open = float(opening_candle_data['open'])
    #     first_candle_close = float(opening_candle_data['close'])
    #     candle_HL_difference = top_range - bottom_range
    #     movingAverageHigh = (self.moving_average_high(request,high_window_size=int(self.data.get("high_window_size"))))
    #     for i in range(1,int(len(historical_data))):
    #         print(i)
    #         second_candle_data = historical_data[i]
    #         # print(second_candle_data)
    #         second_candle_close = second_candle_data['close']
    #         print(second_candle_close)
    #         moving_Average_High = movingAverageHigh[i]
    #     if candle_HL_difference > float(self.data.get("candle_HL_difference_points")):
    #         if ((second_candle_close > first_candle_open or first_candle_close > first_candle_open)
    #             and(second_candle_close>moving_Average_High and second_candle_close>top_range)
    #             and(first_candle_close>moving_Average_High and first_candle_close>top_range)
    #             and(moving_Average_High>top_range)
    #             and(first_candle_close-top_range<self.data.get("candle_HL_difference_points"))
    #             ):
    #             print("breakout happens")
    #         else:
    #             print("retracement time")
    #             # self.top_range_breakout(request)
    #             # i=0
    #             # retracement_time=int(self.data.get("retracement"))*1000
    #             # while True:
    #             #     i=i+1
    #             #     if i >= len(historical_data):
    #             #         break
    #             #     self.top_range_breakout(request)    
    #             #     time.sleep(retracement_time)
    #     else:
    #         print("ITM buy sell strategy")

    # def bottom_range_breakout(self,request):
    #     from_datetime=self.data.get("from_datetime")
    #     x=from_datetime.replace("T"," ")+":00" 
    #     historical_data = self.historicalData(request=request,from_datetime=x, interval=(self.data.get("interval")+"minute"))
    #     opening_candle_data = historical_data[0]
    #     top_range = float(opening_candle_data['high']) 
    #     bottom_range = float(opening_candle_data['low'])
    #     first_candle_open = float(opening_candle_data['open'])
    #     first_candle_close = float(opening_candle_data['close'])
    #     candle_HL_difference = top_range - bottom_range
    #     movingAverageHigh = (self.moving_average_high(request,high_window_size=int(self.data.get("high_window_size"))))
    #     for i in range(1,len(historical_data)):
    #         second_candle_data = historical_data[i]
    #         print(second_candle_data)
    #         second_candle_close = second_candle_data['close']
    #         moving_Average_High = movingAverageHigh[i]
    #     if candle_HL_difference > float(self.data.get("candle_HL_difference_points")):
    #         if ((second_candle_close < first_candle_open or first_candle_close < first_candle_open)
    #             and(second_candle_close < moving_Average_High and second_candle_close>bottom_range)
    #             and(first_candle_close>moving_Average_High and first_candle_close>bottom_range)
    #             and(moving_Average_High<bottom_range)
    #             and((bottom_range - first_candle_close)<self.data.get("candle_HL_difference_points"))
    #             ):
    #             print("breakout happens")
    #         else:
    #             print(" ")
    #             i=0
    #             retracement_time=int(self.data.get("retracement"))*10000000
    #             while True:
    #                 i=i+1
    #                 if i >= len(historical_data):
    #                     break
    #                 self.bottom_range_breakout(request)    
    #                 time.sleep(retracement_time)
           
    