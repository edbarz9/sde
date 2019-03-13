import feedparser

thinkerviewFeed = "https://www.youtube.com/feeds/videos.xml?channel_id=UCQgWpmt02UtJkyO32HGUASQ"

NewsFeed = feedparser.parse(thinkerviewFeed)
print('Number of RSS posts :', len(NewsFeed.entries))
for i in range(5):
    print(NewsFeed.entries[i].title)
    print(NewsFeed.entries[i].link)
    print(NewsFeed.entries[i].published)
