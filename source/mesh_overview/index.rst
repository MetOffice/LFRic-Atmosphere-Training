**************************************************
2. Unstructured Grid (UGRID) - LFRic output format
**************************************************

This module introduces the unstructured world of meshes which are now
used in LFRic.

.. admonition:: In this module you will learn about...

   * why LFRic output is organised around an unstructured
     cubed-sphere mesh rather than a latitude-longitude grid;
   * how the UGRID convention describes mesh geometry and topology
     using nodes, edges, faces, and connectivity;
   * where LFRic quantities are placed on the mesh, including the
     distinction between face-based and edge-based data;
   * which Python tools support each stage of the workflow, from
     loading and inspecting data with Iris to visualising
     unstructured meshes with PyVista, VTK, and GeoVista;
   * why familiar tasks such as plotting, regridding, and regional
     extraction need different methods for mesh-based data.

.. admonition:: At the end of this module you should be able to...

   * describe the practical differences between structured grids and
     unstructured meshes in LFRic Atmosphere output;
   * recognise the main UGRID mesh elements and explain how they are
     used to store LFRic data;
   * choose appropriate tools to load, inspect, visualise, regrid,
     and subset mesh-based LFRic data;
   * use the mesh tutorial notebooks to load example LFRic data and
     examine its cube, coordinate, and mesh metadata;
   * produce basic plots and visualisations of LFRic mesh data and
     interpret what they show;
   * extract data for a geographical region and explain why this
     differs from simple latitude-longitude array slicing.

.. toctree::
   :maxdepth: 1
   :caption: Contents

   structured/index.rst
   unstructured/index.rst
   exercises/practical_exercises
