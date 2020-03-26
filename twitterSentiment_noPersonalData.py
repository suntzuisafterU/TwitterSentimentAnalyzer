

from textblob import TextBlob
import tweepy
import Statistics as Stat
import time
import pickle
import os.path
import sys
from colorama import init, Fore, Back, Style

#TODO: Implement this program with apscheduler to assess it's function.
# https://apscheduler.readthedocs.io/en/latest/userguide.html

def get_api():
    # TODO: Register for a twitter app, gives you access to api.
    #
    # <your app name here>
    # Owner: <you fill>
    # Owner ID: <you fill>
    #
    # <you fill> (api key)
    # <you fill> (API secret)
    #
    # Access token: <you fill>
    # Access token secret: <you fill>

    # FULL API function stub
    consumer_key = 
    secret_key = 

    access_token = 
    access_token_secret = 

    auth = tweepy.OAuthHandler(consumer_key, secret_key)
    auth.set_access_token(access_token, access_token_secret)

    api = tweepy.API(auth)
    return api


def analyze_tweets(search_param, param_stat, api):
    public_tweets = api.search(search_param)
    tweets_queue = param_stat.get_tweets()

    f1 = open("sentimentTextFiles\\" + search_param + "Sentiment.txt", 'w')

    new_tweets = 0
    # analyse any new tweets
    for tweet in public_tweets:
        if tweet.text not in tweets_queue and not tweet.retweeted:
            analysis = TextBlob(tweet.text)
            if analysis[0] != 0.0:
                param_stat.add(analysis.sentiment[0])
                tweets_queue.append(tweet.text)
                new_tweets += 1

    # calculate and print the averages
    avg = format(param_stat.get_avg() * 100, ".2f")
    if float(avg) >= 0:
        print(Fore.GREEN + "%" + avg + Fore.RESET, "Current avg sentiment, with", new_tweets,
              "new tweet(s) about", Fore.BLUE + search_param + Fore.RESET)
    else:
        print(Fore.RED + "%" + avg + Fore.RESET , "Current avg sentiment, with", new_tweets,
              "new tweet(s) about", Fore.BLUE + search_param + Fore.RESET)
    f1.write("%" + avg + " latest average sentiment recorded on " + time.asctime() + " for search term " + search_param)
    f1.close()


def save_object(obj, filename):
    with open(filename, 'wb') as output:  # Overwrites any existing file.
        pickle.dump(obj, output, pickle.HIGHEST_PROTOCOL)


if __name__ == "__main__":
    # Initialize list for search queries
    sp_list = []
    """
    if command line args used:
    Command line args:
        Number of desired iterations (int)
        Length of sleep between iterations in minutes (float)
        Every additional string is treated as a search param (any word, I used ticker symbols.)
    """
    if len(sys.argv) > 1:
        iterations = int(sys.argv[1])
        interval = float(sys.argv[2])
        for x in range(3, len(sys.argv)):
            print(sys.argv[x])
            assert isinstance(sys.argv[x], str), "Non-string argument entered from the command line."
            tempStr = sys.argv[x].lstrip().rstrip()
            sp_list.append(tempStr)
    # else ask for console input
    else:
        iterations = int(input("How many times would you like the program to iterate?: "))
        interval = float(input("Enter your desired interval in minutes: "))
        done = False
        print("Enter 'START' once you have entered all desired search terms.")
        while not done:
            searchTerm = input("Enter a desired search term: ")
            searchTerm.lstrip().rstrip()
            #TODO: Add 'or list of terms separated by anything' functionality.
            if searchTerm != "START" and searchTerm != "":
                assert isinstance(searchTerm, str), "Non-string argument entered from console."
                sp_list.append(searchTerm)
            elif searchTerm == "START":
                done = True
            # else: pass

    # check if we have an existing pickle jar
    if os.path.exists("stat_dict.pkl"):
        # load pickle
        with open('stat_dict.pkl', 'rb') as oldJarOfPickles:
            stat_dict = pickle.load(oldJarOfPickles)
        # add any new queries
        keys = stat_dict.keys()
        for search in sp_list:
            assert isinstance(search, str)
            if search not in keys:
                stat_dict[search] = Stat.Statistics(search)

    # if there is no pickle file, create a whole new dict of Statistics objects
    else:
        stat_dict = {}
        for search in sp_list:
            assert isinstance(search, str)
            stat_dict[search] = Stat.Statistics(search)

    # get api
    api = get_api()

    # initialize dictionary of color strings
    init(convert=True)

    # Analyse tweets
    for j in range(iterations):
        for item in sp_list:
            assert isinstance(item, str), "Non-string param"
            analyze_tweets(item, stat_dict[item], api)
        time.sleep(60*interval)

    # Save the dictionary of Statistics ADT's
    save_object(stat_dict, "stat_dict.pkl")
    sys.exit()
