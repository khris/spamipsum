# -*- coding: utf-8 -*-
import os

from spamipsum.reader import EOD
from spamipsum.reader import FileReader


def test_file_reader():
    fake_path = '../fake'
    with FileReader(fake_path) as reader:
        for _ in reader:
            pass

    dir_path = os.path.join(os.path.abspath(__file__),
                            os.path.pardir,
                            'res/single_file_test')
    with FileReader(dir_path) as reader:
        words = []
        for word in reader:
            words.append(word)
        assert len(words) == 5
        assert words[0] == 'First'
        assert words[1] == 'Second'
        assert words[2] == 'Third'
        assert words[3] == 'Fourth'

    dir_path = os.path.join(os.path.abspath(__file__),
                            os.path.pardir,
                            'res/multi_file_test')
    with FileReader(dir_path) as reader:
        words = []
        for word in reader:
            words.append(word)
        assert len(words) == (4 + 1) * 3
        assert words[(4 + 1) * 0] == 'First'
        assert isinstance(words[(4 + 1) * 1 - 1], EOD)
        assert words[(4 + 1) * 1] == 'AAA'
        assert isinstance(words[(4 + 1) * 2 - 1], EOD)
        assert words[(4 + 1) * 2] == 'QQQ'
        assert isinstance(words[(4 + 1) * 3 - 1], EOD)
