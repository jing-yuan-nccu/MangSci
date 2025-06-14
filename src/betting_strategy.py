from abc import ABC, abstractmethod
import pandas as pd
import numpy as np

class BettingType:
    WIN = "win"
    PLACE = "place"

class BettingStrategy(ABC):
    def __init__(self, betting_type=BettingType.WIN):
        self.betting_type = betting_type
    
    @abstractmethod
    def select_horse(self, race_group):
        """選擇要投注的馬匹"""
        pass
        
    def get_result(self, selected):
        """根據賭博類型取得結果"""
        # 確保 selected 是 Series
        if isinstance(selected, pd.DataFrame):
            selected = selected.iloc[0]
            
        if self.betting_type == BettingType.WIN:
            return selected["result"] == 1
        else:  # PLACE
            return selected["place_result"] == 1

class RandomStrategy(BettingStrategy):
    def select_horse(self, race_group):
        """隨機選擇一匹馬"""
        return race_group.sample(n=1)

class OddsBasedStrategy(BettingStrategy):
    def __init__(self, min_odds=1.0, max_odds=float('inf'), betting_type=BettingType.WIN):
        super().__init__(betting_type)
        self.min_odds = min_odds
        self.max_odds = max_odds
        
    def select_horse(self, race_group):
        """根據賠率範圍選擇馬匹"""
        odds_column = "win_dividend1" if self.betting_type == BettingType.WIN else "place_odds"
        filtered = race_group[
            (race_group[odds_column] >= self.min_odds) & 
            (race_group[odds_column] <= self.max_odds)
        ]
        if len(filtered) == 0:
            return race_group.sample(n=1)
        return filtered.sample(n=1)

class MinOddsBasedStrategy(BettingStrategy):
    def select_horse(self, race_group):
        """選擇賠率最低（最熱門）的馬"""
        odds_column = "win_dividend1" if self.betting_type == BettingType.WIN else "place_odds"
        min_odds = race_group[odds_column].min()
        selected = race_group[race_group[odds_column] == min_odds]
        
        # 檢查是否有符合條件的馬匹
        if len(selected) == 0:
            return race_group.sample(n=1)
            
        return selected.sample(n=1)  # 若有多匹賠率一樣，隨機選一

class MaxOddsBasedStrategy(BettingStrategy):
    def select_horse(self, race_group):
        """選擇賠率最低（最熱門）的馬"""
        odds_column = "win_dividend1" if self.betting_type == BettingType.WIN else "place_odds"
        max_odds = race_group[odds_column].max()
        selected = race_group[race_group[odds_column] == max_odds]
        
        # 檢查是否有符合條件的馬匹
        if len(selected) == 0:
            return race_group.sample(n=1)
            
        return selected.sample(n=1)  # 若有多匹賠率一樣，隨機選一

class MaxJockeyBasedStrategy(BettingStrategy):
        
    def select_horse(self, race_group):
        """根據騎師勝率選擇馬匹"""
        # 根據投注類型選擇對應的勝率欄位
        win_rate_column = "jockey_win_rate_top1" if self.betting_type == BettingType.WIN else "jockey_win_rate_top3"
        
        # 找出勝率最高的騎師
        max_win_rate = race_group[win_rate_column].max()
        selected = race_group[race_group[win_rate_column] == max_win_rate]
        
        # 檢查是否有符合條件的馬匹
        if len(selected) == 0:
            return race_group.sample(n=1)
            
        return selected.sample(n=1)  # 若有多匹馬的騎師勝率一樣，隨機選一 
    
class JockeyBasedStrategy(BettingStrategy):
    def __init__(self, min_win_rate=0.0, max_win_rate=1.0, betting_type=BettingType.WIN):
        super().__init__(betting_type)
        self.min_win_rate = min_win_rate
        self.max_win_rate = max_win_rate
        
    def select_horse(self, race_group):
        """根據騎師勝率區間選擇馬匹"""
        # 根據投注類型選擇對應的勝率欄位
        win_rate_column = "jockey_win_rate_top1" if self.betting_type == BettingType.WIN else "jockey_win_rate_top3"
        
        # 在勝率區間內選擇馬匹
        filtered = race_group[
            (race_group[win_rate_column] >= self.min_win_rate) & 
            (race_group[win_rate_column] <= self.max_win_rate)
        ]
        
        # 如果沒有符合條件的馬匹，則從整個賽事組中隨機選擇
        if len(filtered) == 0:
            return race_group.sample(n=1)
            
        return filtered.sample(n=1)  # 若有多匹馬符合條件，隨機選一
    
class MaxHorseBasedStrategy(BettingStrategy):
        
    def select_horse(self, race_group):
        """根據馬匹勝率選擇馬匹"""
        # 根據投注類型選擇對應的勝率欄位
        win_rate_column = "horse_win_rate_top1" if self.betting_type == BettingType.WIN else "horse_win_rate_top3"
        
        # 找出勝率最高的馬匹
        max_win_rate = race_group[win_rate_column].max()
        selected = race_group[race_group[win_rate_column] == max_win_rate]
        
        # 檢查是否有符合條件的馬匹
        if len(selected) == 0:
            return race_group.sample(n=1)
            
        return selected.sample(n=1)  # 若有多匹馬勝率一樣，隨機選一 

