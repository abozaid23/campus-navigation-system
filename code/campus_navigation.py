"""
============================================================
 Nile University Campus Navigation System
 Course  : Discrete Mathematics — Spring 2026
 Project : Graph Representation + BFS Traversal
 Members : Yousef Nasser Abozaid
           Mostafa Yousif
============================================================

This program models the Nile University campus as a graph.
  - Buildings  →  Vertices (nodes)
  - Roads/paths →  Edges (connections)

We store the graph in THREE different ways so you can see
how each representation works in practice:
  1. Adjacency List  (a dictionary — our main data structure)
  2. Adjacency Matrix (a 2D list of 0s and 1s)
  3. Edge List        (a plain list of (A, B) pairs)

We also include BFS traversal to explore the campus from
any starting building.
"""

from collections import deque   # deque gives us an efficient queue for BFS


# ─────────────────────────────────────────────────────────
#  SECTION 1 — THE GRAPH DATA
#  We define our campus using an Adjacency List first.
#  It's the most natural format to work with in Python.
# ─────────────────────────────────────────────────────────

# Each key is a building (vertex).
# Each list contains the buildings directly connected to it (neighbors).
campus_map = {
    "Main Gate":           ["Library", "Engineering Building"],
    "Library":             ["Main Gate", "Student Center"],
    "Engineering Building":["Main Gate", "Computer Lab"],
    "Student Center":      ["Library", "Cafeteria"],
    "Computer Lab":        ["Engineering Building"],
    "Cafeteria":           ["Student Center"]
}

# We keep an ordered list of all building names.
# This is important for building the adjacency matrix — we need a fixed index for each vertex.
BUILDINGS = list(campus_map.keys())   # e.g. BUILDINGS[0] = "Main Gate", BUILDINGS[1] = "Library", ...


# ─────────────────────────────────────────────────────────
#  SECTION 2 — REPRESENTATION FUNCTIONS
#  These three functions show the SAME graph data in
#  three different formats.
# ─────────────────────────────────────────────────────────

def get_adjacency_list():
    """
    Returns the adjacency list (which is our campus_map dictionary).
    Format:  { vertex : [neighbor1, neighbor2, ...] }
    
    Best when: the graph is sparse (few edges relative to vertices),
               or when we need to quickly loop over a node's neighbors.
    """
    return campus_map   # We already have it — just return it!


def get_adjacency_matrix():
    """
    Builds and returns a 2D adjacency matrix.
    
    Size: N x N, where N = number of buildings.
    matrix[i][j] = 1 means building i is directly connected to building j.
    matrix[i][j] = 0 means NO direct connection.
    
    Because our graph is UNDIRECTED, the matrix is always symmetric:
    if matrix[i][j] == 1 then matrix[j][i] == 1 too.
    
    Best when: we need to quickly check if two specific nodes are connected
               (just look up matrix[i][j] — O(1) time).
    """
    n = len(BUILDINGS)

    # Start with an n×n grid of zeros
    matrix = [[0] * n for _ in range(n)]

    # Now fill in the 1s based on our adjacency list
    for building, neighbors in campus_map.items():
        i = BUILDINGS.index(building)       # row index for this building
        for neighbor in neighbors:
            j = BUILDINGS.index(neighbor)   # column index for the neighbor
            matrix[i][j] = 1               # mark the connection

    return matrix


def get_edge_list():
    """
    Builds and returns a list of all unique edges.
    Format:  [ (buildingA, buildingB), ... ]
    
    Because the graph is undirected, we only store each edge ONCE.
    We avoid duplicates by only recording an edge (A→B) when the index
    of A is less than the index of B.
    
    Best when: we need to iterate over all edges (e.g., for algorithms like Kruskal's MST).
    """
    edges = []

    for building, neighbors in campus_map.items():
        i = BUILDINGS.index(building)
        for neighbor in neighbors:
            j = BUILDINGS.index(neighbor)
            # Only add the edge if we haven't added its reverse already
            if i < j:
                edges.append((building, neighbor))

    return edges


# ─────────────────────────────────────────────────────────
#  SECTION 3 — DISPLAY FUNCTIONS
#  Pretty-print each representation to the terminal.
# ─────────────────────────────────────────────────────────

