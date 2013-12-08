# -*- coding: utf-8 -*-
import os

from spamipsum import SpamIpsum


def test_spamipsum_feed_from_files():
    file_dir = os.path.dirname(os.path.abspath(__file__))
    dir_path = os.path.join(file_dir, 'res/single_file_test')
    si = SpamIpsum()
    si.feed_from_files(dir_path)
    sentence = si.make_sentence()
    assert isinstance(sentence, str)
    assert len(sentence) > 0
