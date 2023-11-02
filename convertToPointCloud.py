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
    

   
    #ax.scatter3D(x_vals, y_vals, z_vals, cmap='Greens')
   
    img = ax.scatter(x_vals,  z_vals,y_vals)
    fig.colorbar(img)
    ax.set_title('3D Parametric Plot')

    # Set axes label
    ax.set_xlabel('x', labelpad=20)
    ax.set_ylabel('y', labelpad=20)
    ax.set_zlabel('z', labelpad=20)

    plt.show()


def getPointsFromFile(file, normalize = True):
    data = pd.DataFrame(list(csv.reader(file, delimiter=" ")),columns=["type", "x", "y", "z"])
    # data.index += 1
    

    vertices = data[data["type"] == "v"]
    vertices = vertices.drop(["type"], axis=1)
    vertices = vertices.astype("float")

    

    if(normalize):

        globalMin = min([vertices["x"].min(), vertices["y"].min(), vertices["z"].min()])
        globalMax = max([vertices["x"].max(), vertices["y"].max(), vertices["z"].max()])

        normalized_vertices_x=(vertices["x"]-globalMin)/(globalMax-globalMin)
        normalized_vertices_y=(vertices["y"]-globalMin)/(globalMax-globalMin)
        normalized_vertices_z=(vertices["z"]-globalMin)/(globalMax-globalMin)

        vertices["x"] = normalized_vertices_x
        vertices["y"] = normalized_vertices_y
        vertices["z"] = normalized_vertices_z

    faces =  data[data["type"] == "f"]
    faces = faces.drop(["type"], axis=1)
    faces = faces.astype("int")
    


    return (vertices, faces)

def convertToGrid(points):
    points3d = np.array()


def main():

    f = openFile("sample.obj")
    points, _ = getPointsFromFile(f, normalize=True)

    convertToGrid(points)

    return points



