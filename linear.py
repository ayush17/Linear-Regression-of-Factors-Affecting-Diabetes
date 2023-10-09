import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def estimate_coefficients(x, y):
    # number of observations/points
    no_observation = np.size(x)

    # mean of x and y vector
    slope_x = np.mean(x)
    slope_y = np.mean(y)

    # calculating cross-deviation and deviation about x
    S_xy = np.sum(y*x) - no_observation*slope_y*slope_x
    S_xx = np.sum(x*x) - no_observation*slope_x*slope_x

    # calculating regression coefficients
    b_1 = S_xy / S_xx
    b_0 = slope_y - b_1*slope_x

    return (b_0, b_1)


def plot_regression(x, y, b):
    # plotting the actual points as scatter plot
    plt.scatter(x, y, color="m",
                marker="o", s=30)

    # predicted response vector
    diabetes_pred = b[0] + b[1]*x

    # plotting the regression line
    plt.plot(x, diabetes_pred, color="g")

    # putting labels
    plt.xlabel('x')
    plt.ylabel('y')

    # function to show plot
    plt.show()


def main():
    # observations / data

    diabt = pd.read_excel('diabetes.xlsx')
    diabArray = np.array(diabt)
    diabetesList = list(diabArray)

    obses = pd.read_excel('obesity.xlsx')
    obsArray = np.array(obses)
    obesityList = list(obsArray)
    obesityArray = []
    diabetesArray = []

    for fpsObesity in obesityList:
        for fpsDiabetes in diabetesList:
            if fpsDiabetes[1] == fpsObesity[1]:
                obesityArray.append(fpsObesity[4])
                diabetesArray.append(fpsDiabetes[4])

    obesityOnX = np.array(obesityArray)
    diabetesOnY = np.array(diabetesArray)

    print("Lenght of the obesity array", len(obesityArray))
    print("Lenght of the diabetes array", len(diabetesArray))
    # Just plot the points in x and y axis
    # plt.plot(obesityOnX, diabetesOnY)
    # naming the x axis
    plt.xlabel('Obesity - axis')
    # naming the y axis
    plt.ylabel('Diabetes - axis')
    # obesityOnX = np.linspace(16, 20, 4)

    # Breakin the graph into two parts
    # just count number of points in diabetes array which is from 0-16 and from 16-20
    # Break x axis between the number of fragments with linspace fragments=number of points in diabetes array

    pointsGreaterThan5Diabetes = []
    for value in diabetesArray:
        if (value > 5):
            pointsGreaterThan5Diabetes.append(value)

    obesityOnX = np.linspace(16, 32, len(pointsGreaterThan5Diabetes))
    print("lenght of obesity array", len(obesityOnX))
    print("length of diabetes array", len(pointsGreaterThan5Diabetes))
    plt.scatter(obesityOnX, pointsGreaterThan5Diabetes)
    # plt.show()
    # estimating coefficients
    # coefficient = estimate_coefficients(obesityOnX, pointsGreaterThan5Diabetes)
    # print("coefficients are->:\nb_0 = {}  \
    #       \nb_1 = {}".format(coefficient[0], coefficient[1]))

    # plotting regression line
    # plot_regression(obesityOnX, diabetesOnY, coefficient)


if __name__ == "__main__":
    main()
