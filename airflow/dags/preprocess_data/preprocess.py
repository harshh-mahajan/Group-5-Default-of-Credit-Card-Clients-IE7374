import pandas as pd
import pickle
import os
import logging


"""
    Preprocess the data and store it as a pickle file.

    This function takes the path to the data and the type of data (train or test), reads the data from an Excel file,
    performs preprocessing by dropping specified columns, and stores the preprocessed data as a pickle file.
    Additionally, it logs the preprocessing steps and storage of the processed data.

    Args:
        path (str): The path to the Excel file containing the data.
        type (str): The type of data ('train' or 'test').

    Returns:
        pandas.DataFrame: The preprocessed DataFrame.
"""

    
def process(path, type):
    current_directory = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    preprocesslog = os.path.join(current_directory, "preprocess_data/preprocess.log")


    logging.basicConfig(filename=preprocesslog, level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    logging.warning("Starting a new run")
    
    # read data
    df = pd.read_excel(io = path, index_col=False)
    df = df.drop(columns=['ID','EDUCATION', 'MARRIAGE','AGE']) # drop columns

    if path == 'train':
        logging.info("columns dropped train data")
    elif path == 'test':
        logging.info("columns dropped from test data")

    
    # dump data into pickle formats
    if type == 'train':
        trainpath = os.path.join(current_directory, "data/train_processed_data.pkl")

        with open(trainpath, 'wb') as file:
            pickle.dump(df, file)
        logging.info("train data pickled and stored")

    elif type == 'test':
        testpath = os.path.join(current_directory, "data/new_processed_data.pkl")

        with open(testpath, 'wb') as file:
            pickle.dump(df, file)
        logging.info("test data pickled and stored")
    
    return df
    

if __name__ == "__main__":
    process()

    