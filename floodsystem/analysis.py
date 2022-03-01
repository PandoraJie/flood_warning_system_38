import numpy as np
from datetime import datetime, timedelta
import matplotlib.dates


def polyfit(dates, levels, p):

  x = matplotlib.dates.date2num(dates)
  y = levels

  shift = x[0]
  for i in range(len(x)):
    x[i] = x[i]-shift
  p_coeff = np.polyfit(x, y, p)
  poly = np.poly1d(p_coeff)
  
  #return a tuple
  return (poly, shift)