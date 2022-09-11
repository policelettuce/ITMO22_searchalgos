from collections import deque


def find_common_element(array1, array2):
    for i in array1:
        for j in array2:
            if i == j: return i
    return None


def depth_limited_search(currNode, finishNode, graph, visited, depth, searchDepth):
    depth += 1
    queue = deque()
    queue += graph[currNode]
    if currNode == finishNode:
        visited.append(currNode)
        return True
    if currNode in visited:
        return False

    visited.append(currNode)
    for node in graph[currNode]:
        if node not in visited and depth <= searchDepth:
            result = depth_limited_search(node, finishNode, graph, visited, depth, searchDepth)
            if result: return True


def bidirectional_iterative_deepening_search(startNode, finishNode, graph, searchDepth, maxDepth):
    while searchDepth <= maxDepth:
        depth = 0
        visitedFromStart = []
        visitedFromFinish = []
        resultStart = depth_limited_search(startNode, finishNode, graph, visitedFromStart, depth, searchDepth)
        resultFinish = depth_limited_search(finishNode, startNode, graph, visitedFromFinish, depth, searchDepth)
        middleNode = find_common_element(visitedFromStart, visitedFromFinish)
        if resultStart == True:
            print("Found start-to-finish solution! Search depth: " + str(searchDepth))
            print(visitedFromStart)
            return
        elif resultFinish == True:
            print("Found finish-to-start solution! Search depth: " + str(searchDepth))
            print(visitedFromFinish)
            return
        elif middleNode != None:
            print("Found a middle node - " + str(middleNode) + "!")
            print(visitedFromStart)
            print(visitedFromFinish)
            return
        else:
            print("No solutions found on depth " + str(searchDepth) + ". Increasing search depth...")
            searchDepth *= 2

    print("Maximum search depth reached, no solutions found...")


graph = {
    "Брест": ["Вильнюс", "Витебск", "Калининград"],
    "Вильнюс": ["Брест", "Калининград", "Каунас", "Киев", "Даугавпилс"],
    "Витебск": ["Брест", "Вильнюс", "Воронеж", "Волгоград", "Ниж.Новгород", "С.Петербург", "Орел"],
    "Воронеж":  ["Витебск", "Волгоград", "Ярославль"],
    "Волгоград":  ["Воронеж", "Витебск", "Житомир"],
    "Даугавпилс": ["Вильнюс"],
    "Донецк": ["Житомир", "Кишинев", "Москва", "Орел"],
    "Калининград":  ["Брест", "Вильнюс", "С.Петербург"],
    "Каунас":  ["Вильнюс", "Рига"],
    "Казань": ["Москва", "Уфа"],
    "Киев":  ["Вильнюс", "Житомир", "Кишинев", "Одесса", "Харьков"],
    "Житомир":  ["Киев", "Донецк", "Волгоград"],
    "Кишинев":  ["Киев", "Донецк"],
    "Ниж.Новгород": ["Витебск", "Москва"],
    "С.Петербург":  ["Витебск", "Калининград", "Рига", "Москва", "Мурманск"],
    "Самара": ["Уфа"],
    "Симферополь": ["Харьков"],
    "Минск": ["Москва", "Мурманск", "Ярославль"],
    "Москва":  ["Казань", "Ниж.Новгород", "Минск", "Донецк", "С.Петербург", "Орел"],
    "Мурманск":  ["С.Петербург", "Минск"],
    "Орел":  ["Витебск", "Донецк", "Москва"],
    "Одесса":  ["Киев"],
    "Рига":  ["С.Петербург", "Каунас", "Таллин"],
    "Таллин":  ["Рига"],
    "Уфа": ["Казань", "Самара"],
    "Харьков":  ["Киев", "Симферополь"],
    "Ярославль":  ["Воронеж", "Минск"],
}
start = 'Рига'
finish = 'Одесса'
searchDepth = 1
maxDepth = 32

bidirectional_iterative_deepening_search(start, finish, graph, searchDepth, maxDepth)