from colorama import init, Fore, Back, Style
import click
from scrapper import fetchNews

@click.command()
@click.option("--category",
              default="",
              type=click.Choice(["", "national", "business", "sports", "world",
                            "politics", "technology", "startup", "entertainment",
                            "miscellaneous", "hatke", "science", "automobile"]))
def inshorts(category):
    news = fetchNews(category)
    if news['success'] == False:
        print(Fore.RED + Style.BRIGHT + news["errorMessage"])


if __name__ == "__main__":
    init()
    inshorts()