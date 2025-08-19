import numpy as np

if not hasattr(np, "VisibleDeprecationWarning"):
    try:
        from numpy.exceptions import VisibleDeprecationWarning as _VDW
    except Exception:
        class _VDW(DeprecationWarning):
            pass
    np.VisibleDeprecationWarning = _VDW

import pandas as pd
import sweetviz as sv

df = pd.read_csv("../data/processed_cleveland.csv")
df2 = pd.read_csv("../data/processed_framingham.csv")

report = sv.analyze(df)
report2 = sv.analyze(df2)

report.show_html("cleveland_report.html")
report2.show_html("framingham_report.html")