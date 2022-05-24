# Uncolor
## 🎨 | Uncomplicated colorizing tool for your terminal

Inspired on the Node's package *Chalk*, Uncolor wants to make easier styles for the terminal. No reset needed, no aditional functions, just simple.

### Why a new style package?
I made this package for have a style formatter different to Colorama, easy to use and uncomplicated. I also created it for learn modules in Python, so this is my first package. I'm proud of it :)

### Installation
**Note:** *Uncolor requires* **Python 3.10** *or higher*
```sh
pip install uncolor
```

### Usage
Uncolor only has one function
```py
from uncolor import uncolor

my_colorful_string = uncolor("This is really awesome!", ["red", "blueBg", "bold"])

print(my_colorful_string)
```

The styles that you want goes into the array. Uncolor supports the next styles:
| Text color | Background color | Style |
|--|--|---|
| `white` `black` `green` `yellow` `brown` `blue` `cyan` `purple` `red`   | `whiteBg` `blackBg` `greenBg` `yellowBg` `brownBg` `blueBg` `cyanBg` `purpleBg` `redBg` | `bold` `italic` `underline` `blink` `inverse` `hidden`  `crossed` |
| `lightgray` `darkgray` `lightgreen` `lightblue`  `lightred`  `lightpurple` `lightcyan` | `lightgrayBg` `darkgrayBg` `lightgreenBg` `lightblueBg`  `lightredBg`  `lightpurpleBg` `lightcyanBg` |  `end` or `reset` (no needed except if you want) |


### License
Uncolor is under MIT license. You can feel free to use, read, copy and edit the code ;)
