from App.ProblemBuilder.Builder import BuildProblem
from App.OpenMC.OpenMCInterface import OpenMCInterface
from Materials.UO2 import UO2
from openmc_process import CreateCSV

problem = BuildProblem("/home/jacob/aardvark/Case/mesh.msh")

problem.SetMaterial("solid", UO2())
problem.SetMaterial("fluid", UO2())
problem.SetOpenMCBC("hot", "vacuum")
problem.SetOpenMCBC("cold", "vacuum")


interface = OpenMCInterface()

interface.BuildCase(problem)
interface.RunOpenMC()
CreateCSV(problem)
