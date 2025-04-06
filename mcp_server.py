# basic import 
from mcp.server.fastmcp import FastMCP, Image
from mcp.server.fastmcp.prompts import base
from mcp.types import TextContent
from mcp import types
from PIL import Image as PILImage
import math
import sys
import time
import subprocess
import os
os.environ['DISPLAY'] = ':1'
#os.environ['XAUTHORITY']='/run/user/1000/gdm/Xauthority'
import pyautogui

# instantiate an MCP server client
mcp = FastMCP("Calculator")

# DEFINE TOOLS

#addition tool
@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    print("CALLED: add(a: int, b: int) -> int:")
    return int(a + b)

@mcp.tool()
def add_list(l: list) -> int:
    """Add all numbers in a list"""
    print("CALLED: add(l: list) -> int:")
    return sum(l)

# subtraction tool
@mcp.tool()
def subtract(a: int, b: int) -> int:
    """Subtract two numbers"""
    print("CALLED: subtract(a: int, b: int) -> int:")
    return int(a - b)

# multiplication tool
@mcp.tool()
def multiply(a: int, b: int) -> int:
    """Multiply two numbers"""
    print("CALLED: multiply(a: int, b: int) -> int:")
    return int(a * b)

#  division tool
@mcp.tool() 
def divide(a: int, b: int) -> float:
    """Divide two numbers"""
    print("CALLED: divide(a: int, b: int) -> float:")
    return float(a / b)

# power tool
@mcp.tool()
def power(a: int, b: int) -> int:
    """Power of two numbers"""
    print("CALLED: power(a: int, b: int) -> int:")
    return int(a ** b)

# square root tool
@mcp.tool()
def sqrt(a: int) -> float:
    """Square root of a number"""
    print("CALLED: sqrt(a: int) -> float:")
    return float(a ** 0.5)

# cube root tool
@mcp.tool()
def cbrt(a: int) -> float:
    """Cube root of a number"""
    print("CALLED: cbrt(a: int) -> float:")
    return float(a ** (1/3))

# factorial tool
@mcp.tool()
def factorial(a: int) -> int:
    """factorial of a number"""
    print("CALLED: factorial(a: int) -> int:")
    return int(math.factorial(a))

# log tool
@mcp.tool()
def log(a: int) -> float:
    """log of a number"""
    print("CALLED: log(a: int) -> float:")
    return float(math.log(a))

# remainder tool
@mcp.tool()
def remainder(a: int, b: int) -> int:
    """remainder of two numbers divison"""
    print("CALLED: remainder(a: int, b: int) -> int:")
    return int(a % b)

# sin tool
@mcp.tool()
def sin(a: int) -> float:
    """sin of a number"""
    print("CALLED: sin(a: int) -> float:")
    return float(math.sin(a))

# cos tool
@mcp.tool()
def cos(a: int) -> float:
    """cos of a number"""
    print("CALLED: cos(a: int) -> float:")
    return float(math.cos(a))

# tan tool
@mcp.tool()
def tan(a: int) -> float:
    """tan of a number"""
    print("CALLED: tan(a: int) -> float:")
    return float(math.tan(a))

# mine tool
@mcp.tool()
def mine(a: int, b: int) -> int:
    """special mining tool"""
    print("CALLED: mine(a: int, b: int) -> int:")
    return int(a - b - b)

@mcp.tool()
def create_thumbnail(image_path: str) -> Image:
    """Create a thumbnail from an image"""
    print("CALLED: create_thumbnail(image_path: str) -> Image:")
    img = PILImage.open(image_path)
    img.thumbnail((100, 100))
    return Image(data=img.tobytes(), format="png")

@mcp.tool()
def strings_to_chars_to_int(string: str) -> list[int]:
    """Return the ASCII values of the characters in a word"""
    print("CALLED: strings_to_chars_to_int(string: str) -> list[int]:")
    return [int(ord(char)) for char in string]

