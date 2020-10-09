import csv
import matplotlib.pyplot as plt

filename = 'tv_shows.csv'

#DEFINITIONS

#lists for headers
Row = []
Title = []
Year = []
Age = []
IMDb = []
RottenTomatoes = []
Netflix = []
Hulu = []
PrimeVideo = []
DisneyPlus = []
Tv_Type = []

#totals for avgs
imdbTotalDisney = 0
imdbTotalHulu = 0
imdbTotalNetflix = 0
imdbTotalPrimeVideo = 0
rtTotalDisney = 0
rtTotalHulu = 0
rtTotalNetflix = 0
rtTotalPrimeVideo = 0

#counters for avgs
counterNetflixIMDb = 0
counterHuluIMDb = 0
counterDisneyIMDb = 0
counterPrimeVideoIMDb = 0
counterNetflixRT = 0
counterHuluRT = 0
counterDisneyRT = 0
counterPrimeVideoRT = 0

#averages for each streaming service
imdbAvgNetflix = 0
imdbAvgHulu = 0
imdbAvgDisney = 0
imdbAvgPrimeVideo = 0

#averages for each streaming service
rtAvgNetflix = 0
rtAvgHulu = 0
rtAvgDisney = 0
rtAvgPrimeVideo = 0

#averages per streaming service in lists
averagesIMDb = [imdbAvgNetflix, imdbAvgHulu, imdbAvgDisney, imdbAvgPrimeVideo]
averagesRT = [rtAvgNetflix, rtAvgHulu, rtAvgDisney, rtAvgPrimeVideo]
averagesNormalized = [0, 0, 0, 0]



with open(filename) as f: #opened file
    reader = csv.reader(f)
    header_row = next(reader)
    for index, column_header in enumerate(header_row): # shows index associated with each header
        print(index, column_header.split(","))

    for row in reader: # creates a filled list for each header
        Row.append(row[0])
        Title.append(row[1])
        Year.append(int(row[2]))
        Age.append(row[3])
        IMDb.append(row[4])
        RottenTomatoes.append(row[5])
        Netflix.append(int(row[6]))
        Hulu.append(int(row[7]))
        PrimeVideo.append(int(row[8]))
        DisneyPlus.append(int(row[9]))
        Tv_Type.append(int(row[10]))

for i in range(len(IMDb)): # turns IMDb list into float vals
    if IMDb[i] == "":
        continue
    IMDb[i] = float(IMDb[i])

for i in range(len(RottenTomatoes)): # turns RottenTomatoes into int vals
    if RottenTomatoes[i] == "":
        continue
    if "%" in RottenTomatoes[i]:
        RottenTomatoes[i] = RottenTomatoes[i][:-1]
    RottenTomatoes[i] = int(RottenTomatoes[i])


def avg(ratingList, streamingList, counterStream, ratingTotal):
    for i in range(len(ratingList)):  # creates (for Neflix) total: a val used for computing avgs, and counterx: a val used to subtract from x length when computing avgs
        if streamingList[i] == 1:
            if ratingList[i] == "":
                counterStream += 1
                continue
            ratingTotal += ratingList[i]
        else:
            counterStream += 1
    return ratingTotal / (len(ratingList) - counterStream)

averagesIMDb[0] = avg(IMDb, Netflix, counterNetflixIMDb, imdbTotalNetflix)
averagesIMDb[1] = avg(IMDb, Hulu, counterHuluIMDb, imdbTotalHulu)
averagesIMDb[2] = avg(IMDb, DisneyPlus, counterDisneyRT, imdbTotalDisney)
averagesIMDb[3] = avg(IMDb, PrimeVideo, counterPrimeVideoIMDb, imdbTotalPrimeVideo)

averagesRT[0] = avg(RottenTomatoes, Netflix, counterNetflixRT, rtTotalNetflix)
averagesRT[1] = avg(RottenTomatoes, Hulu, counterHuluRT, rtTotalHulu)
averagesRT[2] = avg(RottenTomatoes, DisneyPlus, counterDisneyRT, rtTotalDisney)
averagesRT[3] = avg(RottenTomatoes, PrimeVideo, counterPrimeVideoRT, rtTotalPrimeVideo)

print(averagesIMDb)
print (averagesRT)

for i in range(len(averagesIMDb)):
    averagesIMDb[i] = averagesIMDb[i] / 10
    averagesRT[i] = averagesRT[i] / 100
    averagesNormalized[i] = averagesIMDb[i] + averagesRT[i]

print(averagesNormalized)