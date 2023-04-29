from array import array
import sys

ansiBase = '\033['


def getStyle(style):
    styles = {
        'black': '30m',
        'red': '31m',
        'green': '32m',
        'brown': '33m',
        'blue': '34m',
        'purple': '35m',
        'cyan': '36m',
        'lightgray': '37m',
        'darkgray': '90m',
        'lightred': '91m',
        'lightgreen': '92m',
        'yellow': '93m',
        'lightblue': '94m',
        'lightpurple': '95m',
        'lightcyan': '96m',
        'white': '97m',
        'blackBg': '40m',
        'redBg': '41m',
        'greenBg': '42m',
        'brownBg': '43m',
        'blueBg': '44m',
        'purpleBg': '45m',
        'cyanBg': '46m',
        'lightgrayBg': '47m',
        'darkgrayBg': '100m',
        'lightredBg': '101m',
        'lightgreenBg': '102m',
        'yellowBg': '103m',
        'lightblueBg': '104m',
        'lightpurpleBg': '105m',
        'lightcyanBg': '106m',
        'whiteBg': '107m',
        'bold': '1m',
        'faint': '2m',
        'italic': '3m',
        'underline': '4m',
        'blink': '5m',
        'inverse': '7m',
        'hidden': '8m',
        'crossed': '9m',
        'end': '0m',
        'reset': '0m',
    }
    return styles.get(style, '')


def uncolor(text: str, styles: array):
    # warn stupid system
    warnings = []

    exporter = ''

    for style in styles:
        code = getStyle(style)
        if code != '':
            exporter += ansiBase + code
        else:
            warnings.append(style)

    exporter += text
    exporter += ansiBase + getStyle('end')

    # Notify inexistent styles
    if len(warnings) > 0:
        print(f'{ansiBase + getStyle("yellowBg") + ansiBase + getStyle("bold")} uncolor | Warning: {ansiBase + getStyle("reset")} The following styles were not found: {ansiBase + getStyle("italic") + str(warnings) + ansiBase + getStyle("reset")}. Try to lowercase the styles.')

    return exporter


sys.modules[__name__] = uncolor
