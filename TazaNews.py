#!/usr/bin/env python3
import os

from gtts import gTTS
from newsapi import NewsApiClient
from playsound import playsound
import pyttsx3
from functools import lru_cache
import pyttsx3


def text_to_speech_pyttsx3(text):
    """
    a speech method using pyttsx3 module
    :param text: take the text data to convert it to speech
    :return:  None
    """
    try:
        engine = pyttsx3.init()

        # Set properties
        engine.setProperty(
            "rate",
            180,
        )  # Speed (words per minute)
        engine.setProperty("volume", 1)  # Volume (0.0 to 1.0)
        voices = engine.getProperty("voices")
        engine.setProperty(
            "voice", voices[33].id
        )  # Change index based on your preference

        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        print(f"An error occurred: {e}")
@lru_cache(maxsize=1)
def speak(data, lang="en"):
    """

    :param data: the text data to convert it to speech
    :param lang:  en statnd for english
    :return: None
    """
    try:
        # generate speech
        tts = gTTS(data, lang=lang, slow=False)
        audio_file = (
            "outputnews.mp3"  # save file to the same dir where program is running..
        )
        tts.save(audio_file)
        playsound(audio_file)
        os.remove(audio_file)
    except Exception as e:
        print(f"Error in text to speech{e}")


class TypesOfNews:
    def __init__(
        self,
        apikey,
    ):
        self.news = NewsApiClient(api_key=apikey)

    try:
        # latestnews = news.get_everything(q='latest',language='en',page_size=10)
        # latestnewsnow = news.get_top_headlines(q='latest',language='en',page_size=30,country='in')
        def toptechnews(self,pagesize):
            news = self.news
            top_headlines_tech = news.get_everything(
                q="technology",
                language="en",
                page_size=pagesize,
                sources="the-verge,ars-technica ,"
                "crypto-coins-news,engadget,"
                "hacker-news,techradar,recode,"
                "techcrunch,the-next-web,wired",
                sort_by="publishedAt",
            )
            newsdata = (top_headlines_tech)["articles"]
            newlist = []
            for news in newsdata:
                if (news["title"]) != "[Removed]":
                    newlist.append((news["title"], news["description"],news['url']))

            for i,news in enumerate(newlist):
                print(f"{i+1} -  {news[0]} \n:--{news[1]}\n Link - {news[2]}")
                print("-------------------------------------------------"
                      "------------------------------"
                      "-------------------------------------------------------------------------")
            return newlist

        def topGeneralNews(self,pagesize):
            news = self.news
            top_headlines_tech = news.get_everything(
                q="latest",
                language="en",
                page_size=pagesize,
                sources="the-times-of-india,the-hindu,abc-news,abc-news-au,al-jazeera-english,associated-press,"
                "bbc-news,cnn,cbs-news,google-news,google-news-in,national-geographic,"
                "msnbc,nbc-news,rte",
                sort_by="publishedAt",
            )
            newsdata = (top_headlines_tech)["articles"]
            newlist = []
            for news in newsdata:
                if (news["title"]) != "[Removed]":
                    newlist.append((news["title"], news["description"], news['url']))

            for i, news in enumerate(newlist):
                print(f"{i + 1} -  {news[0]} \n:--{news[1]}\n Link - {news[2]}")
                print("-------------------------------------------------"
                      "------------------------------"
                      "-------------------------------------------------------------------------")
            return newlist

        def topHealthandScienceNews(self,pagesize):
            news = self.news
            top_headlines_tech = news.get_everything(
                q="latest",
                language="en",
                page_size=pagesize,
                sources="medical-news-today,national-geographic,"
                "new-scientist,next-big-future",
                sort_by="publishedAt",
            )
            newsdata = (top_headlines_tech)["articles"]
            newlist = []
            for news in newsdata:
                if (news["title"]) != "[Removed]":
                    newlist.append((news["title"], news["description"], news['url']))

            for i, news in enumerate(newlist):
                print(f"{i + 1} -  {news[0]} \n:--{news[1]}\n Link - {news[2]}")
                print("-------------------------------------------------"
                      "------------------------------"
                      "-------------------------------------------------------------------------")
            return newlist

        def topSportsNews(self,pagesize):
            news = self.news
            top_headlines_tech = news.get_top_headlines(
                q="latest",
                language="en",
                page_size=pagesize,
                sources="bbc-sport,bleacher-report,espn-cric-info,"
                "espn,fox-sports,the-sport-bible",
                # sort_by='relevancy'
            )
            newsdata = (top_headlines_tech)["articles"]
            newlist = []
            for news in newsdata:
                if (news["title"]) != "[Removed]":
                    newlist.append((news["title"], news["description"], news['url']))

            for i, news in enumerate(newlist):
                print(f"{i + 1} -  {news[0]} \n:--{news[1]}\n Link - {news[2]}")
                print("-------------------------------------------------"
                      "------------------------------"
                      "-------------------------------------------------------------------------")
            return newlist

    except Exception as e:
        print("error fetching news :", e)


def data_to_text(datalist):

    if not datalist:
        return "No Latest news available ..."
    news = "Here are some top picked latest news for you Sir ! ."
    for index, article in enumerate(datalist):
        news += f" news {index+1}... Headline of news, {article[0]}. ;and here are  some details about that;{article[1]} "
    return news


def main():
    apikey = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"// give your apikey here...
    while True:
        try:
            news = TypesOfNews(apikey)  # creating an instance of the class.
            speak("Enter your choice : ..\n 1 - For tech news..\n 2 - For "
                    "general news..\n 3 - For health and science news . and ..\n 4 - For sports news  .. and"
                  "type exit .. to exit the application .. ")
            choice = (
                input(
                    "Enter your choice : \n 1 - For tech news\n 2 - For "
                    "general news\n 3 - For health and science news\n 4 - For sports news \n And exit to e"
                    "xit the application\n  Your choice :"
                )
            )
            if choice == 'exit' or choice == 'Exit':
                speak("Exiting the application sir! .. have ... a good day  ... sir!")
                exit()
            speak("Enter how many headline you want :")
            pagesize = int((input)("Enter how many headline you want :"))

        except Exception as e:
            speak("Please Enter valid choice or Number  of headlines")
            print("Please Enter valid choice or NO. of headlines")
            continue
        if int(choice) == 1:


            newsfeched = news.toptechnews(int(pagesize))
            # print(newsfeched)
            news = data_to_text(newsfeched)
            # print(news)
            speak(news)
        elif int(choice) == 2:
            newsfeched = news.topGeneralNews(int(pagesize))
            news = data_to_text(newsfeched)
            # print(news)
            speak(news)
        elif int(choice) == 3:
            newsfetched = news.topHealthandScienceNews(int(pagesize))
            news = data_to_text(newsfetched)
            # print(news)
            speak(news)

        elif int(choice) == 4:
            newsfetched = news.topSportsNews(int(pagesize))
            news = data_to_text(newsfetched)
            # print(news)
            speak(news)

        else:
            speak("Invalid ; choice ... or Number of headlines ; please choose ... from following choices ")


if __name__ == "__main__":
    main()
