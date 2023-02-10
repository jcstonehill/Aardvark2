import openmc 
from abc import abstractmethod

class MaterialBase():
  
  @abstractmethod
  def k(self, T):
    pass

  @abstractmethod
  def Cp(self, T):
    pass

  @abstractmethod
  def Rho(self, T):
    pass

  @abstractmethod
  def GetOpenMCMaterial(self) -> openmc.Material:
    pass