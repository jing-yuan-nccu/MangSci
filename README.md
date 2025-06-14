# 賽馬投注模擬系統

這是一個用於模擬賽馬投注策略的 Python 專案。該系統可以分析歷史賽馬數據，並使用不同的投注策略進行模擬，以評估策略的有效性。

## 功能特點

- 支援多種投注策略：
  - 隨機策略
  - 賠率基礎策略
  - 騎師勝率策略
  - 馬匹勝率策略
  - 綜合策略（結合馬匹勝率、騎師勝率和賠率）
- 支援不同投注類型：
  - 獨贏（Win）
  - 位置（Place）
- 數據處理和標準化
- 模擬結果分析

## 安裝需求

- Python 3.8+
- pandas
- numpy

## 安裝步驟

1. 克隆專案：
```bash
git clone https://github.com/你的用戶名/MangSci.git
cd MangSci
```

2. 安裝依賴：
```bash
pip install -r requirements.txt
```

## 使用方式

1. 準備數據：
   - 將賽馬數據放入 `data` 目錄

2. 運行模擬：
```python
from src.simulation import Simulation
from src.betting_strategy import CombinedStrategy

# 創建模擬實例
sim = Simulation(data_path="data/your_data.csv")

# 選擇策略
strategy = CombinedStrategy(alpha=0.65, beta=0.25, gamma=0.10)

# 運行模擬
results = sim.run(strategy, n_races=1000)
```

## 專案結構

```
MangSci/
├── src/
│   ├── data_processor.py    # 數據處理模組
│   ├── betting_strategy.py  # 投注策略模組
│   └── simulation.py        # 模擬執行模組
├── data/                    # 數據目錄
├── requirements.txt         # 依賴套件列表
└── README.md               # 專案說明文件
```

## 授權

MIT License 