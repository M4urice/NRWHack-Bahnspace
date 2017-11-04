# -*- coding: utf-8 -*-
"""
bahn_bot.py

"""

if __name__ == '__main__':
    pass
from pprint import pprint
from rocketchat_API.rocketchat import RocketChat
import config
import time

rocket = RocketChat(
    config.BAHN_BOT_NAME, config.BAHN_BOT_PW, server_url='http://10.82.132.65')


class Event(object):
    """docstring for Event"""

    def __init__(self, e_type, message):
        super(Event, self).__init__()
        self.e_type = e_type

        self.message = message


def announce_event(event):

    rocket.chat_post_message("{0} {1}".format(config.FLAIRS[event.e_type], event.message),
                             channel=config.ANNOUNCE_CHANNEL, alias='RE7').json()


def react_to_msg():

    print(rocket.im_list(channel=config.ANNOUNCE_CHANNEL, alias='RE7'))
if __name__ == '__main__':
    react_to_msg()
    # pprint(rocket.channels_list().json())
    # next_stop = Event(0, "Nächster Halt: Solingen Hbf 🚉")
    # tunnel = Event(
    #     0, "Wir fahren gleich in einen Tunnel. Nicht erschrecken. 🚇 👻")
    # wait = Event(-1, "Ein Zug vor uns verzögert unsere Weiterfahrt. 👀")
    # resume = Event(1, "Weiter gehts! ")
    # announce_event(tunnel)
    # time.sleep(10)
    # announce_event(wait)
    # time.sleep(10)
    # announce_event(resume)
    # time.sleep(10)
    # announce_event(next_stop)
