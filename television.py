class Television:
    #Class Variables
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        self._status = False
        self._muted = False
        self._volume = self.MIN_VOLUME
        self._channel = self.MIN_CHANNEL

    def __str__(self):
        return f"Power = {self._status}, Channel = {self._channel}, Volume = {self._volume}"

    def power(self):
        if self._status:
            self._status = False
        else:
            self._status = True

    def mute(self):
        if self._status:
            if self._muted:
                self._muted = False
            else:
                self._muted = True
        else:
            pass

    def channel_up(self):
        if self._status:
            if self._channel == self.MAX_CHANNEL:
                self._channel = self.MIN_CHANNEL
            else:
                self._channel += 1
        else:
            pass

    def channel_down(self):
        if self._status:
            if self._channel == self.MIN_CHANNEL:
                self._channel = self.MAX_CHANNEL
            else:
                self._channel -= 1
        else:
            pass

    def volume_up(self):
        if self._status:
            if self._volume != self.MAX_VOLUME:
                self._volume += 1
            else:
                pass
        else:
            pass

    def volume_down(self):
        if self._status:
            if self._volume != self.MIN_VOLUME:
                self._volume -= 1
            else:
                pass
        else:
            pass

