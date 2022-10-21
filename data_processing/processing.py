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
    
    def generate_signal(self, amplitude, frequency, phase):
        sampleRate=100 
        time=np.arange(0, 20, 1/sampleRate)
        y=amplitude* np.sin(2*np.pi*frequency*time+ phase)
        d = {'time': time, 'y': y}

        return(pd.DataFrame(data=d))

    def add_noise(self, signal, SNR):
        t = signal.iloc[:, 0]
        y = signal.iloc[:, 1]

        initialNoise = np.random.uniform(low=0, high=1, size=len(t))

        multiplicationFactor = (np.mean(y**2)) / (SNR * np.mean(np.square(initialNoise)))

        noise = multiplicationFactor * initialNoise

        signalWithNoise = y + noise

        return(pd.DataFrame({
            't':t,
            'y':signalWithNoise
        }))
    
    def reconstruct_signal(self, sampledSignal):
        try:
            t = sampledSignal.iloc[:, 0]
            y = sampledSignal.iloc[:, 1]
            for i in range(t.shape[0]):
                if t[i] < 0:
                    y[i] = 0
            y = self.reconstructY(t, y)
            reconstructedData = {'t': t, 'y': y}
            reconstructedSignal = pd.DataFrame(reconstructedData)
            return(reconstructedSignal)
        except:
            st.error("Can't reconstruct this signal...")

    def reconstructY(self, t, y):
        Ts = t[2] - t[1]
        fs = 1 / Ts
        z = 0
        for i in range(t.shape[0]):
            z += y[i] * np.sin(np.pi * fs * (t - i * Ts)) / (np.pi * fs * (t - i * Ts))
        return z


    def saving_signal(self):
        """
        save the signal dataframe to csv file with specific path.

        params:
            signalDataFrame (pandas DataFrame): a dataframe of a specific signal.
            savingPath (str): a path of the file that wanted to save.
        """
        return pd.DataFrame(self.signal).to_csv().encode('utf-8')
