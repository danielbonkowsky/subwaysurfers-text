from goose3 import Goose
import subprocess
import sys

def newspaper_text_extraction(article_url):
    g = Goose()
    article = g.extract(article_url)
    return article.cleaned_text, article.title

subprocess.check_call([sys.executable, "-m", "pip", "install", 'goose3'])

from goose3 import Goose

article_url = "https://www.latimes.com/california/story/2024-04-04/electric-and-hybrid-cars-are-set-to-lose-carpool-access-what-you-need-to-know"
text, title = newspaper_text_extraction(article_url=article_url)
print(title)
print(text)