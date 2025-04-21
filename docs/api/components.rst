

PCells
=============================

Parametric Cells for the Generic PDK.

Consider them a foundation from which you can draw inspiration. Feel free to modify their cross-sections and layers to tailor a unique PDK suited for any foundry of your choice.

By doing so, you'll possess a versatile, retargetable PDK, empowering you to design your circuits with speed and flexibility.



components
=============================


analog
=============================



.. autofunction:: gdsfactory.components.analog.interdigital_capacitor

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.interdigital_capacitor(fingers=4, finger_length=20, finger_gap=2, thickness=5, layer='WG').copy()
  c.draw_ports()
  c.plot()



bends
=============================



.. autofunction:: gdsfactory.components.bends.bend_circular

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.bend_circular(angle=90, cross_section='strip', allow_min_radius_violation=False).copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.bends.bend_circular_heater

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.bend_circular_heater(angle=90, heater_to_wg_distance=1.2, heater_width=0.5, layer_heater='HEATER', cross_section='strip', allow_min_radius_violation=False).copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.bends.bend_euler

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.bend_euler(angle=90, p=0.5, with_arc_floorplan=True, cross_section='strip', allow_min_radius_violation=False).copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.bends.bend_euler_s

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.bend_euler_s(p=0.5, with_arc_floorplan=True, cross_section='strip', allow_min_radius_violation=False, port1='o1', port2='o2').copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.bends.bend_s

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.bend_s(size=(11, 1.8), npoints=99, cross_section='strip', allow_min_radius_violation=False).copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.bends.bend_s_offset

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.bend_s_offset(offset=40, radius=10, cross_section='strip', with_euler=True).copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.bends.bezier

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.bezier(control_points=((0, 0), (5, 0), (5, 1.8), (10, 1.8)), npoints=201, with_manhattan_facing_angles=True, cross_section='strip', allow_min_radius_violation=False).copy()
  c.draw_ports()
  c.plot()



containers
=============================



.. autofunction:: gdsfactory.components.containers.add_fiber_array_optical_south_electrical_north

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.add_fiber_array_optical_south_electrical_north(with_loopback=True, pad_pitch=100, pitch=127, pad_gc_spacing=250, electrical_port_orientation=90).copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.containers.add_termination

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.add_termination(component='straight').copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.containers.add_trenches

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.add_trenches(component='coupler', layer_component='WG', layer_trench='DEEP_ETCH', width_trench=2, cross_section='rib_with_trenches', right=0, left=0).copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.containers.add_trenches90

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.add_trenches90(component='bend_euler', layer_component='WG', layer_trench='DEEP_ETCH', width_trench=2, cross_section='rib_with_trenches', top=0, left=0).copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.containers.array

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.array(component='pad', columns=6, rows=1, column_pitch=150, row_pitch=150, add_ports=True, centered=False, auto_rename_ports=False).copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.containers.component_sequence




.. autofunction:: gdsfactory.components.containers.copy_layers

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.copy_layers(factory='cross', layers=((1, 0), (2, 0))).copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.containers.extend_ports

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.extend_ports(component='mmi1x2', length=5, port_type='optical', centered=False, allow_width_mismatch=False, auto_taper=True).copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.containers.extend_ports_list




.. autofunction:: gdsfactory.components.containers.splitter_chain

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.splitter_chain(splitter='mmi1x2', columns=3, bend='bend_s').copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.containers.splitter_tree

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.splitter_tree(coupler='mmi1x2', noutputs=4, spacing=(90, 50), bend_s='bend_s', cross_section='strip').copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.containers.switch_tree

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.switch_tree(noutputs=4, spacing=(500, 100), bend_s='bend_s', cross_section='strip').copy()
  c.draw_ports()
  c.plot()



couplers
=============================



.. autofunction:: gdsfactory.components.couplers.coupler

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.coupler(gap=0.236, length=20, dy=4, dx=10, cross_section='strip', allow_min_radius_violation=False, bend='bend_s').copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.couplers.coupler90

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.coupler90(gap=0.2, bend='bend_euler', straight='straight', cross_section='strip').copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.couplers.coupler90bend

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.coupler90bend(radius=10, gap=0.2, bend='bend_euler', cross_section_inner='strip', cross_section_outer='strip').copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.couplers.coupler90circular

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.coupler90circular(gap=0.2, bend='bend_circular', straight='straight', cross_section='strip').copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.couplers.coupler_adiabatic

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.coupler_adiabatic(length1=20, length2=50, length3=30, wg_sep=1, input_wg_sep=3, output_wg_sep=3, dw=0.1, cross_section='strip').copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.couplers.coupler_asymmetric

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.coupler_asymmetric(gap=0.234, dy=2.5, dx=10, cross_section='strip').copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.couplers.coupler_bent

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.coupler_bent(gap=0.2, radius=26, length=8.6, width1=0.4, width2=0.4, length_straight=10, cross_section='strip').copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.couplers.coupler_broadband

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.coupler_broadband(w_sc=0.5, gap_sc=0.2, w_top=0.6, gap_pc=0.3, legnth_taper=1, bend='bend_euler', coupler_straight='coupler_straight', length_coupler_straight=12.4, lenght_coupler_big_gap=4.7, cross_section='strip', radius=10).copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.couplers.coupler_full

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.coupler_full(coupling_length=40, dx=10, dy=4.8, gap=0.5, dw=0.1, cross_section='strip').copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.couplers.coupler_ring

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.coupler_ring(gap=0.2, radius=5, length_x=4, bend='bend_euler', straight='straight', cross_section='strip', length_extension=3).copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.couplers.coupler_straight

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.coupler_straight(length=10, gap=0.27, cross_section='strip').copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.couplers.coupler_straight_asymmetric

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.coupler_straight_asymmetric(length=10, gap=0.27, width_top=0.5, width_bot=1, cross_section='strip').copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.couplers.coupler_symmetric

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.coupler_symmetric(bend='bend_s', gap=0.234, dy=4, dx=10, cross_section='strip').copy()
  c.draw_ports()
  c.plot()



detectors
=============================



.. autofunction:: gdsfactory.components.detectors.ge_detector_straight_si_contacts

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.ge_detector_straight_si_contacts(length=40, cross_section='pn_ge_detector_si_contacts', via_stack='via_stack_slab_m3', via_stack_width=10, via_stack_spacing=5, via_stack_offset=0, taper_length=20, taper_width=0.8, taper_cros_section='strip').copy()
  c.draw_ports()
  c.plot()



dies
=============================



