"""Routines providing a simple interface to load matching UM and LFRic test data as Iris cubes."""

from pathlib import Path

import iris
iris.FUTURE.datum_support = True  # avoids some irritating warnings




# Useful public variables
data_path = None
um_filepth = None
lfric_filepth = None
lfric_latlon_filepth = None

data_path = Path('../example_data/')

um_filepth = data_path           / 'u-ct674_20210324T0000Z_um_latlon.nc'
lfric_filepth = data_path        / 'u-ct674_20210324T0000Z_lf_ugrid.nc'
lfric_latlon_filepth = data_path / 'u-ct674_20210324T0000Z_lf_latlon.nc'


def um_all_datacubes():
    return iris.load(um_filepth)

def um_orography():
    cube = iris.load_cube(lfric_latlon_filepth, 'surface_altitude')
    return cube

def um_temp():
    cube = iris.load_cube(um_filepth, 'air_temperature_0')
    return cube

def um_rh_alltimes_3d():
    return iris.load_cube(um_filepth, 'relative_humidity')

def um_rh_singletime_2d():
    cube = um_rh_alltimes_3d()
    return cube[0]

def lfric_all_datacubes():
    with iris.LOAD_POLICY.context(support_multiple_references=True):
        cubes = iris.load(lfric_filepth)
    return cubes

def lfric_orography():
    with iris.LOAD_POLICY.context(support_multiple_references=True):
        cube = iris.load_cube(lfric_filepth, 'surface_altitude')
    return cube[0]

def lfric_temp():
    with iris.LOAD_POLICY.context(support_multiple_references=True):
        cube = iris.load_cube(lfric_filepth, 'air_temperature')
    return cube

def lfric_rh_alltimes_3d():
    with iris.LOAD_POLICY.context(support_multiple_references=True):
        rh_cube = iris.load_cube(lfric_filepth, 'relative_humidity_at_screen_level')
    return rh_cube

def lfric_rh_singletime_2d():
    cube = lfric_rh_alltimes_3d()
    return cube[0]
