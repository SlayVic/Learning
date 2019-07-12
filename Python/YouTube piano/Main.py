from threading import Thread
import keyboard
import time

isPlaying = False
breakFlag = False
mainDelay = 0.3
spaceDelay = 0.4
hyphenDelay = 0.6
comaDelay = 0.5
dotComaDelay = 0.7

text = '777 777 79567 8888877776676 9'

def StartPlay(text):
    print("StartPlay started\n")
    # if isPlaying:
    leng = len(text)
    i = 0
    global isPlaying
    global breakFlag
    while i < leng:
        if breakFlag:
            breakFlag = False
            isPlaying = False
            break
        element = text[i]
        if element == '(':
            playSimbol(text[i:i + 5])
            i += 5
        else:
            playSimbol(element)
            i += 1
    isPlaying = False


def playSimbol(simbol):
    if simbol in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
        time.sleep(mainDelay)
        keyboard.press(simbol)
        print(simbol)
    elif simbol == ' ':
        time.sleep(spaceDelay)
    elif simbol == '-':
        time.sleep(hyphenDelay)
    elif simbol == ',':
        time.sleep(comaDelay)
    elif simbol == ';':
        time.sleep(dotComaDelay)
    elif simbol == '/':
        time.sleep(0.5)
    elif simbol in ['(2+J)', '(3+J)', '(5+J)', '(6+J)', '(7+J)', '(9+J)']:
        time.sleep(mainDelay)
        keyboard.press(simbol[1])
        print(simbol)
        keyboard.press('j')
    # elif simbol == '':
    #     pass


def KeyControl():
    global isPlaying
    global breakFlag
    print("KeyControl started")
    while True:
        if not isPlaying and keyboard.is_pressed('['):
            isPlaying = True
            Thread(target=StartPlay, args=(
                text,)).start()
        elif not breakFlag and keyboard.is_pressed(']'):
            breakFlag = True
            continue
        elif keyboard.is_pressed('\\'):
            breakFlag = True
            break




def CheckTime(time):
    leng = len(text)
    time=0
    i = 0
    while i < leng:
        element = text[i]
        if element == '(':
            time += CheckSimbolTime(text[i:i + 5])
            i += 5
        else:
            time += CheckSimbolTime(element)
            i += 1
    print(time)


def CheckSimbolTime(simbol):
    if simbol in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
        return mainDelay
    elif simbol == ' ':
        return spaceDelay
    elif simbol == '-':
        return hyphenDelay
    elif simbol == ',':
        return comaDelay
    elif simbol == ';':
        return dotComaDelay
    elif simbol == '/':
        return 0.5
    elif simbol in ['(2+J)', '(3+J)', '(5+J)', '(6+J)', '(7+J)', '(9+J)']:
        return mainDelay

# CheckTime(text)

if __name__ == '__main__':
    Thread(target=KeyControl).start()

# while True:
#     print(isPlaying)
#     time.sleep(0.5)