.. autofunction:: gdsfactory.components.dies.add_frame

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.add_frame(component='rectangle', width=10, spacing=10, layer='WG').copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.dies.align_wafer

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.align_wafer(width=10, spacing=10, cross_length=80, layer='WG', square_corner='bottom_left').copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.dies.die

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.die(size=(10000, 10000), street_width=100, street_length=1000, die_name='chip99', text_size=100, text_location='SW', layer='FLOORPLAN', bbox_layer='FLOORPLAN', text='text', draw_corners=False).copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.dies.die_with_pads

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.die_with_pads(size=(11470, 4900), ngratings=14, npads=31, grating_pitch=250, pad_pitch=300, grating_coupler='grating_coupler_te', cross_section='strip', pad='pad', layer_floorplan='FLOORPLAN', edge_to_pad_distance=150, edge_to_grating_distance=150, with_loopback=True).copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.dies.seal_ring

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.seal_ring(size=(500, 500), seal='via_stack', width=10, padding=10, with_north=True, with_south=True, with_east=True, with_west=True).copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.dies.seal_ring_segmented

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.seal_ring_segmented(size=(500, 500), length_segment=10, width_segment=3, spacing_segment=2, corner='via_stack_corner45_extended', via_stack='via_stack_m1_mtop', with_north=True, with_south=True, with_east=True, with_west=True).copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.dies.wafer

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.wafer(reticle='die', cols=(2, 6, 6, 8, 8, 6, 6, 2), die_name_col_row=False).copy()
  c.draw_ports()
  c.plot()



edge_couplers
=============================



.. autofunction:: gdsfactory.components.edge_couplers.edge_coupler_array

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.edge_coupler_array(edge_coupler='edge_coupler_silicon', n=5, pitch=127, x_reflection=False, text='text_rectangular', text_offset=(10, 20), text_rotation=0).copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.edge_couplers.edge_coupler_array_with_loopback

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.edge_coupler_array_with_loopback(edge_coupler='edge_coupler_silicon', cross_section='strip', radius=30, n=8, pitch=127, extension_length=1, x_reflection=False, text='text_rectangular', text_offset=(0, 10), text_rotation=0).copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.edge_couplers.edge_coupler_silicon

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.edge_coupler_silicon(length=100, width1=0.5, width2=0.2, with_two_ports=True, port_names=('o1', 'o2'), port_types=('optical', 'edge_coupler'), cross_section='strip').copy()
  c.draw_ports()
  c.plot()



filters
=============================



.. autofunction:: gdsfactory.components.filters.awg

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.awg(arms=10, outputs=3, fpr_spacing=50, arm_spacing=1, cross_section='strip').copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.filters.dbr

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.dbr(w1=0.45, w2=0.55, l1=0.159, l2=0.159, n=10, cross_section='strip', straight_length=0.01).copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.filters.dbr_cell

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.dbr_cell(w1=0.45, w2=0.55, l1=0.159, l2=0.159, cross_section='strip').copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.filters.dbr_tapered

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.dbr_tapered(length=10, period=0.85, dc=0.5, w1=0.4, w2=1, taper_length=20, fins=False, fin_size=(0.2, 0.05), cross_section='strip').copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.filters.fiber

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.fiber(core_diameter=10, cladding_diameter=125, layer_core='WG', layer_cladding='WGCLAD').copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.filters.fiber_array

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.fiber_array(n=8, pitch=127, core_diameter=10, cladding_diameter=125, layer_core='WG', layer_cladding='WGCLAD').copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.filters.free_propagation_region

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.free_propagation_region(width1=2, width2=20, length=20, wg_width=0.5, inputs=1, outputs=10, cross_section='strip').copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.filters.loop_mirror

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.loop_mirror(component='mmi1x2', bend90='bend_euler', cross_section='strip').copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.filters.mode_converter

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.mode_converter(gap=0.3, length=10, coupler_straight_asymmetric='coupler_straight_asymmetric', taper='taper', mm_width=1.2, mc_mm_width=1, sm_width=0.5, taper_length=25, cross_section='strip').copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.filters.polarization_splitter_rotator

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.polarization_splitter_rotator(width_taper_in=(0.54, 0.69, 0.83), length_taper_in=(4, 44), width_coupler=(0.9, 0.404), length_coupler=7, gap=0.15, width_out=0.54, length_out=14.33, dy=5, cross_section='strip').copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.filters.terminator

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.terminator(length=50, tapered_width=0.2, doping_layers=('NPP',), doping_offset=1).copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.filters.terminator_spiral

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.terminator_spiral(separation=3, width_tip=0.2, number_of_loops=1, npoints=1000, cross_section='strip').copy()
  c.draw_ports()
  c.plot()



grating_couplers
=============================



.. autofunction:: gdsfactory.components.grating_couplers.grating_coupler_array

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.grating_coupler_array(grating_coupler='grating_coupler_elliptical', pitch=127, n=6, port_name='o1', rotation=-90, with_loopback=False, cross_section='strip', straight_to_grating_spacing=10, centered=True).copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.grating_couplers.grating_coupler_dual_pol

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.grating_coupler_dual_pol(period_x=0.58, period_y=0.58, x_span=11, y_span=11, length_taper=150, width_taper=10, polarization='te', wavelength=1.55, taper='taper', base_layer='WG', cross_section='strip').copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.grating_couplers.grating_coupler_elliptical

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.grating_coupler_elliptical(polarization='te', taper_length=16.6, taper_angle=40, wavelength=1.554, fiber_angle=15, grating_line_width=0.343, neff=2.638, nclad=1.443, n_periods=30, big_last_tooth=False, layer_slab='SLAB150', slab_xmin=-1, slab_offset=2, spiked=True, cross_section='strip').copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.grating_couplers.grating_coupler_elliptical_arbitrary

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.grating_coupler_elliptical_arbitrary(gaps=(0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1), widths=(0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5), taper_length=16.6, taper_angle=60, wavelength=1.554, fiber_angle=15, nclad=1.443, layer_slab='SLAB150', taper_to_slab_offset=-3, polarization='te', spiked=True, bias_gap=0, cross_section='strip').copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.grating_couplers.grating_coupler_elliptical_lumerical

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.grating_coupler_elliptical_lumerical(parameters=(-2.43, 0.1, 0.48, 0.1, 0.607, 0.1, 0.45, 0.1, 0.427, 0.1, 0.476, 0.1, 0.503, 0.1, 0.51, 0.1, 0.494, 0.108, 0.474, 0.15, 0.433, 0.184, 0.387, 0.236, 0.36, 0.243, 0.358, 0.261, 0.353, 0.247, 0.372, 0.229, 0.378, 0.225, 0.377, 0.22, 0.38, 0.219, 0.38, 0.217, 0.383, 0.218, 0.364, 0.237, 0.368, 0.249, 0.344, 0.273, 0.331, 0.274), layer_slab='SLAB150', taper_angle=55, taper_length=12.6, fiber_angle=5, bias_gap=0, cross_section='strip').copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.grating_couplers.grating_coupler_elliptical_lumerical_etch70

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.grating_coupler_elliptical_lumerical_etch70(parameters=(-2.43, 0.1, 0.48, 0.1, 0.607, 0.1, 0.45, 0.1, 0.427, 0.1, 0.476, 0.1, 0.503, 0.1, 0.51, 0.1, 0.494, 0.108, 0.474, 0.15, 0.433, 0.184, 0.387, 0.236, 0.36, 0.243, 0.358, 0.261, 0.353, 0.247, 0.372, 0.229, 0.378, 0.225, 0.377, 0.22, 0.38, 0.219, 0.38, 0.217, 0.383, 0.218, 0.364, 0.237, 0.368, 0.249, 0.344, 0.273, 0.331, 0.274), layer_slab='SLAB150', taper_angle=55, taper_length=12.6, fiber_angle=5, bias_gap=0, cross_section='strip').copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.grating_couplers.grating_coupler_elliptical_trenches

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.grating_coupler_elliptical_trenches(polarization='te', taper_length=16.6, taper_angle=30, trenches_extra_angle=9, wavelength=1.53, fiber_angle=15, grating_line_width=0.343, neff=2.638, ncladding=1.443, layer_trench='SHALLOW_ETCH', p_start=26, n_periods=30, end_straight_length=0.2, taper='taper', cross_section='strip').copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.grating_couplers.grating_coupler_elliptical_uniform

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.grating_coupler_elliptical_uniform(n_periods=20, period=0.75, fill_factor=0.5).copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.grating_couplers.grating_coupler_loss

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.grating_coupler_loss(pitch=127, grating_coupler='grating_coupler_elliptical_trenches', cross_section='strip', port_name='o1', rotation=-90, nfibers=10, grating_coupler_spacing=5).copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.grating_couplers.grating_coupler_rectangular

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.grating_coupler_rectangular(n_periods=20, period=0.75, fill_factor=0.5, width_grating=11, length_taper=150, polarization='te', wavelength=1.55, taper='taper', layer_slab='SLAB150', fiber_angle=15, slab_xmin=-1, slab_offset=1, cross_section='strip').copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.grating_couplers.grating_coupler_rectangular_arbitrary

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.grating_coupler_rectangular_arbitrary(gaps=(0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2), widths=(0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5), width_grating=11, length_taper=150, polarization='te', wavelength=1.55, slab_xmin=-1, slab_offset=1, fiber_angle=15, cross_section='strip').copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.grating_couplers.grating_coupler_tree

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.grating_coupler_tree(n=4, straight_spacing=4, grating_coupler='grating_coupler_elliptical_te', with_loopback=False, bend='bend_euler', fanout_length=0, cross_section='strip').copy()
  c.draw_ports()
  c.plot()



