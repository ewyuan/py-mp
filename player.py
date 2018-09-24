import pafy
import requests
import time
import bs4
import vlc
import youtube_dl
import song

class Player:
    def __init__(self):
        """
        Instantiates a Player object.

        :return: None
        """
        self.__queue = []
        self.__current_song = None
        self.__next_song = None
        self.__previous_song = None

        self.__is_occupied = False

        self.__vlc_instance = vlc.Instance()
        self.__media_player = vlc_instance.media_player_new()

    def get_queue_size(self):
        """
        Returns the size of the player queue

        :return: int
        """
        return len(self.__queue)

    def print_queue(self):
        """
        Prints the queue

        :return: none
        """
        print("ABC")

    def add_song(self, url):
        """
        Adds a song to the queue, given the url for the song.

        :return: none
        """
        new_song = song.Song(url, self.__vlc_instance)
        self.__queue.append(new_song)

    def remove_song(self, pos):
        """
        Removes a song from the queue, given the position in the queue

        :param pos: int
        :return: none
        """
        self.__queue.pop(pos)

    def get_current_song(self):
        """
        Returns the current song being played.

        :return: Song
        """
        print(self.__current_song.get_title())

    def get_next_song(self):
        """
        Returns the next song that will be played.

        :return: Song
        """
        print(self.__next_song.get_title())

    def get_previous_song(self):
        """
        Returns the previous song that was played.

        :return: Song
        """
        print(self.__previous_song.get_title())

    def pause(self):
        """
        Pauses the current song.

        :return: none
        """
        self.__media_player.set_pause(True)

    def stop(self):
        """
        Stops the current song, moves to the next song in queue.

        :return: none
        """
        self.__media_player.stop()

    def skip(self):
        """
        Skips the current song, moves to the next song in queue.

        :return: none
        """

    def play(self):
        """
        Plays the current song, moves to the next song in queue.

        :return: none
        """

    def clear_queue(self):
        """
        Clears the current queue.

        :return: none
        """
        self.__queue = []
