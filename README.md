# 🌐 GridWorld RL Strategy Evaluation (HW1)

[![Flask](https://img.shields.io/badge/Flask-3.0.0-blue.svg)](https://flask.palletsprojects.com/)
[![Numpy](https://img.shields.io/badge/Numpy-1.26.4-green.svg)](https://numpy.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 📝 專案簡介 / Overview
本專案為深度強化學習（DRL）作業一的實作方案。開發了一個互動式的 **$n \times n$ 網格地圖 (GridWorld)**，旨在展示基本的策略評估（Policy Evaluation）算法。

用戶可以自由設計地圖（起點、終點、障礙物），系統則會隨機生成一組策略（Policy），並透過 Bellman 方程計算出每個格子的狀態價值 $V(s)$。

---

## ✨ 核心功能 / Features

### 1. 互動式地圖開發 (HW1-1)
*   **動態維度**：支援 $5 \times 5$ 到 $9 \times 9$ 的網格調整。
*   **狀態設定**：
    *   **🟢 起點 (Start)**：指定綠色格。
    *   **🔴 終點 (End)**：指定紅色格。
    *   **⚪ 障礙物 (Wall)**：指定灰色格（不可通行），上限為 $n-2$ 個，但也支援 0 牆壁評估。

### 2. 策略顯示與價值評估 (HW1-2)
*   **策略生成**：為所有可行動格子（包含起點）隨機生成行動方向（↑, ↓, ←, →）。
*   **價值計算**：
    *   使用 **Policy Evaluation** 推導 $V(s)$。
    *   **獎勵機制**：每步 Reward = -1，終點為吸收狀態（Value=0）。
    *   **邊界處理**：碰撞牆壁或邊界會停留在原處。
*   **視覺呈現**：格子內同時顯示**箭頭（策略）**與**數字（價值）**。

---

## 🚀 快速開始 / Getting Started

### 1. 本地執行
確保您的環境已安裝 Python 3.x，然後執行：

```powershell
# 安裝依賴
pip install -r requirements.txt

# 啟動後端
python app.py
```
開啟瀏覽器訪問 `http://127.0.0.1:5000`。

### 2. 部署到雲端 (Deployment)
本專案已包含 `Procfile` 與 `requirements.txt`，可直接部署至 **Render** 或 **Heroku**。
*   **Build Command**: `pip install -r requirements.txt`
*   **Start Command**: `gunicorn app:app`

---

## 🛠 技術棧 / Tech Stack
*   **Backend**: Python Flask (處理算法與 API)
*   **Frontend**: Vanilla HTML/JavaScript (處理 UI 互動與 CSS 特效)
*   **Computing**: Numpy (向量化計算)
*   **Aesthetics**: 現代深色模式、毛玻璃效果 (Glassmorphism)

---

## 📚 學術背景 / RL Context
本專案實作之 Policy Evaluation 公式：
$$V_{k+1}(s) = \sum_{a} \pi(a|s) \sum_{s', r} p(s', r | s, a) [r + \gamma V_k(s')]$$
由於本案採用確定性隨機策略，公式簡化為：
$$V(s) = R + \gamma V(s_{next})$$

---

## 👥 作者 / Author
*   **Github**: [davidkuo3](https://github.com/davidkuo3)
