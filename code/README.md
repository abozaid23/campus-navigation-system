# Nile University Campus Navigation System

## Project Title
Graph Representation & BFS Traversal — Campus Navigation System

## Description
This project models the Nile University campus as an **undirected, unweighted graph** and demonstrates three standard graph representation techniques:

1. **Adjacency List** — A Python dictionary where each building maps to its list of direct neighbors. This is the primary data structure used throughout the program.
2. **Adjacency Matrix** — A 2D grid (N × N) where a cell value of `1` means two buildings are directly connected. Allows O(1) edge lookup.
3. **Edge List** — A plain list of `(Building A, Building B)` pairs representing every unique path in the campus.

The program also demonstrates the **conversion from Adjacency List to Adjacency Matrix** step by step, and includes a **Breadth-First Search (BFS)** traversal that explores the campus level-by-level from any starting building.

### Campus Graph
```
Main Gate ── Library ── Student Center ── Cafeteria
    │
Engineering Building ── Computer Lab
```

**Vertices (Buildings):** 6  
**Edges (Paths):** 5  
**Graph Type:** Undirected, Unweighted

## Tools Used
- **Language:** Python 3
- **Standard Library:** `collections.deque` (for the BFS queue)
- **No external packages required**

## How to Run Your Code

### Requirements
- Python 3.6 or later installed on your machine.
- No additional packages need to be installed.

### Steps
1. Download or copy the file `campus_navigation.py` to your computer.
2. Open a terminal (Command Prompt on Windows, Terminal on Mac/Linux).
3. Navigate to the folder containing the file:
   ```bash
   cd path/to/your/folder
   ```
4. Run the program:
   ```bash
   python campus_navigation.py
   ```
5. Use the numbered menu (1–8) to explore all features.

### Menu Options
| Option | Feature |
|--------|---------|
| 1 | Display Adjacency List |
| 2 | Display Adjacency Matrix |
| 3 | Display Edge List |
| 4 | Show Graph Statistics |
| 5 | Run BFS Traversal (choose a starting building) |
| 6 | Step-by-step List → Matrix Conversion demo |
| 7 | Search for a building by name |
| 8 | Exit |

## Members
- Yousef Nasser Abozaid — 241002067
- Mostafa Yousif — 241001668

## Course
Discrete Mathematics — Spring 2026 | Nile University
