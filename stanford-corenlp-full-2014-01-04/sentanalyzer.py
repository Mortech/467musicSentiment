from subprocess import check_output
import os

#In data folder we need

#Albums csv file with folowing format:
#Album, #Vpossongs, #possongs, #neutralsongs, #negsongs, #Vnegsongs, songsfilename

#Songs csv file with following format:
#song, #Vposlines, #poslines, #neutrallines, #neglines, #Vneglines, location, sentimentfile


albums = {}

for subdir, dirs, files in os.walk('../lyrics/'):
    for file in files:
        alb = subdir[len('../lyrics/'):]
        if alb not in albums:
            albums[alb] = [0,0,0,0,0,{}]


        song = check_output(['java -cp "*" -mx5g edu.stanford.nlp.sentiment.SentimentPipeline -file '+subdir+'/'+file], shell=True)
        songtitle = file[:-4]
        i=0
        vpos=0
        pos=0
        neut=0
        neg=0
        vneg=0
        totalpos = 0
        sentlines= ''
        for line in song.split('\n'):
            if i%2==1:
                line = line[2:]
                sentlines += line + '\n'
                if line=='Very positive':
                    totalpos += 5
                    vpos += 1
                if line=='Positive':
                    totalpos += 1
                    pos += 1
                if line=='Neutral':
                    neut += 1
                if line=='Negative':
                    totalpos -= 1
                    neg += 1
                if line=='Very negative':
                    totalpos -= 5
                    vneg += 1
            i+=1
        if totalpos>10:
            albums[alb][0] += 1
        else if totalpos>3:
            albums[alb][1] += 1
        else if totalpos<-10:
            albums[alb][4] += 1
        else if totalpos<-3:
            albums[alb][3] += 1
        else:
            albums[alb][2] += 1
        albums[alb][5][songtitle] = [vpos, pos, neut, neg, vneg, subdir+'/'+file, subdir+'/'+songtitle+'_sentiment.txt']

        f = open(subdir+'/'+songtitle+'_sentiment.txt', 'w')
        f.write(sentlines)
        f.close()

albumcsvlines = ''
for album, info in albums:
    songcsvlines = ''
    albumcsvlines += album+','+info[0]+','+info[1]+','+info[2]+','+info[3]+','+info[4]+','+album+'.csv'+'\n'
    for song, data in info[5]:
        songcsvlines+=song+','+data[0]+','+data[1]+','+data[2]+','+data[3]+','+data[4]+','+data[5]+','+data[6]+'\n'
    f = open(album+'.csv', 'w')
    f.write(songcsvlines)
    f.close()
f = open('artist.csv', 'w')
f.write(albumcsvlines)
f.close()
