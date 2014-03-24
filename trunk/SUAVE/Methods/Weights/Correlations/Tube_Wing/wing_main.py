# wing_main.py
# 
# Created:  Andrew Wendorff, Jan 2014
# Modified: Andrew Wendorff, Feb 2014       


# ----------------------------------------------------------------------
#  Imports
# ----------------------------------------------------------------------

from SUAVE.Attributes import Units as Units
import numpy as np
from SUAVE.Structure import (
    Data, Container, Data_Exception, Data_Warning,
)

# ----------------------------------------------------------------------
#   Method
# ----------------------------------------------------------------------

def wing_main(S_gross_w,b,lambda_w,t_c_w,sweep_w,Nult,TOW,wt_zf):
    """ weight = SUAVE.Methods.Weights.Correlations.Tube_Wing.wing_main\
    (S_gross_w,b,lambda_w,t_c_w,sweep_w,Nult,TOW,wt_zf)
        Calculate the wing weight of the aircraft based on the fully-stressed 
        bending weight of the wing box        
        
        Inputs:
            S_gross_w - area of the wing [meters**2]
            b - span of the wing [meters**2]
            lambda_w - taper ratio of the wing [dimensionless]
            t_c_w - thickness-to-chord ratio of the wing [dimensionless]
            sweep_w - sweep of the wing [radians]
            Nult - ultimate load factor of the aircraft [dimensionless]
            TOW - maximum takeoff weight of the aircraft [kilograms]
            wt_zf - zero fuel weight of the aircraft [kilograms]
        
        Outputs:
            weight - weight of the wing [kilograms]
            
        Assumptions:
            calculated total wing weight based on a bending index and actual data 
            from 15 transport aircraft
    """
    
    # unpack inputs
    span  = b / Units.ft # Convert meters to ft
    taper = lambda_w
    sweep = sweep_w
    area  = S_gross_w / Units.ft**2 # Convert meters squared to ft squared
    mtow  = TOW / Units.lb # Convert kg to lbs
    zfw   = wt_zf / Units.lb # Convert kg to lbs

    # process

    #Calculate weight of wing for traditional aircraft wing
    weight = 4.22*area + 1.642*10.**-6. * Nult*(span)**3. *(mtow*zfw)**0.5 \
             * (1.+2.*taper)/(t_c_w*(np.cos(sweep))**2. * area*(1.+taper) )
    weight = weight * Units.lb # Convert lb to kg
 
    return weight