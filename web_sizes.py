import pickle

with open('./web_size.pickle', 'rb') as handle:
    sites = pickle.load(handle)

with open('./web_size_new.pickle', 'rb') as handle:
    sites_new = pickle.load(handle)

sum = 0
empty_sites = 0
print(sites[0])
print(sites_new[0])

#1. feladat

for item in range(0, len(sites_new)):
    sum += sites_new[item]['size']

totalSize = round(sum / 1024, 2)
print(f"total size is:  {totalSize} Gb")

avgSize = round(totalSize / len(sites_new), 2)
print(f"avg site size is: {avgSize} Gb")

#2. feladat

for x, y in zip(sites, sites_new):
    if x['size'] != y['size']:
        diff = y['size'] - x['size']
        rate = diff / (y['size'] / 100)
        if rate > 0:
            print(f"{y['domain']} changed by: +{round(rate,2)} %")
        else:
            print(f"{y['domain']} changed by: {round(rate,2)} %")

#3. feladat

for x in sites_new:
    if x['size'] == 0:
        empty_sites += 1

print(f"there are {empty_sites} empty sites")

#4. feladat

for x in sites_new:
    if x['size'] > 1024:
        print(f"{x['domain']} is: {round(x['size']/1024,2)} Gb")
    elif x['size'] == 0:
        pass
    else:
        print(f"{x['domain']} is: {round(x['size'],2)} Mb")
