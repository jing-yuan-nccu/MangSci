import pandas as pd
import numpy as np

class DataProcessor:
    def __init__(self):
        self.data = None
        self.processed_data = None
        
    def load_data(self, file_path):
        """載入資料"""
        self.data = pd.read_csv(file_path)
        return self
            
    def filter_columns(self, columns):
        if not isinstance(columns, (list, tuple)):
            raise ValueError("columns 必須是 list")
        # 篩好欄位，並重設 index，避免後面 groupby 出錯
        self.processed_data = self.data[columns].copy().reset_index(drop=True)
        return self
        
    def group_races(self):
        """將資料分組為賽事"""
        if self.processed_data is None:
            raise ValueError("請先載入並處理資料")
        return self.processed_data.groupby('race_id')
        
    def get_races(self):
        """取得賽事資料"""
        if self.processed_data is None:
            raise ValueError("請先載入並處理資料")
        return self.group_races()
        
    def get_data(self):
        """取得處理後的資料"""
        if self.processed_data is None:
            raise ValueError("請先載入並處理資料")
        return self.processed_data
        
    def add_place_result(self):
        """新增位置結果欄位"""
        if self.processed_data is None:
            raise ValueError("請先載入並處理資料")
            
        if 'result' not in self.processed_data.columns:
            raise ValueError("缺少 result 欄位")
            
        self.processed_data['place_result'] = self.processed_data['result'].apply(
            lambda x: 1 if x in [1, 2, 3] else 0
        )
        return self
        
    def _normalize_series(self, series):
        """標準化數列"""
        mean = series.mean()
        std = series.std()
        if std == 0:
            return series - mean  # 如果標準差為0，只做中心化
        return (series - mean) / std

    def add_horse_win_rate(self, n_races=10):
        # DEBUG：印一次狀態
        print("Before groupby:", type(self.processed_data),
              "Index:", self.processed_data.index, 
              "Columns:", self.processed_data.columns.tolist())

        # 確保 horse_id 還在欄位裡
        if 'horse_id' not in self.processed_data.columns:
            raise ValueError("horse_id 欄位不見了！")

        def calculate_win_rate(group):
            # 1. 先按 chronological order
            group = group.sort_values('date')
            # 2. 把 result 往下 shift，一定不要把當前比賽算進去
            wins = (group['result'] == 1).shift(1)
            places = group['result'].isin([1,2,3]).shift(1)
            # 3. rolling 並填 0 (最早的一筆 shift 會是 NaN)
            group['horse_win_rate_top1'] = wins.rolling(window=n_races, min_periods=1).mean().fillna(0)
            group['horse_win_rate_top3'] = places.rolling(window=n_races, min_periods=1).mean().fillna(0)
            return group

        # 重新做一次 index 重設，保證是純粹的欄位
        self.processed_data = self.processed_data.reset_index(drop=True)

        # 再 groupby
        self.processed_data = (
            self.processed_data
                .groupby('horse_id', group_keys=False)
                .apply(calculate_win_rate)
                .reset_index(drop=True)
        )

        # 標準化勝率欄位
        self.processed_data['horse_win_rate_top1'] = self._normalize_series(self.processed_data['horse_win_rate_top1'])
        self.processed_data['horse_win_rate_top3'] = self._normalize_series(self.processed_data['horse_win_rate_top3'])

        print("After groupby:", self.processed_data.shape)
        return self

    def add_jockey_win_rate(self, n_races=10):
        # DEBUG：印一次狀態
        print("Before groupby:", type(self.processed_data),
              "Index:", self.processed_data.index, 
              "Columns:", self.processed_data.columns.tolist())

        # 確保 jockey_id 還在欄位裡
        if 'jockey_id' not in self.processed_data.columns:
            raise ValueError("jockey_id 欄位不見了！")

        def calculate_win_rate(group):
            # 1. 先按 chronological order
            group = group.sort_values('date')
            # 2. 把 result 往下 shift，一定不要把當前比賽算進去
            wins = (group['result'] == 1).shift(1)
            places = group['result'].isin([1,2,3]).shift(1)
            # 3. rolling 並填 0 (最早的一筆 shift 會是 NaN)
            group['jockey_win_rate_top1'] = wins.rolling(window=n_races, min_periods=1).mean().fillna(0)
            group['jockey_win_rate_top3'] = places.rolling(window=n_races, min_periods=1).mean().fillna(0)
            return group

        # 重新做一次 index 重設，保證是純粹的欄位
        self.processed_data = self.processed_data.reset_index(drop=True)

        # 再 groupby
        self.processed_data = (
            self.processed_data
                .groupby('jockey_id', group_keys=False)
                .apply(calculate_win_rate)
                .reset_index(drop=True)
        )

        # 標準化勝率欄位
        self.processed_data['jockey_win_rate_top1'] = self._normalize_series(self.processed_data['jockey_win_rate_top1'])
        self.processed_data['jockey_win_rate_top3'] = self._normalize_series(self.processed_data['jockey_win_rate_top3'])

        print("After groupby:", self.processed_data.shape)
        return self