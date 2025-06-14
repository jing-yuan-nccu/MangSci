from data_processor import DataProcessor
from betting_strategy import RandomStrategy, OddsBasedStrategy, MinOddsBasedStrategy, MaxOddsBasedStrategy, BettingType
from betting_strategy import JockeyBasedStrategy, MaxJockeyBasedStrategy, MaxHorseBasedStrategy, MaxHorseOddsBasedStrategy, MaxJockeyOddsBasedStrategy
from betting_strategy import CombinedStrategy
from simulation import Simulation

def main():
    processor = DataProcessor()
    processor.load_data("./data/simulation_data.csv")
    processor.filter_columns(["race_id", "horse_id", "result", "date",
                              "win_odds", "place_odds", "win_dividend1", 
                              "place_dividend1", "place_dividend2", "place_dividend3",
                              "jockey_id", "jockey_win_top1",  "jockey_win_top3", 
                              "horse_win_top1",  "horse_win_top3"])
    processor.add_place_result()  # 新增 place 結果
    processor.add_horse_win_rate(n_races=10)  # 計算前10場的勝率
    processor.add_jockey_win_rate(n_races=10)  # 計算前10場的勝率

    # 取得賽事資料
    races = processor.get_races()
    
    # 設定模擬參數
    n_simulations = 10
    
    # print("\n=== 隨機策略模擬 (WIN) ===")
    # # 使用隨機策略 (WIN)
    # random_strategy_win = RandomStrategy(betting_type=BettingType.WIN)
    # random_sim_win = Simulation(n_simulations, random_strategy_win)
    # random_results_win = random_sim_win.run_simulation(races).get_results()
    
    # print("\n=== 隨機策略模擬 (PLACE) ===")
    # # 使用隨機策略 (PLACE)
    # random_strategy_place = RandomStrategy(betting_type=BettingType.PLACE)
    # random_sim_place = Simulation(n_simulations, random_strategy_place)
    # random_results_place = random_sim_place.run_simulation(races).get_results()
    
    # print("\n=== 賠率策略模擬 (WIN) ===")
    # # 使用賠率策略 (WIN)
    # odds_strategy_win = OddsBasedStrategy(min_odds=2.0, max_odds=5.0, betting_type=BettingType.WIN)
    # odds_sim_win = Simulation(n_simulations, odds_strategy_win)
    # odds_results_win = odds_sim_win.run_simulation(races).get_results()
    
    # print("\n=== 賠率策略模擬 (PLACE) ===")
    # # 使用賠率策略 (PLACE)
    # odds_strategy_place = OddsBasedStrategy(min_odds=2.0, max_odds=5.0, betting_type=BettingType.PLACE)
    # odds_sim_place = Simulation(n_simulations, odds_strategy_place)
    # odds_results_place = odds_sim_place.run_simulation(races).get_results()

    # print("\n=== 最低賠率策略模擬 (WIN) ===")
    # min_odds_strategy_win = MinOddsBasedStrategy(betting_type=BettingType.WIN)
    # min_odds_sim_win = Simulation(n_simulations, min_odds_strategy_win)
    # min_odds_results_win = min_odds_sim_win.run_simulation(races).get_results()

    # print("\n=== 最低賠率策略模擬 (PLACE) ===")
    # min_odds_strategy_place = MinOddsBasedStrategy(betting_type=BettingType.PLACE)
    # min_odds_sim_place = Simulation(n_simulations, min_odds_strategy_place)
    # min_odds_results_place = min_odds_sim_place.run_simulation(races).get_results()
    
    # print("\n=== 最高賠率策略模擬 (WIN) ===")
    # max_odds_strategy_win = MaxOddsBasedStrategy(betting_type=BettingType.WIN)
    # max_odds_sim_win = Simulation(n_simulations, max_odds_strategy_win)
    # max_odds_results_win = max_odds_sim_win.run_simulation(races).get_results()

    # print("\n=== 最高賠率策略模擬 (PLACE) ===")
    # max_odds_strategy_place = MaxOddsBasedStrategy(betting_type=BettingType.PLACE)
    # max_odds_sim_place = Simulation(n_simulations, max_odds_strategy_place)
    # max_odds_results_place = max_odds_sim_place.run_simulation(races).get_results()

    # print("\n=== 騎師勝率策略模擬 (WIN) ===")
    # jockey_strategy_win = JockeyBasedStrategy(0.05,1,betting_type=BettingType.WIN)
    # jockey_sim_win = Simulation(n_simulations, jockey_strategy_win)
    # jockey_results_win = jockey_sim_win.run_simulation(races).get_results()

    # print("\n=== 騎師勝率策略模擬 (PLACE) ===")
    # jockey_strategy_place = JockeyBasedStrategy(0.17,1,betting_type=BettingType.PLACE)
    # jockey_sim_place = Simulation(n_simulations, jockey_strategy_place)
    # jockey_results_place = jockey_sim_place.run_simulation(races).get_results()

    # print("\n=== 騎師勝率策略模擬 (WIN) ===")
    # jockey_strategy_win = JockeyBasedStrategy(betting_type=BettingType.WIN)
    # jockey_sim_win = Simulation(n_simulations, jockey_strategy_win)
    # jockey_results_win = jockey_sim_win.run_simulation(races).get_results()

    # print("\n=== 騎師勝率策略模擬 (PLACE) ===")
    # jockey_strategy_place = JockeyBasedStrategy(betting_type=BettingType.PLACE)
    # jockey_sim_place = Simulation(n_simulations, jockey_strategy_place)
    # jockey_results_place = jockey_sim_place.run_simulation(races).get_results()

    # print("\n=== 馬匹勝率策略模擬 (WIN) ===")
    # horse_strategy_win = MaxHorseBasedStrategy(betting_type=BettingType.WIN)
    # horse_sim_win = Simulation(n_simulations, horse_strategy_win)
    # horse_results_win = horse_sim_win.run_simulation(races).get_results()

    # print("\n=== 馬匹勝率策略模擬 (PLACE) ===")
    # horse_strategy_place = MaxHorseBasedStrategy(betting_type=BettingType.PLACE)
    # horse_sim_place = Simulation(n_simulations, horse_strategy_place)
    # horse_results_place = horse_sim_place.run_simulation(races).get_results()

    # print("\n=== 馬匹賠率策略模擬 (WIN) ===")
    # horse_strategy_win = MaxHorseOddsBasedStrategy(betting_type=BettingType.WIN)
    # horse_sim_win = Simulation(n_simulations, horse_strategy_win)
    # horse_results_win = horse_sim_win.run_simulation(races).get_results()

    # print("\n=== 馬匹賠率策略模擬 (PLACE) ===")
    # horse_strategy_place = MaxHorseOddsBasedStrategy(betting_type=BettingType.PLACE)
    # horse_sim_place = Simulation(n_simulations, horse_strategy_place)
    # horse_results_place = horse_sim_place.run_simulation(races).get_results()

    # print("\n=== 騎師賠率策略模擬 (WIN) ===")
    # jockey_strategy_win = MaxJockeyOddsBasedStrategy(betting_type=BettingType.WIN)
    # jockey_sim_win = Simulation(n_simulations, jockey_strategy_win)
    # jockey_results_win = jockey_sim_win.run_simulation(races).get_results()
    
    # print("\n=== 騎師賠率策略模擬 (PLACE) ===")
    # jockey_strategy_place = MaxJockeyOddsBasedStrategy(betting_type=BettingType.PLACE)
    # jockey_sim_place = Simulation(n_simulations, jockey_strategy_place)
    # jockey_results_place = jockey_sim_place.run_simulation(races).get_results()

    print("\n=== 綜合策略模擬 (WIN) ===")
    combined_strategy_win = CombinedStrategy(alpha=0.75, beta=0.25, gamma=0.10, betting_type=BettingType.WIN)
    combined_sim_win = Simulation(n_simulations, combined_strategy_win)
    combined_results_win = combined_sim_win.run_simulation(races).get_results()

    print("\n=== 綜合策略模擬 (PLACE) ===")
    combined_strategy_place = CombinedStrategy(alpha=0.75, beta=0.25, gamma=0.10, betting_type=BettingType.PLACE)
    combined_sim_place = Simulation(n_simulations, combined_strategy_place)
    combined_results_place = combined_sim_place.run_simulation(races).get_results()

    # 輸出結果
    # print("\n=== 隨機策略統計 (WIN) ===")
    # print(f"平均每場模擬賽事數：{random_results_win['avg_races']:.1f}")
    # print(f"平均損益：{random_results_win['mean']:.2f}")
    # print(f"損益標準差：{random_results_win['std']:.2f}")
    # print(f"最小損益：{random_results_win['min']:.2f}")
    # print(f"最大損益：{random_results_win['max']:.2f}")
    
    # print("\n=== 隨機策略統計 (PLACE) ===")
    # print(f"平均每場模擬賽事數：{random_results_place['avg_races']:.1f}")
    # print(f"平均損益：{random_results_place['mean']:.2f}")
    # print(f"損益標準差：{random_results_place['std']:.2f}")
    # print(f"最小損益：{random_results_place['min']:.2f}")
    # print(f"最大損益：{random_results_place['max']:.2f}")
    
    # print("\n=== 賠率策略統計 (WIN) ===")
    # print(f"平均每場模擬賽事數：{odds_results_win['avg_races']:.1f}")
    # print(f"平均損益：{odds_results_win['mean']:.2f}")
    # print(f"損益標準差：{odds_results_win['std']:.2f}")
    # print(f"最小損益：{odds_results_win['min']:.2f}")
    # print(f"最大損益：{odds_results_win['max']:.2f}")
    
    # print("\n=== 賠率策略統計 (PLACE) ===")
    # print(f"平均每場模擬賽事數：{odds_results_place['avg_races']:.1f}")
    # print(f"平均損益：{odds_results_place['mean']:.2f}")
    # print(f"損益標準差：{odds_results_place['std']:.2f}")
    # print(f"最小損益：{odds_results_place['min']:.2f}")
    # print(f"最大損益：{odds_results_place['max']:.2f}")

    # print("\n=== 最低賠率策略統計 (PLACE) ===")
    # print(f"平均每場模擬賽事數：{min_odds_results_place['avg_races']:.1f}")
    # print(f"平均損益：{min_odds_results_place['mean']:.2f}")
    # print(f"損益標準差：{min_odds_results_place['std']:.2f}")
    # print(f"最小損益：{min_odds_results_place['min']:.2f}")
    # print(f"最大損益：{min_odds_results_place['max']:.2f}")

    # print("\n=== 最低賠率策略統計 (WIN) ===")
    # print(f"平均每場模擬賽事數：{min_odds_results_win['avg_races']:.1f}")
    # print(f"平均損益：{min_odds_results_win['mean']:.2f}")
    # print(f"損益標準差：{min_odds_results_win['std']:.2f}")
    # print(f"最小損益：{min_odds_results_win['min']:.2f}")
    # print(f"最大損益：{min_odds_results_win['max']:.2f}")

    # print("\n=== 最高賠率策略統計 (WIN) ===")
    # print(f"平均每場模擬賽事數：{max_odds_results_win['avg_races']:.1f}")
    # print(f"平均損益：{max_odds_results_win['mean']:.2f}")
    # print(f"損益標準差：{max_odds_results_win['std']:.2f}")
    # print(f"最小損益：{max_odds_results_win['min']:.2f}")
    # print(f"最大損益：{max_odds_results_win['max']:.2f}")

    # print("\n=== 最高賠率策略統計 (PLACE) ===")
    # print(f"平均每場模擬賽事數：{max_odds_results_place['avg_races']:.1f}")
    # print(f"平均損益：{max_odds_results_place['mean']:.2f}")
    # print(f"損益標準差：{max_odds_results_place['std']:.2f}")
    # print(f"最小損益：{max_odds_results_place['min']:.2f}")
    # print(f"最大損益：{max_odds_results_place['max']:.2f}")

    # print("\n=== 騎師勝率策略統計 (WIN) ===")
    # print(f"平均每場模擬賽事數：{jockey_results_win['avg_races']:.1f}")
    # print(f"平均損益：{jockey_results_win['mean']:.2f}")
    # print(f"損益標準差：{jockey_results_win['std']:.2f}")
    # print(f"最小損益：{jockey_results_win['min']:.2f}")
    # print(f"最大損益：{jockey_results_win['max']:.2f}")

    # print("\n=== 騎師勝率策略統計 (PLACE) ===")
    # print(f"平均每場模擬賽事數：{jockey_results_place['avg_races']:.1f}")
    # print(f"平均損益：{jockey_results_place['mean']:.2f}")
    # print(f"損益標準差：{jockey_results_place['std']:.2f}")
    # print(f"最小損益：{jockey_results_place['min']:.2f}")
    # print(f"最大損益：{jockey_results_place['max']:.2f}")

    # print("\n=== 騎師勝率策略統計 (WIN) ===")
    # print(f"平均每場模擬賽事數：{jockey_results_win['avg_races']:.1f}")
    # print(f"平均損益：{jockey_results_win['mean']:.2f}")
    # print(f"損益標準差：{jockey_results_win['std']:.2f}")
    # print(f"最小損益：{jockey_results_win['min']:.2f}")
    # print(f"最大損益：{jockey_results_win['max']:.2f}")

    # print("\n=== 騎師勝率策略統計 (PLACE) ===")
    # print(f"平均每場模擬賽事數：{jockey_results_place['avg_races']:.1f}")
    # print(f"平均損益：{jockey_results_place['mean']:.2f}")
    # print(f"損益標準差：{jockey_results_place['std']:.2f}")
    # print(f"最小損益：{jockey_results_place['min']:.2f}")
    # print(f"最大損益：{jockey_results_place['max']:.2f}")

    # print("\n=== 馬匹勝率策略統計 (WIN) ===")
    # print(f"平均每場模擬賽事數：{horse_results_win['avg_races']:.1f}")
    # print(f"平均損益：{horse_results_win['mean']:.2f}")
    # print(f"損益標準差：{horse_results_win['std']:.2f}")
    # print(f"最小損益：{horse_results_win['min']:.2f}")
    # print(f"最大損益：{horse_results_win['max']:.2f}")  

    # print("\n=== 馬匹勝率策略統計 (PLACE) ===")
    # print(f"平均每場模擬賽事數：{horse_results_place['avg_races']:.1f}")
    # print(f"平均損益：{horse_results_place['mean']:.2f}")
    # print(f"損益標準差：{horse_results_place['std']:.2f}")
    # print(f"最小損益：{horse_results_place['min']:.2f}")
    # print(f"最大損益：{horse_results_place['max']:.2f}")

    # print("\n=== 馬匹賠率策略統計 (WIN) ===")
    # print(f"平均每場模擬賽事數：{horse_results_win['avg_races']:.1f}")
    # print(f"平均損益：{horse_results_win['mean']:.2f}")
    # print(f"損益標準差：{horse_results_win['std']:.2f}")
    # print(f"最小損益：{horse_results_win['min']:.2f}")
    # print(f"最大損益：{horse_results_win['max']:.2f}")

    # print("\n=== 馬匹賠率策略統計 (PLACE) ===")
    # print(f"平均每場模擬賽事數：{horse_results_place['avg_races']:.1f}")
    # print(f"平均損益：{horse_results_place['mean']:.2f}")
    # print(f"損益標準差：{horse_results_place['std']:.2f}")
    # print(f"最小損益：{horse_results_place['min']:.2f}")
    # print(f"最大損益：{horse_results_place['max']:.2f}")

    # print("\n=== 騎師賠率策略統計 (WIN) ===")
    # print(f"平均每場模擬賽事數：{jockey_results_win['avg_races']:.1f}")
    # print(f"平均損益：{jockey_results_win['mean']:.2f}")
    # print(f"損益標準差：{jockey_results_win['std']:.2f}")
    # print(f"最小損益：{jockey_results_win['min']:.2f}")
    # print(f"最大損益：{jockey_results_win['max']:.2f}")

    # print("\n=== 騎師賠率策略統計 (PLACE) ===")
    # print(f"平均每場模擬賽事數：{jockey_results_place['avg_races']:.1f}")
    # print(f"平均損益：{jockey_results_place['mean']:.2f}")
    # print(f"損益標準差：{jockey_results_place['std']:.2f}")
    # print(f"最小損益：{jockey_results_place['min']:.2f}")
    # print(f"最大損益：{jockey_results_place['max']:.2f}")

    print("\n=== 綜合策略統計 (WIN) ===")
    print(f"平均每場模擬賽事數：{combined_results_win['avg_races']:.1f}")
    print(f"平均損益：{combined_results_win['mean']:.2f}")
    print(f"損益標準差：{combined_results_win['std']:.2f}")
    print(f"最小損益：{combined_results_win['min']:.2f}")
    print(f"最大損益：{combined_results_win['max']:.2f}")

    print("\n=== 綜合策略統計 (PLACE) ===")
    print(f"平均每場模擬賽事數：{combined_results_place['avg_races']:.1f}")
    print(f"平均損益：{combined_results_place['mean']:.2f}")
    print(f"損益標準差：{combined_results_place['std']:.2f}")
    print(f"最小損益：{combined_results_place['min']:.2f}")
    print(f"最大損益：{combined_results_place['max']:.2f}")

if __name__ == "__main__":
    main()
