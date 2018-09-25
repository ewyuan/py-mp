import pafy


class Song:
    def __init__(self, url, vlc):
        """
        Instantiates a Song object with a url and vlc object.

        :param url: str
        :param vlc: str
        :return: None
        """
        self.__url = url
        self.__vlc = vlc
        self.__audio = pafy.new(url)
        self.__media = self.__vlc.media_new(self.get_audio_url())

    def get_title(self):
        """
        Returns the title of this Song.

        :return: str
        """
        return self.__audio.title

    def get_length(self):
        """
        Returns the length of this Song.

        :return: int
        """
        return self.__audio.length

    def get_audio_url(self):
        """
        Returns the audio URL of this Song.

        :return: str
        """
        return self.__audio.getbestaudio().url

    def get_media(self):
        """
        Returns the media of this Song.

        :return: Media
        """
        return self.__media
