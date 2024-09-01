import multiprocessing
from datetime import datetime

def read_info(name):
    all_data = []
    with open(name,'r', encoding = 'utf-8') as file:
        line = file.readline()
        while line:
            all_data.append(line)
            line = file.readline()


start_time = datetime.now()
read_info('file 1.txt')
read_info('file 2.txt')
read_info('file 3.txt')
read_info('file 4.txt')
finish_time = datetime.now()
res_time = finish_time - start_time
print(f'Линейный вызов {res_time}')

if __name__ == '__main__':

    with multiprocessing.Pool(processes=4) as pool:
        start_time = datetime.now()
        file_names = ['file 1.txt', 'file 2.txt', 'file 3.txt', 'file 4.txt']
        pool.map(read_info,file_names)
    finish_time = datetime.now()
    res_time = finish_time - start_time
    print(f'Многопроцессный вызов {res_time}')


