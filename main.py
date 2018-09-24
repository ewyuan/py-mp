import pafy
import requests
import time
import bs4
import vlc
import youtube_dl
import pdb
import re

from player import Player

# paused = False
#
def grab_search_query(search_query):
    """
    Returns the most relevant URL with the corresponding search query.

    :param search_query: str
    :return: str
    """
    search_query = search_query.replace(" ", "+")
    base_url = "https://www.youtube.com"
    url = base_url + "/results?sp=EgIQAVAU&q=" + search_query
    session = requests.get(url=url)
    soup = bs4.BeautifulSoup(session.content, "html.parser")
    videos = soup.findAll('a', attrs={'class': 'yt-uix-tile-link'})
    regex = re.compile("^/watch\?v=.*$")
    filtered_videos = []
    for item in videos:
        if regex.search(item["href"]):
            filtered_videos.append(item["href"])
    most_relevant_url = base_url + filtered_videos[0]
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
    start_time = time.time()
    prompt_printed = False
    user_opt = 'none'
    while True:
        if not prompt_printed:
            user_opt = input("Enter control option (Type 'help' for list of available options): ")
            prompt_printed = True
        else:
            if user_opt == 'help':
                print("\n"
                      "add [song] - Adds [song] to the queue\n"
                      "clear - Clears the queue\n"
                      "pause - Pause the current song\n"
                      "resume - Resumes the current song\n"
                      "queue - Prints the current queue\n"
                      "skip - Plays the next song in queue\n"
                      "exit - Exits the program")

            elif user_opt[0:3] == 'add':
                query = user_opt[4:]
                url = grab_search_query(query)
                player.add_song(url)
                print("Added " + query + " to queue.")

            elif user_opt == 'clear':
                player.clear_queue()
                print("Cleared the queue.")

            elif user_opt == "queue": # not displaying queue properly
                output = ""
                queue = player.get_queue()
                for i in range(len(queue)):
                    output += "[" + str(i + 1) + "] - " + queue[i].get_title() + "\n"
                print(queue)

            elif user_opt == 'pause':
                player.pause()
                print("Pausing " + player.get_current_song().get_title() + ".")

            elif user_opt == 'resume':
                player.resume()
                print("Resuming " + player.get_current_song().get_title() + ".")

            elif user_opt == 'skip':
                player.skip()
                print("Skipping " + player.get_previous_song().get_title() + ".")

            elif user_opt == 'exit':
                break

            else:
                print("Option " + user_opt + " not supported.")

            prompt_printed = False
