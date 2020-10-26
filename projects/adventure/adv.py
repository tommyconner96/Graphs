from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()
# NOTE delete if not used may need later:
# BFS uses queue - FIFO
class Queue():
    def __init__(self):
        self.queue = []
    def enqueue(self, value):
        self.queue.append(value)
    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None
            
    def size(self):
        return len(self.queue)


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)
# this will be used for our return path
opposite_directions = { "n": "s", "s": "n", "w": "e", "e": "w" }
# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []
# return path
return_path = []
visited = set()
# boolean for if all rooms have been traversed. this will end the while loop
# traversal_done = False
player_room_graph = {}

def add_room(room_id, exit_options, last_room_direction, last_room):
    player_room_graph[room_id] = {}
    for option in exit_options:
        if option != last_room_direction:
            player_room_graph[room_id][option] = "?"
        else:
            player_room_graph[room_id][option] = last_room

# add room to graph
add_room(player.current_room.id, player.current_room.get_exits(), None, None)

# traversal loop willl continue until all rooms have been visited and traversal_done is marked True
# while traversal_done is not True:
# UPDATE: we can just check it this way, no need for the boolean
# this also saves 14 moves
while len(visited) < 500:
    room_id = player.current_room.id
    exits = player.current_room.get_exits()
    moves = []
    print(f"room: {room_id}, exits: {exits}")
    print(len(visited))
    for exit_option in exits:
    # find the path to the shortest unexplored room by using 
    # a breadth-first search for a room with a `'?'` for an exit.
        if player_room_graph[room_id][exit_option] == "?":
            moves.append(exit_option)
    
    if len(moves) == 0:
        # out of unexplored/? exit options so lets go back, if possible
        if len(return_path) > 0:
            move = return_path.pop(-1)
            print(f" move: {move} (been here before)")
            traversal_path.append(move)
            player.travel(move)
            # if we are in the starting room, the return path is empty
            if player.current_room.id == world.starting_room:
                return_path = []
        
        else:
            # once we get to this point, we traversed all possible rooms
            # and are back at the starting room
            # so lets end the while loop
            # traversal_done = True
            print(visited)
            break

    else:
        # the next move in queue
        move = moves[0]
        print(f"move: {move}")
        # add it to our travershal path
        traversal_path.append(move)
        # adding the inverse to our return path so we can get back
        return_path.append(opposite_directions[move])
        # move it move it
        player.travel(move)
        # defining out new room
        new_room = player.current_room.id
        player_room_graph[room_id][move] = new_room
        # if we haven't been here before lets add it to visited Set
        if new_room not in visited:
            visited.add(new_room)
            add_room(new_room, player.current_room.get_exits(), opposite_directions[move], room_id)

# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    # print(move)
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms", len(room_graph), len(visited_rooms))



#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")