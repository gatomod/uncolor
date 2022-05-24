from array import array
import sys

ansiBase = '\033['

# códigos ANSI más comunes / common ANSI codes


def getStyle(style):
    match style:
        case 'black':
            return '30m'
        case 'red':
            return '31m'
        case 'green':
            return '32m'
        case 'brown':
            return '33m'
        case 'blue':
            return '34m'
        case 'purple':
            return '35m'
        case 'cyan':
            return '36m'
        case 'lightgray':
            return '37m'
        case 'darkgray':
            return '90m'
        case 'lightred':
            return '91m'
        case 'lightgreen':
            return '92m'
        case 'yellow':
            return '93m'
        case 'lightblue':
            return '94m'
        case 'lightpurple':
            return '95m'
        case 'lightcyan':
            return '96m'
        case 'white':
            return '97m'
        case 'blackBg':
            return '40m'
        case 'redBg':
            return '41m'
        case 'greenBg':
            return '42m'
        case 'brownBg':
            return '43m'
        case 'blueBg':
            return '44m'
        case 'purpleBg':
            return '45m'
        case 'cyanBg':
            return '46m'
        case 'lightgrayBg':
            return '47m'
        case 'darkgrayBg':
            return '100m'
        case 'lightredBg':
            return '101m'
        case 'lightgreenBg':
            return '102m'
        case 'yellowBg':
            return '103m'
        case 'lightblueBg':
            return '104m'
        case 'lightpurpleBg':
            return '105m'
        case 'lightcyanBg':
            return '106m'
        case 'whiteBg':
            return '107m'
        case 'bold':
            return '1m'
        case 'faint':
            return '2m'
        case 'italic':
            return '3m'
        case 'underline':
            return '4m'
        case 'blink':
            return '5m'
        case 'inverse':
            return '7m'
        case 'hidden':
            return '8m'
        case 'crossed':
            return '9m'
        case 'end':
            return '0m'
        case 'reset':
            return '0m'
        case _:
            return ''


def uncolor(text: str, styles: array):
    # warn stupid system
    warnings = []

    exporter = ''

    for style in styles:
        if getStyle(style) != '':
            exporter += ansiBase + getStyle(style)
        else:
            warnings.append(style)

    exporter += text
    exporter += ansiBase + getStyle('end')

    # Notify inexistent styles
    if len(warnings) > 0:
        print(f'{ansiBase + getStyle("yellowBg") + ansiBase + getStyle("bold")} uncolor | Warning: {ansiBase + getStyle("reset")} The following styles were not found: {ansiBase + getStyle("italic") + str(warnings) + ansiBase + getStyle("reset")}. Try to lowercase the styles.')

    return exporter


sys.modules[__name__] = uncolor
