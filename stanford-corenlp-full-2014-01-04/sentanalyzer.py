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

        if file[-14:]!='_sentiment.txt':
            song = check_output(['java', '-cp', "*", '-mx5g', 'edu.stanford.nlp.sentiment.SentimentPipeline', '-file', subdir+'/'+file])
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
            elif totalpos>3:
                albums[alb][1] += 1
            elif totalpos<-10:
                albums[alb][4] += 1
            elif totalpos<-3:
                albums[alb][3] += 1
            else:
                albums[alb][2] += 1
            albums[alb][5][songtitle] = [vpos, pos, neut, neg, vneg, subdir+'/'+file, subdir+'/'+songtitle+'_sentiment.txt']

            f = open(subdir+'/'+songtitle+'_sentiment.txt', 'w')
            f.write(sentlines)
            f.close()
        print 'album= '+alb+' song='+file[:-4]

albumcsvlines = ''
for album, info in albums.iteritems():
    songcsvlines = ''
    albumcsvlines += album+','+str(info[0])+','+str(info[1])+','+str(info[2])+','+str(info[3])+','+str(info[4])+','+album+'.csv'+'\n'
    for song, data in info[5].iteritems():
        songcsvlines+=song+','+str(data[0])+','+str(data[1])+','+str(data[2])+','+str(data[3])+','+str(data[4])+','+str(data[5])+','+str(data[6])+'\n'
    f = open(album+'.csv', 'w')
    f.write(songcsvlines)
    f.close()
f = open('artist.csv', 'w')
f.write(albumcsvlines)
f.close()