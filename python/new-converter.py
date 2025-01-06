input = int(input("Please enter your time in minutes here >>"))
hours = input//60
minutes = input%60
days = hours//24
hours = hours-days*24

if days == 0:
    
    print(hours, 'hours', minutes, 'minutes')
else:
    break()

if days == 1:
    
    print(days, 'day', hours, 'hours', minutes, 'minutes')

else:

    print(days, 'days', hours, 'hours', minutes, 'minutes')






#if hours >= 24:
#    days = hours//24
#    hours = hours-days*24
#    print(days, 'days', hours, 'hours and', minutes, 'minutes')
#else:
#    print(hours, 'hours', minutes, 'minutes')





#print(input//60, 'hours and', input%60, 'minutes')
