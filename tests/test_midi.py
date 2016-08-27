import os
import shutil
import unittest

from twelve_tone.midi import MIDIFile


class TestMIDIFile(unittest.TestCase):

    def test_init(self):
        m = MIDIFile()
        self.assertEquals(m.step_counter, 0)
        m = MIDIFile(filename="test.mid")
        self.assertEquals(m.filename, 'test.mid')

    def test_create(self):
        notes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        path = 'tmp'
        os.makedirs(path)
        os.chdir(path)
        m = MIDIFile(filename='test.mid')
        m.create(notes)
        self.assertTrue(os.path.exists(os.path.join(os.getcwd(), 'test.mid')))
        os.chdir(os.pardir)
        shutil.rmtree('tmp', ignore_errors=True)
