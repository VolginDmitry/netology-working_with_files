'''with open('recipes.txt') as f:
     #data = f.readline()#.strip()
     for line in f:
         ingredient_name = line.strip()
         ingredient_count = f.readline().strip()
         #print(ingredient_name)
         print(int(ingredient_count))'''
         


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
         
         
#print('   skjfn   \n sfvsv'.strip())


"""
def parse_cookbook(file_path):
    cook_book = {}
    
    with open(file_path, 'r', encoding='utf-8') as file:
        while True:
            dish_name = file.readline().strip()  # Читаем название блюда
            if not dish_name:  # Если достигнут конец файла
                break
            
            # Читаем количество ингредиентов
            ingredients_count = int(file.readline().strip())
            ingredients = []

            for _ in range(ingredients_count):
                line = file.readline().strip()
                ingredient_name, quantity, measure = line.split(' | ')
                ingredient = {
                    'ingredient_name': ingredient_name,
                    'quantity': int(quantity),
                    'measure': measure
                }
                ingredients.append(ingredient)

            # Добавляем информацию о блюде в словарь
            cook_book[dish_name] = ingredients
    
    return cook_book"""
