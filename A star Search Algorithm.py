import heapq

my_map = {
'Aa': {'Bb':6, 'Ff':3},
'Bb': {'Aa':6, 'Dd':2, 'Cc':3},
'Cc': {'Bb':3, 'Dd':1, 'Ee':5, 'Aa':1},
'Dd': {'Bb':2, 'Cc':1, 'Ee':8},
'Ee': {'Dd':8, 'Ii':5, 'Cc':5, 'Jj':3},
'Ff': {'Aa':3, 'Gg':1, 'Hh':7},
'Gg': {'Ff':1, 'Ii':3},
'Hh': {'Ii':2, 'Ff':7},
'Ii': {'Gg':3, 'Ee':5, 'Jj':3},
'Jj': {'Ee':5, 'Ii':3},
}
heuristic_value = {
'Aa':10,
'Bb':8,
'Cc':5,
'Dd':7,
'Ee':3,
'Ff':6,
'Gg':5,
'Hh':3,
'Ii':1,
'Jj':0,
}

def a_star_search(graph,start_state,goal_state,heuristic_value):
    ol=[(0,start_state)]
    cl=set()
    goal_score={location: float('inf') for location in graph}
    goal_score[start_state]=0

    while ol:
        current_g,c_node=heapq.heappop(ol)

        if c_node == goal_state:
            return goal_score[goal_state]
        
        if c_node in cl:
            continue

        cl.add(c_node)

        for neighbour,dis in graph[c_node].items():
            tentative=goal_score[c_node]+dis

            if tentative < goal_score[neighbour]:
                goal_score[neighbour]=tentative
                f_score=tentative+heuristic_value[neighbour]
                heapq.heappush(ol,(f_score,neighbour))
    return float('inf')

start_location='Aa'
goal_location='Jj'
short_path = a_star_search(my_map, start_location, goal_location, heuristic_value)
if (short_path < float('inf')):
    print(f"The short path from {start_location} till {goal_location} : {short_path} km.")
else:
    print(f"Path is not found from {start_location} till {goal_location}. Thank You!!!")