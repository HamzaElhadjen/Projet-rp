from rush_hour import RushHourPuzzle
from BFS import bfs
from a import astar, h1, h2, h3


def main():
    # 1. Create the puzzle
    puzzle = RushHourPuzzle(csv_file="examples/1.csv")

    print("Board size:", puzzle.board_height, "x", puzzle.board_width)
    puzzle.printBoard()
    print("Is goal state?", puzzle.isGoal())

    # 2. Run BFS to solve the puzzle
    solution_node = bfs(
        puzzle,
        RushHourPuzzle.successorFunction,
        RushHourPuzzle.isGoal
    )

    # 3. Print the sequence of boards and moves
    if solution_node:
        print("\nSolution found! Moves to solve the puzzle:")
        path = solution_node.getPath()
        actions = solution_node.getSolution()
        for i, state in enumerate(path):
            print(f"\nStep {i}:")
            state.printBoard()
            if i < len(actions):
                print(f" → {actions[i]}")
    else:
        print("No solution found.")

    # 4. Run A* with 3 heuristics (correct indentation ✅)
    print("\nRunning A* with h1...")
    solution_h1 = astar(puzzle, h1)
    if solution_h1:
        print(f"Solution found with h1 in {len(solution_h1.getSolution())} moves.")

    print("\nRunning A* with h2...")
    solution_h2 = astar(puzzle, h2)
    if solution_h2:
        print(f"Solution found with h2 in {len(solution_h2.getSolution())} moves.")

    print("\nRunning A* with h3...")
    solution_h3 = astar(puzzle, h3)
    if solution_h3:
        print(f"Solution found with h3 in {len(solution_h3.getSolution())} moves.")


if __name__ == "__main__":
    main()
