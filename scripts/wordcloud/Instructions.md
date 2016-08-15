## Instructions for creating a wordcloud in R

#### First, make sure that wordcount.csv has been saved to the S3 bucket (docoverload in our example)

#### Cleaning: download wordcount.csv from S3 and open in excel
	- Sort by wordcount, descending. Remove the most common words (if desired): the, and, in, for, be, by, is, shall, that, this, as, with, on, such, at, has, from, its, an, it, if, To, If
	- Label column 1 "text" and column 2 "frequency"

#### Install and open R

#### Run R code
 - Change path name to suit your machine
 - Can adjust parameters to show different outputs as desired. For example:
    - `min.freq=INT` : can adjust int so that words that show up LESS frequently than that number are NOT part of the wordcloud
    - `max.words=INT` : set the total number of words you want included in the word cloud
    - `

