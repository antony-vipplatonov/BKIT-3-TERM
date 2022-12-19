def field(items, *args):
    assert len(args) > 0
    for elem in items:
        if len(args) == 1:
            if elem.get(args[0]) != None:
                yield "'" + elem[args[0]] + "'"
        else:
            line = {}
            for one in args:
                line[one] = elem[one]
            yield line


goods = [{'title': 'Ковёр', 'price': 2000, 'color': 'green'},
         {'title': 'Диван для отдыха', 'price': 5300, 'color': 'black'}]
print((", ").join(field(goods, 'title')))
result = [elem for elem in field(goods, 'title', 'price')]
print(*result, sep=", ")
