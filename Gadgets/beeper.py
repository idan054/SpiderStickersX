import numpy as np
import sounddevice as sd


def beep(frequency, duration):
    sample_rate = 44100  # Standard audio sample rate
    t = np.linspace(0, duration / 1000, int(sample_rate * (duration / 1000)), False)  # Generate time array
    tone = 0.5 * np.sin(2 * np.pi * frequency * t)  # Generate sine wave for the beep
    sd.play(tone, sample_rate)
    sd.wait()  # Wait for the sound to finish

