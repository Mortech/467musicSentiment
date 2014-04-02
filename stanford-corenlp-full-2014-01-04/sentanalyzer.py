from subprocess import check_output

stuff = check_output(['java -cp "*" -mx5g edu.stanford.nlp.sentiment.SentimentPipeline -file input.txt'], shell=True)

print "output is: "+stuff