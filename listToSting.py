def listToString(list):
    final_string = ''
    for i in range(len(list)):
        if i == len(list) - 1:
            final_string += list[i]
        elif i == len(list) - 2:
            final_string = final_string + list[i] + ' i '
        else:
            final_string = final_string + list[i] + ', '
    return final_string

i = 0;
tab = [];

while True:
    print('Podaj ' + str(i + 1) + ' słowo w tablicy')
    print('By zakonczyć i skonwertować tablicę na string kliknij enter nie wpisując nic!')
    char = input()
    if char == '':
        break
    else:
        tab.append(char)

print('otrzymany string: ')
print(listToString(tab))
