# import os

# folder_path = 'C:\Premiere2023\SoursCopenhagen'  # вкажіть шлях до необхідної папки

# # перевірка наявності папки за вказаним шляхом
# if os.path.exists(folder_path):
#     # перебір файлів у папці
#     for filename in os.listdir(folder_path):
#         # перевірка чи є це файл (а не папка)
#         if os.path.isfile(os.path.join(folder_path, filename)):
#             # заміна другої букви "У" на "H" у назві файлу
#             new_filename = filename[:1] + 'H' + filename[2:]
#             # перейменування файлу
#             os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_filename))
#     print("Заміна виконана успішно.")
# else:
#     print("Папка за вказаним шляхом не знайдена.")


# def capital_text(text):
#   # розділити текст на речення за допомогою регулярних виразів
#   import re
#   sentences = re.split(r'([.!?])\s*', text)
#   # створити порожній список для зберігання речень з великими літерами
#   capitalized_sentences = []
#   # для кожного речення в списку
#   for sentence in sentences:
#     # якщо речення не пусте
#     if sentence:
#       # зробити великою першу літеру речення і додати до списку
#       capitalized_sentences.append(sentence[0].upper() + sentence[1:])
#   # об'єднати список речень в один рядок і повернути його
#   return ''.join(capitalized_sentences)

# # тестування функції
# text = "дуже часто люди у своїх повідомленнях не ставлять великі літери, особливо це стало масовим явищем в еру мобільних. пристроїв. це може ускладнити читання і розуміння тексту! що ви думаєте про це?"
# print(capital_text(text))



# def all_sub_lists(some_list):
#     if len(some_list) == 0:
#         return [[]]  # повертаємо порожній список як підсписок, якщо вхідний список порожній
#     sub_lists = all_sub_lists(some_list[:-1])  # рекурсивно знаходимо всі підсписки для списку без останнього елемента
#     return sub_lists + [i + [some_list[-1]] for i in sub_lists]  # додаємо всі підсписки, які містять останній елемент

# input_list = [1, 2, 3, 4, 5]
# result = all_sub_lists(input_list)
# print(result)



# counter = 0
# resul = []
# last_letter = None

# def encode(data):
#     global counter
#     global last_letter
#     global resul
        
#     if data == [] or data == '':
#         print('[]')
#         return []


#     if len(data) == 2:

#         if data[0] == data[1] == last_letter:
#             counter += 2
#             resul.append(str(data[0]))
#             resul.append(counter)
#             result = resul
#             resul = []
#             return result
          

#         if data[0] == data[1]:
#             resul.append(str(data[0]))
#             resul.append(2)
#             result = resul
#             resul = []
#             return result

#     elif data[0] == data [1]:
#         counter += 1
#         last_letter = data[0]
#         return encode (data[1:])

#     else:
#         resul.append(str(data[0]))
#         resul.append(counter)
#         counter = 1
#         return encode (data[1:])

