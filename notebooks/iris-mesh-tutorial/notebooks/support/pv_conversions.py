"""Utility functions for converting Iris Cubes to PyVista (plottable) objects."""

from geovista import Transform


def pv_from_lfric_cube(cube):
    """Use Geovista to make a PyVista PolyData from a mesh-based 2D face cube."""
    if cube.location != "face":
        # For now only support face data, as connectivity info is different for other types
        raise ValueError(f"cube location must be 'face', not {cube.location}")
    lon, lat = cube.mesh.node_coords
    face_node = cube.mesh.face_node_connectivity
    # Returns a PyVista PolyData class.
    return Transform.from_unstructured(
        xs=lon.points,
        ys=lat.points,
        connectivity=face_node.indices_by_location(),
        start_index=face_node.start_index,
        data=cube.data,
        name=cube.name()
    )


def pv_from_um_cube(cube):
    """Use Geovista to make a PyVista PolyData from a grid-structured 2D cube."""
    xco = cube.coord(axis='x')
    yco = cube.coord(axis='y')
    for co in (xco, yco):
        if not co.has_bounds():
            co.guess_bounds()
    # Returns a PyVista PolyData class.
    return Transform.from_1d(xs=xco.bounds, ys=yco.bounds, data=cube.data, name=cube.name())
