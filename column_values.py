import pandas as pd, os

class UCE:
    """Extract unique values from a CSV/Excel column."""
    def __init__(self, base='/content/drive/MyDrive/dissertation_data'):
        self.base = base
        self.fmts = {'.csv', '.xlsx', '.xls'}

    def uniques(self, fname, col, sheet=None):
        paths = [os.path.join(self.base, fname), fname]  # Try Drive path then local
        for path in paths:
            if os.path.exists(path):
                ext = os.path.splitext(path)[1].lower()
                if ext not in self.fmts:
                    raise ValueError(f"Unsupported format: {ext}")
                df = pd.read_csv(path) if ext == '.csv' else pd.read_excel(path, sheet_name=sheet)
                if col not in df.columns:
                    raise ValueError(f"'{col}' not in columns: {df.columns.tolist()}")
                return sorted(df[col].dropna().unique())
        raise FileNotFoundError(f"File not found in: {paths}")

def print_uniques(fname, col, sheet=None):
    try:
        vals = UCE().uniques(fname, col, sheet)
        for v in vals:
            print(f"• {v}\n")
    except Exception as e:
        print("Error:", e)
