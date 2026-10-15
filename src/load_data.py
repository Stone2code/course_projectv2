import sys
import pandas as pd

def load_data(path: str) -> pd.DataFrame:
 """Load a CSV file into a DataFrame.
 Args:
 path: Relative path to the CSV file.
 Returns:
 The loaded data.
 """

 return pd.read_csv(path, sep=",", encoding="utf-8-sig")
if __name__ == "__main__":
 print(load_data(sys.argv[1]).head())

 def fib_mgx(position:int):
    if position <= 1:
        return position
    return fib(position - 1) + fib(position - 2)