mmis
=============================



.. autofunction:: gdsfactory.components.mmis.mmi

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.mmi(inputs=1, outputs=4, width_taper=1, length_taper=10, length_mmi=5.5, width_mmi=5, gap_input_tapers=0.25, gap_output_tapers=0.25, taper='taper', straight='straight', cross_section='strip').copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.mmis.mmi1x2

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.mmi1x2(width_taper=1, length_taper=10, length_mmi=5.5, width_mmi=2.5, gap_mmi=0.25, cross_section='strip').copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.mmis.mmi1x2_with_sbend

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.mmi1x2_with_sbend(with_sbend=True, cross_section='strip').copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.mmis.mmi2x2

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.mmi2x2(width_taper=1, length_taper=10, length_mmi=5.5, width_mmi=2.5, gap_mmi=0.25, cross_section='strip').copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.mmis.mmi2x2_with_sbend

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.mmi2x2_with_sbend(with_sbend=True, cross_section='strip').copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.mmis.mmi_90degree_hybrid

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.mmi_90degree_hybrid(width=0.5, width_taper=1.7, length_taper=40, length_mmi=175, width_mmi=10, gap_mmi=0.8, straight='straight', cross_section='strip').copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.mmis.mmi_tapered

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.mmi_tapered(inputs=1, outputs=2, width_taper_in=2, length_taper_in=1, width_taper=1, length_taper=10, length_mmi=5.5, width_mmi=5, gap_input_tapers=0.25, gap_output_tapers=0.25, cross_section='strip').copy()
  c.draw_ports()
  c.plot()



mzis
=============================



.. autofunction:: gdsfactory.components.mzis.mzi

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.mzi(delta_length=10, length_y=2, length_x=0.1, bend='bend_euler', straight='straight', splitter='mmi1x2', with_splitter=True, port_e1_splitter='o2', port_e0_splitter='o3', port_e1_combiner='o2', port_e0_combiner='o3', port1='o1', port2='o2', nbends=2, cross_section='strip', mirror_bot=False, add_optical_ports_arms=False, min_length=0.01, auto_rename_ports=True).copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.mzis.mzi1x2_2x2

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.mzi1x2_2x2(delta_length=10, length_y=2, length_x=0.1, bend='bend_euler', straight='straight', splitter='mmi1x2', combiner='mmi2x2', with_splitter=True, port_e1_splitter='o2', port_e0_splitter='o3', port_e1_combiner='o3', port_e0_combiner='o4', port1='o1', port2='o2', nbends=2, cross_section='strip', mirror_bot=False, add_optical_ports_arms=False, min_length=0.01, auto_rename_ports=True).copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.mzis.mzi2x2_2x2_phase_shifter

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.mzi2x2_2x2_phase_shifter(delta_length=10, length_y=2, length_x=200, bend='bend_euler', straight='straight', straight_x_top='straight_heater_metal', splitter='mmi2x2', combiner='mmi2x2', with_splitter=True, port_e1_splitter='o3', port_e0_splitter='o4', port_e1_combiner='o3', port_e0_combiner='o4', port1='o1', port2='o2', nbends=2, cross_section='strip', mirror_bot=False, add_optical_ports_arms=False, min_length=0.01, auto_rename_ports=True).copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.mzis.mzi_lattice

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.mzi_lattice(coupler_lengths=(10, 20), coupler_gaps=(0.2, 0.3), delta_lengths=(10,), mzi='mzi_coupler', splitter='coupler').copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.mzis.mzi_lattice_mmi

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.mzi_lattice_mmi(coupler_widths=(None, None), coupler_widths_tapers=(1, 1), coupler_lengths_tapers=(10, 10), coupler_lengths_mmis=(5.5, 5.5), coupler_widths_mmis=(2.5, 2.5), coupler_gaps_mmis=(0.25, 0.25), taper_functions_mmis=('taper', 'taper'), straight_functions_mmis=('straight', 'straight'), cross_sections_mmis=('strip', 'strip'), delta_lengths=(10,), mzi='mzi2x2_2x2', splitter='mmi2x2').copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.mzis.mzi_pads_center

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.mzi_pads_center(ps_top='straight_heater_metal', ps_bot='straight_heater_metal', mzi='mzi', pad='pad_small', length_x=500, length_y=40, mzi_sig_top='top_r_e2', mzi_gnd_top='top_l_e2', mzi_sig_bot='bot_l_e2', mzi_gnd_bot='bot_r_e2', pad_sig_bot='e1_1_1', pad_sig_top='e3_1_3', pad_gnd_bot='e4_1_2', pad_gnd_top='e2_1_2', delta_length=40, cross_section='strip', cross_section_metal='metal_routing', pad_pitch='pad_pitch').copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.mzis.mzi_phase_shifter

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.mzi_phase_shifter(delta_length=10, length_y=2, length_x=200, bend='bend_euler', straight='straight', straight_x_top='straight_heater_metal', splitter='mmi1x2', with_splitter=True, port_e1_splitter='o2', port_e0_splitter='o3', port_e1_combiner='o2', port_e0_combiner='o3', port1='o1', port2='o2', nbends=2, cross_section='strip', mirror_bot=False, add_optical_ports_arms=False, min_length=0.01, auto_rename_ports=True).copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.mzis.mzi_phase_shifter_top_heater_metal

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.mzi_phase_shifter_top_heater_metal(delta_length=10, length_y=2, length_x=200, bend='bend_euler', straight='straight', straight_x_top='straight_heater_metal', splitter='mmi1x2', with_splitter=True, port_e1_splitter='o2', port_e0_splitter='o3', port_e1_combiner='o2', port_e0_combiner='o3', port1='o1', port2='o2', nbends=2, cross_section='strip', mirror_bot=False, add_optical_ports_arms=False, min_length=0.01, auto_rename_ports=True).copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.mzis.mzi_pin

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.mzi_pin(delta_length=0, length_y=2, length_x=100, bend='bend_euler', straight='straight', straight_x_top='straight_pin', splitter='mmi1x2', with_splitter=True, port_e1_splitter='o2', port_e0_splitter='o3', port_e1_combiner='o2', port_e0_combiner='o3', port1='o1', port2='o2', nbends=2, cross_section='strip', cross_section_x_top='pin', mirror_bot=False, add_optical_ports_arms=False, min_length=0.01, auto_rename_ports=True).copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.mzis.mzit

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.mzit(w0=0.5, w1=0.45, w2=0.55, dy=2, delta_length=10, length=1, coupler_length1=5, coupler_length2=10, coupler_gap1=0.2, coupler_gap2=0.3, taper='taper', taper_length=5, bend90='bend_euler', straight='straight', coupler1='coupler', coupler2='coupler', cross_section='strip').copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.mzis.mzit_lattice

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.mzit_lattice(coupler_lengths=(10, 20), coupler_gaps=(0.2, 0.3), delta_lengths=(10,)).copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.mzis.mzm

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.mzm(delta_length=10, length_y=2, length_x=200, bend='bend_euler', straight='straight', straight_x_top='straight_pin', straight_x_bot='straight_pin', splitter='mmi1x2', with_splitter=True, port_e1_splitter='o2', port_e0_splitter='o3', port_e1_combiner='o2', port_e0_combiner='o3', port1='o1', port2='o2', nbends=2, cross_section='strip', mirror_bot=False, add_optical_ports_arms=False, min_length=0.01, auto_rename_ports=True).copy()
  c.draw_ports()
  c.plot()



