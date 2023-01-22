from requests_html import HTMLSession
import pandas as pd

session=HTMLSession()
url="https://www.youtube.com/@OdinSchool/videos"

r=session.get(url)
r.html.render(sleep=1, keep_page=True, scrolldown=1)
videos=r.html.find('#dismissible')
videoDict={}

for item in videos:
    video={
        "title": item.text,
        "link": item.absolute_links

    }
    print(video)



