import os
import json
import tempfile
import subprocess
from fastmcp import FastMCP
import pyautogui
from PIL import ImageGrab
import pygetwindow as gw
from pywinauto import Application

# Import internal modules
try:
    from modules.browser_sniper import BrowserSniper
    from modules.solvers.raven_apm import RavenMatrixSolver
    from modules.solvers.competency_profiler import CompetencyProfiler
    from modules.solvers.personality_inventory import PersonalityInventorySolver
    from modules.solvers.retail_sjt import RetailSJTSolver
    from modules.solvers.portrait_values import PortraitValuesProfiler
except ImportError:
    import sys
    sys.path.append(os.path.dirname(os.path.abspath(__file__)))
    from modules.browser_sniper import BrowserSniper
    from modules.solvers.raven_apm import RavenMatrixSolver
    from modules.solvers.competency_profiler import CompetencyProfiler
    from modules.solvers.personality_inventory import PersonalityInventorySolver
    from modules.solvers.retail_sjt import RetailSJTSolver
    from modules.solvers.portrait_values import PortraitValuesProfiler

mcp = FastMCP("Phantom-Hand")

# ==========================================
# 1. CORE SCREEN & RPA TOOLS
# ==========================================

@mcp.tool()
def get_screen_size() -> str:
    """Gets the width and height of the main screen."""
    width, height = pyautogui.size()
    return f"Screen size: {width}x{height}"

@mcp.tool()
def take_screenshot() -> str:
    """Takes a screenshot of the entire screen and returns the absolute file path."""
    img = ImageGrab.grab()
    fd, path = tempfile.mkstemp(suffix=".png")
    os.close(fd)
    img.save(path)
    return f"Screenshot saved to: {path}. Use the view_file tool on this path to see it."

@mcp.tool()
def mouse_click(x: int, y: int, button: str = "left", clicks: int = 1) -> str:
    """Moves the mouse to the specified (x, y) coordinates and clicks."""
    pyautogui.click(x=x, y=y, button=button, clicks=clicks)
    return f"Clicked {button} button at ({x}, {y}) {clicks} time(s)."

@mcp.tool()
def type_text(text: str, interval: float = 0.0) -> str:
    """Types the given string of text."""
    pyautogui.write(text, interval=interval)
    return f"Typed text: '{text}'"

@mcp.tool()
def press_key(key: str) -> str:
    """Presses a specific keyboard key (e.g., 'enter', 'tab', 'esc', 'ctrl')."""
    pyautogui.press(key)
    return f"Pressed key: '{key}'"

@mcp.tool()
def hotkey(keys: list[str]) -> str:
    """Presses a combination of keys (e.g., ['ctrl', 'c'])."""
    pyautogui.hotkey(*keys)
    return f"Pressed hotkey combination: {keys}"

# ==========================================
# 2. GHOST COM & BACKGROUND AUTOMATION
# ==========================================

@mcp.tool()
def type_in_background(title_keyword: str, text: str) -> str:
    """Sends keystrokes to a background window via UI Automation without stealing focus."""
    try:
        app = Application(backend="uia").connect(title_re=f".*{title_keyword}.*", timeout=3)
        window = app.top_window()
        window.type_keys(text, set_foreground=False, with_spaces=True, with_newlines=True)
        return f"Successfully sent keys to background window: {window.window_text()}"
    except Exception as e:
        return f"Error sending keys to background window: {e}"

@mcp.tool()
def execute_python_in_session(code: str) -> str:
    """Executes arbitrary python code directly in the user's interactive Windows session."""
    fd, path = tempfile.mkstemp(suffix=".py")
    os.write(fd, code.encode("utf-8"))
    os.close(fd)
    try:
        result = subprocess.run(["python", path], capture_output=True, text=True, timeout=25)
        return f"STDOUT:\n{result.stdout}\nSTDERR:\n{result.stderr}"
    except Exception as e:
        return f"Execution failed: {e}"

# ==========================================
# 3. APEX BROWSER SNIPER PROTOCOL (CSP-BYPASS)
# ==========================================

@mcp.tool()
def list_active_windows(keyword: str = "") -> list[str]:
    """Lists titles of all currently open desktop windows, optionally filtered by keyword."""
    windows = gw.getAllWindows()
    titles = [w.title for w in windows if w.title.strip()]
    if keyword:
        titles = [t for t in titles if keyword.lower() in t.lower()]
    return titles

@mcp.tool()
def inject_browser_javascript(window_keyword: str, js_code: str) -> str:
    """
    Bypasses Content Security Policy (CSP) and devtools detachment by injecting raw JavaScript 
    directly into the target browser window via the URL bar (Ctrl+L -> javascript: -> Enter).
    """
    success = BrowserSniper.inject_js(window_keyword, js_code)
    if success:
        return f"Successfully injected and executed JavaScript in window matching '{window_keyword}'."
    return f"Failed to inject JavaScript: window matching '{window_keyword}' not found or unreachable."

@mcp.tool()
def eval_browser_javascript(window_keyword: str, js_function_or_expr: str, timeout: float = 2.0) -> str:
    """
    Executes JavaScript in the target browser and returns the evaluation result back to the AI 
    via a zero-latency clipboard bridge.
    """
    result = BrowserSniper.eval_js(window_keyword, js_function_or_expr, timeout=timeout)
    return json.dumps(result, indent=2)

# ==========================================
# 4. COGNITIVE ASSESSMENT & PROFILER SOLVERS
# ==========================================

@mcp.tool()
def solve_raven_apm(question_num: int) -> str:
    """
    Retrieves the verified mathematical/topological pattern solution and answer key 
    for Raven's Advanced Progressive Matrices (APM Set II) items 1 to 36.
    """
    sol = RavenMatrixSolver.get_solution(question_num)
    return json.dumps(sol, indent=2)

@mcp.tool()
def evaluate_competency(statement_text: str) -> str:
    """
    Analyzes a workplace behavioral statement, classifies it into a Learning Agility dimension, 
    and generates the optimal Likert rating (1-5) for high-performance enterprise assessment profiling.
    """
    dim = CompetencyProfiler.classify_statement(statement_text)
    score = CompetencyProfiler.score_statement(statement_text)
    return json.dumps({
        "statement": statement_text,
        "dimension": dim,
        "recommended_score": score
    }, indent=2)

@mcp.tool()
def solve_personality_item(question_num: int) -> str:
    """Returns optimal 5-point Likert response for Big Five 60-item Workplace Personality Inventory."""
    choice = PersonalityInventorySolver.get_recommended_choice(question_num)
    return json.dumps({"question_num": question_num, "recommended_choice": choice}, indent=2)

@mcp.tool()
def solve_retail_sjt(role: str, question_num: int) -> str:
    """
    Returns optimal decision and reasoning for Situational Judgement Tests.
    Role can be 'merchandising' or 'sales'.
    """
    if "merchandis" in role.lower():
        action = RetailSJTSolver.get_merchandising_action(question_num)
    else:
        action = RetailSJTSolver.get_sales_action(question_num)
    return json.dumps(action, indent=2)

@mcp.tool()
def solve_portrait_value(question_num: int) -> str:
    """Returns optimal 6-point PVQ score index and text for Schwartz Human Values items 1 to 57."""
    idx = PortraitValuesProfiler.get_score_index(question_num)
    text = PortraitValuesProfiler.get_option_text(question_num)
    return json.dumps({"question_num": question_num, "score_index": idx, "option_text": text}, indent=2)

if __name__ == "__main__":
    mcp.run(transport='stdio')
