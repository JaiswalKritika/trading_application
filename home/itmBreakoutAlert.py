import pandas as pd
import numpy as np
import datetime
# from datetime import datetime
from typing import Optional, Tuple
import time
from apps.home.kite_init import kiteInit
import math


class breakoutLogic():

    def __init__(self) -> None:

        print('Object Created')

        self.establish_db()
        
        print("orb_range_candle_time:", self.orb_range_candle_time, "(", type(self.orb_range_candle_time) ,")")
        print("or_breakout_candle_time:", self.or_breakout_candle_time, "(", type(self.or_breakout_candle_time) ,")")
        print("orb_ma_h:", self.orb_ma_h, "(", type(self.orb_ma_h) ,")")
        print("orb_ma_l:", self.orb_ma_l, "(", type(self.orb_ma_l) ,")")
        print("orb_range_start_time:", self.orb_range_start_time, "(", type(self.orb_range_start_time) ,")")
        print("orb_retracement_time:", self.orb_retracement_time, "(", type(self.orb_retracement_time) ,")")
        print("itm_ma_h:", self.itm_ma_h, "(", type(self.itm_ma_h) ,")")
        print("itm_ma_l:", self.itm_ma_l, "(", type(self.itm_ma_l) ,")")
        print("itm_ma_oi:", self.itm_ma_oi, "(", type(self.itm_ma_oi) ,")")
        print("itm_reentry_after_mins:", self.itm_reentry_after_mins, "(", type(self.itm_reentry_after_mins) ,")")
        print("itm_entry_points_difference:", self.itm_entry_points_difference, "(", type(self.itm_entry_points_difference) ,")")
        print("itm_exit_points_difference:", self.itm_exit_points_difference, "(", type(self.itm_exit_points_difference) ,")")
        print("itm_sl_points_difference:", self.itm_sl_points_difference, "(", type(self.itm_sl_points_difference) ,")")
        print("itm_sl_cost_points_difference:", self.itm_sl_cost_points_difference, "(", type(self.itm_sl_cost_points_difference) ,")")
        print("itm_vwap_points_difference:", self.itm_vwap_points_difference, "(", type(self.itm_vwap_points_difference) ,")")
        print("itm_sold_option_premium_decay:", self.itm_sold_option_premium_decay, "(", type(self.itm_sold_option_premium_decay) ,")")
        print("itm_profit_percent:", self.itm_profit_percent, "(", type(self.itm_profit_percent) ,")")
        print("itm_profit_increment:", self.itm_profit_increment, "(", type(self.itm_profit_increment) ,")")
        print("itm_first_target_qty:", self.itm_first_target_qty, "(", type(self.itm_first_target_qty) ,")")
        print("itm_second_target_qty:", self.itm_second_target_qty, "(", type(self.itm_second_target_qty) ,")")
        print("itm_order_type:", self.itm_order_type, "(", type(self.itm_order_type) ,")")
        print("itm_last_entry_condition_check_time:", self.itm_last_entry_condition_check_time, "(", type(self.itm_last_entry_condition_check_time) ,")")
        print("itm_pyramid_start_time:", self.itm_pyramid_start_time, "(", type(self.itm_pyramid_start_time) ,")")
        print("itm_last_pyramid_condition_check_time:", self.itm_last_pyramid_condition_check_time, "(", type(self.itm_last_pyramid_condition_check_time) ,")")
        print("itm_second_tranche_time_diffence_mins:", self.itm_second_tranche_time_diffence_mins, "(", type(self.itm_second_tranche_time_diffence_mins) ,")")
        print("itm_order_qty:", self.itm_order_qty, "(", type(self.itm_order_qty) ,")")
        print("itm_order_multiplier:", self.itm_order_multiplier, "(", type(self.itm_order_multiplier) ,")")
        print("nifty_instrument_token:", self.nifty_instrument_token, "(", type(self.nifty_instrument_token) ,")")
        print("nifty_hl_difference_points:", self.nifty_hl_difference_points, "(", type(self.nifty_hl_difference_points) ,")")
        print("nifty_hl_difference_points:", self.nifty_hl_difference_points, "(", type(self.nifty_hl_difference_points) ,")")
        print("nifty_or_breakout_range_point_diff:", self.nifty_or_breakout_range_point_diff, "(", type(self.nifty_or_breakout_range_point_diff) ,")")
        print("bankNifty_instrument_token:", self.bankNifty_instrument_token, "(", type(self.bankNifty_instrument_token) ,")")
        print("bankNifty_hl_difference_points:", self.bankNifty_hl_difference_points, "(", type(self.bankNifty_hl_difference_points) ,")")
        print("bankNifty_or_range_point_difference:", self.bankNifty_or_range_point_difference, "(", type(self.bankNifty_or_range_point_difference) ,")")
        print("bankNifty_or_breakout_range_point_diff:", self.bankNifty_or_breakout_range_point_diff, "(", type(self.bankNifty_or_breakout_range_point_diff) ,")")
        print("finNifty_instrument_token:", self.finNifty_instrument_token, "(", type(self.finNifty_instrument_token) ,")")
        print("finNifty_hl_difference_points:", self.finNifty_hl_difference_points, "(", type(self.finNifty_hl_difference_points) ,")")
        print("finNifty_or_range_point_difference:", self.finNifty_or_range_point_difference, "(", type(self.finNifty_or_range_point_difference) ,")")
        print("finNifty_or_breakout_range_point_diff:", self.finNifty_or_breakout_range_point_diff, "(", type(self.finNifty_or_breakout_range_point_diff) ,")")
 
 
    def establish_db(self):

        self.kite = kiteInit()
        self.orb_range_candle_time = self.kite.generic_params["orb_range_candle_time"]
        self.or_breakout_candle_time = self.kite.generic_params["or_breakout_candle_time"]
        self.orb_ma_h = self.kite.generic_params["orb_ma_h"]
        self.orb_ma_l = self.kite.generic_params["orb_ma_l"]
        self.orb_range_start_time1 = str(self.kite.generic_params["orb_range_start_time"]+":00")#time
        self.orb_range_start_time = datetime.datetime.strptime(self.orb_range_start_time1, '%H:%M:%S').time()
        self.orb_retracement_time = self.kite.generic_params["orb_retracement_time"]
        self.itm_ma_h = self.kite.generic_params["itm_ma_h"]
        self.itm_ma_l = self.kite.generic_params["itm_ma_l"]
        self.itm_ma_oi = self.kite.generic_params["itm_ma_oi"]
        self.itm_reentry_after_mins = self.kite.generic_params["itm_reentry_after_mins"]
        self.itm_entry_points_difference = self.kite.generic_params["itm_entry_points_difference"]
        self.itm_exit_points_difference = self.kite.generic_params["itm_exit_points_difference"]
        self.itm_sl_points_difference = self.kite.generic_params["itm_sl_points_difference"]
        self.itm_sl_cost_points_difference = self.kite.generic_params["itm_sl_cost_points_difference"]
        self.itm_vwap_points_difference = self.kite.generic_params["itm_vwap_points_difference"]
        self.itm_sold_option_premium_decay = self.kite.generic_params["itm_sold_option_premium_decay"]
        self.itm_profit_percent = self.kite.generic_params["itm_profit_percent"]
        self.itm_profit_increment = self.kite.generic_params["itm_profit_increment"]
        self.itm_first_target_qty = self.kite.generic_params["itm_first_target_qty"]
        self.itm_second_target_qty = self.kite.generic_params["itm_second_target_qty"]
        self.itm_order_type = str(self.kite.generic_params["itm_order_type"])#buy/sell/both
        self.itm_last_entry_condition_check_time1 = str(self.kite.generic_params["itm_last_entry_condition_check_time"]+":00")#time
        self.itm_last_entry_condition_check_time = datetime.datetime.strptime(self.itm_last_entry_condition_check_time1, '%H:%M:%S').time()
        self.itm_pyramid_start_time = self.kite.generic_params["itm_pyramid_start_time"]
        self.itm_last_pyramid_condition_check_time1 = str(self.kite.generic_params["itm_last_pyramid_condition_check_time"]+":00")#time
        self.itm_last_pyramid_condition_check_time = datetime.datetime.strptime(self.itm_last_pyramid_condition_check_time1, '%H:%M:%S').time()
        self.itm_second_tranche_time_diffence_mins = self.kite.generic_params["itm_second_tranche_time_diffence_mins"]
        self.itm_order_qty = self.kite.generic_params["itm_order_qty"]
        self.itm_order_multiplier = self.kite.generic_params["itm_order_multiplier"]

        self.nifty_instrument_token = self.kite.nifty_params["nifty_instrument_token"]
        self.nifty_hl_difference_points = self.kite.nifty_params["nifty_hl_difference_points"]
        self.nifty_or_range_point_difference = self.kite.nifty_params["nifty_or_range_point_difference"]
        self.nifty_or_breakout_range_point_diff = (self.kite.nifty_params["nifty_or_breakout_range_point_diff"])

        self.bankNifty_instrument_token = self.kite.banknifty_params["bankNifty_instrument_token"]
        self.bankNifty_hl_difference_points = self.kite.banknifty_params["bankNifty_hl_difference_points"]
        self.bankNifty_or_range_point_difference = self.kite.banknifty_params["bankNifty_or_range_point_difference"]
        self.bankNifty_or_breakout_range_point_diff = self.kite.banknifty_params["bankNifty_or_breakout_range_point_diff"]

        self.finNifty_instrument_token = self.kite.finnifty_params["finNifty_instrument_token"]
        self.finNifty_hl_difference_points = self.kite.finnifty_params["finNifty_hl_difference_points"]
        self.finNifty_or_range_point_difference = self.kite.finnifty_params["finNifty_or_range_point_difference"]
        self.finNifty_or_breakout_range_point_diff = self.kite.finnifty_params["finNifty_or_breakout_range_point_diff"]

        self.applicable_script = self.kite.applicable_scripts
        self.instrument_token = self.kite.nifty_params[f"{self.applicable_script}_instrument_token"]
        self.hl_difference_points = self.kite.nifty_params[f"{self.applicable_script}_hl_difference_points"]
        self.or_range_point_difference = self.kite.nifty_params[f"{self.applicable_script}_or_range_point_difference"]
        self.or_breakout_range_point_diff = (self.kite.nifty_params[f"{self.applicable_script}_or_breakout_range_point_diff"])       
        

    def historicalData(self,request):
        pass


    def itmBreakoutAlert(self, request):

        moving_rows = max(self.itm_ma_h, self.itm_ma_l)

        past_days_required = math.ceil(self.or_breakout_candle_time*moving_rows/375)
        print(f'past_days_required: {past_days_required}')


        today = datetime.date.today()
        yesterday = today - datetime.timedelta(days=1)
        few_days_ago = today - datetime.timedelta(days=past_days_required+5)


        last_few_trading_day_df = pd.DataFrame(self.kite.historicalData(request, self.instrument_token, few_days_ago,
                                                                     yesterday,'minute'))
        
        last_few_trading_day_df =  resample_df(last_few_trading_day_df.copy(),
                                        x_minutes = self.or_breakout_candle_time)
        
        last_few_trading_day_df = last_few_trading_day_df.iloc[-moving_rows:]
        
        # print(len(last_few_trading_day_df))
        # print(last_few_trading_day_df)
        
        
        start_time = datetime.time(9, 15)
        end_time = datetime.time(19, 30)


        # Different States
        orb_range_checked = False

        while True:
            if current_time() >= start_time:
                break
        
        # get latest values from db
        self.establish_db()

        # Check for Activator only in Trading Hours
        if start_time <= current_time() <= end_time:

            # waiting time is the time to wait till starttime + candle time has passed to get atleast one candle.
            waiting_time = add_mins_to_time(self.orb_range_start_time, self.orb_range_candle_time)

            while True:
                if current_time() > waiting_time:
                    break

            if current_time() >= waiting_time and orb_range_checked is False:

                print('Reached inside Activator')

                orb_range_checked = True

                #####################################################################################
                # curr_day_df = pd.DataFrame(self.kite.historicalData(request, self.ttoken, few_days_ago, 
                #                                                      today,'minute'))


                curr_day_df = pd.DataFrame(self.kite.historicalData(request, self.instrument_token, today, 
                                                                     today,'minute'))
                                
                curr_day_after_start_time_df = curr_day_df[curr_day_df['date'].dt.time > self.orb_range_start_time]

                curr_day_after_start_time_df = resample_df(curr_day_after_start_time_df.copy(),
                                                            x_minutes = self.orb_range_candle_time)
                
                orb_first_candle = curr_day_after_start_time_df.head(1)
            
                top_range = orb_first_candle.loc[0, 'high']
                # print(type(top_range))
                
                bottom_range = orb_first_candle.loc[0, 'low']
                # print(type(bottom_range))
                
                hl_difference = top_range - bottom_range
                # print(type(hl))
                print('Checking Range Condition')
                
                if hl_difference < self.hl_difference_points:

                    print('Range Condition True')
                    
                    return True, 'Range'
            
                    # itm_buy_sell_strategy()
                        
                else:
                    while current_time() < end_time:
                        ###########################################################################################
                        # curr_day_df = pd.DataFrame(self.kite.historicalData(request, self.ttoken, few_days_ago, today,'minute' ))

                        curr_day_df = pd.DataFrame(self.kite.historicalData(request, self.instrument_token, today, today,'minute' ))

                        or_breakout_df = resample_df(curr_day_df.copy(), self.or_breakout_candle_time)

                        or_breakout_df = pd.concat([last_few_trading_day_df, or_breakout_df])

                        or_breakout_df['ma_h'] = or_breakout_df['high'].rolling(window=self.orb_ma_h).mean()
                        or_breakout_df['ma_l'] = or_breakout_df['low'].rolling(window=self.orb_ma_l).mean()
                        or_breakout_df['day'] = or_breakout_df['date'].dt.date

                        ############################################################################################
                        # or_breakout_df = or_breakout_df[or_breakout_df['date'] >= today]
                        or_breakout_df['date'] = pd.to_datetime(or_breakout_df['date']).dt.date

                        or_breakout_df = or_breakout_df[or_breakout_df['date'] >= today]

                        top_activator_flag = self.test_top_range(request, or_breakout_df.copy(), top_range)

                        if top_activator_flag:
                            return True, 'top_range_breakout'
                        
                        # bottom_activator_flag = self.test_bottom_range(request, or_breakout_df.copy(), bottom_range)

                        # if bottom_activator_flag:
                        #     return True, 'bottom_range_breakout'

        return False


    def test_top_range(self, request, df, top_range):

        today = datetime.date.today()
        
        row = df.iloc[-1]  

        i = df.index[-1]

        previous_close = df.iat[i-1, df.columns.get_loc('close')]

        c1 = (previous_close > row['open']) or (row['close'] > row['open'])
        c2 = (previous_close > row['ma_h']) and (previous_close > top_range)
        c3 = (row['close'] > row['ma_h']) and (row['close'] > top_range)
        c4 = row['ma_h'] > top_range
        
        print(c1, c2, c3, c4)

        ###########################
        if 1:
        
        # if c1 and c2 and c3 and c4:
        
            # print('Inside if')
            
            c5 = row['close'] - top_range < self.or_breakout_range_point_diff
            
            if c5*0:
                print('Pre Final Breakout True ')
                return True
            
            else:
                end_of_retracement = add_mins_to_time(current_time(), self.orb_retracement_time)

                print(f'End of Retracement: {end_of_retracement} | {current_time()}')

                while current_time() <= end_of_retracement:
                    
                    print(self.kite.get_ltp(request, [self.instrument_token])[str(self.instrument_token)]['last_price'])
                    # if (self.kite.get_ltp(request, [self.instrument_token])[str(self.instrument_token)]['last_price'] <= 
                    #     top_range + self.or_breakout_range_point_diff):
                    #     print('breakout_in_retracement')
                    #     return True
                time.sleep(20)

        else:
            time.sleep(60)
        
        return False
            

    def test_bottom_range(self, request, df, bottom_range):     
        today = datetime.date.today()
        
        row = df.iloc[-1]  

        i = df.index[-1]

        previous_close = df.iat[i-1, df.columns.get_loc('close')]

        c1 = (previous_close < row['open']) or (row['close'] < row['open'])
        c2 = (previous_close < row['ma_l']) and (previous_close < bottom_range)
        c3 = (row['close'] > row['ma_h']) and (row['close'] > bottom_range)
        c4 = row['ma_l'] < bottom_range
        
        print(c1, c2, c3, c4)

        ###########################
        # if 1
        
        if c1 and c2 and c3 and c4:
        
            # print('Inside if')
            
            c5 = bottom_range - row['close'] < self.or_breakout_range_point_diff
            
            if c5:
                print('Pre Final Breakout True ')
                return True
            
            else:
                end_of_retracement = add_mins_to_time(current_time(), self.orb_retracement_time)

                print(f'End of Retracement: {end_of_retracement} | {current_time()}')

                while current_time() <= end_of_retracement:
                    
                    # print(self.kite.get_ltp(request, [self.ttoken])[str(self.ttoken)]['last_price'])
                    if (self.kite.get_ltp(request, [self.instrument_token])[str(self.instrument_token)]['last_price'] <= 
                        bottom_range + self.or_breakout_range_point_diff):
                        print('breakout_in_retracement')
                        return True
                time.sleep(20)

        else:
            time.sleep(60)
        
        return False


def resample_df(df: pd.DataFrame, x_minutes : Optional[int] = 15) -> pd.DataFrame:
    
    # print('inside resampling')
    # print(df)
    df.set_index('date', inplace=True)
    x_minutes = str(x_minutes) + 'T'
    resampled_df = df.resample(x_minutes, origin = 'start').agg({
        'open': 'first',
        'high': 'max',
        'low': 'min',
        'close': 'last'
    })
    resampled_df.reset_index(inplace=True)

    return resampled_df


def add_mins_to_time(time: datetime.time, mins: int) -> datetime.time:

    mins = datetime.timedelta(minutes=mins)
    current_date = datetime.datetime.now().date()
    start_datetime = datetime.datetime.combine(current_date, time)
    result = start_datetime + mins

    return result.time()


def current_time() -> datetime.time:
    curr_time = datetime.datetime.now().time()
    return curr_time


def itm_buy_sell_strategy():
    pass
