number_of_cats = 15
cans_per_day = 2
one_week = 7

total_cans = number_of_cats * cans_per_day
total_cans_per_week = number_of_cats * cans_per_day * one_week
one_day = "{} cats eat {} cans per day".format(number_of_cats,total_cans)
one_week = "{} cats eat {} cans in {} days".format(number_of_cats,total_cans_per_week,one_week)
print(one_day)
print(one_week)


