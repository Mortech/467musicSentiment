from subprocess import check_output
import os

stuff = check_output(['java -cp "*" -mx5g edu.stanford.nlp.sentiment.SentimentPipeline -file ../lyrics/queen/doingallright.txt'], shell=True)

print stuff

#for subdir, dirs, files in os.walk('../lyrics/'):
#    for file in files:
#        print subdir+'/'+file