def display_adjacency_list():
    """Prints the adjacency list in a clean, readable format."""
    print("\n" + "="*50)
    print("  REPRESENTATION 1 — Adjacency List")
    print("="*50)
    print("  Format: Building  →  [Connected Buildings]\n")

    adj = get_adjacency_list()
    for building, neighbors in adj.items():
        connected_str = ", ".join(neighbors)
        print(f"  {building:<26} → [{connected_str}]")

    print("="*50 + "\n")


def display_adjacency_matrix():
    """Prints the adjacency matrix with building name labels on both axes."""
    print("\n" + "="*50)
    print("  REPRESENTATION 2 — Adjacency Matrix")
    print("="*50)
    print("  (1 = connected,  0 = not connected)\n")

    matrix = get_adjacency_matrix()
    n = len(BUILDINGS)

    # Print short labels for columns (we abbreviate to keep the table readable)
    short_labels = [b.split()[0][:4] for b in BUILDINGS]   # e.g. "Main", "Libr", "Engi" ...

    # Column headers
    header = "  {:<26}".format("") + "  ".join(f"{lbl:>4}" for lbl in short_labels)
    print(header)
    print("  " + "-" * (len(header) - 2))

    # Each row = one building's connections
    for i in range(n):
        row_label = f"  {BUILDINGS[i]:<26}"
        row_values = "  ".join(f"   {matrix[i][j]}" for j in range(n))
        print(row_label + row_values)

    print("="*50 + "\n")


def display_edge_list():
    """Prints every unique edge as a pair of building names."""
    print("\n" + "="*50)
    print("  REPRESENTATION 3 — Edge List")
    print("="*50)
    print("  Format: (Building A)  ──  (Building B)\n")

    edges = get_edge_list()
    for idx, (a, b) in enumerate(edges, start=1):
        print(f"  Edge {idx}: {a}  ──  {b}")

    print(f"\n  Total unique edges: {len(edges)}")
    print("="*50 + "\n")


def display_graph_statistics():
    """Shows a quick summary: how many vertices and edges the graph has."""
    num_vertices = len(BUILDINGS)

    # Count unique edges (same trick as get_edge_list)
    total_connections = sum(len(v) for v in campus_map.values())
    num_edges = total_connections // 2   # divide by 2 because each edge is listed twice

    print("\n" + "="*50)
    print("  GRAPH STATISTICS")
    print("="*50)
    print(f"  Total Buildings (Vertices) : {num_vertices}")
    print(f"  Total Paths     (Edges)    : {num_edges}")
    print(f"  Graph Type                 : Undirected, Unweighted")
    print("="*50 + "\n")


# ─────────────────────────────────────────────────────────
#  SECTION 4 — BFS TRAVERSAL
#  Breadth-First Search explores the graph level by level:
#    Level 0 → the starting building
#    Level 1 → all buildings one step away
#    Level 2 → all buildings two steps away
#    ... and so on until every reachable building is visited.
#
#  Data structure used: a QUEUE (first-in, first-out).
#  We use Python's deque from the collections module
#  because deque.popleft() is O(1), while list.pop(0) is O(n).
# ─────────────────────────────────────────────────────────

