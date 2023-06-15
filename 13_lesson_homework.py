# Les13_Hw by Podkovko Dmitriy

from requests import get
from time import time, sleep
from statistics import mean
from json import loads


def f_read(file_name):
    try:
        with open(file_name, 'r') as f:
            resources = []
            for row in f.read().splitlines():
                resources.append(row)
            return resources
    except Exception as e:
        print(f'Error during opening file: {file_name}')


def f_add(file_name, resource, speed):
    try:
        with open(file_name, 'a', encoding='utf-8') as f:
            f.write(f'{resource}\n    За {speed} сек\n\n')
            return True
    except Exception as e:
        print(f'Error during writing to file: {file_name}')


def api_requests(counter=None):
    counter = counter if counter else 1
    # storage = [] # пока не используем
    lst_resources = f_read('File_resources')
    if lst_resources:
        print('Start ...')
        try:
            i = 0
            while i < len(lst_resources):
                all_results = []
                print(f'Running {lst_resources[i]}')

                for j in range(counter):
                    tm1 = time()
                    # storage.append(get(lst_resources[i]))
                    get(lst_resources[i])
                    tm2 = time()
                    all_results.append(tm2 - tm1)
                    if j != counter - 1: sleep(3) # ограничение на последней итерации счетчика, чтоб не засыпал перед новым ресурсом
                avg = round(mean(all_results), 5)
                f_add('File_results', lst_resources[i], avg)
                i += 1
        except Exception as e:
            print(f'Error during run requests: {lst_resources[i]}')
        print('Finished!')


api_requests(3)


def f_add_Kuna(file_name, string):
    try:
        with open(file_name, 'a', encoding='utf-8') as f:
            f.write(string)
            return True
    except Exception as e:
        print(f'Error during writing to file: {file_name}')


def parse_by_json(answer):
    try:
        data_content = answer.content
        js = loads(data_content)
        buy = float(js['ticker']['buy'])
        sell = float(js['ticker']['sell'])
        return buy, sell
    except Exception as e:
        print('Error during parsing by json!')


def api_requests_Kuna(counter=None, pause=None):
    counter = counter if counter else 1
    pause = pause if pause else 0
    storage_for_buy = []
    storage_for_buy_changes = []
    storage_for_sell = []
    storage_for_sell_changes = []
    for i in range(counter):
        try:
            answer = get('https://kuna.io/api/v2/tickers/btcuah')
        except Exception as e:
            print('Error during run requests to Kuna!')
        buy, sell = parse_by_json(answer)
        print(f'Покупка BTC/UAH: {buy}, Продажа BTC/UAH: {sell}')
        f_add_Kuna('File_Kuna_result', f'Покупка BTC/UAH: {buy}, Продажа BTC/UAH: {sell}\n')
        if len(storage_for_buy) > 0:
            change_buy = round(100 * (storage_for_buy[0] - buy) / storage_for_buy[0], 4)
            if change_buy != 0:
                storage_for_buy_changes.append(change_buy)
                if change_buy > 0:
                    print(f'Покупка \u2193 {abs(change_buy)}%')
                    f_add_Kuna('File_Kuna_result', f'Покупка \u2193 {abs(change_buy)}%\n')
                else:
                    print(f'Покупка \u2191 {abs(change_buy)}%')
                    f_add_Kuna('File_Kuna_result', f'Покупка \u2191 {abs(change_buy)}%\n')
        if len(storage_for_sell) > 0:
            change_sell = round(100 * (storage_for_sell[0] - sell) / storage_for_sell[0], 4)
            if change_sell != 0:
                storage_for_sell_changes.append(change_sell)
                if change_sell > 0:
                    print(f'Продажа \u2193 {abs(change_sell)}%')
                    f_add_Kuna('File_Kuna_result', f'Продажа \u2193 {abs(change_sell)}%\n')
                else:
                    print(f'Продажа \u2191 {abs(change_sell)}%')
                    f_add_Kuna('File_Kuna_result', f'Продажа \u2191 {abs(change_sell)}%\n')
        storage_for_buy.append(buy)
        storage_for_sell.append(sell)
        if i != counter - 1: sleep(pause)


api_requests_Kuna(10, 7)
