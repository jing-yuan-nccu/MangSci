import numpy as np
import pandas as pd
from typing import List

class Simulation:
    def __init__(self, n_simulations: int, betting_strategy):
        self.n_simulations = n_simulations
        self.betting_strategy = betting_strategy
        self.results = []
        self.race_counts = []  # 新增：追蹤每場模擬的賽事數量
        
    def run_simulation(self, races):
        """執行模擬"""
        for sim_num in range(self.n_simulations):
            profit, race_count = self._simulate_one_round(races)
            self.results.append(profit)
            self.race_counts.append(race_count)
            print(f"模擬 #{sim_num + 1}: 跑了 {race_count} 場賽事，損益: {profit:.2f}")
        return self
        
    def _simulate_one_round(self, races):
        """執行一輪模擬"""
        profit = 0
        race_count = 0
        for _, group in races:
            selected = self.betting_strategy.select_horse(group)
            
            # 若 select_horse 回傳為 DataFrame，取第一行
            if hasattr(selected, "iloc"):
                selected = selected.iloc[0]
            
            is_win = self.betting_strategy.get_result(selected)
            betting_type = self.betting_strategy.betting_type

            if betting_type == "win":
                # 獨贏：只算第一名的 win_dividend
                if is_win:
                    odds = float(selected["win_dividend1"])
                    profit += odds/10 - 1
                else:
                    profit -= 1

            elif betting_type == "place":
                # 位置：若進前三名，根據名次用正確的 place_dividend
                result = int(selected["result"])
                
                if result in [1, 2, 3]:
                    # 使用對應名次的 place_dividend
                    odds = float(selected[f"place_dividend{result}"])
                    # place 的獲利計算方式：賠率 - 1
                    if pd.isna(odds):
                        # 缺值你可以自訂：1.賠掉本金 2.視為0 3.略過這場
                        odds = 1
                    profit += odds/10 - 1
                else:
                    profit -= 1

            else:
                raise ValueError(f"不支援的投注類型: {betting_type}")
            
            race_count += 1
        return profit, race_count

    
    def get_results(self):
        """取得模擬結果"""
        return {
            'results': self.results,
            'mean': np.mean(self.results),
            'std': np.std(self.results),
            'min': np.min(self.results),
            'max': np.max(self.results),
            'sum': np.sum(self.results),
            'race_counts': self.race_counts,  # 新增：包含賽事數量資訊
            'avg_races': np.mean(self.race_counts)  # 新增：平均賽事數量
        } 