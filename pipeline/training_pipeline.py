

from src.data_processing import DataProcessing
from src.model_training import Modeltraining

if __name__ == "__main__":
    data_processor = DataProcessing("artifact/raw/data.csv")
    data_processor.run()

    training = Modeltraining()
    training.run()