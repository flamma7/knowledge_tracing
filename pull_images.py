# load in words
# acquire pictures
# approve/deny pictures & repeat
"""
Word source: https://sightwords.com/sight-words/fry/
Approval process
- accept/deny whether to use that word
- accept/deny/forget the picture (forget means no picture for the word)
"""
# acquire sound files
# Push all that to mongo


from gtts import gTTS
from icrawler.builtin import GoogleImageCrawler

with open("words.txt", "r") as f:
    words = f.readlines()[0].split(",")

for i, w in enumerate(words):
    print(i)

    # Grab images
    # google_Crawler = GoogleImageCrawler(storage = {'root_dir': f'images/{w}'})
    # google_Crawler.crawl(keyword = w, max_num = 10)

    # Grab audio
    # text = "Global warming is the long-term rise in the average temperature of the Earth’s climate system"
    # lang = "en"
    # speech = gTTS(text=w, lang=lang, slow=False)
    # speech.save(f"audio/{w}.mp3")
