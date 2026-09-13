# 👻 Project: Phantom-Hand (Apex Ghost-COM Protocol)

An advanced Model Context Protocol (MCP) server for Agentic AI (like Antigravity) that bypasses traditional UI Automation limits by injecting directly into Microsoft Office's Component Object Model (COM) in the background.

## Capabilities

- **Zero-Interference Automation:** Interact with Word, Excel, and PowerPoint without stealing the user's screen focus.
- **	ype_in_background (UIA):** Send keystrokes to background windows.
- **execute_python_in_session (COM Injector):** The ultimate backdoor. Runs arbitrary Python scripts directly in the user's interactive Windows session, allowing standard COM objects (win32com.client) to manipulate running Office applications from the shadows.
- **Standard RPA:** Includes mouse_click, hotkey, 	ype_text, 	ake_screenshot.

## Installation for Antigravity AI

1. Place mcp_server.py in your Antigravity skills folder (e.g., ~/.gemini/config/skills/phantom-hand/mcp_server.py)
2. Add the following to your mcp_config.json:
\\\json
{
  "mcpServers": {
    "phantom-hand": {
      "command": "python",
      "args": ["C:/Users/YOUR_USER/.gemini/config/skills/phantom-hand/mcp_server.py"]
    }
  }
}
\\\
3. Reload Antigravity.

## Usage

When prompted to control an Office app, instruct your AI to use the \execute_python_in_session\ tool with a \win32com.client\ script targeting \Word.Application\, \Excel.Application\, or \PowerPoint.Application\.
