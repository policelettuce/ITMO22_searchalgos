def depth_first_search(currNode, finishNode, graph, visited):
    if currNode == finishNode:
        print("Solution found!")
        visited.append(currNode)
        print(visited)
        return
    if currNode in visited:
        return

    visited.append(currNode)
    for node in graph[currNode]:
        if node not in visited:
            depth_first_search(node, finishNode, graph, visited)


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
visited = []

depth_first_search(start, finish, graph, visited)
