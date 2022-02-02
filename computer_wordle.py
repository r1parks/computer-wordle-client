#!/usr/bin/env python3

import api
from urllib.parse import urljoin


GREEN = 'G'
YELLOW = 'Y'
GRAY = '.'

with open('wordlist.txt') as wordlist_file:
    wordlist = tuple(line.strip() for line in wordlist_file)


class Game:
    def __init__(self):
        response = api.start_new_game()
        self._game_id = response['game_id']
        self._public_game_id = response['public_game_id']
        self._current_hint = response['hint']

    def current_hint(self):
        return self._current_hint

    def guess(self, guess):
        response = api.make_guess(self._game_id, guess)
        return_value = {'guess_response': response['response']}
        if 'next_hint' in response:
            self._current_hint = response['next_hint']
            return_value['next_hint'] = response['next_hint']
        return return_value

    def status(self):
        return api.get_game_status(self._game_id)

    def url(self):
        return urljoin(api.BASE_URL, f'/game/{self._public_game_id}/')
