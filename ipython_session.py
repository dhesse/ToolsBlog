import gzip
import csv
from itertools import islice
from collections import defaultdict
with gzip.GzipFile("ObservationData_vhltxod.csv.gz") as input_file:
    obs_reader = csv.reader(input_file, delimiter=',')
    for row in islice(obs_reader, 5):
        print row
sisal_prices = defaultdict(dict)
with gzip.GzipFile("ObservationData_vhltxod.csv.gz") as input_file:
    obs_reader = csv.reader(input_file, delimiter=',')
    for row in obs_reader:
        country, product, element, unit, date, value = row
        if product == 'Sisal' and unit == 'Standard Local Currency/tonne':
            year = int(date[4:8])
            sisal_prices[country][year] = float(value)
sisal_normalized_prices = defaultdict(float)
ncountries = 0
for country in sisal_prices:
    if 2000 in sisal_prices[country]:
        for year, value in sisal_prices[country].items():
            sisal_normalized_prices[year] += value / sisal_prices[country][2000]
        ncountries += 1
for i in sisal_normalized_prices:
    sisal_normalized_prices[i] = sisal_normalized_prices[i] / ncountries
import matplotlib.pyplot as plt
xvals, yvals = sorted(sisal_normalized_prices), [sisal_normalized_prices[i] for i in sorted(sisal_normalized_prices)]
plt.plot(xvals, yvals)
plt.xlabel("year")
plt.ylabel("sisal price, normalized")
plt.show()
