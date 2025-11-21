class Television:
    """
    A class representing the details of a television object.
    """
    #Class Variables
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        """
        Method to set default values for a television object
        :default status: False (TV Off)
        :default muted: False (Not muted)
        :default volume: MIN_VOLUME = 0
        :default channel: MIN_CHANNEL = 0
        """
        self._status = False
        self._muted = False
        self._volume = self.MIN_VOLUME
        self._channel = self.MIN_CHANNEL

    def __str__(self):
        return f"Power = {self._status}, Channel = {self._channel}, Volume = {self._volume}"

    def power(self):
        """
        Method to change power status of television object
        """
        if self._status:
            self._status = False
        else:
            self._status = True

    def mute(self):
        """
        Method to change muted status of television object
        """
        if self._muted:
            self._muted = False
        else:
            self._muted = True

    def channel_up(self):
        """
        Method to increase channel value of television object
        If channel is at MAX_CHANNEL, then channel becomes MIN_CHANNEL
        """
        if self._channel == self.MAX_CHANNEL:
            self._channel = self.MIN_CHANNEL
        else:
            self._channel += 1

    def channel_down(self):
        """
        Method to decrease channel value of television object
        If channel is at MIN_CHANNEL, then channel becomes MAX_CHANNEL
        """
        if self._channel == self.MIN_CHANNEL:
            self._channel = self.MAX_CHANNEL
        else:
            self._channel -= 1

    def volume_up(self):
        """
        Method to increase volume value of television object
        If volume is at MAX_VOLUME, then volume is unchanged
        """
        if self._volume != self.MAX_VOLUME:
            self._volume += 1
        else:
            pass

    def volume_down(self):
        """
        Method to decrease volume value of television object
        If volume is at MIN_VOLUME, then volume is unchanged
        """
        if self._volume != self.MIN_VOLUME:
            self._volume -= 1
        else:
            pass
