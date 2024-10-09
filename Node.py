class Node():
    def __init__(self, parentNode, state, action, pathCost, depth):
        self.__parentNode = parentNode
        self.__state = state
        self.__action = action
        self.__pathCost = pathCost
        self.__depth = depth

    def get_parent(self):
        return self.__parentNode
    def get_path_cost(self):
        return self.__pathCost
    def getState(self):
        return self.__state
    def getAction(self):
        return self.__action
    def getDepth(self):
        return self.__depth
    def __lt__(self, other):
        return self.__pathCost < other.get_path_cost() #for comparison of nodes based on path cost

def calculate_path_cost(node):
    total_cost = 0
    while node is not None:
        total_cost += node.get_path_cost()
        node = node.get_parent()
    return total_cost
def findSequence(node):
    actionList = []
    while node is not None:
        actionList.append(node.getAction())
        node = node.get_parent()
    actionList.reverse()
    actionList.pop(0)
    return actionList