pads
=============================



.. autofunction:: gdsfactory.components.pads.pad

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.pad(size=(100, 100), layer='MTOP', port_inclusion=0, port_orientation=0, port_orientations=(180, 90, 0, -90), port_type='pad').copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.pads.pad_array

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.pad_array(pad='pad', columns=6, rows=1, column_pitch=150, row_pitch=150, port_orientation=0, layer='MTOP', centered_ports=False, auto_rename_ports=False).copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.pads.pad_array0

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.pad_array0(pad='pad', columns=1, rows=3, column_pitch=150, row_pitch=150, port_orientation=0, layer='MTOP', centered_ports=False, auto_rename_ports=False).copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.pads.pad_array180

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.pad_array180(pad='pad', columns=1, rows=3, column_pitch=150, row_pitch=150, port_orientation=180, layer='MTOP', centered_ports=False, auto_rename_ports=False).copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.pads.pad_array270

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.pad_array270(pad='pad', columns=6, rows=1, column_pitch=150, row_pitch=150, port_orientation=270, layer='MTOP', centered_ports=False, auto_rename_ports=False).copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.pads.pad_array90

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.pad_array90(pad='pad', columns=6, rows=1, column_pitch=150, row_pitch=150, port_orientation=90, layer='MTOP', centered_ports=False, auto_rename_ports=False).copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.pads.pad_gsg_open

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.pad_gsg_open(size=(22, 7), layer_metal='MTOP', metal_spacing=5, short=False, pad='pad', pad_pitch=150, route_xsize=50).copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.pads.pad_gsg_short

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.pad_gsg_short(size=(22, 7), layer_metal='MTOP', metal_spacing=5, short=True, pad='pad', pad_pitch=150, route_xsize=50).copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.pads.pad_rectangular

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.pad_rectangular(size='pad_size', layer='MTOP', port_inclusion=0, port_orientation=0, port_orientations=(180, 90, 0, -90), port_type='pad').copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.pads.pad_small

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.pad_small(size=(80, 80), layer='MTOP', port_inclusion=0, port_orientation=0, port_orientations=(180, 90, 0, -90), port_type='pad').copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.pads.pads_shorted

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.pads_shorted(pad='pad', columns=8, pad_pitch=150, layer_metal='MTOP', metal_width=10).copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.pads.rectangle_with_slits

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.rectangle_with_slits(size=(100, 200), layer='WG', layer_slit='SLAB150', centered=False, slit_size=(1, 1), slit_column_pitch=20, slit_row_pitch=20, slit_enclosure=10).copy()
  c.draw_ports()
  c.plot()



pcms
=============================



