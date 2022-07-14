import numpy as np
import scipy.stats as stats

hand = [17,15,19,17,21]
height = [150,154,169,172,175]

print(f"Correlation value = \n{np.corrcoef(hand, height)}")

from scipy.stats import pearsonr 
l = list(pearsonr(hand, height))
print("Pearsonr value: ", l)

if l[1] > 0.05:
    print("Result: We reject Null Hypothesis")
else:
    print("Result: We accept Null Hypothesis")
