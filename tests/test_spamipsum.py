# -*- coding: utf-8 -*-
import os

from spamipsum import SpamIpsum


def test_spamipsum_feed_from_files():
    dir_path = os.path.join(os.path.abspath(__file__),
                            os.path.pardir,
                            'res/single_file_test')
    si = SpamIpsum()
    si.feed_from_files(dir_path)
    sentence = si.make_sentence()
    assert isinstance(sentence, str)
    assert len(sentence) > 0
