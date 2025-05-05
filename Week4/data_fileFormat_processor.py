import pandas as pd
from PIL import Image
import numpy as np

class DataFileFormat_Processor:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = None

    def load_data(self):
        if self.file_path.endswith('.csv'):
            self.data = pd.read_csv(self.file_path)
        elif self.file_path.endswith('.parquet'):
            self.data = pd.read_parquet(self.file_path)
        elif self.file_path.endswith('.txt'):
            self.data = pd.read_csv(self.file_path, delim_whitespace=True )
        elif self.file_path.endswith('.jpg'):
            self.Img_file()
        else:
            raise ValueError("Unsupported file format. Please use CSV, txt, img, or Parquet.")
        print(f"Data loaded successfully from {self.file_path}")
    
    # Load image file
    def Img_file(self):
        
        img = Image.open(self.file_path)
        # Convert image to numpy array
        self.img_array = np.array(img)
        # Convert the image file into pandas DataFrame( Reshaping )
        self.data = pd.DataFrame(self.img_array.reshape(-1, self.img_array.shape[-1]), 
                                     columns=['R', 'G', 'B'])        
    def initial_processing(self):
        if self.data is None:
            raise ValueError("No data loaded.")
        
        print("Initial Data Summary:")
        print(self.data.info())
        print("\nMissing Values:")
        print(self.data.isnull().sum())
        print("\nDescriptive Statistics:")
        print(self.data.describe())

def main():
    
    #file_path blow
    #sample_junk_mail.csv
    #sample_text.txt
    #Sample_data_2.parquet
    #Pikachu.jpg
    
    file_path = 'Pikachu.jpg' 
    processor = DataFileFormat_Processor(file_path)
    processor.load_data()
    processor.initial_processing()

if __name__ == "__main__":
    main()
