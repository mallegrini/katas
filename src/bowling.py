# https://www.slideshare.net/kevinrutherford/ocp-kata-24027400
class BowlingGame:

    def __init__(self):
        self._rolls = []

    def roll(self, pins):
        self._rolls.append(pins)

    def score(self):
        total = 0
        newFrame = True
        frameNum = 1
        rolls = self._rolls
        for i in range(0, len(rolls)):
            if frameNum > 10: break
            total += rolls[i]
            if newFrame and rolls[i] == 10: # strike
                total += rolls[i+1] + rolls[i+2]
                newFrame = True
                frameNum += 1
            elif not newFrame and rolls[i-1] + rolls[i] == 10: # spare
                total += rolls[i+1]
                newFrame = True
                frameNum += 1
            else: # open frame
                newFrame = not newFrame
                if newFrame: frameNum += 1
        return total

if __name__ == '__main__':
    g = BowlingGame()
    for i in range(9):
        g.roll(10)
    g.roll(3)
    g.roll(5)
    print(g.score()) # 259 is correct!
