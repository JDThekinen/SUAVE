## @ingroup Analyses-Weights 
# Weights_BWB.py
#
# Created: Apr 2017, Matthew Clarke

# ----------------------------------------------------------------------
#  Imports
# ----------------------------------------------------------------------

import SUAVE
from SUAVE.Core import Data
from Weights import Weights


# ----------------------------------------------------------------------
#  Analysis
# ----------------------------------------------------------------------

## @ingroup Analyses-Weights
class Weights_BWB(Weights):
    """ This is class that evaluates the weight of a BWB aircraft
    
    Assumptions:
        None

    Source:
        N/A

    Inputs:
        None
      
    Outputs:
        None

    Properties Used:
         N/A
    """
    def __defaults__(self):
        """This sets the default values and methods for the BWB weight analysis.
    
        Assumptions:
        None

        Source:
        N/A

        Inputs:
        None

        Outputs:
        None

        Properties Used:
        N/A
        """           
        self.tag = 'weights_bwb'
        
        self.vehicle  = Data()
        self.settings = Data()
        
        
    def evaluate(self,conditions=None):
        """Evaluate the weight analysis.
    
        Assumptions:
        None

        Source:
        N/A

        Inputs:
        None

        Outputs:
        results

        Properties Used:
        N/A
        """         
        # unpack
        vehicle = self.vehicle
        empty   = SUAVE.Methods.Weights.Correlations.BWB.empty

        
        # evaluate
        results = empty(vehicle)
        
        # storing weigth breakdown into vehicle
        vehicle.weight_breakdown = results 

        # updating empty weight
        vehicle.mass_properties.operating_empty = results.empty
              
        # done!
        return results
    
    
    def finalize(self):
        """Finalize the weight analysis.
    
        Assumptions:
        None

        Source:
        N/A

        Inputs:
        None

        Outputs:
        None

        Properties Used:
        N/A
            """           
        self.mass_properties = self.vehicle.mass_properties
        
        return
        