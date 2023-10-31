import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def openFile(path : str):
    f = open(path, "r")
    return f

def plotPoints(points):
    fig = plt.figure()
    ax = fig.add_subplot(projection='3d')
    ax.grid()
    x_vals = points["x"]
    y_vals = points["y"]
    z_vals = points["z"]
    

    print(x_vals)
    #ax.scatter3D(x_vals, y_vals, z_vals, cmap='Greens')
   
    img = ax.scatter(x_vals,  z_vals,y_vals)
    fig.colorbar(img)
    ax.set_title('3D Parametric Plot')

    # Set axes label
    ax.set_xlabel('x', labelpad=20)
    ax.set_ylabel('y', labelpad=20)
    ax.set_zlabel('z', labelpad=20)

    plt.show()






def main():
    vertices = []

    f = openFile("sample.obj")
    data = pd.DataFrame(list(csv.reader(f, delimiter=" ")),columns=["type", "x", "y", "z"])
   # data.index += 1 
    
    vertices = data[data["type"] == "v"]
    vertices = vertices.drop(["type"], axis=1)
    vertices = vertices.astype("float")


    faces =  data[data["type"] == "f"]
    faces = faces.drop(["type"], axis=1)
    faces = faces.astype("int")

    plotPoints(vertices)






main()