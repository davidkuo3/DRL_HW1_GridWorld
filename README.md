# 🌐 GridWorld RL Strategy & Value Iteration (HW1)

[![Flask](https://img.shields.io/badge/Flask-3.0.0-blue.svg)](https://flask.palletsprojects.com/)
[![Numpy](https://img.shields.io/badge/Numpy-1.26.4-green.svg)](https://numpy.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 📝 專案簡介 / Overview
本專案為深度強化學習（DRL）作業一的完整實作。開發了一個互動式的 **$n \times n$ 網格地圖 (GridWorld)**，旨在展示兩大強化學習核心算法：
1.  **策略評估 (Policy Evaluation)**：評估隨機策略下的狀態價值。
2.  **價值迭代 (Value Iteration)**：推導並尋找網格世界中的最佳政策 (Optimal Policy)。

用戶可以自由設計地圖（起點、終點、障礙物），並選擇不同的算法來觀察價值函數 $V(s)$ 與行動政策（箭頭方向）的動態變化。

---

## ✨ 核心功能 / Features

### 1. 互動式地圖開發 (HW1-1)
*   **動態維度**：支援 $5 \times 5$ 到 $9 \times 9$ 的網格調整。
*   **狀態設定**：
    *   **🟢 起點 (Start)**：指定綠色格。
    *   **🔴 終點 (End)**：指定紅色格。
    *   **⚪ 障礙物 (Wall)**：指定灰色格（不可通行），上限為 $n-2$ 個。

### 2. 策略顯示與價值評估 (HW1-2)
*   **功能**：評估一組隨機生成的行動方向（↑, ↓, ←, →）。
*   **價值計算**：使用 **Policy Evaluation** 公式迭代直至收斂。
*   **獎勵機制**：每步 Reward = -1，終點為吸收狀態（Value=0）。

### 3. 最佳政策推導 (HW1-3)
*   **功能**：使用 **Value Iteration** 算法自動計算每個狀態的最佳行動。
*   **效果**：產生的箭頭政策將會始終朝向終點，並自動避開用戶設定的障礙物。
*   **視覺化**：網格同步更新為最佳價值函數 $V^*(s)$ 與最佳行動箭頭。

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
*   **Backend**: Python Flask (處理算法邏輯與 REST API)
*   **Frontend**: Vanilla HTML/JavaScript (處理 UI 互動與 CSS 特效)
*   **Computing**: Numpy (高效矩陣運算與算法實作)
*   **Aesthetics**: 現代深色模式、毛玻璃效果 (Glassmorphism)、動態按鈕特效

---

## 📚 學術背景 / RL Context

### Policy Evaluation (HW1-2)
用於計算給定策略 $\pi$ 的價值函數：
$$V_{\pi}(s) = \sum_{a} \pi(a|s) \sum_{s', r} p(s', r | s, a) [r + \gamma V_{\pi}(s')] \approx R + \gamma V_{\pi}(s_{next})$$

### Value Iteration (HW1-3)
用於直接搜尋最佳價值函數：
$$V_{k+1}(s) = \max_{a} \sum_{s', r} p(s', r | s, a) [r + \gamma V_k(s')] = \max_{a} [R + \gamma V_k(s_{next})]$$
最佳政策推導：
$$\pi^*(s) = \arg\max_{a} \sum_{s', r} p(s', r | s, a) [r + \gamma V^*(s')]$$

---

## 👥 作者 / Author
*   **Github**: [davidkuo3](https://github.com/davidkuo3)
