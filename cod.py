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
items = {'ОСЬ 3519.21.00.025': {4014: {'время поставки': [22, 22, 224, 224, 210, 210], '2016-05-19 00:00:00': [9299.363057324841], '2016-05-20 00:00:00': [9299.363057324841], '2017-05-10 00:00:00': [9299.363057324841]}}, 'Ось 3519.21.00.025': {4012: {'время поставки': [337, 214, 214, 128, 123, 64, 43, 127, 191, 98, None, None, None, None, None, None], '2018-12-13 00:00:00': [26751.5923566879], '2019-10-30 00:00:00': [26751.5923566879], '2020-12-23 00:00:00': [26751.5923566879], 'None': [26751.5923566879]}, 4014: {'время поставки': [75, 72, 129, 116, 71, 76, None, None, 54], '2020-01-15 00:00:00': [9299.363057324841], '2020-04-29 00:00:00': [9299.363057324841], '2020-05-08 00:00:00': [9299.363057324841], '2020-05-12 00:00:00': [9299.363057324841], '2020-08-05 00:00:00': [9299.363057324841], '2020-09-30 00:00:00': [9299.363057324841], 'None': [9299.363057324841], '2021-02-10 00:00:00': [10318.47133757962]}, 3961: {'время поставки': [None, None], 'None': [25477.70700636943]}, 3952: {'время поставки': [None], 'None': [12101.91082802548]}, 3915: {'время поставки': [30], '2021-09-22 00:00:00': [18280.25477707006]}}}
print(items)
d_items = {}
for i in items:
    if i not in d_items:
        d_items[i] = {}
        for ii in items[i]:
            if ii not in d_items[i]:
                d_items[i][ii] = {"максимальное время поставки": 0, "минимальное время поставки": 0, "среднее время поставки": 0, "среднее изменеение цены": 0, "последняя цена": 0}
            pris = []
            years = {}
            for iii in items[i][ii]:
                if iii == 'время поставки':
                    if len(list(filter(lambda x: x is not None, items[i][ii]['время поставки']))) == 0:
                        d_items[i][ii]["среднее время поставки"] = 0
                        d_items[i][ii]["максимальное время поставки"] = 0
                        d_items[i][ii]["минимальное время поставки"] = 0
                    else:
                        d_items[i][ii]["среднее время поставки"] = sum(list(filter(lambda x: x is not None, items[i][ii]['время поставки']))) // len(list(filter(lambda x: x is not None, items[i][ii]['время поставки'])))
                        d_items[i][ii]["максимальное время поставки"] = max(
                            list(filter(lambda x: x is not None, items[i][ii]['время поставки'])))
                        d_items[i][ii]["минимальное время поставки"] = min(
                            list(filter(lambda x: x is not None, items[i][ii]['время поставки'])))
                else:
                    if iii != 'None':
                        if iii[:4] not in years:
                            years[iii[:4]] = items[i][ii][iii]
                        else:
                            for f in items[i][ii][iii]:
                                years[iii[:4]].append(f)
            years_d = {}
            c = 0
            for r in sorted(years):
                c += 1
                if len(years[r]) == 0:
                    years_d[r] = 0
                else:
                    years_d[r] = sum(
                        list(filter(lambda x: x is not None, years[r]))) // len(
                        list(filter(lambda x: x is not None, years[r])))
                    if c == len(years):
                        d_items[i][ii]["последняя цена"] = sum(list(filter(lambda x: x is not None, years[r]))) // len(list(filter(lambda x: x is not None, years[r])))
            print(years_d)



print(d_items)