.. autofunction:: gdsfactory.components.pcms.cavity

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.cavity(component='dbr', coupler='coupler', length=0.1, gap=0.2).copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.pcms.cdsem_all

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.cdsem_all(widths=(0.4, 0.45, 0.5, 0.6, 0.8, 1), dense_lines_width=0.3, dense_lines_width_difference=0.02, dense_lines_gap=0.3, dense_lines_labels=('DL', 'DM', 'DH'), straight='straight', bend90='bend_circular', cross_section='strip', text='text_rectangular', spacing=5, cdsem_bend180='cdsem_bend180', text_size=1).copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.pcms.cdsem_bend180

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.cdsem_bend180(width=0.5, radius=10, wg_length=420, straight='straight', bend90='bend_circular', cross_section='strip', text='text_rectangular', text_size=1).copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.pcms.cdsem_coupler

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.cdsem_coupler(length=420, gaps=(0.15, 0.2, 0.25), cross_section='strip_no_ports', text='text_rectangular', spacing=7, text_size=1).copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.pcms.cdsem_straight

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.cdsem_straight(widths=(0.4, 0.45, 0.5, 0.6, 0.8, 1), length=420, cross_section='strip_no_ports', text='text_rectangular', spacing=7, text_size=1).copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.pcms.cdsem_straight_density

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.cdsem_straight_density(widths=(0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3), gaps=(0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3, 0.3), length=420, label='', cross_section='strip_no_ports', text='text_rectangular', text_size=1).copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.pcms.cutback_2x2

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.cutback_2x2(component='mmi2x2', cols=4, rows=5, port1='o1', port2='o2', port3='o3', port4='o4', bend180='bend_circular180', mirror=False, cross_section='strip', straight='straight').copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.pcms.cutback_bend

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.cutback_bend(component='bend_euler', straight='straight', straight_length=5, rows=6, cols=5).copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.pcms.cutback_bend180

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.cutback_bend180(component='bend_euler180', straight='straight', straight_length=5, rows=6, cols=6, spacing=3).copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.pcms.cutback_bend180circular

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.cutback_bend180circular(component='bend_circular180', straight='straight', straight_length=5, rows=6, cols=6, spacing=3).copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.pcms.cutback_bend90

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.cutback_bend90(component='bend_euler', straight='straight', straight_length=5, rows=6, cols=6, spacing=5).copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.pcms.cutback_bend90circular

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.cutback_bend90circular(component='bend_circular', straight='straight', straight_length=5, rows=6, cols=6, spacing=5).copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.pcms.cutback_component

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.cutback_component(component='taper_0p5_to_3_l36', cols=4, rows=5, port1='o1', port2='o2', bend180='bend_euler180', mirror=False, mirror1=False, mirror2=False, straight='straight', cross_section='strip').copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.pcms.cutback_component_mirror

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.cutback_component_mirror(component='taper_0p5_to_3_l36', cols=4, rows=5, port1='o1', port2='o2', bend180='bend_euler180', mirror=True, mirror1=False, mirror2=False, straight='straight', cross_section='strip').copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.pcms.cutback_splitter

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.cutback_splitter(component='mmi1x2', cols=4, rows=5, port1='o1', port2='o2', port3='o3', bend180='bend_euler180', mirror=False, straight='straight', cross_section='strip').copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.pcms.greek_cross

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.greek_cross(length=30, layers=('WG', 'N'), widths=(2, 3), via_stack='via_stack_npp_m1', layer_index=0).copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.pcms.greek_cross_with_pads

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.greek_cross_with_pads(pad='pad', pad_pitch=150, greek_cross_component='greek_cross', pad_via='via_stack_m1_mtop', pad_port_name='e4').copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.pcms.litho_calipers

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.litho_calipers(notch_size=(2, 5), notch_spacing=2, num_notches=11, offset_per_notch=0.1, row_spacing=0, layer1='WG', layer2='SLAB150').copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.pcms.litho_ruler

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.litho_ruler(height=2, width=0.5, spacing=2, scale=(3, 1, 1, 1, 1, 2, 1, 1, 1, 1), num_marks=21, layer='WG').copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.pcms.litho_steps

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.litho_steps(line_widths=(1, 2, 4, 8, 16), line_spacing=10, height=100, layer='WG').copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.pcms.pixel

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.pixel(size=1, layer='WG').copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.pcms.qrcode

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.qrcode(data='mask01', psize=1, layer='WG').copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.pcms.resistance_meander

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.resistance_meander(pad_size=(50, 50), num_squares=1000, width=1, res_layer='MTOP', pad_layer='MTOP').copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.pcms.resistance_sheet

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.resistance_sheet(width=10, layers=('HEATER',), layer_offsets=(0, 0.2), pad='via_stack_heater_mtop', pad_size=(50, 50), pad_pitch=100, pad_port_name='e4').copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.pcms.staircase

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.staircase(component='bend_euler', straight='straight', length_v=5, length_h=5, rows=4).copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.pcms.verniers

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.verniers(widths=(0.1, 0.2, 0.3, 0.4, 0.5), gap=0.1, xsize=100, layer_label='TEXT', straight='straight', cross_section='strip_no_ports').copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.pcms.version_stamp

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.version_stamp(labels=('demo_label',), with_qr_code=False, layer='WG', pixel_size=1, text_size=10).copy()
  c.draw_ports()
  c.plot()



rings
=============================



.. autofunction:: gdsfactory.components.rings.coupler_bend

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.coupler_bend(radius=10, coupler_gap=0.2, coupling_angle_coverage=120, cross_section_inner='strip', cross_section_outer='strip', bend_output='bend_euler').copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.rings.coupler_ring_bend

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.coupler_ring_bend(radius=10, coupler_gap=0.2, coupling_angle_coverage=90, length_x=0, cross_section_inner='strip', cross_section_outer='strip', bend_output='bend_euler', straight='straight').copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.rings.disk

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.disk(radius=10, gap=0.2, wrap_angle_deg=180, parity=1, cross_section='strip').copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.rings.disk_heater

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.disk_heater(radius=10, gap=0.2, wrap_angle_deg=180, parity=1, cross_section='strip', heater_layer='HEATER', via_stack='via_stack_heater_mtop', heater_width=5, heater_extent=2, via_width=10, port_orientation=90).copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.rings.ring

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.ring(radius=10, width=0.5, angle_resolution=2.5, layer='WG', angle=360).copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.rings.ring_crow

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.ring_crow(gaps=(0.2, 0.2, 0.2, 0.2), radius=(10, 10, 10), ring_cross_sections=('strip', 'strip', 'strip'), length_x=0, lengths_y=(0, 0, 0), cross_section='strip').copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.rings.ring_crow_couplers

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.ring_crow_couplers(radius=(10, 10, 10), bends=('bend_circular', 'bend_circular', 'bend_circular'), ring_cross_sections=('strip', 'strip', 'strip'), couplers=('coupler', 'coupler', 'coupler', 'coupler')).copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.rings.ring_double

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.ring_double(gap=0.2, radius=10, length_x=0.01, length_y=0.01, bend='bend_euler', straight='straight', coupler_ring='coupler_ring', cross_section='strip').copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.rings.ring_double_bend_coupler

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.ring_double_bend_coupler(radius=5, gap=0.2, coupling_angle_coverage=70, length_x=0.6, length_y=0.6, cross_section_inner='strip', cross_section_outer='strip').copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.rings.ring_double_heater

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.ring_double_heater(gap=0.2, radius=10, length_x=1, length_y=0.01, coupler_ring='coupler_ring', straight='straight', bend='bend_euler', cross_section_heater='heater_metal', cross_section_waveguide_heater='strip_heater_metal', cross_section='strip', via_stack='via_stack_heater_mtop_mini', via_stack_offset=(1, 0), with_drop=True).copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.rings.ring_double_pn

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.ring_double_pn(add_gap=0.3, drop_gap=0.3, radius=5, doping_angle=85, doped_heater=True, doped_heater_angle_buffer=10, doped_heater_layer='NPP', doped_heater_width=0.5, doped_heater_waveguide_offset=2.175, with_drop=True).copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.rings.ring_single

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.ring_single(gap=0.2, radius=10, length_x=4, length_y=0.6, bend='bend_euler', straight='straight', coupler_ring='coupler_ring', cross_section='strip').copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.rings.ring_single_array

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.ring_single_array(ring='ring_single', spacing=5, cross_section='strip').copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.rings.ring_single_bend_coupler

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.ring_single_bend_coupler(radius=5, gap=0.2, coupling_angle_coverage=180, bend='bend_circular', bend_output='bend_euler', length_x=0.6, length_y=0.6, cross_section_inner='strip', cross_section_outer='strip').copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.rings.ring_single_dut

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.ring_single_dut(component='straight', gap=0.2, length_x=4, length_y=0, radius=5, coupler='coupler_ring', bend='bend_euler', with_component=True, port_name='o1').copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.rings.ring_single_heater

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.ring_single_heater(gap=0.2, radius=10, length_x=1, length_y=0.01, coupler_ring='coupler_ring', straight='straight', bend='bend_euler', cross_section_heater='heater_metal', cross_section_waveguide_heater='strip_heater_metal', cross_section='strip', via_stack='via_stack_heater_mtop_mini', via_stack_offset=(1, 0), with_drop=False).copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.rings.ring_single_pn

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.ring_single_pn(gap=0.3, radius=5, doping_angle=250, doped_heater=True, doped_heater_angle_buffer=10, doped_heater_layer='NPP', doped_heater_width=0.5, doped_heater_waveguide_offset=1.175, pn_vias='via_stack_slab_m3', pn_vias_width=3).copy()
  c.draw_ports()
  c.plot()



