from collections import defaultdict


class forwardAlgoHMM(object):
    startState = '(q0)'

    def __init__(self):
        self.totalStates = []
        self.x = defaultdict(lambda: defaultdict(lambda: 0.0))
        self.y = defaultdict(lambda: defaultdict(lambda: 0.0))

    def add(self, currentState, transition={}, emission={}):
        self.totalStates.append(currentState)

        for destination, probability in transition.items():
            self.x[currentState][destination] = probability

        for observation, probability in emission.items():
            self.y[currentState][observation] = probability

    def forwardAlgo(self, observations):
        self.forward = [{}]
        for each in self.totalStates:
            self.forward[0][each] = self.x[self.startState][each] * self.y[each][
                observations[0]]
        for trellis in range(1, len(observations)):
            self.forward.append({})
            for each in self.totalStates:
                self.forward[trellis][each] = sum((self.forward[trellis - 1][y0] * self.x[y0][
                    each] * self.y[each][observations[trellis]]) for y0 in self.totalStates)
        p = sum((self.forward[len(observations) - 1][s]) for s in self.totalStates)
        return p

    def probabilityCalculator(self, observations):
        probability = self.forwardAlgo(observations)
        print('Probability for the given observation is', probability)


hmm = forwardAlgoHMM()
hmm.add(forwardAlgoHMM.startState, dict(H=0.8, C=0.2))
hmm.add('H', dict(H=0.7, C=0.3), {1: .2, 2: .4, 3: .4})
hmm.add('C', dict(H=0.4, C=0.6), {1: .5, 2: .4, 3: .1})
hmm.probabilityCalculator([3, 3, 1, 1, 2, 3, 3, 1, 2])
hmm.probabilityCalculator([3, 3, 1, 1, 2, 2, 3, 1, 3])