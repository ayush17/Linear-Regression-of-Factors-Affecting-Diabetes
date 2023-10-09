import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def main():

    # Gathering diabetes the data
    diabt = pd.read_excel('diabetes.xlsx')
    diabArray = np.array(diabt)
    diabetesList = list(diabArray)
    # Removing outliers from diabetes
    diabetesDataFrame = pd.DataFrame(
        diabetesList, columns=['Year', 'FIPS', 'County', 'State', '%Diabetes'])

    min_thresold, max_thresold = diabetesDataFrame['%Diabetes'].quantile([
                                                                         0.05, 0.99])
    dataFrameWithoutOutliers = diabetesDataFrame[(
        diabetesDataFrame['%Diabetes'] <= max_thresold) & (diabetesDataFrame['%Diabetes'] >= min_thresold)]

    print("Data count of diabetes with outliers", diabetesDataFrame.shape[0])
    print("Data count of diabetes without outliers",
          dataFrameWithoutOutliers.shape[0])

    # diabetesList = dataFrameWithoutOutliers.values.tolist()
    # Gathering obesity data
    obses = pd.read_excel('obesity.xlsx')
    obsArray = np.array(obses)
    obesityList = list(obsArray)

    # Removing outliers from obesity
    obesityDataFrame = pd.DataFrame(
        obesityList, columns=['Year', 'FIPS', 'County', 'State', '%Obesity'])

    min_thresold, max_thresold = obesityDataFrame['%Obesity'].quantile([
        0.05, 0.99])

    print("min_thresold->", min_thresold)
    print("max_thresold->", max_thresold)
    dataFrameWithoutOutliers = obesityDataFrame[(
        obesityDataFrame['%Obesity'] <= max_thresold) & (obesityDataFrame['%Obesity'] >= min_thresold)]

    print("Data count of obesity with outliers", obesityDataFrame.shape[0])
    print("Data count of obesity without outliers",
          dataFrameWithoutOutliers.shape[0])
    # obesityList = dataFrameWithoutOutliers.values.tolist()

    obesityArray = []
    diabetesArray = []

    for fpsObesity in obesityList:
        for fpsDiabetes in diabetesList:
            if fpsDiabetes[1] == fpsObesity[1]:
                obesityArray.append(fpsObesity[4])
                diabetesArray.append(fpsDiabetes[4])
    obesityOnX = np.array(obesityArray)
    diabetesOnY = np.array(diabetesArray)
    print(len(obesityOnX))
    print(len(diabetesOnY))
    # Plotting the values
    plt.scatter(obesityOnX, diabetesOnY)
    # naming the x axis
    plt.xlabel('Obesity - axis')
    # naming the y axis
    plt.ylabel('Diabetes - axis')
    plt.show()


if __name__ == "__main__":
    main()
