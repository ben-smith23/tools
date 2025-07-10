import pandas as pd
import os

class UCE:
    """Extract unique values from a CSV/Excel column."""
    def __init__(self, base='/content/drive/MyDrive/'):
        self.base = base
        self.fmts = {'.csv', '.xlsx', '.xls'}

    def uniques(self, fname, col, sheet=None):
        path = os.path.join(self.base, fname)
        if not os.path.exists(path):
            raise FileNotFoundError(f"{path} not found")
        ext = os.path.splitext(fname)[1].lower()
        if ext not in self.fmts:
            raise ValueError(f"Bad format: {ext}")
        df = pd.read_csv(path) if ext == '.csv' else pd.read_excel(path, sheet_name=sheet)
        if col not in df.columns:
            raise ValueError(f"'{col}' not in {list(df.columns)}")
        return sorted(df[col].dropna().unique())

def print_uniques(fname, col, sheet=None):
    try:
        vals = UCE().uniques(fname, col, sheet)
        for v in vals:
            print(f"• {v}\n")
    except Exception as e:
        print("Error:", e)


