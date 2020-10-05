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


with open(filename) as f: #opened file
    reader = csv.reader(f)
    header_row = next(reader)
    for index, column_header in enumerate(header_row): # shows index associated with each header
        print(index, column_header.split(","))

    for row in reader: # creates a filled list for each header
        Row.append(row[0])
        Title.append(row[1])
        Year.append(row[2])
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


    for i in range(len(IMDb)): # creates (for Neflix) total: a val used for computing avgs, and counterx: a val used to subtract from x length when computing avgs
        if Netflix[i] == 1:
            if IMDb[i] == "":
                counterNetflixIMDb += 1
                continue
            imdbTotalNetflix += IMDb[i]
        else:
            counterNetflixIMDb += 1

    for i in range(len(IMDb)): # same as above but for Hulu
        if Hulu[i] == 1:
            if IMDb[i] == "":
                counterHuluIMDb += 1
                continue
            imdbTotalHulu += IMDb[i]
        else:
            counterHuluIMDb += 1

    for i in range(len(IMDb)): # same as above but for DisneyPlus
        if DisneyPlus[i] == 1:
            if IMDb[i] == "":
                counterDisneyIMDb += 1
                continue
            imdbTotalDisney += IMDb[i]
        else:
            counterDisneyIMDb += 1

    for i in range(len(IMDb)): # same as above but for PrimeVideo
        if PrimeVideo[i] == 1:
            if IMDb[i] == "":
                counterPrimeVideoIMDb += 1
                continue
            imdbTotalPrimeVideo += IMDb[i]
        else:
            counterPrimeVideoIMDb += 1

    for i in range(len(RottenTomatoes)): # creates (for Neflix) total: a val used for computing avgs, and counterx: a val used to subtract from x length when computing avgs
        if Netflix[i] == 1:
            if RottenTomatoes[i] == "":
                counterNetflixRT += 1
                continue
            rtTotalNetflix += RottenTomatoes[i]
        else:
            counterNetflixRT += 1

    for i in range(len(RottenTomatoes)): # same as above but for Hulu
        if Hulu[i] == 1:
            if RottenTomatoes[i] == "":
                counterHuluRT += 1
                continue
            rtTotalHulu += RottenTomatoes[i]
        else:
            counterHuluRT += 1

    for i in range(len(RottenTomatoes)): # same as above but for DisneyPlus
        if DisneyPlus[i] == 1:
            if RottenTomatoes[i] == "":
                counterDisneyRT += 1
                continue
            rtTotalDisney += RottenTomatoes[i]
        else:
            counterDisneyRT += 1

    for i in range(len(RottenTomatoes)): # same as above but for PrimeVideo
        if PrimeVideo[i] == 1:
            if RottenTomatoes[i] == "":
                counterPrimeVideoRT += 1
                continue
            rtTotalPrimeVideo += RottenTomatoes[i]
        else:
            counterPrimeVideoRT += 1

#averages for each streaming service (Prime Video has highest IMDb avg)
imdbAvgNetflix = imdbTotalNetflix / (len(IMDb) - counterNetflixIMDb)
imdbAvgHulu = imdbTotalHulu / (len(IMDb) - counterHuluIMDb)
imdbAvgDisney = imdbTotalDisney / (len(IMDb) - counterDisneyIMDb)
imdbAvgPrimeVideo = imdbTotalPrimeVideo / (len(IMDb) - counterPrimeVideoIMDb)

#averages for each streaming service (DisneyPlus has highest Rotten Tomatoes avg)
rtAvgNetflix = rtTotalNetflix / (len(RottenTomatoes) - counterNetflixRT)
rtAvgHulu = rtTotalHulu / (len(RottenTomatoes) - counterHuluRT)
rtAvgDisney = rtTotalDisney / (len(RottenTomatoes) - counterDisneyRT)
rtAvgPrimeVideo = rtTotalPrimeVideo / (len(RottenTomatoes) - counterPrimeVideoRT)

print("\nIMDb")
print("netflix: " + str(imdbAvgNetflix))
print("hulu: " + str(imdbAvgHulu))
print("Disney: " + str(imdbAvgDisney))
print("Prime Video: " + str(imdbAvgPrimeVideo))

print("\nRotten Tomatoes")
print("netflix: " + str(rtAvgNetflix))
print("hulu: " + str(rtAvgHulu))
print("Disney: " + str(rtAvgDisney))
print("Prime Video: " + str(rtAvgPrimeVideo))

plt.plot([1,2,3] , [2,4,5])
plt.show()