import vlc
from .song import Song


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

        self.__vlc_instance = vlc.Instance()
        self.__media_player = self.__vlc_instance.media_player_new()

    def get_queue_size(self):
        """
        Returns the size of the player queue

        :return: int
        """
        return len(self.__queue)

    def get_queue(self):
        """
        Prints the queue

        :return: list
        """
        return self.__queue

    def add_song(self, url):
        """
        Adds a song to the queue, given the url for the song.

        :return: none
        """
        new_song = Song(url, self.__vlc_instance)
        self.__queue.append(new_song)

        if self.get_queue_size() == 1:
            self.__next_song = new_song

        if not self.__media_player.is_playing() and self.__current_song is None:
            self.play_next()

    def remove_song(self, pos):
        """
        Removes a song from the queue, given the position in the queue, and returns the item removed.

        :param pos: int
        :return: Song
        """
        if self.__queue[pos] == self.__next_song:
            if not pos == self.get_queue_size() - 1:
                self.__next_song = self.__queue[pos+1]
            else:
                self.__next_song = None

        return self.__queue.pop(pos)

    def get_current_song(self):
        """
        Returns the current song being played.

        :return: Song
        """
        return self.__current_song

    def get_next_song(self):
        """
        Returns the next song that will be played.

        :return: Song
        """
        return self.__next_song

    def get_previous_song(self):
        """
        Returns the previous song that was played.

        :return: Song
        """
        return self.__previous_song

    def pause(self):
        """
        Pauses the current song.

        :return: none
        """
        self.__media_player.set_pause(True)

    def resume(self):
        """
        Resumes the current song.

        :return: none
        """
        self.__media_player.set_pause(False)

    def __stop(self):
        """
        Stops the current song, moves to the next song in queue.

        :return: none
        """
        self.__media_player.stop()

        self.__previous_song = self.__current_song
        self.__current_song = None

    def rewind(self):
        self.__media_player.set_time(0)

    def skip(self):
        """
        Skips the current song, moves to the next song in queue.

        :return: none
        """
        self.__stop()

        if len(self.__queue) > 0:
            self.play_next()

    def play_next(self):
        """
        Plays the first song in the queue.

        :return: none
        """
        if self.get_queue_size() == 0:
            print("No songs in queue to play.")
        else:
            if self.__next_song is not None:
                self.__current_song = self.__next_song
            else:
                self.__current_song = self.__queue[0]

            if self.get_queue_size() == 1:
                self.__next_song = None
            else:
                self.__next_song = self.__queue[1]

            self.__queue.pop(0)
            self.__media_player.set_media(self.__current_song.get_media())
            self.__media_player.play()

    def clear_queue(self):
        """
        Clears the current queue.

        :return: none
        """
        self.__queue = []

    def get_state(self):
        """
        Returns the state of the MediaPlayer.

        :return: int
        """
        return self.__media_player.get_state()

    def get_length(self):
        """
        Returns the length (in ms) of the current song.

        :return: int
        """
        return self.__media_player.get_length()

    def get_time(self):
        """
        Returns the time (in ms) of the current song.

        :return: int
        """
        return self.__media_player.get_time()

    def get_position(self):
        """
        Returns the position (between 0.0 to 1.0) of the current song.

        :return: double
        """
        return self.__media_player.get_position()
