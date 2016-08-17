# Run in R

## Installing necessary packages
install.packages("wordcloud")
library(wordcloud)

## Importing data
wordcount = read.csv("~/Desktop/wordcloud/wordcount.csv", header=TRUE)

## Creating the wordcloud
wordcloud(wordcount$text,wordcount$frequency,scale=c(4,.5),min.freq=3,max.words=100, random.color=TRUE, rot.per=.1,ordered.colors=FALSE,use.r.layout=FALSE, fixed.asp=TRUE)
