# 👻 Project: Phantom-Hand (Universal Agentic Automation & Cognitive Solver Skill)

A universal Model Context Protocol (MCP) server & **Agentic Skill Package** that empowers **any AI Agent** (Antigravity, Claude Desktop, Cursor, Continue.dev, etc.) to bypass traditional UI automation limits, execute headless COM object manipulations, bypass strict browser Content Security Policies (CSP), and solve complex cognitive reasoning, situational judgment, and workplace personality assessments.

---

## ⚡ Core Capabilities

### 1. 🎯 Apex Browser Sniper Protocol (CSP-Immune DOM Automation)
*   **Zero-Extension & Zero-Port Injection:** Injects and executes arbitrary JavaScript directly into active browser tabs (Chrome, Edge, Firefox, Brave) via an interactive address bar handshake (`Ctrl+L` -> `javascript:` -> `Ctrl+V` -> `Enter`).
*   **Bypasses Content Security Policy (CSP):** Overcomes website restrictions where `eval()` or third-party extension content scripts are blocked by the host server.
*   **Two-Way Clipboard Bridge:** Returns DOM scrape results and computed JSON data back to Python in milliseconds using temporary DOM bridge handshakes without file I/O delays.
*   **Asynchronous Batch Pacing:** Dispatches multi-action sequences with configurable intervals (250ms–400ms) to ensure backend AJAX requests complete cleanly without race conditions.

### 2. 🧠 Comprehensive Cognitive & Assessment Solvers
*   **Raven's Advanced Progressive Matrices (APM Set II):** 36-item visual logic solver covering rotation, XOR segment cancellation, progression addition, and distribution-of-three features.
*   **Corporate Learning Agility Profiler:** Classifies behavioral statements into 5 core organizational agility dimensions (Mental, People, Change, Results, Self-Awareness) with 5-point Likert ratings.
*   **Big Five Workplace Personality Inventory:** 60-item psychometric evaluation engine (Emotional Stability, Conscientiousness, Extraversion, Agreeableness, Openness) with anti-faking moderation.
*   **Retail & Corporate Situational Judgement Tests (SJT):** Case decision matrices for Head Office (*Merchandising Support Officer*) and Store Frontline (*Sales Officer*).
*   **Schwartz Portrait Values Questionnaire (PVQ-57):** 57 universal human values dimensions mapped to corporate cultures (Integrity, Humility, Respect, Teamwork).
*   **Human-in-the-Loop (HitL) Guardrails:** Non-destructive completion mode that automatically completes $N-1$ items while preserving the final question for manual user review and final submission.

### 3. 👻 Ghost-COM Office Automation
*   **Zero-Interference Automation:** Directly interfaces with Microsoft Office's Component Object Model (Word, Excel, PowerPoint) in the background without stealing the user's active window focus.
*   **execute_python_in_session:** Interactive Windows session execution environment allowing full desktop API calls (`pygetwindow`, `pywinauto`, `win32com`).

---

## 🛠️ MCP Tool Reference

| Tool | Category | Description |
|:---|:---:|:---|
| `inject_browser_javascript` | Browser Sniper | Injects raw JS into target browser window via URL bar, bypassing CSP |
| `eval_browser_javascript` | Browser Sniper | Injects JS and reads returned data via two-way clipboard handshake |
| `list_active_windows` | Window Management | Lists titles of all currently open desktop application windows |
| `solve_raven_apm` | Cognitive Solver | Returns verified solutions and geometric rules for APM Set II items |
| `evaluate_competency` | Cognitive Solver | Analyzes workplace statements and returns optimal Likert ratings |
| `solve_personality_item` | Cognitive Solver | Returns optimal response for Big Five 60-item Personality Inventory |
| `solve_retail_sjt` | Cognitive Solver | Returns decision rationale for Merchandising and Sales SJT scenarios |
| `solve_portrait_value` | Cognitive Solver | Returns score index and text for Schwartz PVQ-57 values items |
| `execute_python_in_session` | Execution Backdoor | Runs arbitrary Python code inside the user's interactive desktop session |
| `type_in_background` | Ghost-COM | Types keys directly into background windows without changing focus |
| `take_screenshot` | Vision & RPA | Takes high-resolution screenshots for vision-enabled agents |
| `mouse_click` | Vision & RPA | Clicks specific $(x, y)$ desktop coordinates |
| `type_text` | Vision & RPA | Types string inputs directly into active inputs |
| `press_key` | Vision & RPA | Presses individual keys (`enter`, `tab`, `esc`, etc.) |
| `hotkey` | Vision & RPA | Executes multi-key combinations (`ctrl+c`, `ctrl+v`, etc.) |

---

## 📦 Universal Installation

### Requirements
*   Windows 10 / 11
*   Python 3.10+
*   Dependencies:
    ```bash
    pip install fastmcp pyautogui pillow pygetwindow pywinauto pywin32 pyperclip
    ```

### 1. Antigravity Skill Registration
This repository contains a full `SKILL.md` specification and is automatically discoverable when placed in `~/.gemini/config/skills/phantom-hand/`.

### 2. Antigravity MCP Server (`~/.gemini/config/mcp_config.json`)
```json
{
  "mcpServers": {
    "phantom-hand": {
      "command": "python",
      "args": ["C:/Users/ROG G532 LV/.gemini/antigravity/scratch/Phantom-Hand/mcp_server.py"]
    }
  }
}
```

### 3. Claude Desktop (`claude_desktop_config.json`)
```json
{
  "mcpServers": {
    "phantom-hand": {
      "command": "python",
      "args": ["C:/Path/To/Phantom-Hand/mcp_server.py"]
    }
  }
}
```

### 4. Cursor IDE
1. Open **Cursor Settings** > **Features** > **MCP**.
2. Click **+ Add New MCP Server**.
3. Type: `stdio`
4. Command: `python C:/Path/To/Phantom-Hand/mcp_server.py`

---

## 👤 Author
Developed by **Wahyu Nur Iman** ([@wahyunuriman999](https://github.com/wahyunuriman999)).
Distributed under the MIT License.
