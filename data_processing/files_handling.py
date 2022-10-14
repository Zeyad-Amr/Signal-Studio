import os
import pandas as pd

outputFileName = 'output.csv'


def reading_signal(filePath):
    """
    return a dataframe from a read file format.

    params:
        filePath (str): a path of the file that wanted to read.

    Returns:
        signalDataFrame (pandas DataFrame): a pandas DataFrame for the signal generated from the csv file.

    """
    try:
        outputFileName = os.path.basename(filePath)
        signalDataFrame = pd.read_csv(filePath)
        return signalDataFrame
    except Exception:
        raise ValueError("An Error Occur While Reading the file, please try again.")


def saving_signal(signalDataFrame, savingPath):
    """
    save the signal dataframe to csv file with specific path.

    params:
        signalDataFrame (pandas DataFrame): a dataframe of a specific signal.
        savingPath (str): a path of the file that wanted to save.
    """
    try:
        if(os.path.isfile(savingPath)):
            signalDataFrame.to_csv(os.path.join(savingPath), index=False)
        else:
            signalDataFrame.to_csv(os.path.join(savingPath, outputFileName), index=False)
    except:
        raise ValueError("An Error Occur while Saving the file, please try again.")