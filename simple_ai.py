#!/usr/bin/env python3

import computer_wordle
import random


def main():
    game = computer_wordle.Game()
    while game.current_hint() is not None:
        possible_words = [word for word in computer_wordle.wordlist if len(word) == len(game.current_hint())]
        while True:
            guess_word = random.choice(possible_words)
            response = game.guess(guess_word)
            guess_response = response['response']
            print(f"{guess_word} -> {guess_response}")
            if 'next_hint' in response.keys():
                # Solved the word, on to the next one!
                print(f"SOLVED! Target word = {guess_word}")
                break
            for idx in range(len(guess_response)):
                if guess_response[idx] != computer_wordle.GRAY:
                    possible_words = [
                        word for word in possible_words
                        if guess_word[idx] in word and word != guess_word
                    ]


if __name__ == '__main__':
    main()
