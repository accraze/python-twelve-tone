"""
MIDI file generation using mido.

This module provides MIDI export functionality for twelve-tone compositions
using the mido library, which is actively maintained and supports standard
MIDI file format.
"""
from typing import List


class MIDIFile(object):
    """
    MIDI file generator for twelve-tone compositions.
    
    Creates MIDI files from pitch class sequences using the mido library.
    Each note is represented as a quarter note with a fixed tempo.
    """
    
    def __init__(self, BPM: int = 120, filename: str = 'example.mid'):
        """
        Initialize MIDI file generator.
        
        Args:
            BPM: Tempo in beats per minute (default: 120)
            filename: Output MIDI filename
        """
        self.BPM = BPM
        self.filename = filename
        self.filename = filename if filename.endswith('.mid') else f'{filename}.mid'
    
    def create(self, notes: List[int]) -> None:
        """
        Create a MIDI file from a sequence of pitch classes.
        
        Args:
            notes: List of integers (1-12) representing pitch classes.
                  1=C, 2=C#, 3=D, etc.
        """
        import mido
        from mido import MidiTrack, MidiFile, Message, MetaMessage
        
        # Create a new MIDI file
        mid = MidiFile()
        mid.ticks_per_beat = 480  # Standard PPQ (Pulses Per Quarter note)
        
        # Create a track
        track = MidiTrack()
        mid.tracks.append(track)
        
        # Add track name
        track.append(MetaMessage('track_name', name='Twelve Tone', time=0))
        
        # Set tempo (microseconds per beat)
        tempo = mido.bpm2tempo(self.BPM)
        track.append(MetaMessage('set_tempo', tempo=tempo, time=0))
        
        # Add notes
        # Each note is a quarter note (480 ticks)
        note_duration = 480
        current_time = 0
        
        for note_num in notes:
            # Convert pitch class (1-12) to MIDI note number
            # We'll use octave 4 as the base (C4 = 60)
            midi_pitch = (note_num - 1) + 60  # C4 = 60, C#4 = 61, etc.
            
            # Note on
            track.append(Message('note_on', note=midi_pitch, velocity=64, time=current_time))
            current_time = 0  # Reset time for next message
            
            # Note off (after duration)
            track.append(Message('note_off', note=midi_pitch, velocity=64, time=note_duration))
        
        # End of track
        track.append(MetaMessage('end_of_track', time=0))
        
        # Save the MIDI file
        mid.save(self.filename)
