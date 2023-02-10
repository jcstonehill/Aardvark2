import openmc
from Materials.MaterialBase import MaterialBase

class UO2(MaterialBase):

  def k(self, T):
    pass

  def Cp(self, T):
    pass

  def Rho(self, T):
    return 1

  def GetOpenMCMaterial(self) -> openmc.Material:
    material = openmc.Material()

    material.add_element("U", enrichment = 0.97, percent=1)

    return material