class SignalProcessing:
    def __init__(self):
        self.signal = None
        self.sampleRate = None
    
    def initialize_signal(self, signal):
        self.signal = signal
        # TODO: get the sample rate = 2 * max_freq
        self.sampleRate = 0

    def sample_signal(self, sampleRate = None):
        if sampleRate == None:
            sampleRate = self.sampleRate

        # Process the signal
        pass