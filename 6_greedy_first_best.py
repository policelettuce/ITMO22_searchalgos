def return_array_sorted_by_distance(node, graph, distance_to_odessa):
    neighbours = graph[node]
    distances = []
    for neighbour in neighbours:
        distances.append(distance_to_odessa[neighbour])

    distances.sort()
    sortedNodes = []
    for dist in distances:
        key = list(distance_to_odessa.keys())[list(distance_to_odessa.values()).index(dist)]
        sortedNodes.append(key)
    return sortedNodes


def greedy_first_best_search(currNode, finishNode, graph, distance_to_odessa, visited):
    if currNode == finishNode:
        print("Solution found!")
        visited.append(currNode)
        print(visited)
        return
    if currNode in visited:
        return

    visited.append(currNode)
    nodes = return_array_sorted_by_distance(currNode, graph, distance_to_odessa)
    for node in nodes:
        if node not in visited:
            greedy_first_best_search(node, finishNode, graph, distance_to_odessa, visited)


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

distance_to_odessa = {
    "Брест": 803,
    "Вильнюс": 990,
    "Витебск": 970,
    "Воронеж": 843,
    "Волгоград": 1062,
    "Даугавпилс": 1084,
    "Донецк": 560,
    "Калининград": 1165,
    "Каунас": 1051,
    "Казань": 1640,
    "Киев": 439,
    "Житомир": 446,
    "Кишинев": 154,
    "Ниж.Новгород": 1423,
    "С.Петербург": 1495,
    "Самара": 1574,
    "Симферополь": 313,
    "Минск": 855,
    "Москва": 1136,
    "Мурманск": 2504,
    "Орел": 815,
    "Одесса": 0,
    "Рига": 1249,
    "Таллин": 1493,
    "Уфа": 1988,
    "Харьков": 561,
    "Ярославль": 1384
}

start = "Рига"
finish = "Одесса"
visited = []

greedy_first_best_search(start, finish, graph, distance_to_odessa, visited)
