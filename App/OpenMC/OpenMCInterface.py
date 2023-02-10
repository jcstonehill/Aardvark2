from App.ProblemBuilder.Problem import Problem
import openmc

class OpenMCInterface:
    def BuildCase(self, problem: Problem):

        
        openmcMaterials = openmc.Materials()
        openmcCells = []
        openmcTallies = openmc.Tallies()
        for cell in problem.cells:
            cell.openmcMaterial.temperature = cell.T
            cell.openmcMaterial.set_density('g/cm3', cell.material.Rho(cell.T))
            openmcMaterials.append(cell.openmcMaterial)

            openmcCells.append(cell.openmcCell)
            openmcTallies.append(cell.openmcTally)

        openmcMaterials.cross_sections = "/home/jacob/aardvark/App/OpenMC/endfb-viii.0-hdf5/cross_sections.xml"
        openmcMaterials.export_to_xml()
        
        openmcTallies.export_to_xml()

        root_universe = openmc.Universe(cells=openmcCells)

        geometry = openmc.Geometry()
        geometry.root_universe = root_universe
        geometry.export_to_xml()

        openmcSettings = openmc.Settings()
        openmcSettings.batches = 12
        openmcSettings.inactive = 10
        openmcSettings.particles = 10000
        openmcSettings.export_to_xml()

        # plot = openmc.Plot()
        # plot.filename = 'pinplot'
        # plot.origin = (0, 0, -0.499999999)
        # plot.width = (1.1, 1.1)
        # plot.pixels = (200, 200)
        # plot.basis = 'xy'
        # vox_plot = openmc.Plot()
        # vox_plot.type = 'voxel'
        # vox_plot.width = (1, 1, 1)
        # vox_plot.pixels = (400, 400, 200)

        # plots = openmc.Plots()
        # plots.append(plot)
        # plots.export_to_xml()

    def RunOpenMC(self):
        openmc.run()

    def PlotOpenMC(self):
        openmc.plot_geometry()



            