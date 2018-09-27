import requests
import bs4
import re

def grab_search_query(search_query):
    """
    Returns the most relevant URL with the corresponding search query.

    :param search_query: str
    :return: str
    """
    search_query = search_query.replace(" ", "+")
    base_url = "https://www.youtube.com"
    url = base_url + "/results?sp=EgIQAVAU&q=" + search_query
    try:
        session = requests.get(url=url)
        soup = bs4.BeautifulSoup(session.content, "html.parser")
        videos = soup.findAll('a', attrs={'class': 'yt-uix-tile-link'})

        regex = re.compile("^/watch\?v=.*$")
        filtered_videos = []

        for item in videos:
            if regex.search(item["href"]):
                filtered_videos.append(item["href"])

        if len(filtered_videos) == 0:
            return None

        most_relevant_url = base_url + filtered_videos[0]
        return most_relevant_url
    except:
        return None

def grab_search_query_list(search_query):
    """
    Returns the (up to ) 10 most relevant URLs with the corresponding search query.

    :param search_query: str
    :return: list
    """
    try:
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
                filtered_videos.append((base_url + item["href"],item["title"]))

        return filtered_videos
    except:
        return None

def handle_inputs(player):
    """
    Prompts the user for input and handles options they select.

    :return: None
    """
    prompt_printed = False
    user_opt = ""
    while True:
        if not prompt_printed:
            user_input = input("Enter control option (Type 'help' for list of available options): ")

            user_opt = user_input.split(' ', 1)[0]
            args = ""
            try:
                args = user_input.split(' ', 1)[1]
            except:
                pass

            prompt_printed = True
        else:
            if user_opt == 'help':
                print("\n"
                      "add [song] - Adds [song] to the queue\n"
                      "add-list [song] - Lists top 10 songs found and lets you pick which to add\n"
                      "clear - Clears the queue\n"
                      "pause - Pause the current song\n"
                      "resume - Resumes the current song\n"
                      "queue - Prints the current queue\n"
                      "skip - Plays the next song in queue\n"
                      "cur - Get the title of the current song\n"
                      "time - Get the time of the current song\n"
                      "prev - Get the title of the previous song\n"
                      "rewind - Restart the current song\n"
                      "remove [pos] - Removes the song in position [pos] from the q\n"
                      "play [song] - Stops the current song and plays [song] instead\n"
                      "play-list [song] - Lists top 10 songs found and lets you pick which to play\n"
                      "volume [+/-] - Increase or decreases the volume by 10%% for each + or -\n"
                      "exit - Exits the program\n")

            elif user_opt == 'add-list':
                if len(args) > 0:
                    urls = grab_search_query_list(args)

                    if len(urls) == 0:
                        print("Song '" + args + "' not found.")
                    else:
                        display_list = 'n'
                        cur_pos = 0
                        song_selected = False
                        while display_list == 'n' and cur_pos < len(urls):
                            output = ""
                            loop_amount = min(10, len(urls)-cur_pos)
                            for i in range(loop_amount):
                                output += "[" + str(i+cur_pos + 1) + "] - " + urls[i+cur_pos][1] + "\n"
                            print(output)
                            cur_pos += loop_amount

                            list_num = input("Choose a number in the list ([x] - cancel, [n] - display more): ")
                            display_list = list_num

                            pos_not_int = False
                            try:
                                pos = int(list_num) - 1
                            except:
                                pos_not_int = True

                            if not pos_not_int:
                                if pos >= len(urls) or pos < 0:
                                    print("Illegal index entered.")
                                else:
                                    player.add_song(urls[pos][0])
                                    song_selected = True
                                    print("Added '" + args + "' to queue.")
                            elif list_num == 'x':
                                print("add-list cancelled.")
                            elif list_num != 'n':
                                print("arg " + list_num + " not recognized, exiting add-list.")

                        if cur_pos >= len(urls) and not song_selected:
                            print("All " + str(len(urls)) + " videos displayed.")
                            list_num = input("Choose a number in the list ([x] - cancel): ")

                            pos_not_int = False
                            try:
                                pos = int(list_num) - 1
                            except:
                                pos_not_int = True

                            if not pos_not_int:
                                if pos >= len(urls) or pos < 0:
                                    print("Illegal index entered.")
                                else:
                                    player.add_song(urls[pos][0])
                                    print("Added '" + args + "' to queue.")
                            elif list_num == 'x':
                                print("add-list cancelled.")
                            else :
                                print("arg " + list_num + " not recognized, exiting add-list.")
                else:
                    print("add-list requires a [song] argument.")

            elif user_opt == 'add':
                if len(args) > 0:
                    url = grab_search_query(args)

                    if url is not None:
                        player.add_song(url)
                        print("Added '" + args + "' to queue.")
                    else:
                        print("Song '" + args + "' not found.")
                else:
                    print("add requires a [song] argument.")

            elif user_opt == 'clear':
                player.clear_queue()
                print("Cleared the queue.")

            elif user_opt == 'time':
                if player.get_current_song() is None:
                    print("No song currently playing")
                else:
                    length = convert_ms(player.get_length())
                    current = convert_ms(player.get_time())
                    position = player.get_position()
                    title = player.get_current_song().get_title()
                    pound = "=" * int(40 * position)
                    dash = "-" * int((40 * (1 - position)))
                    progress = "[" + pound + dash + "] (" + str(int(position * 100)) + "%) " + current + " of " + length
                    text = title + ": " + progress
                    print(text)

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

            elif user_opt == 'rewind':
                player.rewind()

            elif user_opt == 'remove':
                if len(args) > 0:
                    pos_not_int = False
                    try:
                        pos = int(args) - 1
                    except:
                        print("Illegal position entered.")
                        pos_not_int = True

                    if not pos_not_int:
                        if pos >= player.get_queue_size() or pos < 0:
                            print("Illegal position entered.")
                        else:
                            removed_song = player.remove_song(pos)
                            print("Removed " + removed_song.get_title() + " from queue")
                else:
                    print("remove requires a [pos] argument.")

            elif user_opt == 'play-list':
                if len(args) > 0:
                    urls = grab_search_query_list(args)

                    if len(urls) == 0:
                        print("Song '" + args + "' not found.")
                    else:
                        display_list = 'n'
                        cur_pos = 0
                        song_selected = False
                        while display_list == 'n' and cur_pos < len(urls):
                            output = ""
                            loop_amount = min(10, len(urls)-cur_pos)
                            for i in range(loop_amount):
                                output += "[" + str(i+cur_pos + 1) + "] - " + urls[i+cur_pos][1] + "\n"
                            print(output)
                            cur_pos += loop_amount

                            list_num = input("Choose a number in the list ([x] - cancel, [n] - display more): ")
                            display_list = list_num

                            pos_not_int = False
                            try:
                                pos = int(list_num) - 1
                            except:
                                pos_not_int = True

                            if not pos_not_int:
                                if pos >= len(urls) or pos < 0:
                                    print("Illegal index entered.")
                                else:
                                    player.play_over_cur_song(urls[pos][0])
                                    song_selected = True
                                    print("Playing '" + args + "'.")
                            elif list_num == 'x':
                                print("play-list cancelled.")
                            elif list_num != 'n':
                                print("arg " + list_num + " not recognized, exiting play-list.")

                        if cur_pos >= len(urls) and not song_selected:
                            print("All " + str(len(urls)) + " videos displayed.")
                            list_num = input("Choose a number in the list ([x] - cancel): ")

                            pos_not_int = False
                            try:
                                pos = int(list_num) - 1
                            except:
                                pos_not_int = True

                            if not pos_not_int:
                                if pos >= len(urls) or pos < 0:
                                    print("Illegal index entered.")
                                else:
                                    player.play_over_cur_song(urls[pos][0])
                                    print("Playing '" + args + "'.")
                            elif list_num == 'x':
                                print("play-list cancelled.")
                            else :
                                print("arg " + list_num + " not recognized, exiting play-list.")

                else:
                    print("play-list requires a [song] argument.")

            elif user_opt == 'play':
                if len(args) > 0:
                    url = grab_search_query(args)

                    if url is not None:
                        player.play_over_cur_song(url)
                        print("Playing '" + args + "'.")
                    else:
                        print("Song '" + args + "' not found.")
                else:
                    print("play requires a [song] argument.")

            elif user_opt == 'volume':
                if len(args) > 0:
                    pct = 0
                    legal_input = True
                    for sign in args:
                        if sign == '-':
                            pct -= 10
                        elif sign == '+':
                            pct += 10
                        else:
                            legal_input = False

                    if legal_input:
                        if pct > 0:
                            player.increase_vol(pct)
                        else:
                            player.decrease_vol(abs(pct))
                    else:
                        print("'" + args + "' is an illegal combination of +/-")
                else:
                    print("volume requires a [+/-] argument.")

            elif user_opt == 'exit':
                break

            else:
                print("Option '" + user_opt + "' not supported.")

            prompt_printed = False

def convert_ms(ms):
    """
    Converts milliseconds into h:m:s

    :param ms: int
    :return: str
    """
    seconds = (ms / 1000) % 60
    seconds = int(seconds)
    if seconds < 10:
        seconds = "0" + str(seconds)
    else:
        seconds = str(seconds)

    minutes = (ms / (1000 * 60)) % 60
    minutes = int(minutes)
    if minutes < 10:
        minutes = "0" + str(minutes)
    else:
        minutes = str(minutes)

    hours = (ms / (1000 * 60 * 60)) % 24
    hours = int(hours)
    if hours < 10:
        hours = "0" + str(hours)
    else:
        hours = str(hours)
    return hours + ":" + minutes + ":" + seconds
