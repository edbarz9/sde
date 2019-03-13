import feedparser

thinkerviewFeed = "https://www.youtube.com/feeds/videos.xml?channel_id=UCQgWpmt02UtJkyO32HGUASQ"
dirtyBiologyFeed = "https://www.youtube.com/feeds/videos.xml?channel_id=UCtqICqGbPSbTN09K1_7VZ3Q"

feeds = [thinkerviewFeed,dirtyBiologyFeed]

NewsFeed = feedparser.parse(thinkerviewFeed)
print('Number of RSS posts :', len(NewsFeed.entries))
for i in range(5):
    print(NewsFeed.entries[i].title)
    print(NewsFeed.entries[i].link)
    print(NewsFeed.entries[i].published)