def bfs_traversal(start_location):
    """
    Performs BFS starting from start_location.
    Prints the order in which buildings are visited.
    
    How BFS works (step by step):
      1. Put the starting building in the queue and mark it visited.
      2. Take the building at the FRONT of the queue.
      3. Add all of its unvisited neighbors to the BACK of the queue.
      4. Mark each neighbor as visited so we don't visit it twice.
      5. Repeat steps 2-4 until the queue is empty.
    """
    print(f"\n" + "="*50)
    print(f"  BFS TRAVERSAL — Starting from: {start_location}")
    print("="*50)

    # Guard: make sure the starting location actually exists
    if start_location not in campus_map:
        print(f"  ERROR: '{start_location}' not found in the campus map.")
        print("="*50 + "\n")
        return

    visited      = set()                  # keeps track of where we've already been
    queue        = deque([start_location])# the BFS queue — starts with just the source
    visited.add(start_location)

    traversal_order = []   # we'll record the visit order here

    step = 0   # step counter, just so the output is educational

    while queue:
        step += 1
        current = queue.popleft()          # visit the building at the front
        traversal_order.append(current)

        print(f"\n  Step {step}: Visiting '{current}'")

        # Explore all direct connections from the current building
        neighbors_to_add = []
        for neighbor in campus_map[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                neighbors_to_add.append(neighbor)

        if neighbors_to_add:
            print(f"    → Adding to queue: {', '.join(neighbors_to_add)}")
        else:
            print(f"    → No new neighbors to add.")

    # Print the final traversal path
    print(f"\n  Full BFS Path: {' → '.join(traversal_order)}")
    print(f"  Total buildings visited: {len(traversal_order)}")
    print("="*50 + "\n")


# ─────────────────────────────────────────────────────────
#  SECTION 5 — CONVERSION: Adjacency List → Matrix
#  This is a required part of Project II.
#  We show explicitly how to take our adjacency list and
#  convert it into an adjacency matrix.
# ─────────────────────────────────────────────────────────

def demonstrate_conversion():
    """
    Demonstrates the conversion from Adjacency List to Adjacency Matrix.
    Shows the logic step by step so it's easy to follow.
    """
    print("\n" + "="*50)
    print("  CONVERSION: Adjacency List  →  Adjacency Matrix")
    print("="*50)
    print("\n  Step 1: Assign an index number to each building:")
    for idx, building in enumerate(BUILDINGS):
        print(f"    Index {idx}  →  {building}")

    print("\n  Step 2: For each edge in the adjacency list,")
    print("          set matrix[row][col] = 1 (and matrix[col][row] = 1):\n")

    edges = get_edge_list()
    for a, b in edges:
        i = BUILDINGS.index(a)
        j = BUILDINGS.index(b)
        print(f"    Edge ({a}  ──  {b})")
        print(f"         → matrix[{i}][{j}] = 1  and  matrix[{j}][{i}] = 1")

    print("\n  Step 3: The resulting matrix is shown in Representation 2 above.")
    print("="*50 + "\n")


# ─────────────────────────────────────────────────────────
#  SECTION 6 — SEARCH UTILITY
#  Simple helper that lets a user look up a building
#  by typing part of its name.
# ─────────────────────────────────────────────────────────

def search_location(search_term):
    """Finds any buildings whose name contains the search term (case-insensitive)."""
    print(f"\n--- Search Results for '{search_term}' ---")
    found = False

    for building in campus_map:
        if search_term.lower() in building.lower():
            connections = ", ".join(campus_map[building])
            print(f"  > Found: {building}")
            print(f"    Direct connections: {connections}")
            found = True

    if not found:
        print("  X No matching location found.")
    print("------------------------------------------\n")


# ─────────────────────────────────────────────────────────
#  SECTION 7 — MAIN MENU
#  Simple text-based menu to interact with the program.
# ─────────────────────────────────────────────────────────

def main():
    """Entry point — shows the interactive menu and handles user input."""
    while True:
        print("\n" + "="*50)
        print("  Nile University Campus Navigation System")
        print("  Graph Representation — Discrete Math 2026")
        print("="*50)
        print("  1. Display Adjacency List")
        print("  2. Display Adjacency Matrix")
        print("  3. Display Edge List")
        print("  4. Show Graph Statistics")
        print("  5. Run BFS Traversal")
        print("  6. Demonstrate List → Matrix Conversion")
        print("  7. Search for a Location")
        print("  8. Exit")
        print("="*50)

        choice = input("  Enter your choice (1-8): ").strip()

        if choice == '1':
            display_adjacency_list()

        elif choice == '2':
            display_adjacency_matrix()

        elif choice == '3':
            display_edge_list()

        elif choice == '4':
            display_graph_statistics()

        elif choice == '5':
            print("\n  Available buildings:")
            for b in BUILDINGS:
                print(f"    - {b}")
            start = input("\n  Enter the starting building for BFS: ").strip()

            # Match the user's input (case-insensitive) to the real building name
            matched = None
            for b in BUILDINGS:
                if start.lower() == b.lower():
                    matched = b
                    break

            if matched:
                bfs_traversal(matched)
            else:
                print("\n  X Building not found. Please check the spelling.")

        elif choice == '6':
            demonstrate_conversion()

        elif choice == '7':
            term = input("  Enter part of the building name to search: ").strip()
            search_location(term)

        elif choice == '8':
            print("\n  Thank you for using the Campus Navigation System. Goodbye!\n")
            break

        else:
            print("\n  X Invalid choice. Please enter a number between 1 and 8.")


# Run the program only when this file is executed directly
if __name__ == "__main__":
    main()
