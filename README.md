![wadjet logo, pink digital text on blue statue eye](wadjet.JPG)


## a python library for working with nasa open apis


+ Currently wadjet has two submodules but I would love to add more.
+ (Please send PRs with cool ones.)

## Submodules

### neo
+ NEO (near earth object) - neo.py instantiates a NEO class
+ run_neo - This mode finds objects nearby in orbit, selects one at random and introduces you to that space object.

+ example `python wadjet.py --mode=neo()` output:

```
There are 19668 total near earth objects at this time
Let's look @ a random one

			~ 💫 Hello my real name is (1990 UN) ~

			~ 🦄 But you can call me Zelaya San Alfonso de la Montaña 19 ~

			~ 🐛 My number is 3092102 ~

			~ 🐲 It has been said of me ~

			~ ️🌚 nice, this near earth object is a superb friend  ~

			~ ⛳ Check out some of my stats: ~

			~ 📤 Max Diameter: 0.1185877909 kilometers ~

			~ 📥 Min Diameter: 0.0530340723 kilometers ~

```

### image
+ image.py - houses an Image class to handle image data
+ run_image - This mode gets a random cool nasa pic that matches your keyword
from the images api and opens it in your browser
+ + default keyword is 'moon'
+ `python wadjet.py --mode=image --keyword=sun`

## To get going 👇🏽

`pip install -r requirements.txt`

`python wadjet.py`


## Requirements

Runs on python 3.6

Uses NASA's open API
