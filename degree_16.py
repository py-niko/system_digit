# делим данное число на основание новой системы счисления и фиксируем целое частное и остаток от деления (остаток всегда меньше основания);
# если полученное частное больше основания, то делим частное на основание и вновь фиксируем новое частное и остаток от деления;
# повторяем этот процесс до тех пор, пока частное не получится меньше делителя, то есть основания новой системы счисления;
# полученные остатки, являющиеся цифрами числа в новой системе счисления, приводим в соответствие с ее алфавитом;
# записываем последнее частное и полученные остатки в обратном порядке в ряд слева направо.


x = int(input())
perevod = []

while x >= 2:
    ostatok = x % 2
    shastnoe = x // 2
    x = shastnoe
    perevod.append(ostatok)
perevod.append(shastnoe)
end = ''
for i in range(len(perevod)):
    end += str(perevod[i])
print(end)
# s = ''
# for i in range(len(one_six)):
#     s += str(one_six[i])

