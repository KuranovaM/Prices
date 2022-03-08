from manufacturer import Manufacturer
# from openpyxl import load_workbook
# from datetime import timedelta
#
# wb = load_workbook(filename = 'datamon (1).xlsx')
# sheet_ranges = wb['Sheet1']
# tovar = ["ОСЬ 3519.21.00.025", "Ось 3519.21.00.025"]
# tovars = {"ОСЬ 3519.21.00.025": {"имя": {"дата": [], "среднее время поставки": []}}}
# items = {}
# c = 0
# for i in range(1, sheet_ranges.max_row):
#     if sheet_ranges[i][0].value in tovar:
#         if sheet_ranges[i][0].value not in items:
#             items[sheet_ranges[i][0].value] = {}
#         if sheet_ranges[i][10].value not in items[sheet_ranges[i][0].value]:
#             items[sheet_ranges[i][0].value][sheet_ranges[i][10].value] = {"время поставки": []}
#         if str(sheet_ranges[i][2].value) not in items[sheet_ranges[i][0].value][sheet_ranges[i][10].value]:
#             items[sheet_ranges[i][0].value][sheet_ranges[i][10].value][str(sheet_ranges[i][2].value)] = [sheet_ranges[i][7].value]
#             items[sheet_ranges[i][0].value][sheet_ranges[i][10].value]["время поставки"].append(sheet_ranges[i][3].value)
#         else:
#             if sheet_ranges[i][7].value not in items[sheet_ranges[i][0].value][sheet_ranges[i][10].value][str(sheet_ranges[i][2].value)]:
#                 items[sheet_ranges[i][0].value][sheet_ranges[i][10].value][str(sheet_ranges[i][2].value)].append(sheet_ranges[i][7].value)
#             items[sheet_ranges[i][0].value][sheet_ranges[i][10].value]["время поставки"].append(
#                 sheet_ranges[i][3].value)
# items = {'Ось 3519.21.00.025': {4012: {'время поставки': [337, 214, 214, 128, 123, 64, 43, 127, 191, 98, None, None, None, None, None, None], '2018-12-13 00:00:00': [26751.5923566879], '2019-10-30 00:00:00': [26751.5923566879], '2020-12-23 00:00:00': [26751.5923566879], 'None': [26751.5923566879]}, 4014: {'время поставки': [75, 72, 129, 116, 71, 76, None, None, 54], '2020-01-15 00:00:00': [9299.363057324841], '2020-04-29 00:00:00': [9299.363057324841], '2020-05-08 00:00:00': [9299.363057324841], '2020-05-12 00:00:00': [9299.363057324841], '2020-08-05 00:00:00': [9299.363057324841], '2020-09-30 00:00:00': [9299.363057324841], 'None': [9299.363057324841], '2021-02-10 00:00:00': [10318.47133757962]}, 3961: {'время поставки': [None, None], 'None': [25477.70700636943]}, 3952: {'время поставки': [None], 'None': [12101.91082802548]}, 3915: {'время поставки': [30], '2021-09-22 00:00:00': [18280.25477707006]}}}
new_items = {'OСЬ 3519.21.00.025': [Manufacturer(code=4014, arrival_times=[22, 22, 224, 224, 210, 210], prices={2016: 9299.363057324841})], 'Ось 3519.21.00.025': [Manufacturer(code=4012, arrival_times=[337, 214, 214, 128, 123, 64, 43, 127, 191, 98, None, None, None, None, None, None], prices={2018: 26751.5923566879, 2019: 26751.5923566879, 2020: 26751.5923566879, None: 26751.5923566879}), Manufacturer(code=4014, arrival_times=[75, 72, 129, 116, 71, 76, None, None, 54], prices={2020: [9299.363057324841, 9299.363057324841, 9299.363057324841, 9299.363057324841, 9299.363057324841, 9299.363057324841], 2021: 10318.47133757962, None: 9299.363057324841}), Manufacturer(code=3961, arrival_times=[None, None], prices={None: 25477.70700636943}), Manufacturer(code=3952, arrival_times=[None], prices={None: 12101.91082802548}), Manufacturer(code=3915, arrival_times=[30], prices={2021: 18280.25477707006})]}
d_items = {}
for item in new_items:
    if item not in d_items:
        d_items[item] = {}
        for manufacturer in new_items[item]:
            if manufacturer not in d_items[item]:
                d_items[item][manufacturer] = {"максимальное время поставки": 0, "минимальное время поставки": 0, "среднее время поставки": 0, "среднее изменеение цены": 0, "максимальная цена": 0, "минимальная цена": 0}
            if len(list(filter(lambda x: x is not None, manufacturer.get_arrival_times()))) == 0:
                d_items[item][manufacturer]["среднее время поставки"] = 0
                d_items[item][manufacturer]["максимальное время поставки"] = 0
                d_items[item][manufacturer]["минимальное время поставки"] = 0
            else:
                d_items[item][manufacturer]["среднее время поставки"] = sum(list(filter(lambda x: x is not None, manufacturer.get_arrival_times()))) // len(list(filter(lambda x: x is not None, manufacturer.get_arrival_times())))
                d_items[item][manufacturer]["максимальное время поставки"] = max(
                    list(filter(lambda x: x is not None, manufacturer.get_arrival_times())))
                d_items[item][manufacturer]["минимальное время поставки"] = min(
                    list(filter(lambda x: x is not None, manufacturer.get_arrival_times())))
            print(manufacturer.get_prices())
print(d_items)