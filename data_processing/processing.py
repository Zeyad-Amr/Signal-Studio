import os
import streamlit as st
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
            return({
                "name":os.path.basename(filePath),
                "signal":self.signal
            })
        except Exception:
            raise ValueError("An Error Occur While Reading the file, please try again.")

    def sample_signal(self, signal, sampleRate):
        try:
            t = signal.iloc[:, 0]
            y = signal.iloc[:, 1]

            freqs = np.fft.fftfreq(len(t))
            maxFrequency = 2

            # guard class for freq
            # BUG  # error catch should be handled to catch this message instead of throw (can't sample the function)
            if sampleRate < (2*maxFrequency) or sampleRate > t.shape[0]:
                raise ValueError('Sample Rate isn''t enough')

            step = t.shape[0]//sampleRate
            timeArray = []
            amplitudeArray = []
            i = 0

            while (i < t.shape[0]):
                timeArray.append(t[i])
                amplitudeArray.append(y[i])
                i += step
                i = int(i)
            d = {'t': timeArray, 'y': amplitudeArray}
            signal = pd.DataFrame(data=d)
            return(signal)
        except:
            raise ValueError("Can't sample the function")

    def saving_signal(self):
        """
        save the signal dataframe to csv file with specific path.

        params:
            signalDataFrame (pandas DataFrame): a dataframe of a specific signal.
            savingPath (str): a path of the file that wanted to save.
        """
        return pd.DataFrame(self.signal).to_csv().encode('utf-8')