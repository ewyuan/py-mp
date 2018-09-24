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
        self.__media_player = self.__vlc_instance.media_player_new()

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
        return self.__current_song()

    def get_next_song(self):
        """
        Returns the next song that will be played.

        :return: Song
        """
        return self.__next_song()

    def get_previous_song(self):
        """
        Returns the previous song that was played.

        :return: Song
        """
        return self.__previous_song()

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
        Plays the first song in the queue.

        :return: none
        """

        self.__previous_song = self.__current_song

        if self.__next_song is not None:
            self.__current_song = self.__next_song
        else:
            self.__current_song = self.__queue[0]

        self.remove_song(0)

        if self.get_queue_size() == 0:
            self.__next_song = None
        else:
            self.__next_song = self.__queue[0]

        self.__media_player.set_media(self.__current_song.get_media())
        self.__media_player.play()

    def clear_queue(self):
        """
        Clears the current queue.

        :return: none
        """
        self.__queue = []
