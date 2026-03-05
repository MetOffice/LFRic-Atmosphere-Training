# routines
import geovista as gv


# How to suppress warnings about the texture buffer overflow.
#  -- these seem to always occur when using software-emulated OpenGL, but can be ignored for now
def suppress_vtk_warnings():
    import vtk
    vtk.vtkObject.GlobalWarningDisplayOff()
  
# Just for now :  call this always
# suppress_vtk_warnings()


from geovista import Transform, GeoPlotter

def popup_2d_data_xx_yy(sample, title=None) -> None:
    """Quick display of Geovista sample data."""
    
    # create the mesh from the sample data
    mesh = gv.Transform.from_2d(sample.lons, sample.lats, data=sample.data)

    # remove cells from the mesh with nan values
    mesh = mesh.threshold()

    # plot the mesh, and add extra context elements
    plotter = gv.GeoPlotter()
    sargs = dict(title=f"{sample.name} / {sample.units}", shadow=True)
    plotter.add_mesh(mesh, show_edges=True, scalar_bar_args=sargs)
    
    # a base layer shows a global image, and stops it being see-through where there is no data
    plotter.add_base_layer(texture=gv.natural_earth_1())
    # coastlines are always a handy reference
    plotter.add_coastlines()
    # axes for orientation
    plotter.add_axes()
    # title for plot
    if title is None:
        title = sargs['title']
    plotter.add_text(
        title,
        position="upper_left",
        font_size=10,
        shadow=True,
    )
    
    # display the plot
    plotter.show()


def side_by_side_plotter(pv_left, pv_right, show_coastlines=True, show_baselayer=False):
    """
    Plot two meshes alongside each other with same controls.

    Return a new plotter, ready to display.
    
    """
    plotter = GeoPlotter(shape=(1, 2))

    plotter.subplot(0, 0)
    if show_coastlines:
        plotter.add_coastlines()
    if show_baselayer:
        plotter.add_base_layer(texture=gv.natural_earth_1())
    plotter.add_mesh(pv_left, show_edges=True, cmap='magma')

    plotter.subplot(0, 1)
    if show_coastlines:
        plotter.add_coastlines()
    if show_baselayer:
        plotter.add_base_layer(texture=gv.natural_earth_1())
    plotter.add_mesh(pv_right, show_edges=True, cmap='magma')

    # Make left+right move together
    plotter.link_views()

    # Try to rationalise the global view a little.
    plotter.view_xz()
    
    return plotter
    