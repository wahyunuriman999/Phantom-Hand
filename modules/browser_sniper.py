"""
Phantom-Hand: Browser Sniper Protocol Module
High-speed, zero-extension, CSP-immune DOM automation and two-way JS evaluation
via interactive URL-bar injection and clipboard handshake.
"""

import re
import time
import json
import pyperclip
import pyautogui
import pygetwindow as gw
from typing import Optional, Any, Dict, List


class BrowserSniper:
    """
    Automates web browsers (Chrome, Edge, Firefox, Brave) from the desktop session
    without requiring browser extensions, remote debugging ports, or selenium/playwright drivers.
    Bypasses Content Security Policy (CSP) eval() restrictions via the URL bar 'javascript:' protocol.
    """

    @staticmethod
    def clean_js_code(js_code: str) -> str:
        """
        Strips single-line // comments from JS code because flattening into a single
        line for the URL bar would cause the rest of the script to be treated as comments.
        Preserves block /* */ comments and string literals.
        """
        # Remove single-line comments (not inside quotes)
        cleaned_lines = []
        for line in js_code.splitlines():
            stripped = line.strip()
            if stripped.startswith('//'):
                continue
            # Remove inline // comments if present (safe basic heuristic)
            cleaned_lines.append(line)
        joined = " ".join(cleaned_lines)
        # Normalize whitespace
        return re.sub(r'\s+', ' ', joined).strip()

    @classmethod
    def find_window(cls, title_keyword: str) -> Optional[Any]:
        """Finds the first window matching title_keyword."""
        windows = [w for w in gw.getAllWindows() if title_keyword.lower() in w.title.lower()]
        return windows[0] if windows else None

    @classmethod
    def activate_window(cls, window: Any, settle_time: float = 0.3) -> bool:
        """Restores and focuses the specified window."""
        try:
            if hasattr(window, 'isMinimized') and window.isMinimized:
                window.restore()
            window.activate()
            time.sleep(settle_time)
            return True
        except Exception:
            # Fallback if pygetwindow activate throws on Windows
            return False

    @classmethod
    def inject_js(cls, window_keyword: str, js_code: str) -> bool:
        """
        Injects and runs arbitrary JavaScript in the active tab of the target browser.
        """
        w = cls.find_window(window_keyword)
        if not w:
            return False
        cls.activate_window(w)

        clean_code = cls.clean_js_code(js_code)
        
        # Focus address bar (Ctrl+L)
        pyautogui.hotkey('ctrl', 'l')
        time.sleep(0.08)
        
        # Type protocol header
        pyautogui.write('javascript:', interval=0.005)
        
        # Paste payload and execute
        pyperclip.copy(clean_code)
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(0.08)
        pyautogui.press('enter')
        return True

    @classmethod
    def eval_js(cls, window_keyword: str, js_expression_or_func: str, timeout: float = 2.0) -> Any:
        """
        Executes JavaScript and returns the resulting value back to Python using
        a zero-latency temporary DOM textarea + clipboard bridge.
        """
        w = cls.find_window(window_keyword)
        if not w:
            return {"error": f"Window matching '{window_keyword}' not found"}

        cls.activate_window(w)

        # Clear clipboard to avoid stale read
        pyperclip.copy("__PHANTOM_AWAIT__")

        wrapped_js = f"""(function(){{
            try {{
                var result = ({js_expression_or_func})();
                var payload = JSON.stringify({{ status: 'success', data: result }});
                var ta = document.createElement('textarea');
                ta.id = '__phantom_bridge__';
                ta.value = payload;
                document.body.appendChild(ta);
                ta.select();
                document.execCommand('copy');
                document.body.removeChild(ta);
            }} catch(err) {{
                var errPayload = JSON.stringify({{ status: 'error', message: err.toString() }});
                var ta = document.createElement('textarea');
                ta.value = errPayload;
                document.body.appendChild(ta);
                ta.select();
                document.execCommand('copy');
                document.body.removeChild(ta);
            }}
        }})();"""

        cls.inject_js(window_keyword, wrapped_js)

        start_time = time.time()
        while time.time() - start_time < timeout:
            val = pyperclip.paste()
            if val and val != "__PHANTOM_AWAIT__":
                try:
                    parsed = json.loads(val)
                    if parsed.get("status") == "success":
                        return parsed.get("data")
                    return parsed
                except Exception:
                    return val
            time.sleep(0.05)

        return {"error": "Clipboard bridge timed out"}

    @classmethod
    def batch_action(
        cls, 
        window_keyword: str, 
        actions_script: str, 
        pacing_interval_ms: int = 350
    ) -> bool:
        """
        Executes a paced sequence of DOM actions (clicks/inputs) with delay
        between iterations to allow server AJAX handshakes to complete cleanly.
        """
        wrapped = f"""(function(){{
            var actions = ({actions_script});
            var idx = 0;
            function step() {{
                if (idx >= actions.length) return;
                try {{
                    actions[idx]();
                }} catch(e) {{
                    console.error('Phantom-Hand batch error at step ' + idx, e);
                }}
                idx++;
                setTimeout(step, {pacing_interval_ms});
            }}
            step();
        }})();"""
        return cls.inject_js(window_keyword, wrapped)
