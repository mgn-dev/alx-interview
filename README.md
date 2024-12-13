# ALX Interview — Technical Preparation

A curated collection of **11 algorithmic and systems challenges** designed to sharpen the problem-solving skills tested in technical interviews. Each challenge lives in its own directory with a reference implementation, main test driver, and focused README.

These problems span **Python**, **JavaScript**, and core computer-science topics: dynamic programming, graph traversal, backtracking, bit manipulation, HTTP APIs, and stream processing.

---

## Skills covered


- Translate ambiguous interview prompts into precise algorithm designs
- Choose appropriate data structures (arrays, graphs, stacks, hash maps) under time pressure
- Build solutions that handle edge cases and invalid input gracefully
- Analyze time and space complexity and articulate trade-offs verbally
- Work with standard libraries (`re`, `request`, `sys`) and external APIs
- Write clean, PEP 8–compliant Python and idiomatic Node.js

---

## Challenge Index

| # | Directory | Problem | Core Concepts | Language |
|---|-----------|---------|---------------|----------|
| 0 | [0x00-pascal_triangle](0x00-pascal_triangle/) | Generate Pascal's triangle to *n* rows | 2D arrays, combinatorics | Python |
| 1 | [0x01-lockboxes](0x01-lockboxes/) | Determine if all lockboxes can be opened | Graph reachability, BFS/stack | Python |
| 2 | [0x02-minimum_operations](0x02-minimum_operations/) | Minimum copy/paste ops to get *n* H characters | Number theory, prime factorization | Python |
| 3 | [0x03-log_parsing](0x03-log_parsing/) | Parse stdin log lines, aggregate stats | Regex, signal handling, streaming I/O | Python |
| 4 | [0x04-utf8_validation](0x04-utf8_validation/) | Validate a byte sequence as UTF-8 | Bit masking, encoding rules | Python |
| 5 | [0x05-nqueens](0x05-nqueens/) | Solve the N-Queens puzzle | Backtracking, constraint satisfaction | Python |
| 6 | [0x06-starwars_api](0x06-starwars_api/) | Print Star Wars film characters in order | HTTP requests, async recursion, JSON | JavaScript |
| 7 | [0x07-rotate_2d_matrix](0x07-rotate_2d_matrix/) | Rotate an *n×n* matrix 90° clockwise in-place | Matrix transpose, in-place algorithms | Python |
| 8 | [0x08-making_change](0x08-making_change/) | Fewest coins to make a target amount | Dynamic programming, coin change | Python |
| 9 | [0x09-island_perimeter](0x09-island_perimeter/) | Compute perimeter of a grid island | Grid traversal, adjacency counting | Python |
| 10 | [0x0A-primegame](0x0A-primegame/) | Determine winner of a prime-selection game | Game theory, sieve, optimal play | Python |

---

## Challenge Summaries

### 0x00. Pascal's Triangle

Implement `pascal_triangle(n)` returning the first *n* rows of Pascal's triangle. Each interior element is the sum of the two elements above it. Edge case: return `[]` when *n ≤ 0*.

**Skills:** Nested loops, list comprehensions, mathematical patterns.

---

### 0x01. Lockboxes

Given *n* boxes where box *i* contains keys to other boxes, determine whether every box can be opened starting from box 0 (which is unlocked). Model keys as edges in a directed graph and check reachability.

**Skills:** Graph modeling, stack-based DFS, boolean tracking arrays.

---

### 0x02. Minimum Operations

Starting with a file containing one `H`, you may only **Copy All** then **Paste**. Find the minimum operations to produce exactly *n* `H` characters. The optimal strategy relates to the prime factorization of *n*.

**Skills:** Divisor iteration, greedy decomposition, O(√n) analysis.

---

### 0x03. Log Parsing

Read Apache-style log lines from **stdin** in real time. Every 10 lines (and on `SIGINT`), print total transferred size and counts per HTTP status code (200, 301, 400, 401, 403, 404, 405, 500). Uses regex to parse each line.

**Skills:** Regular expressions, signal handlers, incremental aggregation, Unix pipelines.

```bash
./0-generator.py | ./0-stats.py
```

---

### 0x04. UTF-8 Validation

Given a list of integers representing bytes, return `True` if they form a valid UTF-8 encoding. Handle 1-byte ASCII, 2-byte, 3-byte, and 4-byte sequences using bit-level checks.

**Skills:** Bitwise operations, state machine over byte sequences.

---

### 0x05. N Queens

Place *N* non-attacking queens on an *N×N* board. Print every solution as a list of `[row, column]` coordinates. *N* must be an integer ≥ 4.

**Skills:** Backtracking, diagonal/column conflict detection, recursion.

---

### 0x06. Star Wars API

Node.js script that accepts a Star Wars film ID, fetches the film from the SWAPI-compatible endpoint, then retrieves and prints each character's name **in the order listed** in the film response.

**Skills:** HTTP with `request`, nested async callbacks, JSON parsing, CLI arguments.

```bash
./0-starwars_characters.js 3
```

---

### 0x07. Rotate 2D Matrix

Rotate an *n×n* integer matrix 90 degrees clockwise **in place** (no return value). Achieve this with transpose + row reversal.

**Skills:** In-place matrix manipulation, index swapping.

---

### 0x08. Making Change

Given coin denominations and a target total, return the minimum number of coins needed, or `-1` if impossible. Classic bottom-up dynamic programming.

**Skills:** DP table construction, unreachable-state handling.

---

### 0x09. Island Perimeter

Given a 2D grid of `0` (water) and `1` (land), compute the perimeter of the single island. Count exposed edges; no lakes inside the island.

**Skills:** Grid iteration, boundary detection, adjacency logic.

---

### 0x0A. Prime Game

Maria and Ben alternate removing a prime and all its multiples from a set `{1, …, x}` across multiple rounds. Both play optimally; Maria goes first. Return the overall winner (`"Maria"`, `"Ben"`, or `None` on tie).

**Skills:** Prime sieving, combinatorial game theory, simulation.

---

## How to Run

Each challenge directory is self-contained:

```bash
# Python challenges
cd 0x00-pascal_triangle
python3 0-main.py

# JavaScript challenge
cd 0x06-starwars_api
./0-starwars_characters.js 1
```

Most Python tasks include a `*-main.py` driver that imports and exercises the solution function with predefined test cases matching the ALX checker format.

---

## Recommended Study Order

1. **Warm-up** — Pascal's Triangle, Rotate 2D Matrix, Island Perimeter
2. **Core algorithms** — Lockboxes, Minimum Operations, Making Change, N Queens
3. **Systems & I/O** — Log Parsing, UTF-8 Validation, Star Wars API
4. **Advanced** — Prime Game (combines number theory and game theory)

---

## Environment

| Tool | Version |
|------|---------|
| Python | 3.x |
| Node.js | For `0x06-starwars_api` |
| `request` npm module | Star Wars API challenge |

No external dependencies are required for the Python-only challenges beyond the standard library.

---

## License

Public domain.