shapes
=============================



.. autofunction:: gdsfactory.components.shapes.C

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.C(width=1, size=(10, 20), layer='WG', port_type='electrical').copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.shapes.L

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.L(width=1, size=(10, 20), layer='MTOP', port_type='electrical').copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.shapes.circle

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.circle(radius=10, angle_resolution=2.5, layer='WG').copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.shapes.compass

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.compass(size=(4, 2), layer='WG', port_type='electrical', port_inclusion=0, port_orientations=(180, 90, 0, -90), auto_rename_ports=True).copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.shapes.cross

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.cross(length=10, width=3, layer='WG').copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.shapes.ellipse

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.ellipse(radii=(10, 5), angle_resolution=2.5, layer='WG').copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.shapes.fiducial_squares

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.fiducial_squares(layers=((1, 0),), size=(5, 5), offset=0.14).copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.shapes.hexagon

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.hexagon(sides=6, side_length=10, layer='WG', port_type='placement').copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.shapes.marker_te

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.marker_te(size=(10.4, 10.4), layer='TE', centered=True, port_type='electrical', port_orientations=(180, 90, 0, -90)).copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.shapes.marker_tm

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.marker_tm(size=(10.4, 10.4), layer='TM', centered=True, port_type='electrical', port_orientations=(180, 90, 0, -90)).copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.shapes.nxn

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.nxn(west=1, east=4, north=0, south=0, xsize=8, ysize=8, wg_width=0.5, layer='WG', wg_margin=1).copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.shapes.octagon

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.octagon(sides=8, side_length=10, layer='WG', port_type='placement').copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.shapes.rectangle

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.rectangle(size=(4, 2), layer='WG', centered=False, port_type='electrical', port_orientations=(180, 90, 0, -90)).copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.shapes.rectangles

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.rectangles(size=(4, 2), layers=('WG', 'SLAB150'), centered=True).copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.shapes.regular_polygon

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.regular_polygon(sides=6, side_length=10, layer='WG', port_type='placement').copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.shapes.triangle

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.triangle(x=10, xtop=0, y=20, ybot=0, layer='WG').copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.shapes.triangle2

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.triangle2(spacing=3).copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.shapes.triangle2_thin

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.triangle2_thin(spacing=3).copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.shapes.triangle4

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.triangle4().copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.shapes.triangle4_thin

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.triangle4_thin(spacing=3).copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.shapes.triangle_thin

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.triangle_thin(x=2, xtop=0.2, y=5, ybot=0, layer='WG').copy()
  c.draw_ports()
  c.plot()



spirals
=============================



.. autofunction:: gdsfactory.components.spirals.delay_snake

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.delay_snake(length=1600, length0=0, length2=0, n=2, cross_section='strip').copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.spirals.delay_snake2

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.delay_snake2(length=1600, length0=0, length2=0, n=2, bend180='bend_euler180', cross_section='strip').copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.spirals.delay_snake_sbend

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.delay_snake_sbend(length=100, length1=0, length4=0, radius=5, waveguide_spacing=5, bend='bend_euler', sbend='bend_s', sbend_xsize=100, cross_section='strip').copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.spirals.spiral

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.spiral(length=100, bend='bend_euler', straight='straight', cross_section='strip', spacing=3, n_loops=6).copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.spirals.spiral_double

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.spiral_double(min_bend_radius=10, separation=2, number_of_loops=3, npoints=1000, cross_section='strip', bend='bend_circular').copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.spirals.spiral_inductor

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.spiral_inductor(width=3, pitch=3, turns=16, outer_diameter=800, tail=50).copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.spirals.spiral_racetrack

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.spiral_racetrack(straight_length=20, spacings=(2, 2, 3, 3, 2, 2), bend_s='bend_s', cross_section='strip', extra_90_deg_bend=False, allow_min_radius_violation=False).copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.spirals.spiral_racetrack_fixed_length

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.spiral_racetrack_fixed_length(length=1000, in_out_port_spacing=150, n_straight_sections=8, min_spacing=5, bend='bend_circular', bend_s='bend_s', cross_section='strip').copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.spirals.spiral_racetrack_heater_doped

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.spiral_racetrack_heater_doped(straight_length=30, spacing=2, num=8, bend_s='bend_s', waveguide_cross_section='strip', heater_cross_section='npp').copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.spirals.spiral_racetrack_heater_metal

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.spiral_racetrack_heater_metal(straight_length=30, spacing=2, num=8, bend_s='bend_s', waveguide_cross_section='strip', heater_cross_section='heater_metal', via_stack='via_stack_heater_mtop').copy()
  c.draw_ports()
  c.plot()



superconductors
=============================



.. autofunction:: gdsfactory.components.superconductors.hline

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.hline(length=10, width=0.5, layer='WG', port_type='optical').copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.superconductors.optimal_90deg

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.optimal_90deg(width=100, num_pts=15, length_adjust=1, layer=(1, 0)).copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.superconductors.optimal_hairpin

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.optimal_hairpin(width=0.2, pitch=0.6, length=10, turn_ratio=4, num_pts=50, layer=(1, 0)).copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.superconductors.optimal_step

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.optimal_step(start_width=10, end_width=22, num_pts=50, width_tol=0.001, anticrowding_factor=1.2, symmetric=False, layer=(1, 0)).copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.superconductors.snspd

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.snspd(wire_width=0.2, wire_pitch=0.6, size=(10, 8), turn_ratio=4, terminals_same_side=False, layer=(1, 0), port_type='electrical').copy()
  c.draw_ports()
  c.plot()



tapers
=============================



