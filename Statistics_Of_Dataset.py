import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('ADL_202_ex.csv') # Opening CSV File

OvMean = df['Mark'].mean() # Mean of whole Dataset
print("Overall Mean mark: ", round(OverallMean, 4), "\n")

# Mean Line Plotting
X_Axis = df['Sl No']
Y_Axis = [OvMean] * len(X_Axis)
plt.plot(X_Axis, Y_Axis, color='green', linestyle='dotted', label='Mean Line')

# ------------------------------------------------------------------------------------------------------------------------- #

# MALE DATA MANIPULATION
mData = df.loc[df['Gender'] == 'm'] # Separating Male's Data
mMean = mData['Mark'].mean() # Male's mean mark
mLowMark = mData['Mark'].min() # Male's min mark
mHighMark = mData['Mark'].max() # Male's max mark

# Printing Male's mark Details
print(f"Male's Mean mark: {round(mMean, 4)}\nMale's Highest mark: {mHighMark}\nMale's Lowest mark: {mLowMark}\n")

# Male max mark plotting
mHighers = df.loc[(df['Mark'] == mHighMark) & ( df['Gender'] == 'm')] # Male's max marks for graph plotting
plt.scatter(mHighers['Sl No'], mHighers['Mark'], marker='x', facecolor='green', label="Male's Highest Marks") # Scatter Plotting

# Male min mark plotting
mLowers = df.loc[(df['Mark'] == mLowMark) & ( df['Gender'] == 'm')] # Male's min marks for graph plotting
plt.scatter(mLowers['Sl No'], mLowers['Mark'], marker='.', facecolor='red', label="Male's Lowest Mark") # Scatter Plotting

# ------------------------------------------------------------------------------------------------------------------------- #
 
# FEMALE DATA MANIPULATION
fData = df.loc[df['Gender'] == 'f'] # Separating Female's Data
fMean = fData['Mark'].mean() # Female's mean mark
fLowMark = fData['Mark'].min() # Female's min mark
fHighMark = fData['Mark'].max() # Female's max mark

# Printing Female's mark Details
print(f"Female's Mean mark: {fMean}\nFemale's Highest mark: {fHighMark}\nFemale's Lowest mark: {fLowMark}\n")

# Female's max mark plotting
fHighers = df.loc[(df['Mark'] == fHighMark) & ( df['Gender'] == 'f')] # Female's max marks for graph plotting
plt.scatter(fHighers['Sl No'], fHighers['Mark'], marker='x', facecolor='blue', label="Female's Highest Marks") # Scatter Plotting

# Female's min mark plotting
fLowers = df.loc[(df['Mark'] == fLowMark) & ( df['Gender'] == 'f')] # Female's min marks for graph plotting
plt.scatter(fLowers['Sl No'], fLowers['Mark'], marker='o', facecolor='orange', label="Female's Lowest Mark") # Scatter Plotting

# ------------------------------------------------------------------------------------------------------------------------- #

plt.xlabel("Serial Number")
plt.ylabel("Marks")

# Key Box
plt.legend(bbox_to_anchor = (1.5 , 1.03))

plt.show() # Displaying the Graph

# RESULT
print(f"Females's mean mark, {fMean} > Male's mean mark, {round(mMean, 4)}\n")
print("Therefore, both Mathematically & Graphically", '\033[1m' + 'Females are better performers.' + '\033[0m')
