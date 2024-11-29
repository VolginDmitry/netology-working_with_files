with open('recipes.txt') as f:
    cook_book = {}
    for line in f:
        dish_name = line.strip()
        ingredient_count = f.readline().strip()
        product_list = []
        
        for i in range(int(ingredient_count)):
            ing = f.readline()
            ingredient_name, quantity, measure = ing.strip().split(' | ')
            product_list.append({
                'ingredient_name': ingredient_name,
                'quantity': quantity,
                'measure': measure
            })

        dict_dish = {dish_name: product_list}

        empty_line = f.readline()  
        cook_book.update(dict_dish)

def get_shop_list_by_dishes(dishes, person_count):
        cooking_list = {}
        for dish in dishes:
            if dish in cook_book:
                for product in cook_book[dish]:
                    if product['ingredient_name'] not in cooking_list:
                        value = {'quantity': int(product['quantity']) * person_count, 'measure': product['measure']}
                        cooking_list[product['ingredient_name']] = value
                    else:
                        cooking_list[product['ingredient_name']]['quantity'] += int(product['quantity']) * person_count
        return cooking_list

print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))