.. autofunction:: gdsfactory.components.tapers.ramp

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.ramp(length=10, width1=5, width2=8, layer='WG').copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.tapers.taper

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.taper(length=10, width1=0.5, with_two_ports=True, cross_section='strip', port_names=('o1', 'o2'), port_types=('optical', 'optical'), with_bbox=True).copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.tapers.taper_0p5_to_3_l36

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.taper_0p5_to_3_l36(cross_section='strip').copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.tapers.taper_adiabatic

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.taper_adiabatic(width1=0.5, width2=5, length=0, alpha=1, wavelength=1.55, npoints=200, cross_section='strip', max_length=200).copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.tapers.taper_cross_section

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.taper_cross_section(cross_section1='strip_rib_tip', cross_section2='rib2', length=10, npoints=100, linear=False, width_type='sine').copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.tapers.taper_cross_section_linear

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.taper_cross_section_linear(cross_section1='strip_rib_tip', cross_section2='rib2', length=10, npoints=2, linear=True, width_type='sine').copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.tapers.taper_cross_section_parabolic

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.taper_cross_section_parabolic(cross_section1='strip_rib_tip', cross_section2='rib2', length=10, npoints=101, linear=False, width_type='parabolic').copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.tapers.taper_cross_section_sine

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.taper_cross_section_sine(cross_section1='strip_rib_tip', cross_section2='rib2', length=10, npoints=101, linear=False, width_type='sine').copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.tapers.taper_electrical

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.taper_electrical(length=10, width1=0.5, with_two_ports=True, cross_section='metal_routing', port_names=('e1', 'e2'), port_types=('electrical', 'electrical'), with_bbox=True).copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.tapers.taper_from_csv

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.taper_from_csv(cross_section='strip').copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.tapers.taper_nc_sc

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.taper_nc_sc(width1=1, width2=0.5, length=20, layer_wg='WG', layer_nitride='WGN', width_tip_nitride=0.15, width_tip_silicon=0.15, cross_section='strip').copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.tapers.taper_parabolic

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.taper_parabolic(length=20, width1=0.5, width2=5, exp=0.5, npoints=100, layer='WG').copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.tapers.taper_sc_nc

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.taper_sc_nc(width1=0.5, width2=1, length=20, layer_wg='WG', layer_nitride='WGN', width_tip_nitride=0.15, width_tip_silicon=0.15, cross_section='strip').copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.tapers.taper_strip_to_ridge

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.taper_strip_to_ridge(length=10, width1=0.5, width2=0.5, w_slab1=0.15, w_slab2=6, layer_wg='WG', layer_slab='SLAB90', cross_section='strip', use_slab_port=False).copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.tapers.taper_strip_to_ridge_trenches

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.taper_strip_to_ridge_trenches(length=10, width=0.5, slab_offset=3, trench_width=2, trench_layer='DEEP_ETCH', layer_wg='WG', trench_offset=0.1).copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.tapers.taper_strip_to_slab150

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.taper_strip_to_slab150(length=10, width1=0.5, width2=0.5, w_slab1=0.15, w_slab2=6, layer_wg='WG', layer_slab='SLAB150', cross_section='strip', use_slab_port=False).copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.tapers.taper_w10_l100

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.taper_w10_l100(cross_section='strip').copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.tapers.taper_w10_l150

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.taper_w10_l150(cross_section='strip').copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.tapers.taper_w10_l200

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.taper_w10_l200(cross_section='strip').copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.tapers.taper_w11_l200

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.taper_w11_l200(cross_section='strip').copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.tapers.taper_w12_l200

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.taper_w12_l200(cross_section='strip').copy()
  c.draw_ports()
  c.plot()



texts
=============================



.. autofunction:: gdsfactory.components.texts.pixel_array

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.pixel_array(pixels='\n XXX\nX   X\nXXXXX\nX   X\nX   X\n\n', pixel_size=10, layer='M1').copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.texts.text

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.text(text='abcd', size=10, position=(0, 0), justify='left', layer='WG').copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.texts.text_freetype

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.text_freetype(text='a', size=10, justify='left', layer='WG').copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.texts.text_klayout

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.text_klayout(text='a', layer='WG').copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.texts.text_lines

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.text_lines(text=('Chip', '01'), size=0.4, layer='WG').copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.texts.text_rectangular

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.text_rectangular(text='abcd', size=10, position=(0, 0), justify='left', layer='WG').copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.texts.text_rectangular_multi_layer

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.text_rectangular_multi_layer(text='abcd', layers=('WG', 'M1', 'M2', 'MTOP')).copy()
  c.draw_ports()
  c.plot()



vias
=============================



.. autofunction:: gdsfactory.components.vias.via

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.via(size=(0.7, 0.7), enclosure=1, layer='VIAC', bbox_offset=0, pitch=2).copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.vias.via_chain

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.via_chain(num_vias=100, cols=10, via='via1', contact='via_stack_m2_m3', layers_bot=('M1',), layers_top=('M2',), offsets_top=(0,), offsets_bot=(0,), via_min_enclosure=1, min_metal_spacing=1, contact_offset=0).copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.vias.via_circular

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.via_circular(radius=0.35, enclosure=1, layer='VIAC', pitch=2, angle_resolution=2.5).copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.vias.via_corner

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.via_corner(cross_section=(({'function': 'metal2', 'module': 'gdsfactory.cross_section'}, (0, 180)), ({'function': 'metal3', 'module': 'gdsfactory.cross_section'}, (90, 270))), layers_labels=('m2', 'm3')).copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.vias.via_stack

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.via_stack(size=(11, 11), layers=('M1', 'M2', 'MTOP'), correct_size=True, slot_horizontal=False, slot_vertical=False, port_orientations=(180, 90, 0, -90)).copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.vias.via_stack_corner45

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.via_stack_corner45(width=10, layers=('M1', 'M2', 'MTOP'), correct_size=True).copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.vias.via_stack_corner45_extended

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.via_stack_corner45_extended(corner='via_stack_corner45', via_stack='via_stack', width=3, length=10).copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.vias.via_stack_heater_mtop_mini

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.via_stack_heater_mtop_mini(size=(4, 4), layers=('HEATER', 'M2', 'MTOP'), correct_size=True, slot_horizontal=False, slot_vertical=False, port_orientations=(180, 90, 0, -90)).copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.vias.via_stack_m1_m3

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.via_stack_m1_m3(size=(11, 11), layers=('M1', 'M2', 'MTOP'), correct_size=True, slot_horizontal=False, slot_vertical=False, port_orientations=(180, 90, 0, -90)).copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.vias.via_stack_m1_mtop

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.via_stack_m1_mtop(size=(11, 11), layers=('M1', 'M2', 'MTOP'), correct_size=True, slot_horizontal=False, slot_vertical=False, port_orientations=(180, 90, 0, -90)).copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.vias.via_stack_m2_m3

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.via_stack_m2_m3(size=(11, 11), layers=('M2', 'MTOP'), correct_size=True, slot_horizontal=False, slot_vertical=False, port_orientations=(180, 90, 0, -90)).copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.vias.via_stack_npp_m1

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.via_stack_npp_m1(size=(11, 11), layers=('WG', 'NPP', 'M1'), correct_size=True, slot_horizontal=False, slot_vertical=False, port_orientations=(180, 90, 0, -90)).copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.vias.via_stack_slab_m1

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.via_stack_slab_m1(size=(11, 11), layers=('SLAB90', 'M1'), correct_size=True, slot_horizontal=False, slot_vertical=False, port_orientations=(180, 90, 0, -90)).copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.vias.via_stack_slab_m1_horizontal

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.via_stack_slab_m1_horizontal(size=(11, 11), layers=('SLAB90', 'M1'), correct_size=True, slot_horizontal=True, slot_vertical=False, port_orientations=(180, 90, 0, -90)).copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.vias.via_stack_slab_m2

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.via_stack_slab_m2(size=(11, 11), layers=('SLAB90', 'M1', 'M2'), correct_size=True, slot_horizontal=False, slot_vertical=False, port_orientations=(180, 90, 0, -90)).copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.vias.via_stack_slab_npp_m3

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.via_stack_slab_npp_m3(size=(11, 11), layers=('SLAB90', 'NPP', 'M1'), correct_size=True, slot_horizontal=False, slot_vertical=False, port_orientations=(180, 90, 0, -90)).copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.vias.via_stack_with_offset

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.via_stack_with_offset(layers=('PPP', 'M1'), size=(10, 10)).copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.vias.via_stack_with_offset_m1_m3

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.via_stack_with_offset_m1_m3(layers=('M1', 'M2', 'MTOP'), size=(10, 10)).copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.vias.via_stack_with_offset_ppp_m1

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.via_stack_with_offset_ppp_m1(layers=('PPP', 'M1'), size=(10, 10)).copy()
  c.draw_ports()
  c.plot()



