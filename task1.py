regions = ['chuy', 'issyk_kul', 'naryn', 'osh', 'jalal_abad', 'talas', 'batken']
temperature = []
for i in range(len(regions)):
    temperature.append((int(input(f'Enter temperature for {regions[i]} region: '))))
aver_temp = round(sum(temperature)/len(temperature), 1)
print(f'Average temperature in Kyrgyzstan for today is {aver_temp} °C.')
