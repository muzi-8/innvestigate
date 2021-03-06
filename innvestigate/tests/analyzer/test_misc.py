# Begin: Python 2/3 compatibility header small
# Get Python 3 functionality:
from __future__ import\
    absolute_import, print_function, division, unicode_literals
from future.utils import raise_with_traceback, raise_from
# catch exception with: except Exception as e
from builtins import range, map, zip, filter
from io import open
import six
# End: Python 2/3 compatability header small


###############################################################################
###############################################################################
###############################################################################


import pytest


from innvestigate.utils.tests import dryrun

from innvestigate.analyzer import Input
from innvestigate.analyzer import Random


###############################################################################
###############################################################################
###############################################################################


@pytest.mark.fast
@pytest.mark.precommit
def test_fast__Input():

    def method(model):
        return Input(model)

    dryrun.test_analyzer(method, "trivia.*:mnist.log_reg")


@pytest.mark.fast
@pytest.mark.precommit
def test_fast__Random():

    def method(model):
        return Random(model)

    dryrun.test_analyzer(method, "trivia.*:mnist.log_reg")
