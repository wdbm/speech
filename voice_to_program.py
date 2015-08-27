#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
################################################################################
#                                                                              #
# voice_to_program                                                             #
#                                                                              #
################################################################################
#                                                                              #
# LICENCE INFORMATION                                                          #
#                                                                              #
# This program provides procedures to engage a speech synthesizer and connect  #
# it to a sound program. The speech synthesizer is Festival and the sound      #
# program is Skype.                                                            #
#                                                                              #
# 2015 Will Breaden Madden, w.bm@cern.ch                                       #
#                                                                              #
# Subject to ATLAS Data Access Policy, this software is released under the     #
# terms of the GNU General Public License version 3 (GPLv3).                   #
#                                                                              #
# For a copy of the ATLAS Data Access Policy, see                              #
# DOI: 10.7483/OPENDATA.ATLAS.T9YR.Y7MZ or http://opendata.cern.ch/record/413. #
#                                                                              #
# For a copy of the GNU General Public License, see                            #
# http://www.gnu.org/licenses/.                                                #
#                                                                              #
################################################################################
"""

name    = "voice_to_program"
version = "2015-08-27T0810Z"

import os
import subprocess
import signal

def main():

    print("\n{name}".format(name = name))
    raw_input(
        "\nReady to load a dummy sound card driver...\n" +\
        "Press Enter to continue."
    )
    os.system("sudo modprobe snd-dummy")
    raw_input(
        "\nReady to set Festival running...\n" +\
        "Press Enter to continue."
    )
    process_Festival = subprocess.Popen(["festival", "--tts", "/var/log/dmesg"], preexec_fn = os.setsid)
    raw_input(
        "\nReady to open PulseAudio Volume Control...\n" +\
        "Press Enter to continue.")
    os.system("pavucontrol &")
    raw_input(
        "\nIn PulseAudio Volume Control, select the tab \"Playback\".\n" +\
        "Identify Festival in operaton.\n" +\
        "Change the output sink of Festival to \"Dummy Analog Stereo\".\n" +\
        "Press Enter to continue."
    )
    raw_input(
        "\nReady to stop Festival running...\n" +\
        "Press Enter to continue."
    )
    os.killpg(os.getpgid(process_Festival.pid), 9)
    raw_input(
        "\nIn PulseAudio Volume Control, select the tab \"Recording\".\n" +\
        "Start a Skype call to \"Skype Test Call\".\n" +\
        "In PulseAudio Volume Control, identify Skype in operation.\n" +\
        "Change the input source of Skype to \"Monitor of Dummy Analog " +\
        "Stereo\"\n" +\
        "End the Skype call.\n" +\
        "Press Enter to continue."
    )
    raw_input(
        "\nReady for text entry speech synthesis broadcast to Skype...\n" +\
        "Press Enter to continue (and then make the Skype call when ready).\n"
    )
    while True:
        text = raw_input("> ")
        os.system("echo \"{text}\" | festival --tts".format(text = text))

if __name__ == "__main__":
    main()
