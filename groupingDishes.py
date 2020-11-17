dishes = [["Salad", "Tomato", "Cucumber", "Salad", "Sauce"],
            ["Pizza", "Tomato", "Sausage", "Sauce", "Dough"],
            ["Quesadilla", "Chicken", "Cheese", "Sauce"],
            ["Sandwich", "Salad", "Bread", "Tomato", "Cheese"]]

def groupingDishes(dishes):
    d = {}

    for l in dishes:
        dish = l[0]
        for i in l[1:]:
            if i not in d:
                d[i] = [dish]
            else:
                d[i] += [dish]

    out = []
    for i in sorted(d):
        if len(d[i]) > 1:
            out += [[i] + sorted(d[i])]
    
    print(out)

groupingDishes(dishes)