@mcp.tool()
def int_list_to_exponential_sum(int_list: list) -> float:
    """Return sum of exponentials of numbers in a list"""
    print("CALLED: int_list_to_exponential_sum(int_list: list) -> float:")
    return sum(math.exp(i) for i in int_list)

@mcp.tool()
def fibonacci_numbers(n: int) -> list:
    """Return the first n Fibonacci Numbers"""
    print("CALLED: fibonacci_numbers(n: int) -> list:")
    if n <= 0:
        return []
    fib_sequence = [0, 1]
    for _ in range(2, n):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence[:n]

# open pinta application
@mcp.tool()
def open_pinta_application() -> bool:
    """Launch Pinta and bring it to the foreground"""
    print("CALLED: open_and_focus_pinta() -> bool")
    try:
        subprocess.Popen(['pinta'])
        time.sleep(3)
        pinta_toolbar_position = (33, 403)  # Adjust if needed
        pyautogui.moveTo(*pinta_toolbar_position, duration=0.5)
        pyautogui.click()
        print("[LOG] Pinta opened and brought to front.")
        return True
    except Exception as e:
        print(f"[ERROR] Failed to open or focus Pinta: {e}")
        return False

# select rectangle tool in pinta
@mcp.tool()
def select_rectangle_tool() -> bool:
    """Select the Rectangle Tool in Pinta"""
    print("CALLED: select_rectangle_tool() -> bool")
    try:
        rectangle_tool_position = (93, 751)
        pyautogui.moveTo(*rectangle_tool_position, duration=0.5)
        pyautogui.click()
        time.sleep(0.5)
        print("[LOG] Rectangle Tool selected.")
        return True
    except Exception as e:
        print(f"[ERROR] Failed to select Rectangle Tool: {e}")
        return False

# select text tool in pinta
@mcp.tool()
def select_text_tool() -> bool:
    """Select the Text Tool in Pinta"""
    print("CALLED: select_text_tool() -> bool")
    try:
        text_tool_position = (94, 681)
        pyautogui.moveTo(*text_tool_position, duration=0.5)
        pyautogui.click()
        time.sleep(0.5)
        print("[LOG] Text Tool selected.")
        return True
    except Exception as e:
        print(f"[ERROR] Failed to select Text Tool: {e}")
        return False
        
# select circle tool in pinta
@mcp.tool()
def select_circle_tool() -> bool:
    """Select the Circle Tool in Pinta"""
    print("CALLED: select_circle_tool() -> bool")
    try:
        text_tool_position = (92, 829)
        pyautogui.moveTo(*text_tool_position, duration=0.5)
        pyautogui.click()
        time.sleep(0.5)
        print("[LOG] Circle Tool selected.")
        return True
    except Exception as e:
        print(f"[ERROR] Failed to select Circle Tool: {e}")
        return False

# draw rectangle using coordinates
@mcp.tool()
def draw_rectangle(x1: int, y1: int, x2: int, y2: int) -> bool:
    """Draw a rectangle from (x1, y1) to (x2, y2)"""
    print("CALLED: draw_rectangle(x1: int, y1: int, x2: int, y2: int) -> bool")
    try:
        pyautogui.moveTo(x1, y1, duration=0.5)
        pyautogui.mouseDown()
        pyautogui.moveTo(x2, y2, duration=0.5)
        pyautogui.mouseUp()
        print(f"[LOG] Rectangle drawn from ({x1}, {y1}) to ({x2}, {y2}).")
        return True
    except Exception as e:
        print(f"[ERROR] Failed to draw rectangle: {e}")
        return False

