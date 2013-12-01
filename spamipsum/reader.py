# -*- coding: utf-8 -*-
from contextlib import contextmanager
from fileinput import FileInput
import fileinput
import os

DEFAULT_ENCODING = 'utf-8'


class EOD(object):
    """
    End of Document
    """
    pass


@contextmanager
def FileReader(path):
    if os.path.exists(path):
        yield _get_word_from_file(path)
    else:
        yield iter([])


def _get_word_from_file(path):
    first = True
    for root, dirs, files in os.walk(path):
        with FileInput(files=_get_full_paths(root, files),
                       openhook=fileinput.hook_encoded(DEFAULT_ENCODING)) as f:
            for line in f:
                if f.isfirstline():
                    if first:
                        first = False
                    else:
                        yield EOD()
                for word in line.split():
                    yield word
    yield EOD()


def _get_full_paths(root_dir, filenames):
    return map(lambda filename: os.path.join(root_dir, filename), filenames)
