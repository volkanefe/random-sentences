import random, csv, os


if os.path.exists('sentences.csv'):
    os.remove('sentences.csv')

number = 0
sentences = []
subjectList = []
verbList = []
timeList = []

subjectDosya = open('subject.txt', 'r')
subjectRows = subjectDosya.readlines()
for subjectRow in subjectRows:
    subjectList.append(subjectRow)

verbDosya = open('verb.txt', 'r')
verbRows = verbDosya.readlines()
for verbRow in verbRows:
    verbList.append(verbRow)

timeDosya = open('time.txt', 'r')
timeRows = timeDosya.readlines()
for timeRow in timeRows:
    timeList.append(timeRow)

while number < 2300:
        sentence = str(random.choice(subjectList)).strip() + " " + str(random.choice(verbList)).strip() + " " + str(random.choice(timeList)).strip()
        if sentence not in sentences:
            sentences.append(sentence)
        number += 1

with open('sentences.csv', 'w', newline="") as csv_file:
    writer = csv.writer(csv_file)
    for Row in sentences:
        writer.writerow(str(Row).splitlines())