# write text inside a rectangle
@mcp.tool()
def write_text_inside_rectangle(text: str, x1: int, y1: int, x2: int, y2: int) -> bool:
    """Write text at the center of a rectangle defined by (x1, y1) and (x2, y2)"""
    print("CALLED: write_text_inside_rectangle(text: str, x1: int, y1: int, x2: int, y2: int) -> bool")
    try:
        center_x = (x1 + x2) // 2
        center_y = (y1 + y2) // 2
        pyautogui.moveTo(center_x, center_y, duration=0.5)
        pyautogui.click()
        pyautogui.typewrite(text, interval=0.1)
        print(f'[LOG] Text "{text}" written at center of rectangle.')
        return True
    except Exception as e:
        print(f"[ERROR] Failed to write text '{text}': {e}")
        return False
        
# draw circle using coordinates
@mcp.tool()
def draw_circle(x1: int, y1: int, radius: int) -> bool:
    """Draw a circle with center x1,y1 coordinate and radius"""
    print("CALLED: draw_circle(x1: int, y1: int, radius: int) -> bool")
    try:
        x1 = x1 - radius
        y1 = y1 + radius
        x2 = x1 + 2*radius
        y2 = y1 - 2*radius
        pyautogui.moveTo(x1, y1, duration=0.5)
        pyautogui.mouseDown()
        pyautogui.moveTo(x2, y2, duration=0.5)
        pyautogui.mouseUp()
        print(f"[LOG] circle drawn from ({x1}, {y1}) to ({x2}, {y2}).")
        return True
    except Exception as e:
        print(f"[ERROR] Failed to draw circle: {e}")
        return False
        
# get lines of rectangle
@mcp.tool()
def get_lines_of_rectangle(x1: int, y1: int, x2: int, y2: int) -> dict:
    """Get coordinates of 4 lines of a rectangle given rectangle coordinates as (x1,y1) (x1,y2)"""
    print("CALLED: get_lines_of_rectangle(x1: int, y1: int, x2: int, y2: int) -> dict")
    try:
        lines = {
        "left_line":   {"x1": x1, "y1": y1, "x2": x1, "y2": y2},
        "top_line":    {"x1": x1, "y1": y1, "x2": x2, "y2": y1},
        "right_line":  {"x1": x2, "y1": y1, "x2": x2, "y2": y2},
        "bottom_line": {"x1": x1, "y1": y2, "x2": x2, "y2": y2},
        }
        print(f"[LOG] Lines extracted from rectangle ({x1}, {y1}) to ({x2}, {y2}) are {lines}.")
        return lines
    except Exception as e:
        print(f"[ERROR] Failed to draw rectangle: {e}")
        return {}

# get mid point of line
@mcp.tool()
def get_midpoint_of_line(x1: int, y1: int, x2: int, y2: int) -> dict:
    """Get (x,y) coordinates of midpoint of a line given line coordinate as x1,y1,x2,y2"""
    print("CALLED: get_midpoint_of_line(x1: int, y1: int, x2: int, y2: int) -> dict)")
    try:
        x = (x1+x2) // 2
        y = (y1+y2) // 2

        return {"x":x, "y":y}
    except Exception as e:
        print(f"[ERROR] Failed to draw rectangle: {e}")
        return {}


# DEFINE RESOURCES

# Add a dynamic greeting resource
@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    print("CALLED: get_greeting(name: str) -> str:")
    return f"Hello, {name}!"


# DEFINE AVAILABLE PROMPTS
@mcp.prompt()
def review_code(code: str) -> str:
    return f"Please review this code:\n\n{code}"
    print("CALLED: review_code(code: str) -> str:")


@mcp.prompt()
def debug_error(error: str) -> list[base.Message]:
    return [
        base.UserMessage("I'm seeing this error:"),
        base.UserMessage(error),
        base.AssistantMessage("I'll help debug that. What have you tried so far?"),
    ]

if __name__ == "__main__":
    # Check if running with mcp dev command
    print("STARTING")
    if len(sys.argv) > 1 and sys.argv[1] == "dev":
        mcp.run()  # Run without transport for dev server
    else:
        mcp.run(transport="stdio")  # Run with stdio for direct execution
