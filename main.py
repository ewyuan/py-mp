import pafy
import requests
import time
import bs4
import vlc
import youtube_dl
from player import Player

# paused = False
#
def grab_search_query(search_query):
    """
    Returns the most relevant URL with the corresponding search query.

    :param search_query: str
    :return: str
    """
    search_query.replace(" ", "+")
    base_url = "https://www.youtube.com"
    url = base_url + "/results?sp=EgIQAVAU&q=" + search_query
    session = requests.get(url=url)
    soup = bs4.BeautifulSoup(session.content, "html.parser")
    videos = soup.findAll('a', attrs={'class': 'yt-uix-tile-link'})

    most_relevant_url = base_url + videos[0]["href"]
    return most_relevant_url
#
# def play_audio(url):
#     audio = pafy.new(url)
#     best_audio_url = audio.getbestaudio().url
#
#     # Create a new vlc instance
#     vlc_instance = vlc.Instance()
#     # Create a new media player instance
#     media_player = vlc_instance.media_player_new()
#     # Create a new media instance
#     media = vlc_instance.media_new(best_audio_url)
#
#     # Set the media and start the player
#     media_player.set_media(media)
#     media_player.play()
#
#     global paused
#
#     starting_time = time.time()
#     prompt_printed = False
#     user_opt = 'none'
#     while (time.time() - starting_time) < audio.length:
#         if not prompt_printed:
#             user_opt = input('Enter control option (type help for list of available options): ')
#             prompt_printed = True
#         else:
#             if user_opt == 'help':
#                 print("\npause - Pause the current song\nresume - Resumes the current song\nstop - Stop playing the current song\n")
#
#             elif user_opt == 'pause':
#                 media_player.set_pause(True)
#                 print("Song has been paused.")
#
#             elif user_opt == 'resume':
#                 media_player.set_pause(False)
#                 print("Resuming song.")
#
#             elif user_opt == 'stop':
#                 media_player.stop()
#                 print("Song has been stopped.")
#                 break
#
#             else:
#                 print("Option " + user_opt + " not supported.")
#
#             prompt_printed = False
#
#     print("Song completed in " + str(time.time() - starting_time) + "s")


if __name__ == "__main__":
    player = Player()
    search_query = input("Please enter the song you are searching for: ")
    url = grab_search_query(search_query)
    player.add_song(url)
    player.play()
    # start_time = time.time()
    # song_name = input("Please enter the song you are searching for: ")
    # result = grab_search_query(song_name)
    # play_audio(result[1])
    # print("--- %s seconds ---" % (time.time() - start_time))
