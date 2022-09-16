""" global settings file """
DEBUG = True
WIDTH = 1280
HEIGHT = 720
FPS = 60
CUSTOM_TITLE = "Magic 8 Ball"

# True of False boolean, not indexing
LIGHT_MODE = 1

# this is where I would put my color schema, if i had one
TEXT_COLOR = "#000000" if LIGHT_MODE else "#FFFFFF"
COLOR_BACKGROUND = "#80bfff" if LIGHT_MODE else "#7733ff"
BAR_COLOR = "#1a8cff" if LIGHT_MODE else "#8080ff"

# ball options
RESULTS = [
            ["It is Certain", "It is decidedly so", "without a doubt", "yes definitely", "you may rely on it"],
            ["As I see it, yes", "most likely", "outlook good", "yes", "signs point to yes"],
            ["Reply hazy, try again", "Ask again later", "better not tell you now", "cannot predict now", "concentrate and ask again"],
            ["Don't count on it", "My reply is NO", "My sources say no", "outlook not so good", "very doubtful"]
            ]