waveguides
=============================



.. autofunction:: gdsfactory.components.waveguides.crossing

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.crossing().copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.waveguides.crossing45

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.crossing45(port_spacing=40, alpha=0.08, npoints=101, cross_section='strip', cross_section_bends='strip').copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.waveguides.crossing_etched

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.crossing_etched(width=0.5, r1=3, r2=1.1, w=1.2, L=3.4, layer_wg='WG', layer_slab='SLAB150').copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.waveguides.crossing_linear_taper

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.crossing_linear_taper(width1=2.5, width2=0.5, length=3, cross_section='strip', taper='taper').copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.waveguides.straight

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.straight(length=10, npoints=2, cross_section='strip').copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.waveguides.straight_array

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.straight_array(n=4, spacing=4, length=10, cross_section='strip').copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.waveguides.straight_heater_doped_rib

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.straight_heater_doped_rib(length=320, nsections=3, cross_section='strip_rib_tip', cross_section_heater='rib_heater_doped', via_stack='via_stack_slab_npp_m3', via_stack_metal='via_stack_m1_mtop', via_stack_metal_size=(10, 10), via_stack_size=(10, 10), taper='taper_cross_section', heater_width=2, heater_gap=0.8, via_stack_gap=0, width=0.5, xoffset_tip1=0.2, xoffset_tip2=0.4).copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.waveguides.straight_heater_doped_strip

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.straight_heater_doped_strip(length=320, nsections=3, cross_section='strip_heater_doped', cross_section_heater='rib_heater_doped', via_stack='via_stack_npp_m1', via_stack_metal='via_stack_m1_mtop', via_stack_metal_size=(10, 10), via_stack_size=(10, 10), taper='taper_cross_section', heater_width=2, heater_gap=0.8, via_stack_gap=0, width=0.5, xoffset_tip1=0.2, xoffset_tip2=0.4).copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.waveguides.straight_heater_meander

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.straight_heater_meander(length=300, spacing=2, cross_section='strip', heater_width=2.5, extension_length=15, layer_heater='HEATER', via_stack='via_stack_heater_mtop', heater_taper_length=10, taper_length=10, n=3).copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.waveguides.straight_heater_meander_doped

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.straight_heater_meander_doped(length=300, spacing=2, cross_section='strip', heater_width=1.5, extension_length=15, layers_doping=('P', 'PP', 'PPP'), radius=5, straight_widths=(0.8, 0.9, 0.8), taper_length=10).copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.waveguides.straight_heater_metal

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.straight_heater_metal(length=320, length_undercut_spacing=0, length_undercut=5, length_straight=0.1, length_straight_input=0.1, cross_section='strip', cross_section_heater='heater_metal', cross_section_waveguide_heater='strip_heater_metal', cross_section_heater_undercut='strip_heater_metal_undercut', with_undercut=False, via_stack='via_stack_heater_mtop', heater_taper_length=5).copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.waveguides.straight_heater_metal_90_90

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.straight_heater_metal_90_90(length=320, length_undercut_spacing=0, length_undercut=5, length_straight=0.1, length_straight_input=0.1, cross_section='strip', cross_section_heater='heater_metal', cross_section_waveguide_heater='strip_heater_metal', cross_section_heater_undercut='strip_heater_metal_undercut', with_undercut=False, via_stack='via_stack_heater_mtop', port_orientation1=90, port_orientation2=90, heater_taper_length=5).copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.waveguides.straight_heater_metal_simple

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.straight_heater_metal_simple(length=320, cross_section_heater='heater_metal', cross_section_waveguide_heater='strip_heater_metal', via_stack='via_stack_heater_mtop', heater_taper_length=5).copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.waveguides.straight_heater_metal_undercut

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.straight_heater_metal_undercut(length=320, length_undercut_spacing=6, length_undercut=30, length_straight=0.1, length_straight_input=15, cross_section='strip', cross_section_heater='heater_metal', cross_section_waveguide_heater='strip_heater_metal', cross_section_heater_undercut='strip_heater_metal_undercut', with_undercut=True, via_stack='via_stack_heater_mtop', heater_taper_length=5).copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.waveguides.straight_heater_metal_undercut_90_90

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.straight_heater_metal_undercut_90_90(length=320, length_undercut_spacing=6, length_undercut=30, length_straight=0.1, length_straight_input=15, cross_section='strip', cross_section_heater='heater_metal', cross_section_waveguide_heater='strip_heater_metal', cross_section_heater_undercut='strip_heater_metal_undercut', with_undercut=True, via_stack='via_stack_heater_mtop', port_orientation1=90, port_orientation2=90, heater_taper_length=5).copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.waveguides.straight_piecewise

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.straight_piecewise(port_names=('o1', 'o2'), name='core').copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.waveguides.straight_pin

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.straight_pin(length=500, via_stack='via_stack_slab_m3', via_stack_width=10, via_stack_spacing=2, taper='taper_strip_to_ridge').copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.waveguides.straight_pin_slot

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.straight_pin_slot(length=500, cross_section='pin', via_stack='via_stack_m1_mtop', via_stack_width=10, via_stack_slab='via_stack_slab_m1_horizontal', via_stack_spacing=3, via_stack_slab_spacing=2, taper='taper_strip_to_ridge').copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.waveguides.straight_pn

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.straight_pn(length=2000, cross_section='pn', via_stack='via_stack_slab_m3', via_stack_width=10, via_stack_spacing=2, taper='taper_strip_to_ridge').copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.waveguides.straight_pn_slot

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.straight_pn_slot(length=500, via_stack='via_stack_m1_mtop', via_stack_width=10, via_stack_slab='via_stack_slab_m1_horizontal', via_stack_spacing=3, via_stack_slab_spacing=2, taper='taper_strip_to_ridge').copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.waveguides.wire_corner

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.wire_corner(cross_section='metal_routing', port_names=('e1', 'e2'), port_types=('electrical', 'electrical')).copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.waveguides.wire_corner45

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.wire_corner45(cross_section='metal_routing', radius=10, with_corner90_ports=True).copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.waveguides.wire_corner_sections

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.wire_corner_sections(cross_section='metal_routing').copy()
  c.draw_ports()
  c.plot()




.. autofunction:: gdsfactory.components.waveguides.wire_straight

.. plot::
  :include-source:

  import gdsfactory as gf

  c = gf.components.wire_straight(length=10, npoints=2, cross_section='metal_routing').copy()
  c.draw_ports()
  c.plot()
