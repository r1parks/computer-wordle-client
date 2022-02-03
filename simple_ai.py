#!/usr/bin/env python3

import computer_wordle
import random
import webbrowser


def main():

    # Create a new game for today's challenge
    game = computer_wordle.Game()

    # The game.current_hint() will be None once the game is over
    while game.current_hint() is not None:

        # all words in the word list that are of the correct length (this challenge uses both 5 and 6 letter words)
        possible_words = [word for word in computer_wordle.wordlist if len(word) == len(game.current_hint())]

        # Keep guessing until the current word is solved (no guess limit per word)
        while True:

            # Pick a random word from the list of possible words
            guess_word = random.choice(possible_words)

            response = game.guess(guess_word)
            guess_response = response['guess_response']
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
    print(f"Done. Results at {game.url()}")
    webbrowser.open(game.url())


if __name__ == '__main__':
    main()
