import csv
import random

CostMed = []
DistMed = []
RateMed = []
RecMed = []

def fitness(cost,distance,rating):
    return 0.2*float(cost)+0.4*distance+0.4*float(rating)

with open(r"assets/Hospital_Data.csv","r") as file:
    readdata=csv.reader(file)
    data = list(readdata)
    data.pop(0)
    costdata = sorted(data,key=lambda x: x[1])
    distdata = sorted(data,key=lambda x: random.randint(1,101))
    ratedata = sorted(data,key=lambda x: x[4])
    recdata = sorted(data,key=lambda x: fitness(x[1],random.randint(1,101),x[4]))
    for i in costdata[1:]:
        CostMed.append(f"""Hospital(
hospName: '{i[0]}',
hospPrice: '{i[1]}-{i[3]}',
stars: {i[4]},
image: 'images/hosp.jpg',
),\n""")
    for i in distdata[1:]:
        DistMed.append(f"""Hospital(
hospName: '{i[0]}',
hospPrice: '{i[1]}-{i[3]}',
stars: {i[4]},
image: 'images/hosp.jpg',
),\n""")
    for i in ratedata[1:]:
        RateMed.append(f"""Hospital(
hospName: '{i[0]}',
hospPrice: '{i[1]}-{i[3]}',
stars: {i[4]},
image: 'images/hosp.jpg',
),\n""")
    for i in recdata[1:]:
        RecMed.append(f"""Hospital(
hospName: '{i[0]}',
hospPrice: '{i[1]}-{i[3]}',
stars: {i[4]},
image: 'images/hosp.jpg',
),\n""")
    
with open(r"lib/data.dart",'a') as file:
    file.write("List<Hospital> costhosp = [\n")
    for i in CostMed:
        file.write(i)
    file.write("];\n")
    file.write("List<Hospital> disthosp = [\n")
    for i in DistMed:
        file.write(i)
    file.write("];\n")
    file.write("List<Hospital> ratehosp = [\n")
    for i in RateMed:
        file.write(i)
    file.write("];\n")
    file.write("List<Hospital> rechosp = [\n")
    for i in RecMed:
        file.write(i)
    file.write("];\n")