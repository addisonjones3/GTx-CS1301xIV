#!/usr/bin/env python

with open('Prob8FullSample.csv', 'r') as f:
    rows = f.read().split('\n')
    name_dict = {}
    for row in rows:
        rowlist = row.split(',')
        if rowlist[0] not in name_dict.keys():
            name_dict[rowlist[0]] = [[rowlist[2], int(rowlist[1])]]
        else:
            name_dict[rowlist[0]].append([rowlist[2], int(rowlist[1])])
# print (name_dict['Jaime'])

# unique_names = []
# for namerow in name_list:
#     if namerow[0] not in unique_names:
#         unique_names.append(namerow[0])
# # 15790 correct answer
# print (len(unique_names))

# total births 7030332
# total_births = 0
# for row in name_list:
#     total_births += int(row[1])
# print (total_births)

# boy unique Z names 159
# boy_z_names = []
# for row in name_list:
#     if row[0][0] == 'Z' and row[2] == 'Boy':
#         boy_z_names.append(row[0])
# print (len(boy_z_names))

# max births Q name girl Quinn
# max_girl_q_births = {'name': '', 'births': 0}
# for row in name_list:
#     if row[0][0] == 'Q' and row[2] == 'Girl':
#         if int(row[1]) > max_girl_q_births['births']:
#             max_girl_q_births['name'] = row[0]
#             max_girl_q_births['births'] = int(row[1])
# print ('{0} with {1} births'.format(max_girl_q_births['name'], max_girl_q_births['births']))

# total babies names begin and end w/ AEIOU 672960
# vowels = ['a', 'e', 'i', 'o', 'u']
# num_vowels = 0
# for row in name_list:
#     if row[0][0].lower() in vowels and row[0][-1] in vowels:
#         num_vowels += int(row[1])
# print(num_vowels)

# least common first letter of baby's name U - 6283
#
# fletter_births = {}
# for name in name_dict.keys():
#     currbirths = 0
#     for gender in name_dict[name]:
#         currbirths += gender[1]
#     if name[0] not in fletter_births.keys():
#         fletter_births[name[0]] = currbirths
#     else:
#         fletter_births[name[0]] += currbirths
#
# lcommon_fletter = {'fletter': '', 'births': 0}
# for letter in fletter_births.keys():
#     a = fletter_births[letter]
#     b = lcommon_fletter['births']
#     if fletter_births[letter] < lcommon_fletter['births'] or lcommon_fletter['fletter'] == '':
#         lcommon_fletter['fletter'] = letter
#         lcommon_fletter['births'] = fletter_births[letter]
# print (lcommon_fletter)

# births w/ least common letter fname A - 983627
# fletter_births = {}
# for name in name_dict.keys():
#     currbirths = 0
#     for gender in name_dict[name]:
#         currbirths += gender[1]
#     if name[0] not in fletter_births.keys():
#         fletter_births[name[0]] = currbirths
#     else:
#         fletter_births[name[0]] += currbirths
#
# mcommon_fletter = {'fletter': '', 'births': 0}
# for letter in fletter_births.keys():
#     a = fletter_births[letter]
#     b = mcommon_fletter['births']
#     if fletter_births[letter] > mcommon_fletter['births'] or mcommon_fletter['fletter'] == '':
#         mcommon_fletter['fletter'] = letter
#         mcommon_fletter['births'] = fletter_births[letter]
# print (mcommon_fletter)

# most common name regardless of gender, births w/ most common name - Isabella, 42623

# mcommon_name = {'name': '', 'births': 0}
# for name in name_dict.keys():
#     currbirths = 0
#     for gender in name_dict[name]:
#         currbirths += gender[1]
#
#     if currbirths > mcommon_name['births']:
#         mcommon_name['name'] = name
#         mcommon_name['births'] = currbirths
# print (mcommon_name)

# name w/ smallest diff between boy/girls - True, 0

diff = {'name': '', 'diff': 0}
for name in name_dict.keys():
    if len(name_dict[name]) > 1:
        currdiff = abs(name_dict[name][0][1] - name_dict[name][1][1])
        if currdiff < diff['diff'] or diff['name'] == '':
            diff['name'] = name
            diff['diff'] = currdiff
print(diff)