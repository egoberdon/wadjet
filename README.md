![wadjet logo, pink digital text on blue statue eye](wadjet.JPG)


a python library for working with nasa open apis

Currently wadjet only has one mode but I would love to add many.

(Please send PRs with cool ones.)

This mode finds the objects nearby in orbit, gets the first 12,
selects one at random and introduces you to that space object.

To get going 👇🏽

`pip install -r requirements.txt`
`python wadjet.py`

example output:
```
There are 19668 total near earth objects at this time
Lets check out 12 of them
Digging further let's look @ a random one

			~ 💫 Hello my real name is (1990 UN) ~

			~ 🦄 But you can call me Zelaya San Alfonso de la Montaña 19 ~

			~ 🐛 My number is 3092102 ~

			~ 🐲 It has been said of me ~

			~ ️🌚 nice, this near earth object is a superb friend  ~

			~ ⛳ Check out some of my stats: ~

			~ 📤 Max Diameter: 0.1185877909 kilometers ~

			~ 📥 Min Diameter: 0.0530340723 kilometers ~

```
Runs on python 3.6
Uses NASA's open API - NEO