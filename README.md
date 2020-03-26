# TwitterSentimentAnalyzer
Based on code from Siraj Rival (You Tube) and expanded to allow for data persistence, periodic sentiment analysis, and command line or console arguments. https://www.youtube.com/watch?v=o_OZdbCzHUA

To use the program yourself, sign up for a twitter API at https://apps.twitter.com/

## Example usage and output
Command line args are:
- Number of iterations (int)
- Number of minutes between each iteration (float)
- All other strings are treated as search keywords
```
$ python twitterSentiment.py 10 .3 COVID-19 covid coronavirus corona-virus pandemic China rabbits
COVID-19
covid
coronavirus
corona-virus
pandemic
China
rabbits
%9.85 Current avg sentiment, with 15 new tweet(s) about COVID-19
%-13.16 Current avg sentiment, with 15 new tweet(s) about covid
%4.05 Current avg sentiment, with 14 new tweet(s) about coronavirus
%0.13 Current avg sentiment, with 13 new tweet(s) about corona-virus
%2.21 Current avg sentiment, with 15 new tweet(s) about pandemic
%11.90 Current avg sentiment, with 14 new tweet(s) about China
%5.08 Current avg sentiment, with 10 new tweet(s) about rabbits
%7.18 Current avg sentiment, with 13 new tweet(s) about COVID-19
%-6.02 Current avg sentiment, with 15 new tweet(s) about covid
%0.53 Current avg sentiment, with 15 new tweet(s) about coronavirus
%-0.85 Current avg sentiment, with 13 new tweet(s) about corona-virus
%3.80 Current avg sentiment, with 13 new tweet(s) about pandemic
%5.90 Current avg sentiment, with 15 new tweet(s) about China
%4.62 Current avg sentiment, with 1 new tweet(s) about rabbits
```
