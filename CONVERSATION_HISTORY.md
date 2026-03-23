# 📜 對話紀錄與開發歷程 | Conversation History & Dev Log

> [!NOTE]
> 本文件記錄了關於 **GridWorld RL Strategy Evaluation** 專案的開發歷程、對話摘要與關鍵技術決策。

---

## 🗓️ 2026-03-11 | Session 1: 核心功能開發
**對話 ID**: `b3c31f06-e7c0-4afd-9254-ec41107b0446`
**主題**: Streamlit / Flask Gridworld App 實作

### 🎯 初始需求 (USER Objective)
建立一個可互動的 GridWorld 環境，用於展示 Policy Evaluation 算法：
- 支持 $n \times n$ 網格（$5 \leq n \leq 9$）。
- 用戶可自定義起點（綠）、終點（紅）、障礙物（灰）。
- 隨機生成策略（Policy）並顯示箭頭。
- 計算並顯示各狀態的價值函數 $V(s)$。

### 🏗️ 實作成果
- **後端 (Backend)**: 採用 Python Flask 框架處理算法邏輯。
- **算法**: 實作了基於 Bellman 方程的迭代式 Policy Evaluation。
    - **Reward**: 每步為 -1，旨在找出最短路徑趨勢。
    - **Gamma ($\gamma$)**: 設定為 0.95。
    - **收斂準則**: $10^{-4}$。
- **前端 (Frontend)**: 使用 Vanilla HTML/JS 與 CSS，實現現代感的毛玻璃 (Glassmorphism) 設計風格。
- **部署準備**: 增加了 `Procfile` 與 `requirements.txt` 以支援雲端部署。

---

## 🗓️ 2026-03-13 | Session 2: 歷史歸檔與後續優化
**對話 ID**: `8bf92267-df7b-415d-a5d3-bf23459ed303`
**主題**: 專案管理與對話存檔

### 🛠️ 目前動作
- [x] 建立 `CONVERSATION_HISTORY.md` 紀錄開發軌跡。
- [ ] 準備進行後續功能擴充或 Bug 修復。

### 📌 關鍵決策記錄
1. **框架選擇**: 雖然初始討論提到 Streamlit，但最終選擇 Flask 以獲得更靈活的 UI 控制能力（如 CSS 動畫與自定義交互）。
2. **獎勵機制**: 採用 $R = -1$ 搭配終點 $V=0$ 的標準設置。
3. **視覺反饋**: 決定在同一個網格內同時顯示策略箭頭與數值，以增強直觀性。

---

## 🗓️ 2026-03-23 | Session 3: HW1-3 Value Iteration 實作與 GitHub 部署
**對話 ID**: `c66f5007-8220-4181-85cc-85c5e0723e7f`
**主題**: 實作價值迭代算法與最佳政策推導

### 🎯 需求說明 (HW1-3)
- 實作 **價值迭代 (Value Iteration)** 算法。
- 推導並顯示每個格子的 **最佳政策 (Optimal Policy)**。
- 更新網格顯示，支援在隨機政策與最佳政策之間切換。
- 將程式碼同步更新至 GitHub。

### 🏗️ 實作成果
- **算法更新 (`app.py`)**:
    - 推導最佳價值函數 $V^*(s)$ 與對應的最佳行動 $\pi^*(s)$。
- **介面優化 (`index.html`)**:
    - 新增 **Algorithm Selector** 下拉選單，支援切換 HW1-2 (Random) 與 HW1-3 (Optimal)。
    - 優化地圖設定邏輯，調整網格大小時會盡量保留原有的牆壁配置。
- **說明文件更新 (`README.md`)**:
    - 完整描述了 HW1-3 的功能與 Bellman Optimality 公式。
- **版本控制**:
    - 成功 Push 所有變更至 GitHub `davidkuo3/DRL_HW1_GridWorld`。

### 📌 關鍵決策記錄
1. **導航邏輯**: 在 Value Iteration 中，箭頭能動態避開所有牆壁並指向最佳路徑。
2. **單一 Route 擴展**: `/compute` API 現在可選算法，增強了系統靈活性。

---

> [!TIP]
> 之後若有重要的討論或功能變更，建議持續更新此文檔以維持開發透明度。
