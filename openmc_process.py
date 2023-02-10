import openmc
from App.ProblemBuilder.Problem import Problem

def CreateCSV(problem: Problem):
    sp = openmc.StatePoint("statepoint.12.h5")

    with open("output.csv", 'w') as file:
        file.write("x, y, z, value\n")
        
        for cell in problem.cells:
            tally = sp.get_tally(id=cell.id)
            cell.Q = float(tally.mean[0][0][0])


            

            for cell in problem.cells:
                x = str(cell.centerPoint[0])
                y = str(cell.centerPoint[1])
                z = str(cell.centerPoint[2])

                file.write(x + ", " + y + ", " + z + ", " + str(cell.Q) + "\n")