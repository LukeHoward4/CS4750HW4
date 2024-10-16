import Node
import State



#Minimax4 implements a two ply minimax algorithm that determines which node should be chosen.
#Input parameters: startNode, the current node of the game. player, the id of the current player
def minimax2(startNode, player):
    l1 = Node.expand(startNode)
    l1Dict = {}
    nodesGenerated = len(l1) + 1
    #Determing which path to take.
    for node in l1:
        expansion = Node.expand(node)
        nodesGenerated += len(expansion)
        minVal = findMin(expansion, player)
        l1Dict[node] = minVal
    nodesGenerated = len(l1Dict)
    maxVal = max(l1Dict.values())
    #Implementing tiebreakers
    maximums = []
    for key in l1Dict.keys():
        if(l1Dict[key] == maxVal):
            maximums.append(key)
    returnNode = maximums[0]
    smallestX = int(returnNode.getAction()[10])
    smallestY = int(returnNode.getAction()[13])
    for node in maximums[1:]:
        x = int(node.getAction()[10])
        y = int(node.getAction()[13])
        if(x < smallestX):
            returnNode = node
            smallestX = x
            smallestY = y
        elif(x == smallestX):
            if(y < smallestY):
                returnNode = node
                smallestX = x
                smallestY = y
    print("Generated " + str(nodesGenerated) + " nodes")
    return returnNode
#Minimax4 implements a four ply minimax algorithm that determines which node should be chosen.
#Input parameters: startNode, the current node of the game. player, the id of the current player
def minimax4(startNode, player):
    l1 = Node.expand(startNode)
    l1Dict = {}
    nodesGenerated = len(l1) + 1
    for node in l1:
        l2 = Node.expand(node)
        nodesGenerated += len(l2)
        l2Values = []
        for node2 in l2:
            l3 = Node.expand(node2)
            nodesGenerated += len(l3)
            l3Values = []
            for node3 in l3:
                l4 = Node.expand(node3)
                nodesGenerated += len(l4)
                if(len(l4) > 0):
                    minVal = findMin(l4, player)
                    l3Values.append(minVal)
            if(len(l3Values) > 0):
                l2Values.append(max(l3Values))
        if(len(l2Values) > 0):
            l1Dict[node] = min(l2Values)
    #Determining which node should be taken.
    maxVal = max(l1Dict.values())
    print(maxVal)
    maximums = []
    #Implementing the tiebreaker
    for key in l1Dict.keys():
        if(l1Dict[key] == maxVal):
            maximums.append(key)
    returnNode = maximums[0]
    smallestX = int(returnNode.getAction()[10])
    smallestY = int(returnNode.getAction()[13])
    for node in maximums[1:]:
        
        x = int(node.getAction()[10])
        y = int(node.getAction()[13])
        if(x < smallestX):
            returnNode = node
            smallestX = x
            smallestY = y
        elif(x == smallestX):
            if(y < smallestY):
                returnNode = node
                smallestX = x
                smallestY = y
    print("Generated " + str(nodesGenerated) + " nodes")
    return returnNode
#Finding the minimum heuristic in a list of nodes
def findMin(nodeList, player):
    minimum = 9999999
    for node in nodeList:
        if(node.getState().getHeuristic(player) < minimum):
            minimum = node.getState().getHeuristic(player)
    return minimum
#Finding the maximum heuristic in a list of nodes
def findMax(nodeList, player):
    maximum = -99999999
    for node in nodeList:
        if(node.getState().getHeuristic(player) > maximum):
            maximum = node.getState().getHeuristic(player)
    return maximum



    
