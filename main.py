import sys
import pafy
from pytube import YouTube
import requests
import time
import bs4
import vlc
import simpleaudio as sa
import youtube_dl


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
    return (most_relevant_title, most_relevant_url)


def download(url):
    # yt = YouTube(url)
    # stream = yt.streams.filter(only_audio=True).all()[2]
    # return stream.download("/tmp")

    # ydl_opts = {
    #     'postprocessors': [{
    #         'key': 'FFmpegExtractAudio',
    #         'preferredcodec': 'mp3',
    #         'preferredquality': '128',
    #     }],
    # }
    # with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    #     ydl.download([url])

    instance = vlc.Instance()

    # Create a MediaPlayer with the default instance
    player = instance.media_player_new()

    # Load the media file
    media = instance.media_new("Quavo - W O R K I N  M E-nmjgIrBHg6Y.mp3")


    # Add the media to the player
    player.set_media(media)

    print(media.get_duration())

    # Play for 10 seconds then exit
    player.play()
    time.sleep(10)
    #
    # p = vlc.MediaPlayer(url)
    # p.play()


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
    start_time = time.time()
    result = grab_search_query("work in me")
    print(download(result[1]))
    print("--- %s seconds ---" % (time.time() - start_time))
