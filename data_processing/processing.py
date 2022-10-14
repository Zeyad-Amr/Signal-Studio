import os
import numpy as np
import pandas as pd


class SignalProcessing:
    def __init__(self):
        self.signal = None
        self.sampleRate = 0
        self.outputFileName = "output.csv"
        self.outputFile = pd.DataFrame({}).to_csv().encode('utf-8')
    
    def reading_signal(self, filePath):
        """
        return a dataframe from a read file format.

        params:
            filePath (str): a path of the file that wanted to read.

        Returns:
            signalDataFrame (pandas DataFrame): a pandas DataFrame for the signal generated from the csv file.

        """
        try:
            self.outputFileName = os.path.basename(filePath)
            self.signal = pd.read_csv(filePath)
            # TODO: Change Sample Rate
            self.sampleRate = 0
        except Exception:
            raise ValueError("An Error Occur While Reading the file, please try again.")

    def sample_signal(self, sampleRate = None):
        if sampleRate == None:
            sampleRate = self.sampleRate

        # Process the signal
        values = np.array(self.values)

        factor = (self.Freq_rate_slider.value()/10)
        sampling_freq =factor*self.max_freq
        sampled_time_points = np.arange(self.time[0],self.time[-1],1/sampling_freq)
        sampled_values_points= values[np.searchsorted(self.time,sampled_time_points)]


    def saving_signal(self):
        """
        save the signal dataframe to csv file with specific path.

        params:
            signalDataFrame (pandas DataFrame): a dataframe of a specific signal.
            savingPath (str): a path of the file that wanted to save.
        """
        self.outputFile = pd.DataFrame(self.signal).to_csv().encode('utf-8')