import requests
from time import sleep
from datetime import datetime
from threading import Thread

# start_time = datetime.now()
#
# def write_words(word_count, file_name):
#     with open(file_name,'w',encoding ='utf-8') as file:
#         for word in range(word_count):
#             # print(word + 1,f"Какое-то слово № <{word+1}>", "/n")
#             file.write(f"Какое-то слово № <{word+1}>" + "\n")
#             sleep(0.1)
#             # word += 1
#     print(f"Завершилась запись в файл {file_name}")
# finish_time = datetime()
# res_time = finish_time - start_time
#
# write_words(10, "example1.txt")
# write_words(30, "example2.txt")
# write_words(200, "example3.txt")
# write_words(100, "example4.txt")
# print(res_time)


start_time = datetime.now()
def func(word_count, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        for word in range(word_count):
            file.write(f"Какое-то слово № <{word + 1}>" + "\n")
            sleep(0.1)
        print(f"Завершилась запись в файл {file_name}")

thr_first = Thread(target = func, args = (10, "example5.txt"))
thr_second = Thread(target = func, args = (30, "example6.txt"))
thr_third = Thread(target = func, args = (200, "example7.txt"))
thr_fourth = Thread(target = func, args = (100, "example8.txt"))

thr_first.start()
thr_second.start()
thr_third.start()
thr_fourth.start()

thr_first.join()
thr_second.join()
thr_third.join()
thr_fourth.join()
finish_time = datetime.now()
res_time = finish_time - start_time
print(res_time)
