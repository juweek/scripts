import csv
import collections

raceTotals = collections.Counter() #racial identity groups and numbers
genderTotals = collections.Counter() #gender identity groups and numbers
deliveryTotals = collections.Counter() #gender identity groups and numbers

raceLevels = collections.Counter() #racial identity groups and numbers in each job level
genderLevels = collections.Counter() #gender identity groups and numbers in each job level
deliveryLevels = collections.Counter() #gender identity groups and numbers in each job level


mixedEmployees = 0
rowcount = 0

#iterate over each row in file. on each row, store the race, the gender, the race + job level, and the gender + job level
with open('responses.csv') as file:
    reader = csv.reader(file)

    #for each row, go into the file and get the race
    for row in reader:
        rowcount = rowcount + 1
        #break up multiple answers into list
        currentRaces = row[1].split(',')
        currentGenderIdentities = row[4].split(',')

        if len(currentRaces) > 1:
            #add count for mixed groups
            mixedEmployees = mixedEmployees + 1
        for race in currentRaces:
            #combine race and job level, then store
            raceTotals[race] += 1
            raceLevel = race + row[2]
            isDelivery = race + row[7]
            raceLevels[raceLevel] +=1
            deliveryLevels[isDelivery] +=1
        for gender in currentGenderIdentities:
            #combine gender and job level, then store
            genderTotals[gender] += 1
            genderLevel = gender + row[2]
            isDelivery = gender + row[7]
            genderLevels[genderLevel] +=1
            deliveryLevels[isDelivery] +=1


print('Total responses ', rowcount)
print('\n')
print('More than one race ', mixedEmployees)
print('\n')
print ("\n".join(map(str, raceTotals.most_common())))
print('\n')
print ("\n".join(map(str, raceLevels.most_common())))
print('\n')
print ("\n".join(map(str, genderTotals.most_common())))
print('\n')
print ("\n".join(map(str, genderLevels.most_common())))
print('\n')
print ("\n".join(map(str, deliveryLevels.most_common())))


