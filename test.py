import pandas as pd
import numpy as np

diab = pd.read_excel('diabetes.xlsx')
diabArray = np.array(diab)
diabetesList = list(diabArray)


obs = pd.read_excel('obesity.xlsx')
obsArray = np.array(obs)
obesityList = list(obsArray)


# print(len(obesityList))
# print(len(diabetesList))

# print(obesityList[0][1])
# print(type(diabetesList[0][1]))

obesityArray = []
diabetesArray = []

for fpsObesity in obesityList:
    for fpsDiabetes in diabetesList:
        if fpsDiabetes[1] == fpsObesity[1]:
            obesityArray.append(fpsObesity[4])
            diabetesArray.append(fpsDiabetes[4])

print(len(obesityArray))
print(len(diabetesArray))

# compare obesity FIPS to Diabetes FIPS and on same index get two arrays X->Obesity and Y->Diabetes