class MaxHorseOddsBasedStrategy(BettingStrategy):
    def __init__(self, min_win_rate=0.0, max_win_rate=1.0, min_odds=1.0, max_odds=float('inf'), betting_type=BettingType.WIN):
        super().__init__(betting_type)
        self.min_win_rate = min_win_rate
        self.max_win_rate = max_win_rate
        self.min_odds = min_odds
        self.max_odds = max_odds
        
    def select_horse(self, race_group):
        """根據馬匹勝率和賠率選擇馬匹"""
        # 根據投注類型選擇對應的勝率欄位和賠率欄位
        win_rate_column = "horse_win_rate_top1" if self.betting_type == BettingType.WIN else "horse_win_rate_top3"
        odds_column = "win_dividend1" if self.betting_type == BettingType.WIN else "place_odds"
        
        # 先篩選符合勝率條件的馬匹
        filtered = race_group[
            (race_group[win_rate_column] >= self.min_win_rate) & 
            (race_group[win_rate_column] <= self.max_win_rate) &
            (race_group[odds_column] >= self.min_odds) & 
            (race_group[odds_column] <= self.max_odds)
        ]
        
        # 如果沒有符合條件的馬匹，則從整個賽事組中隨機選擇
        if len(filtered) == 0:
            return race_group.sample(n=1)
            
        # 計算勝率和賠率的綜合分數
        # 使用勝率和賠率的乘積作為評分標準
        filtered['score'] = filtered[win_rate_column] * filtered[odds_column]
        
        # 選擇分數最高的馬匹
        max_score = filtered['score'].max()
        selected = filtered[filtered['score'] == max_score]
        
        return selected.sample(n=1)  # 若有多匹馬分數一樣，隨機選一 
    
class MaxJockeyOddsBasedStrategy(BettingStrategy):
    def __init__(self, min_win_rate=0.0, max_win_rate=1.0, min_odds=1.0, max_odds=float('inf'), betting_type=BettingType.WIN):
        super().__init__(betting_type)
        self.min_win_rate = min_win_rate
        self.max_win_rate = max_win_rate
        self.min_odds = min_odds
        self.max_odds = max_odds
        
    def select_horse(self, race_group):
        """根據馬匹勝率和賠率選擇馬匹"""
        # 根據投注類型選擇對應的勝率欄位和賠率欄位
        win_rate_column = "jockey_win_rate_top1" if self.betting_type == BettingType.WIN else "jockey_win_rate_top3"
        odds_column = "win_dividend1" if self.betting_type == BettingType.WIN else "place_odds"
        
        # 先篩選符合勝率條件的馬匹
        filtered = race_group[
            (race_group[win_rate_column] >= self.min_win_rate) & 
            (race_group[win_rate_column] <= self.max_win_rate) &
            (race_group[odds_column] >= self.min_odds) & 
            (race_group[odds_column] <= self.max_odds)
        ]
        
        # 如果沒有符合條件的馬匹，則從整個賽事組中隨機選擇
        if len(filtered) == 0:
            return race_group.sample(n=1)
            
        # 計算勝率和賠率的綜合分數
        # 使用勝率和賠率的乘積作為評分標準
        filtered['score'] = filtered[win_rate_column] * filtered[odds_column]
        
        # 選擇分數最高的馬匹
        max_score = filtered['score'].max()
        selected = filtered[filtered['score'] == max_score]
        
        return selected.sample(n=1)  # 若有多匹馬分數一樣，隨機選一 

class CombinedStrategy(BettingStrategy):
    def __init__(self, alpha=0.65, beta=0.25, gamma=0.10, betting_type=BettingType.WIN):
        super().__init__(betting_type)
        self.alpha = alpha  # 馬匹勝率權重
        self.beta = beta    # 騎師勝率權重
        self.gamma = gamma  # 賠率權重
        
    def select_horse(self, race_group):
        """根據馬匹勝率、騎師勝率和賠率綜合評分選擇馬匹"""
        # 根據投注類型選擇對應的勝率欄位和賠率欄位
        horse_win_rate = "horse_win_rate_top1" if self.betting_type == BettingType.WIN else "horse_win_rate_top3"
        jockey_win_rate = "jockey_win_rate_top1" if self.betting_type == BettingType.WIN else "jockey_win_rate_top3"
        odds_column = "win_dividend1" if self.betting_type == BettingType.WIN else "place_odds"
        
        # 檢查必要欄位是否存在
        required_columns = [horse_win_rate, jockey_win_rate, odds_column]
        missing_columns = [col for col in required_columns if col not in race_group.columns]
        if missing_columns:
            print(f"警告：缺少必要欄位：{missing_columns}")
            return race_group.sample(n=1)
            
        df = race_group.copy()
        
        # 檢查是否有 NaN 值
        nan_columns = df[required_columns].columns[df[required_columns].isna().any()].tolist()
        if nan_columns:
            print(f"警告：以下欄位包含 NaN 值：{nan_columns}")
            # 將 NaN 值替換為 0
            df[nan_columns] = df[nan_columns].fillna(0)
            
        # 計算綜合評分
        df["score"] = (
            (
            self.alpha * df[horse_win_rate] +
            self.beta * df[jockey_win_rate] 
            )
            * self.gamma * df[odds_column]
        )
        
        # 檢查是否有無限值
        if df["score"].isin([np.inf, -np.inf]).any():
            print("警告：評分計算出現無限值")
            # 將無限值替換為 0
            df["score"] = df["score"].replace([np.inf, -np.inf], 0)
        
        # 選擇評分最高的馬匹
        # max_score = df["score"].max()
        # selected = df[df["score"] == max_score]
            
        # 先找出第三高分數（可能會有並列）
        top_scores = df["score"].nlargest(3).values
        threshold = top_scores[0]

        # 所有 score ≧ 第三高分數的馬都選進來
        selected = df[df["score"] == threshold]

        return selected.sample(n=1)  # 若有多匹馬評分一樣，隨機選一 