import csv
def read_csv(path):
    with open(path, 'r') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        header=next(reader)
        data=[]
        for row in reader:
            iterable=zip(header,row)
            country_dic={key:value for key, value in iterable}
            print('\n')
            data.append(country_dic)
        return data

data=read_csv('world_population.csv')
for item in data:
    print(item)
    print('')