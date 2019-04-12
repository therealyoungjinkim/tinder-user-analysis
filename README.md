# tinder-user-analysis

idea:
get the demographics and sentiment analysis of tinder users the app tries to set me up with

contents:
scrape tinder.py - short code mainly using PyAutoGui to mine the data. instructions in comments but would not suggest use
tinderdata.csv - the uncleaned data gotten from the tinder webapp3
tindercleaning.Rmd - the code used to clean up the data
cleantinder.csv - the 'cleaned' and feature engineered data
report.html - the actual report for easy readin

process:
1) python script to get data from the javascript, and also to 'like' the user (as liked users will not show up again.
  650 observations before getting cut off by tinder. 

2) clean up the data as done in the tindercleaning rmd file

3) EDA and some basic nlp via tidytext's sentiment analysis using the bing standard
