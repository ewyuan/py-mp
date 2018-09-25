import requests
import bs4
import threading
import re
from player import Player


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


def handle_inputs(player):
    search_query = input("Please enter the song you are searching for: ")
    url = grab_search_query(search_query)
    player.add_song(url)
    prompt_printed = False
    user_opt = ""
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
                      "cur - Get the title of the current song\n"
                      "prev - Get the title of the previous song\n"
                      "next - Get the title of the next song\n"
                      "rewind - Restart the current song\n"
                      "remove [pos] - Removes the song in position [pos] from the q\n"
                      "exit - Exits the program\n")

            elif user_opt[0:3] == 'add':
                query = user_opt[4:]
                url = grab_search_query(query)
                player.add_song(url)
                print("Added '" + query + "' to queue.")

            elif user_opt == 'clear':
                player.clear_queue()
                print("Cleared the queue.")

            elif user_opt == 'pause':
                player.pause()
                print("Pausing '" + player.get_current_song().get_title() + "'.")

            elif user_opt == 'resume':
                player.resume()
                print("Resuming '" + player.get_current_song().get_title() + "'.")

            elif user_opt == "queue":  # not displaying queue properly
                output = ""
                queue = player.get_queue()
                for i in range(len(queue)):
                    output += "[" + str(i + 1) + "] - " + queue[i].get_title() + "\n"
                print(output)

            elif user_opt == 'skip':
                player.skip()
                print("Skipping '" + player.get_previous_song().get_title() + "'.")

            elif user_opt == 'cur':
                cur_song = player.get_current_song()
                if cur_song is not None:
                    print("'" + cur_song.get_title() + "'.")
                else:
                    print("No song is currently playing.")

            elif user_opt == 'prev':
                prev_song = player.get_previous_song()
                if prev_song is not None:
                    print("'" + prev_song.get_title() + "'.")
                else:
                    print("No song was previously playing.")

            elif user_opt == 'next':
                next_song = player.get_next_song()
                if next_song is not None:
                    print("'" + next_song.get_title() + "'.")
                else:
                    print("No song is queued up to play next.")

            elif user_opt == 'rewind':
                player.rewind()

            elif user_opt[0:6] == 'remove':
                pos_not_int = False
                try:
                    pos = int(user_opt[7:]) - 1
                except:
                    print("Illegal position entered.")
                    pos_not_int = True

                if not pos_not_int:
                    if pos >= player.get_queue_size() or pos < 0:
                        print("Illegal position entered.")
                    else:
                        removed_song = player.remove_song(pos)
                        print("Removed " + removed_song.get_title() + " from queue")

            elif user_opt == 'exit':
                break

            else:
                print("Option '" + user_opt + "' not supported.")

            prompt_printed = False


if __name__ == "__main__":
    player = Player()
    input_thread = threading.Thread(target=handle_inputs, args=(player,))
    input_thread.start()
    while True:
        if player.get_state().value == 6:
            player.play_next()
        if threading.active_count() != 2:
            break
