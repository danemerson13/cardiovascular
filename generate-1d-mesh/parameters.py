#!/usr/bin/env python

class OutflowBoundaryConditionType(object):
    RCR = "rcr"
    RESISTANCE = "resistance"

class Parameters():
    """ The Parameter class stores the input parameters for a 1D mesh generation.
    """
    class Units(object):
        MM = "mm"
        CM = "cm"

    def __init__(self):
        self.boundary_surfaces_dir = None
        self.output_directory = None
        self.centerlines_input_file = None
        self.centerlines_output_file = None
        self.compute_centerlines = True
        self.compute_mesh = False
        self.mesh_output_file = None
        self.reorganize_seqments = False
        self.solver_output_file = None
        self.surface_model = None
        self.uniform_material = True
        self.wall_properties_input_file = None
        self.wall_properties_output_file = None
        self.write_mesh_file = False
        self.write_solver_file = False

        self.outputformat = "TEXT"

        self.inflow_input_file = None
        self.inlet_face_input_file = None 

        self.uniform_bc = True
        self.outflow_bc_type = OutflowBoundaryConditionType.RCR 
        self.outflow_bc_file = None
        self.outflow_bc_types = {OutflowBoundaryConditionType.RCR : "rcrt.dat", 
                                 OutflowBoundaryConditionType.RESISTANCE : "resistance.dat"}

        # Mesh size in a vessel segment.
        self.dx = 0.1
        # Min number of elements for a segment.
        self.minnumfe = 10
        self.timestep = 0.000588
        self.numtimesteps = 2000
        self.tincr = 20

        # Units conversion from mm to cgs.
        self.units = self.Units.CM
        self.lcoef = 1.0
        self.Acoef = 1.0

        # Physical parameters.
        self.c1 = 0.0e7
        self.c2 = -22.5267
        self.c3 = 2.65e5
        self.density = 1.055
        self.mattype = "OLUFSEN"
        self.viscosity = 0.04

    def set_units(self, units):
        units = units.lower()
        units_ok = True

        if units == self.Units.MM:
            self.lcoef = 0.1
            self.Acoef = 0.01
        elif units == self.Units.CM:
            self.lcoef = 1.0
            self.Acoef = 1.0
        else:
            units_ok = False 

        return units_ok
 

