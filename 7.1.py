# Условие:
# Вам нужно обработать данные о продажах,
# которые представлены в виде списка списков.
# Каждый внутренний список представляет
# собой запись о продаже и содержит следующую информацию:
# ["название товара", количество, цена за единицу].
#
# Напишите функцию, которая принимает такой список списков,
# и ключевые аргументы, которые определяют,
# какую статистику нужно вернуть: общий доход
# или количество проданных единиц каждого товара.



sales_data = [["яблоки", 10, 20], ["груши", 5, 30], ["яблоки", 7, 20]]

def sales_stats(sales_data, revenue = False, quantity = False, customers = False):
        if revenue is True: # общий доход
                list_1 = []
                for i,v in enumerate(sales_data):
                        list_1.append(v[1] * v[2])
                sum_doxoda = sum(list_1)

                return sum_doxoda

        elif quantity is True: # количество проданных единиц каждого товара

                flat_list = [x for xs in sales_data for x in xs] # ['яблоки', 10, 20, 'груши', 5, 30, 'яблоки', 7, 20]

                spisok_1 = flat_list[0:3] # ['яблоки', 10, 20]
                spisok_1_1 = spisok_1[0] # 'яблоки'
                spisok_1_2 = spisok_1[1] # 10
                spisok_1_3 = spisok_1[2] # 20
                # print(f'\nspisok_1 = {spisok_1}, type = {type(spisok_1)}'
                #          f'\nspisok_1_1 = {spisok_1_1}, type = {type(spisok_1_1)}'
                #          f'\nspisok_1_2 = {spisok_1_2}, type = {type(spisok_1_2)}'
                #          f'\nspisok_1_3 = {spisok_1_3}, type = {type(spisok_1_3)}\n')

                spisok_2 = flat_list[3:6]  # ['груши', 5,30]
                spisok_2_1 = spisok_2[0] # 'груши
                spisok_2_2 = spisok_2[1] # 5
                spisok_2_3 = spisok_2[2] # 30
                # print(f'\nspisok_2 = {spisok_2}, type = {type(spisok_2)}'
                #       f'\nspisok_2_1 = {spisok_2_1}, type = {type(spisok_2_1)}'
                #       f'\nspisok_2_2 = {spisok_2_2}, type = {type(spisok_2_2)}'
                #       f'\nspisok_2_3 = {spisok_2_3}, type = {type(spisok_2_3)}\n')

                spisok_3 = flat_list[6:9] # ['яблоки', 7, 20]
                spisok_3_1 = spisok_3[0] # 'яблоки'
                spisok_3_2 = spisok_3[1] # 7
                spisok_3_3 = spisok_3[2] # 20
                # print(f'\nspisok_3 = {spisok_3}, type = {type(spisok_3)}'
                #       f'\nspisok_3_1 = {spisok_3_1}, type = {type(spisok_3_1)}'
                #       f'\nspisok_3_2 = {spisok_3_2}, type = {type(spisok_3_2)}'
                #       f'\nspisok_3_3 = {spisok_3_3}, type = {type(spisok_3_3)}\n')

                kov_podan_dict = {}

                kov_podan_dict[spisok_1_1] = spisok_1_2

                kov_podan_dict[spisok_2_1] = spisok_2_2

                kov_podan_dict[spisok_3_1] = spisok_3_2

                #print(f'kov_podan_dict = {kov_podan_dict}, type = {type(kov_podan_dict)}')

                if spisok_1_1 == spisok_2_1:
                        kov_podan_dict[spisok_1_1] = (spisok_1_2 + spisok_2_2)
                        #return kov_podan_dict

                if spisok_1_1 == spisok_3_1:
                        kov_podan_dict[spisok_1_1] = (spisok_1_2 + spisok_3_2)
                        #return kov_podan_dict

                if spisok_2_1 ==  spisok_3_1:
                       kov_podan_dict[spisok_2_1] = (spisok_2_2 + spisok_3_2)
                       #return kov_podan_dict

                print((f'None, {kov_podan_dict}'))

        elif customers is True: # сторонние ключевые аргументы
                return True

#print(f'\n10 x 20 = {10*20}\n5 x 30 = {5*30}\n7 x 20 = {7*20}\n\n{10*20} +  {5*30} + {7*20} = {10*20 + 5*30 + 7*20}\n')

# Пример работы:
print(sales_stats(sales_data, revenue=True))
# (490, None)
print(sales_stats(sales_data, quantity=True))
# (None, {'яблоки': 17, 'груши': 5})

# При этом ваша функция должна отрабатывать корректно,
# если ей были переданы сторонние ключевые аргументы:
#
print(sales_stats(sales_data, customers=True))
# (None, None)
# Ваша задача:
# только реализовать функцию sales_stats, вызывать её не нужно.