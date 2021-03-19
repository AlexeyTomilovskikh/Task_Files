def create_cook_book(file_name):
    cook_book = {}
    with open('recipes.txt', encoding='utf-8') as f:
        for line in f:
            dish_name = line.lower().strip().capitalize()
            counter = int(f.readline())
            ingredients = []
            for i in range(counter):
                names = ['ingredient_name', 'quantity', 'measure']
                temp_dict = dict(zip(names, (f.readline().strip('\n').split(' | '))))
                temp_dict['quantity'] = int(temp_dict['quantity'])
                ingredients.append(temp_dict)
            cook_book[dish_name] = ingredients
            f.readline()
    return cook_book

def get_shop_list_by_dishes(dishes, person):
    cook_dict = create_cook_book('recipes.txt')
    name_list = []
    ingredien_list = []
    prop_dict = {}
    for dish in dishes:
      if dish in cook_dict:
        dict_list = cook_dict[dish]
        for elem_dict in dict_list:
          if elem_dict['ingredient_name'] in prop_dict:
            x = elem_dict['ingredient_name']
            y = elem_dict['quantity'] * person
            prop_dict[x]['quantity'] += y
          else:
            elem_dict['quantity'] *= person
            ingredien_list.append(elem_dict)
            name_list.append(elem_dict.pop('ingredient_name'))
      prop_dict.update(dict(zip(name_list, ingredien_list)))
    return prop_dict

with open("recipes.txt") as recipe:
  print("Книга рецептов")
  print(recipe.read())
food = input('Какое блюдо из списка приготовить?: ')
p = int(input('Укажите количество порций: '))
print(get_shop_list_by_dishes([food], p))