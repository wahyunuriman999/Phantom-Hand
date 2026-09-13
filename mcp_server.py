import os
import tempfile
import subprocess
from fastmcp import FastMCP
import pyautogui
from PIL import ImageGrab
import pygetwindow as gw
from pywinauto import Application

mcp = FastMCP("ComputerControl")

@mcp.tool()
def get_screen_size() -> str:
    width, height = pyautogui.size()
    return f"Screen size: {width}x{height}"

@mcp.tool()
def take_screenshot() -> str:
    img = ImageGrab.grab()
    fd, path = tempfile.mkstemp(suffix=".png")
    os.close(fd)
    img.save(path)
    return f"Screenshot saved to: {path}. Use the view_file tool on this path to see it."

@mcp.tool()
def mouse_click(x: int, y: int, button: str = "left", clicks: int = 1) -> str:
    pyautogui.click(x=x, y=y, button=button, clicks=clicks)
    return f"Clicked {button} button at ({x}, {y}) {clicks} time(s)."

@mcp.tool()
def type_text(text: str, interval: float = 0.0) -> str:
    pyautogui.write(text, interval=interval)
    return f"Typed text: '{text}'"

@mcp.tool()
def press_key(key: str) -> str:
    pyautogui.press(key)
    return f"Pressed key: '{key}'"

@mcp.tool()
def hotkey(keys: list[str]) -> str:
    pyautogui.hotkey(*keys)
    return f"Pressed hotkey combination: {keys}"

@mcp.tool()
def type_in_background(title_keyword: str, text: str) -> str:
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
        result = subprocess.run(["python", path], capture_output=True, text=True, timeout=15)
        return f"STDOUT:\n{result.stdout}\nSTDERR:\n{result.stderr}"
    except Exception as e:
        return f"Execution failed: {e}"

if __name__ == "__main__":
    mcp.run(transport='stdio')
