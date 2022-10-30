import os
import streamlit as st
import numpy as np
import pandas as pd


class SignalProcessing:
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
            return ({
                "name": os.path.basename(filePath),
                "signal": self.signal
            })
        except Exception:
            raise ValueError(
                "An Error Occur While Reading the file, please try again.")

    def sample_signal(self, signal, sampleRate):
        try:
            t = signal.iloc[:, 0]
            y = signal.iloc[:, 1]
            sampleRate *= 10
            freqs = np.fft.fftfreq(len(t))
            maxFrequency = np.max(freqs)

            if sampleRate < (2 * maxFrequency) or sampleRate > t.shape[0]:
                raise ValueError('Sample Rate isn''t enough')

            step = t.shape[0] // sampleRate
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
            return (signal)
        except:
            raise ValueError("Can't sample the function")

    def generate_signal(self, amplitude, frequency, phase):
        try:
            sampleRate = 100*10
            time = np.arange(0, 10, 1 / sampleRate)
            y = amplitude * np.sin(2 * np.pi * frequency * time + phase)
            d = {'time': time, 'y': y}

            return (pd.DataFrame(data=d))
        except:
            raise ValueError("Can't Generate this signal...")

    def add_noise(self, signal, SNR):
        try:
            t = signal.iloc[:, 0]
            y = signal.iloc[:, 1]

            initialNoise = np.random.uniform(low=0, high=1, size=len(t))

            multiplicationFactor = (np.mean(y ** 2)) / \
                (SNR * np.mean(np.square(initialNoise)))

            noise = multiplicationFactor * initialNoise

            signalWithNoise = y + noise

            return (pd.DataFrame({
                't': t,
                'y': signalWithNoise
            }))
        except:
            raise ValueError("Can't Add Noise to this signal...")

    def reconstruct_signal(self, sampledSignal):
        try:
            time = sampledSignal.iloc[:, 0]
            amplitude = sampledSignal.iloc[:, 1]
            for i in range(time.shape[0]):
                if time[i] < 0:
                    amplitude[i] = 0

            t_reconstruct = np.linspace(time[0], time[time.shape[0]-1], 10000)
            time = np.array(time)
            amplitude = np.array(amplitude)
            amplitude_reconstruction = self.reconstruct_helper(
                time=t_reconstruct, xp=time, fp=amplitude)
            reconstructedData = {'time': t_reconstruct,
                                 'amplitude': amplitude_reconstruction}
            reconstructedSignal = pd.DataFrame(reconstructedData)
            return(reconstructedSignal)
        except:
            st.error("Can't Reconstruct this signal...")

    def reconstruct_helper(self, time, xp, fp):
        time_matrix = np.resize(time, (len(xp), len(time)))
        v = (xp - time_matrix.T)/(xp[1] - xp[0])
        m = fp * np.sinc(v)
        fp_at_x = np.sum(m, axis=1)
        return fp_at_x

    def add_helper(self, firstSignal, secondSignal):
        try:
            outputSignal = {'t': firstSignal.iloc[:, 0],
                            'y': firstSignal.iloc[:, 1] + secondSignal.iloc[:, 1]}

            outputDataFrame = pd.DataFrame(outputSignal)
            return(outputDataFrame)
        except:
            raise ValueError(
                "The Input signals Can't be plotted.")

    def add_signals(self, lstSignals):
        firstSignal = lstSignals[0]
        for i in range(1, len(lstSignals)):
            firstSignal['signal'] = self.add_helper(
                firstSignal['signal'], lstSignals[i]['signal'])

        return firstSignal
