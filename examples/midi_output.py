#!/usr/bin/python
#
# Quick usage example of "grid_instrument" with MIDI output port.
# Works with all Launchpads: Mk1, Mk2, S/Mini, Pro, XL and LaunchKey
# 
#
# David Hilowitz 9/24/17
# decided.ly / davehilowitz.com
#

from grid_instrument import GridInstrument
import rtmidi
import time

def note_callback(messageType, midiNote, velocity):
	if messageType == "note_on":
		midiout.send_message([0x90, midiNote, velocity])
	elif messageType == "note_off":
		midiout.send_message([0x80, midiNote, velocity])

# Create a MIDI output port
midiout = rtmidi.MidiOut()
midiout.open_virtual_port("Grid Instrument (Virtual Port)")

# Set up GridInstrument
instrument = GridInstrument()
instrument.intro_message = 'grid'
instrument.note_callback = note_callback
instrument.start()
