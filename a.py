#init  code =Node (init - state )
# init-codeset F (1)
#OPEN = PriorityQueue ()
#Closed=[]
#while (open is not null)
#    current = open.pop(F_min)
#    Fcurrent.state is goal ()=return current
#    Closed.add(current)
#for ( action,succ_state) in current.stqte.succfet()
#   child = Node (succ_state;current , action)
#child.setF()
#if  child.state not  in  Open qnd  not in Closed 
#   Open.add(child)
#elif child.stqte in  open 
#   child f < n*f
#elif child.state in Closed 
#   child f < n*f 
#   remove n from closed
#   add child  to  open 

import heapq
from node import Node

# ==========================
#      HEURISTICS
# ==========================

def h1(state):
    """Distance from the red car X to the exit."""
    red = next(v for v in state.vehicles if v["id"] == "X")
    distance = state.board_width - (red["col"] + red["length"])
    return distance


def h2(state):
    """h1 + number of vehicles blocking the exit path."""
    red = next(v for v in state.vehicles if v["id"] == "X")
    y = red["row"]
    blocking = 0
    for x in range(red["col"] + red["length"], state.board_width):
        if state.board[y][x] != " ":
            blocking += 1
    return h1(state) + blocking


def h3(state):
    """
    Improved heuristic: h2 + penalty for blocking vehicles that are themselves blocked.
    This encourages moving vehicles that can actually be freed.
    """
    red = next(v for v in state.vehicles if v["id"] == "X")
    y = red["row"]
    blocking = 0
    penalty = 0
    for x in range(red["col"] + red["length"], state.board_width):
        cell = state.board[y][x]
        if cell != " ":
            blocking += 1
            vehicle = next(v for v in state.vehicles if v["id"] == cell)
            # check if that vehicle can move at all
            if not can_vehicle_move(state, vehicle):
                penalty += 1
    return h1(state) + blocking + penalty


def can_vehicle_move(state, vehicle):
    """Check if a vehicle has any free space to move."""
    r, c = vehicle["row"], vehicle["col"]
    length, orient = vehicle["length"], vehicle["orientation"]

    if orient == "H":
        # left
        if c - 1 >= 0 and state.board[r][c - 1] == " ":
            return True
        # right
        if c + length < state.board_width and state.board[r][c + length] == " ":
            return True
    else:
        # up
        if r - 1 >= 0 and state.board[r - 1][c] == " ":
            return True
        # down
        if r + length < state.board_height and state.board[r + length][c] == " ":
            return True
    return False

# ==========================
#        A* SEARCH
# ==========================

def astar(initial_state, heuristic):
    """
    Generic A* search.
    heuristic: one of h1, h2, h3
    """
    start_node = Node(initial_state, None, None, 0)
    start_node.setF(heuristic)
    
    open_list = []
    heapq.heappush(open_list, (start_node.f, start_node))
    visited = set()
    visited.add(initial_state.getStateKey())

    while open_list:
        _, current_node = heapq.heappop(open_list)
        current_state = current_node.state

        if current_state.isGoal():
            return current_node

        for action, successor in current_state.successorFunction():
            key = successor.getStateKey()
            if key in visited:
                continue
            visited.add(key)
            new_node = Node(successor, current_node, action, current_node.g + 1)
            new_node.setF(heuristic)
            heapq.heappush(open_list, (new_node.f, new_node))

    return None
