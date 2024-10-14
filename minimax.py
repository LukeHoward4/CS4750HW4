import Node
import State
import random

def minimax(startNode):
    l1 = Node.expand(startNode)
    l1Dict = {}
    for node in l1:
        expansion = Node.expand(node)
        minVal = findMin(expansion)
        l1Dict[node] = minVal
        print(node.getAction())
        print(minVal)
    maxVal = max(l1Dict.values())
    print("")
    print(maxVal)
    maximums = []
    for key in l1Dict.keys():
        if(l1Dict[key] == maxVal):
            maximums.append(key)
    returnNode = maximums[0]
    smallestX = int(returnNode.getAction()[10])
    smallestY = int(returnNode.getAction()[13])
    print("(" + str(smallestX) + ", " + str(smallestY) + ")")
    for node in maximums[1:]:
        
        x = int(node.getAction()[10])
        y = int(node.getAction()[13])
        print("(" + str(x) + ", " + str(y) + ")")
        if(x < smallestX):
            returnNode = node
            smallestX = x
            smallestY = y
        elif(x == smallestX):
            if(y < smallestY):
                returnNode = node
                smallestX = x
                smallestY = y
    print(returnNode.getAction())
    print(returnNode.getState().getHeuristic())
    return returnNode
def findMin(nodeList):
    minimum = 9999999
    for node in nodeList:
        if(node.getState().getHeuristic() < minimum):
            minimum = node.getState().getHeuristic()
    return minimum
def findMax(nodeList):
    maximum = -99999999
    for node in nodeList:
        if(node.getState().getHeuristic() > maximum):
            maximum = node.getState().getHeuristic()
    return maximum

startingState = State.State([[1, 2], [1, 1]], [[4, 4], [4, 2]])
startingNode = Node.Node(None, startingState, "start", 0.0, 0, 1)
minimax(startingNode)

    
