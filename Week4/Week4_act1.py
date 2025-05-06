import pandas as pd

'''
Due date : 9 May 2025 - 
Load a data for Auckland and Christchurch and compare the temperature 
between two cities in a year monthly basis -  
See Link: https://data.niwa.co.nz/pages/clidb-on-datahub
'''


class Temp:
    def __init__(self):
        
        self.auk = pd.read_csv("Auckland_monthly_temp.csv")
        self.chr = pd.read_csv("Christchurch_monthly_temp.csv")
    
    def filter_year_temp(self):
        
        self.filtered_temp_auk = self.auk[self.auk['YEAR'].isin([2024,2025])]
        print("\n\nAuckland 2024-2025 monthly temperature")
        #print(self.filtered_temp_auk[['PERIOD', 'YEAR', 'STATS_VALUE']])

        self.filtered_temp_chr = self.chr[self.chr['YEAR'].isin([2024,2025])]
        print("\n\nChristchurch 2024-2025 monthly temperature")
        #print(self.filtered_temp_chr[['PERIOD', 'YEAR', 'STATS_VALUE']])
  
    def compare_temp(self):

        # Rename columns to avoid name conflict
        self.filtered_temp_auk.rename(columns={"STATS_VALUE": "Auckland_Temp"}, inplace=True)
        self.filtered_temp_chr.rename(columns={"STATS_VALUE": "Christchurch_Temp"}, inplace=True)
        
        # Remove space for macthing the values 
        self.filtered_temp_auk["PERIOD"] = self.filtered_temp_auk["PERIOD"].str.strip()
        self.filtered_temp_chr["PERIOD"] = self.filtered_temp_chr["PERIOD"].str.strip()
        self.filtered_temp_auk["YEAR"] = self.filtered_temp_auk["YEAR"].astype(str).str.strip()
        self.filtered_temp_chr["YEAR"] = self.filtered_temp_chr["YEAR"].astype(str).str.strip()
        
        # Merge the period and year values in two CSV files 
        self.marged_chart = pd.merge(self.filtered_temp_auk, self.filtered_temp_chr,
                                     on=['PERIOD','YEAR'])
        
        # Make a new column Temp_Diff 
        # which is differece of Auckland and Christchurch's monthly temperutaure
        self.marged_chart["Temp_Diff"] = self.marged_chart["Auckland_Temp"] - self.marged_chart["Christchurch_Temp"]

        print(self.marged_chart)


def main():
    temp = Temp()
    temp.filter_year_temp()
    temp.compare_temp()

if __name__ == "__main__":
    main()