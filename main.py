import sys
import pafy
import youtube_dl
import requests
import time
import bs4
import vlc
import simpleaudio as sa


def grab_search_query(search_query):
    """
    Returns a tuple containing the most relevant title and its URL with the corresponding search query.

    :param search_query: str
    :return: tuple(str, str)
    """
    search_query.replace(" ", "+")
    base_url = "https://www.youtube.com"
    url = base_url + "/results?sp=EgIQAVAU&q=" + search_query
    session = requests.get(url=url)
    soup = bs4.BeautifulSoup(session.content, "html.parser")
    videos = soup.findAll('a', attrs={'class': 'yt-uix-tile-link'})

    most_relevant_title = videos[0]["title"]
    most_relevant_url = base_url + videos[0]["href"]
    return (most_relevant_title, most_relevant_title)



def test(url):
    audio = pafy.new(url)
    best = audio.audiostreams[0]
    instance = vlc.Instance('--input-repeat=-1', '--fullscreen')

    # Define VLC player
    player = instance.media_player_new()

    # Define VLC media
    media = instance.media_new(best)

    # Set player media
    player.set_media(media)

    # Play the media
    player.play()

    time.sleep(10)




if __name__ == "__main__":
    grab_search_query("work in me")
    # a = search_youtube("workinme")
    # print(a)
    # test("https://www.youtube.com/watch?v=nmjgIrBHg6Y")
