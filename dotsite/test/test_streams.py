"""Test stream handlers"""

import sys
from cStringIO import StringIO
from unittest import TestCase


from dotsite.streams import swallow_stdout, swallow_stderr


class TestStreams(TestCase):

    def test_swallow_stdout(self):
        stream = StringIO()
        with swallow_stdout(stream):
            print 'hello',
        self.assertEqual(stream.getvalue(), 'hello')

    def test_swallow_stderr(self):
        stream = StringIO()
        with swallow_stderr(stream):
            print >> sys.stderr, 'hello'
        self.assertEqual(stream.getvalue(), 'hello\n')

    def test_discard_stdout(self):
        """This method is not programatically testable,

        But will produce no expected output
        If it fails it becomes noticable at command line
        """
        # pylint: disable-msg=no-self-use
        with swallow_stdout():
            print 'hello'

    def test_discard_stderr(self):
        """This method is not programatically testable,

        But will produce no expected output
        If it fails it becomes noticable at command line
        """
        # pylint: disable-msg=no-self-use
        with swallow_stderr():
            print >> sys.stderr, 'hello'