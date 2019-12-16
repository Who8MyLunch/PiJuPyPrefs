
import pandas as pd

"""
https://pandas.pydata.org/pandas-docs/stable/user_guide/options.html
"""

def apply():
    """Apply all pandas settings functions

    https://pandas.pydata.org/pandas-docs/stable/user_guide/style.html
    """
    # pd.options.display.max_rows = 999
    pd.options.display.max_columns = None
    pd.options.display.latex.repr = True
    pd.options.display.html.table_schema = True

    # pd.options.display.latex.longtable = False  # default False
