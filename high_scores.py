#!/usr/bin/python3
class HighScores:
    def __init__(self, scores):
        self.scores = scores

    def latest(self):
        return self.scores.pop()

    def personal_best(self):
        return max(self.scores)

    def personal_top_three(self):
        scores = [10, 30, 90, 30, 100, 20, 10, 0, 30, 40, 40, 70, 70]
        scores.sort(reverse=True)
        return scores[:3]

# antother way
    def personal_top_three(self):
        copy_scores = sorted(self.scores, reverse=True)
        return copy_scores[:3]
