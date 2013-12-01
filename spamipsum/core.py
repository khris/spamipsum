# -*- coding: utf-8 -*-
from collections import defaultdict
from itertools import accumulate
import bisect
import random

from spamipsum.reader import EOD
from spamipsum.reader import FileReader

RECOMMENDED_MIN = 3
RECOMMENDED_MAX = 10


class SpamIpsum(object):
    word_map = defaultdict(lambda: defaultdict(lambda: 0))

    def __init__(self):
        pass

    def feed(self, iterable):
        pass

    def feed_from_files(self, dir_path):
        prev_word = None
        with FileReader(dir_path) as f:
            for word in f:
                if isinstance(word, EOD):
                    prev_word = None
                if prev_word is not None:
                    self.word_map[prev_word][word] += 1
                prev_word = word

    def make_sentence(self):
        words = list(self.word_map.keys())
        seed_word = random.choice(words)
        sentence = '{}'.format(seed_word)
        word_count = random.randint(RECOMMENDED_MIN, RECOMMENDED_MAX)
        for x in range(word_count):
            word = self._get_next_word(seed_word)
            if word == '':
                break
            sentence += ' {}'.format(word)
            seed_word = word
        return sentence

    def _get_next_word(self, curr_word):
        if not curr_word in self.word_map:
            return ''

        candidates = self.word_map[curr_word]
        part_scores = list(accumulate(candidates.values()))
        chosen = random.randint(0, part_scores[-1] - 1)
        idx = bisect.bisect_right(part_scores, chosen)
        return list(candidates.keys())[idx]
