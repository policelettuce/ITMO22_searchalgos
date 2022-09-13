def depth_limited_search(currNode, finishNode, graph, visited, depth, searchDepth):
    depth += 1
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


def iterative_deepening_search(startNode, finishNode, graph, searchDepth, maxDepth):
    while searchDepth <= maxDepth:
        depth = 0
        visited = []
        result = depth_limited_search(startNode, finishNode, graph, visited, depth, searchDepth)
        if result != True:
            print("No solutions found on depth " + str(searchDepth) + ". Increasing search depth...")
            print(visited)
            searchDepth *= 2
        else:
            print("Found a solution with search depth " + str(searchDepth) + "!")
            print(visited)
            return

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

iterative_deepening_search(start, finish, graph, searchDepth, maxDepth)