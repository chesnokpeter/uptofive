# answer = 0
# baggage = 0
# list_cut = []
# text = input("Введи оценки ")
# list = text
# for n in range(len(list)):
#     list_cut.append(list[n])
# for i in list_cut:
#     baggage += int(i)
# answer = baggage / len(list_cut)
# print(round(answer, 2))


upFourRatingFive = 0
upFiveRatingFive = 0
upFourRatingFour = 0
list = input("Введи оценки ")
summ = 0
list_cut = []

for n in range(len(list)):
    list_cut.append(list[n])
for i in list_cut:
    summ += int(i)
answer = summ / len(list_cut)
print(f"Средний балл: {round(answer, 2)}")

temp = len(list_cut)
summ1 = summ
while round(summ1 / temp, 2) <= 4.50:
    summ1 += 5
    temp += 1
    upFiveRatingFive = temp - len(list_cut)

temp = len(list_cut)
summ2 = summ
while round(summ2 / temp, 2) <= 3.50:
    summ2 += 5
    temp += 1
    upFourRatingFive = temp - len(list_cut)

temp = len(list_cut)
summ3 = summ
while round(summ3 / temp, 2) <= 3.50:
    summ3 += 4
    temp += 1
    upFourRatingFour = temp - len(list_cut)

print(f"До пятёрки нужно {upFiveRatingFive} пятёрок\nДо четвёрки нужно {upFourRatingFive} пятёрок ИЛИ {upFourRatingFour} четвёрок")

input()

# function Calculate( u5, u4, u3, u2, oe55, oe45, oe44, srB) {var e55 = 0;
# var e45 = 0;
# var e44 = 0;
# var sred = 0;
# var sum = u2*2+u3*3+u4*4+u5*5;
# var kol = u2+u3+u4+u5
# var sre = sum/kol;

# srB.SetValue(sre);
# sred=sre;
# while (sred<4.60) {
# 	e55++;
# 	sred=(sum+e55*5)/(kol+e55);
# }
# oe55.SetValue(e55);
# sred=sre;
# while (sred<3.60) {
# 	e45++;
# 	sred=(sum+e45*5)/(kol+e45);
# }
# oe45.SetValue(e45);
# sred=sre;
# while (sred<3.60) {
# 	e44++;
# 	sred=(sum+e44*4)/(kol+e44);
# }
# oe44.SetValue(e44);}