from miditime.miditime import MIDITime


class MIDIFile(object):

    def __init__(self, BPM=120, filename='example.mid'):
        self.pattern = MIDITime(BPM, filename)
        self.step_counter = 0
        self.filename = filename

    def create(self, notes):
        midinotes = []
        offset = 60
        attack = 200
        beats = 1
        for note in notes:
            pitch = (note - 1) + offset
            midinote = [self.step_counter, pitch, attack, beats]
            midinotes.append(midinote)
            self.step_counter = self.step_counter + 1

        # Add a track with those notes
        self.pattern.add_track(midinotes)

        # Output the .mid file
        self.pattern.save_midi()
