from collections import deque

# Function to check if a state is valid or not
def is_valid(state, capacities):
    return state[0] >= 0 and state[1] >= 0 and state[0] <= capacities[0] and state[1] <= capacities[1]

# Function to solve the water jug problem using BFS
def water_jug_bfs(initial_state, target, capacities):
    visited = set()  # To keep track of visited states
    queue = deque([(initial_state, [])])  # Queue for BFS, with each element being (state, path)

    while queue:
        state, path = queue.popleft()
        if state == target:
            return path + [target]  # If target state is reached, return the path

        visited.add(state)

        # Generate next possible states
        next_states = [
            ((0, state[1]), "Empty Jug 1"),
            ((state[0], 0), "Empty Jug 2"),
            ((capacities[0], state[1]), "Fill Jug 1"),
            ((state[0], capacities[1]), "Fill Jug 2"),
            ((min(state[0] + state[1], capacities[0]), max(0, state[0] + state[1] - capacities[0])), "Pour Jug 2 to Jug 1"),
            ((max(0, state[0] + state[1] - capacities[1]), min(state[0] + state[1], capacities[1])), "Pour Jug 1 to Jug 2")
        ]

        for next_state, action in next_states:
            if next_state not in visited and is_valid(next_state, capacities):
                queue.append((next_state, path + [action]))

    return None  # If no solution is found

# Example usage
initial_state = (0, 0)
target_state = (2, 0)  # Target state: Jug 1 contains 2 liters, Jug 2 contains 0 liters
jug_capacities = (4, 3)  # Capacities of Jug 1 and Jug 2

solution = water_jug_bfs(initial_state, target_state, jug_capacities)
if solution:
    print("Solution found:")
    for step, action in enumerate(solution):
        print(f"Step {step + 1}: {action}")
else:
    print("No solution found.")
