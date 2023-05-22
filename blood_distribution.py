#This program is an implementation of the Edmonds–Karp algorithm to solve the max-flow prolem

def find_path(don,rec, cango, rev_flow):
    find_queue = list(filter(lambda x: (don[x] > 0), range(0,8)))
    #Receiver nodes are re-indexed with an increment of 8 so that both donors and receivers
    #  can be in the same queue
    #In the source array, -2 indicates it hasn't been visited, -1 indicates that it's a possible donor,
    # and a positive number is the index of the node that flow into that node
    source = [-2] * 16
    for f in find_queue:
        source[f] = -1

    #Iterate over the donors and receivers until an open receiver is found using widht-first search
    while len(find_queue) > 0:
        current = find_queue.pop(0)
        #If the current node explored is a donor
        if current < 8:
            for k in cango[current]:
                #If this donate node can receive flow, the algorithm halts and flow and path are determined
                if rec[k] > 0:
                    flow = rec[k]
                    path = [k+8]
                    node = current
                    while node != -1:
                        path = [node] + path
                        node = source[node]
                        if node > 8:
                            flow = min(flow, rev_flow[path[0]][node-8])
                        if node == -1:
                            flow = min(flow, don[path[0]])
                    return path, flow

                elif source[k+8] == -2:
                    source[k+8] = current
                    find_queue.append(k+8)

        #If the current node explored is a receiver
        else:
            rec_current = current - 8
            for m in range(0,8):
                if rev_flow[m][rec_current] > 0 and source[m] == -2:
                    source[m] = rec_current + 8
                    find_queue.append(m)
    
    return [], 0

def allocate(donate, receive):
    total_flow = 0
    cango = [range(0,8),range(1,8,2),[2,3,6,7],[3,7],range(4,8),[5,7],[6,7],[7]]
    rev_flow = [ [0] * 8 for x in range(8)]

    total_flow = 0

    path, cur_flow = find_path(donate,receive, cango, rev_flow)

    k = 0
    while (len(path) > 0):

        total_flow += cur_flow
        donate[path[0]] = donate[path[0]] - cur_flow
        receive[path[-1]-8] = receive[path[-1]-8] - cur_flow
        for i in range(0, len(path)-1):
            if path[i] < 8:
                a = path[i]
                b = path[i+1] - 8
                rev_flow[a][b] += cur_flow
            else:
                rev_flow[path[i+1]][path[i]-8] -= cur_flow
        
        path, cur_flow = find_path(donate,receive, cango, rev_flow)

    return total_flow



if __name__ == "__main__":
    don = [int(x) for x in list(input().split(' '))]
    rec = [int(y) for y in list(input().split(' '))]

    print(allocate(don, rec))
 