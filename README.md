# computer-wordle-client
A client for playing computer-wordle (see https://wordle.bobparks.info)

# Instructions

## Install

1) Fork this repo
2) Clone your forked repo
3) Install requirements `pip install requirements.txt`
4) Run the example AI `python3 simple_ai.py`

Success!

## Make Your Own Wordle Solver

### Instantiate a new Game

```
import computer_wordle
my_new_game = computer_wordle.Game()
```

### Make a first guess

Get the first "hint"

```
hint = my_game.current_hint()
```

The hint will be either `.....` or `......` where each `.` represents an empty gray square, in this version of the game the word can be either 5 or 6 characters. Select a word of the right length and submit it as a guess.

```
word_to_guess = super_cool_word_selection_function()
response = my_game.guess(word_to_guess)
```

*The `super_cool_word_selection_function` is not included. That's the part you're supposed to make

### Process the response

The response uses `.` to represent a grey square, `Y` to represent a yellow square, and `G` to represent a green square. So the response to a guess might look like `.GYYG` to represent ⬜🟩🟨🟨🟩.
