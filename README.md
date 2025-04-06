# 🧠 mcp_server-client_EAG-S-4 - Local Setup

This repository provides a minimal implementation to set up and interact with the **MCP (Modular Computation Protocol)** locally. It consists of a **server** that exposes various computational tools and a **client** that communicates with the server to invoke those tools.

The project is managed using [`uv`](https://github.com/astral-sh/uv), a fast Python package manager and workflow tool.

---

## 📂 Project Structure

- `mcp_server.py` — Hosts the MCP server with 28 tools available for interaction.
- `mcp_client.py` — The entry point of the project; runs a client that connects to the MCP server and calls its tools.

---

## 🛠️ Available Tools on the MCP Server

### 🔢 Math Tools

1. `add(a, b)` — Add two numbers  
2. `add_list(l)` — Add all numbers in a list  
3. `subtract(a, b)` — Subtract two numbers  
4. `multiply(a, b)` — Multiply two numbers  
5. `divide(a, b)` — Divide two numbers  
6. `power(a, b)` — Raise a to the power of b  
7. `sqrt(a)` — Square root  
8. `cbrt(a)` — Cube root  
9. `factorial(a)` — Factorial  
10. `log(a)` — Natural logarithm  
11. `remainder(a, b)` — Modulus operation  
12. `sin(a)` — Sine  
13. `cos(a)` — Cosine  
14. `tan(a)` — Tangent  
15. `mine(a, b)` — Special mining tool  
16. `int_list_to_exponential_sum(int_list)` — Sum of exponentials of integers  
17. `fibonacci_numbers(n)` — First n Fibonacci numbers  

### 🧠 String/Image Tools

18. `strings_to_chars_to_int(string)` — Convert characters to ASCII  
19. `create_thumbnail(image_path)` — Generate a thumbnail from an image  

### 🖌️ Pinta Automation Tools

20. `open_pinta_application()` — Launch and focus Pinta  
21. `select_rectangle_tool()`  
22. `select_text_tool()`  
23. `select_circle_tool()`  
24. `draw_rectangle(x1, y1, x2, y2)`  
25. `write_text_inside_rectangle(text, x1, y1, x2, y2)`  
26. `draw_circle(x1, y1, radius)`  
27. `get_lines_of_rectangle(x1, y1, x2, y2)` — Return lines from rectangle coordinates  
28. `get_midpoint_of_line(x1, y1, x2, y2)` — Return midpoint of a line  

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/mcp-protocol.git
cd mcp-protocol
```

### 2. Install `uv` (if not already installed)

```bash
curl -Ls https://astral.sh/uv/install.sh | sh
```

Verify installation:

```bash
uv --version
```

### 3. Set Up the Project Environment

```bash
uv venv
source .venv/bin/activate  # or .venv\Scripts\activate on Windows
uv pip install -r pyproject.toml
```

> If `requirements.txt` doesn't exist:
> 
> ```bash
> uv pip freeze > requirements.txt
> ```

### 4. Test MCP Server with GUI client

```bash
mcp dev mcp_server.py
```

### 5. Run the Client

```bash
python mcp_client.py
```

---

## 📌 Notes

- Ensure **Pinta** is installed if you're using Pinta-related tools.
- Image tools like `create_thumbnail` require valid image paths.
- `mcp_client.py` is the main entry point to interact with the protocol.

---

## 📄 License

MIT License. Feel free to fork, modify, and contribute.

---

## 🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first.
