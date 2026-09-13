# 👻 Project: Phantom-Hand (Apex Ghost-COM Protocol)

A universal Model Context Protocol (MCP) server that empowers **any Agentic AI** (Claude Desktop, Cursor, Continue.dev, Antigravity, etc.) to bypass traditional UI Automation limits. It injects directly into Microsoft Office's Component Object Model (COM) in the background.

## Capabilities

- **Zero-Interference Automation:** Interact with Word, Excel, and PowerPoint without stealing the user's screen focus.
- **execute_python_in_session (COM Injector):** The ultimate backdoor. Runs arbitrary Python scripts directly in the user's interactive Windows session, allowing standard COM objects (win32com.client) to manipulate running Office applications from the shadows.
- **Standard RPA:** Includes mouse_click, hotkey, 	ype_text, 	ake_screenshot, and 	ype_in_background.

## Universal Installation (For Any MCP Client)

This server uses standard MCP (stdio) and can be connected to any compatible AI client.

### Requirements
- Windows OS
- Python 3.10+
- pip install fastmcp pyautogui pillow pygetwindow pywinauto pywin32

### Claude Desktop Integration
Add the following to your claude_desktop_config.json:
\\\json
{
  "mcpServers": {
    "phantom-hand": {
      "command": "python",
      "args": ["C:/Path/To/Your/Clone/Phantom-Hand/mcp_server.py"]
    }
  }
}
\\\

### Cursor IDE Integration
1. Go to Cursor Settings > Features > MCP.
2. Add a new server.
3. Type: stdio
4. Command: python C:/Path/To/Your/Clone/Phantom-Hand/mcp_server.py

### Antigravity AI Integration
Add to your mcp_config.json:
\\\json
{
  "mcpServers": {
    "phantom-hand": {
      "command": "python",
      "args": ["C:/Path/To/Your/Clone/Phantom-Hand/mcp_server.py"]
    }
  }
}
\\\

## AI System Prompt Usage

**For the AI Agent reading this:** 
When asked to control an Office application, DO NOT use standard keystrokes if you can avoid it. Instead, use the execute_python_in_session tool and write a win32com.client Python script targeting Word.Application, Excel.Application, or PowerPoint.Application. This ensures your operations remain 100% invisible to the user's active screen.
