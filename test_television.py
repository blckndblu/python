import unittest
from television import Television

class TelevisionTestCase(unittest.TestCase):

    def setUp(self):
        self.test_tv1 = Television()
        self.tv1_str = str(self.test_tv1)

    def tearDown(self):
        del self.test_tv1
        del self.tv1_str

    def test_init(self):
        self.assertEqual(self.tv1_str, "Power = False, Channel = 0, Volume = 0")

    def test_power(self):
        #TV On
        self.test_tv1.power()
        self.tv1_str = str(self.test_tv1)
        self.assertEqual(self.tv1_str, "Power = True, Channel = 0, Volume = 0")

        #TV Off
        self.test_tv1.power()
        self.tv1_str = str(self.test_tv1)
        self.assertEqual(self.tv1_str, "Power = False, Channel = 0, Volume = 0")

    def test_mute(self):
        #TV On, Volume Up 1, Mute
        self.test_tv1.power()
        self.test_tv1.volume_up()
        self.test_tv1.mute()
        self.tv1_str = str(self.test_tv1)
        self.assertEqual(self.tv1_str, "Power = True, Channel = 0, Volume = 0")

    def test_channel_up(self):
        #TV Off, Channel Up 1
        self.test_tv1.channel_up()
        self.tv1_str = str(self.test_tv1)
        self.assertEqual(self.tv1_str, "Power = False, Channel = 0, Volume = 0")
        #TV On, Channel Up 1
        self.test_tv1.power()
        self.test_tv1.channel_up() #C1
        self.tv1_str = str(self.test_tv1)
        self.assertEqual(self.tv1_str, "Power = True, Channel = 1, Volume = 0")
        #TV On, Channel Up Past Max (3)
        self.test_tv1.channel_up() #C2
        self.test_tv1.channel_up() #C3
        self.test_tv1.channel_up() #C0
        self.tv1_str = str(self.test_tv1)
        self.assertEqual(self.tv1_str, "Power = True, Channel = 0, Volume = 0")

    def test_channel_down(self):
        #TV Off, Channel Down 1
        self.test_tv1.channel_down()
        self.tv1_str = str(self.test_tv1)
        self.assertEqual(self.tv1_str, "Power = False, Channel = 0, Volume = 0")
        #TV On, Channel Down 1
        self.test_tv1.power()
        self.test_tv1.channel_down()
        self.tv1_str = str(self.test_tv1)
        self.assertEqual(self.tv1_str, "Power = True, Channel = 3, Volume = 0")

    def test_volume_up(self):
        #TV Off, Volume Up 1
        self.test_tv1.volume_up()
        self.tv1_str = str(self.test_tv1)
        self.assertEqual(self.tv1_str, "Power = False, Channel = 0, Volume = 0")
        #TV On, Volume Up 1
        self.test_tv1.power()
        self.test_tv1.volume_up()
        self.tv1_str = str(self.test_tv1)
        self.assertEqual(self.tv1_str, "Power = True, Channel = 0, Volume = 1")
        #TV On, Muted, Volume Up 1
        self.test_tv1.mute()
        self.test_tv1.volume_up()
        self.tv1_str = str(self.test_tv1)
        self.assertEqual(self.tv1_str, "Power = True, Channel = 0, Volume = 0")
        self.test_tv1.mute()
        #TV On, Volume Up Max
        self.test_tv1.volume_up() #V1
        self.test_tv1.volume_up() #V2
        self.test_tv1.volume_up() #V2
        self.tv1_str = str(self.test_tv1)
        self.assertEqual(self.tv1_str, "Power = True, Channel = 0, Volume = 2")

    def test_volume_down(self):
        #set object for testing
        self.test_tv1.power()
        self.test_tv1.volume_up() #V1
        self.test_tv1.volume_up() #V2
        #TV Off, Volume Down 1
        self.test_tv1.power()
        self.test_tv1.volume_down()
        self.tv1_str = str(self.test_tv1)
        self.assertEqual(self.tv1_str, "Power = False, Channel = 0, Volume = 2")
        #TV On, Volume Down 1
        self.test_tv1.power()
        self.test_tv1.volume_down()
        self.tv1_str = str(self.test_tv1)
        self.assertEqual(self.tv1_str, "Power = True, Channel = 0, Volume = 1")
        #TV On, Muted, Volume Down 1
        self.test_tv1.mute()
        self.test_tv1.volume_down()
        self.tv1_str = str(self.test_tv1)
        self.assertEqual(self.tv1_str, "Power = True, Channel = 0, Volume = 0")