import pandas as pd

#File path -> 
# csv: Week4/sample_junk_mail.csv
# parquet: Week4/Sample_data_2.parquet
# text: Week4/sample_text.txt
# img:         


class FileFormat:
    
    def init(self, file_path):
        # Get the path from the user
        #self.file_path = input("Enter the file path: ")
        self.file_path = file_path
        self.data = None

    def load_data(self):
        
        if self.file_path.endswith(".cvs"):
            self.data = pd.read_csv(self.file_path)
        elif self.file_path.endswith(".parquet"):
            self.data = pd.read_parquet(self.file_path)
        elif self.file_path.endswith(".txt"):
            self.data = pd.read_csv(self.file_path, header=None)
        #elif self.file_path.endswith(".img"):
        #    self.data = pd.read
        
        else:
            raise ValueError("Unsupported file format. Please use CSV or Parquet.")
        print(f"Data loaded successfully from {self.file_path}")
    
    def initial_processing(self):
        if self.data is None:
            raise ValueError("No data loaded.")
        
        print("Initial Data Summary:")
        print(self.data.info())
        print("\nMissing Values:")
        print(self.data.isnull().sum())
        print("\nDescriptive Statistics:")
        print(self.data.describe())

# Main
def main():
          
    file_path = 'sample_junk_mail.csv' 
    file = FileFormat(file_path)
    file.load_data()
    file.initial_processing()

if __name__ == "__main__":
    main()