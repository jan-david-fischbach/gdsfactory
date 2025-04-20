<a id="gdsfactory"></a>

# gdsfactory

Main module for gdsfactory.

<a id="gdsfactory.clear_cache"></a>

#### clear\_cache

```python
def clear_cache(kcl: kf.KCLayout = kf.kcl) -> None
```

Clears the whole layout object cache for the default layout.

<a id="gdsfactory"></a>

# gdsfactory

Main module for gdsfactory.

<a id="gdsfactory.clear_cache"></a>

#### clear\_cache

```python
def clear_cache(kcl: kf.KCLayout = kf.kcl) -> None
```

Clears the whole layout object cache for the default layout.

<a id="gdsfactory.font"></a>

# gdsfactory.font

Support for font rendering in GDS files.

Adapted from PHIDL https://github.com/amccaugh/phidl/ by Adam McCaughan

<a id="gdsfactory.cross_section"></a>

# gdsfactory.cross\_section

You can define a path as list of points.

To create a component you need to extrude the path with a cross-section.

<a id="gdsfactory.cross_section.Section"></a>

## Section Objects

```python
class Section(BaseModel)
```

CrossSection to extrude a path with a waveguide.

**Arguments**:

- `width` - of the section (um) or parameterized function from 0 to 1.                 the width at t==0 is the width at the beginning of the Path.                 the width at t==1 is the width at the end.
- `offset` - center offset (um) or function parameterized function from 0 to 1.                 the offset at t==0 is the offset at the beginning of the Path.                 the offset at t==1 is the offset at the end.
- `insets` - distance (um) in x to inset section relative to end of the Path                 (i.e. (start inset, stop_inset)).
- `layer` - layer spec. If None does not draw the main section.
- `port_names` - Optional port names.
- `port_types` - optical, electrical, ...
- `name` - Optional Section name.
- `hidden` - hide layer.
- `simplify` - Optional Tolerance value for the simplification algorithm.                 All points that can be removed without changing the resulting.                 polygon by more than the value listed here will be removed.
- `width_function` - parameterized function from 0 to 1.
- `offset_function` - parameterized function from 0 to 1.
  
  .. code::
  
  0
  
  │        ┌───────┐
  │       │
  │        │ layer │
  │◄─────►│
  │        │       │
  │ width │
  │        └───────┘
  |
  │
  |
  ◄────────────►
  +offset

<a id="gdsfactory.cross_section.ComponentAlongPath"></a>

## ComponentAlongPath Objects

```python
class ComponentAlongPath(BaseModel)
```

A ComponentAlongPath object to place along an extruded path.

**Arguments**:

- `component` - to repeat along the path. The unrotated version should be oriented                 for placement on a horizontal line.
- `spacing` - distance between component placements
- `padding` - minimum distance from the path start to the first component.
- `y_offset` - offset in y direction (um).

<a id="gdsfactory.cross_section.CrossSection"></a>

## CrossSection Objects

```python
class CrossSection(BaseModel)
```

Waveguide information to extrude a path.

**Arguments**:

- `sections` - tuple of Sections(width, offset, layer, ports).
- `components_along_path` - tuple of ComponentAlongPaths.
- `radius` - default bend radius for routing (um).
- `radius_min` - minimum acceptable bend radius.
- `bbox_layers` - layer to add as bounding box.
- `bbox_offsets` - offset to add to the bounding box.
  
  .. code::
  
  
  ┌────────────────────────────────────────────────────────────┐
  │                                                            │
  │                                                            │
  │                   boox_layer                               │
  │                                                            │
  │         ┌──────────────────────────────────────┐           │
  │         │                            ▲         │bbox_offset│
  │         │                            │         ├──────────►│
  │         │           cladding_offset  │         │           │
  │         │                            │         │           │
  │         ├─────────────────────────▲──┴─────────┤           │
  │         │                         │            │           │
  ─ ─┤         │           core   width  │            │           ├─ ─ center
  │         │                         │            │           │
  │         ├─────────────────────────▼────────────┤           │
  │         │                                      │           │
  │         │                                      │           │
  │         │                                      │           │
  │         │                                      │           │
  │         └──────────────────────────────────────┘           │
  │                                                            │
  │                                                            │
  │                                                            │
  └────────────────────────────────────────────────────────────┘

<a id="gdsfactory.cross_section.CrossSection.append_sections"></a>

#### append\_sections

```python
def append_sections(sections: Sections) -> Self
```

Append sections to the cross_section.

<a id="gdsfactory.cross_section.CrossSection.__getitem__"></a>

#### \_\_getitem\_\_

```python
def __getitem__(key: str) -> Section
```

Returns the section with the given name.

<a id="gdsfactory.cross_section.CrossSection.hash"></a>

#### hash

```python
@property
def hash() -> str
```

Returns a hash of the cross_section.

<a id="gdsfactory.cross_section.CrossSection.copy"></a>

#### copy

```python
def copy(width: float | None = None,
         layer: typings.LayerSpec | None = None,
         width_function: typings.WidthFunction | None = None,
         offset_function: typings.OffsetFunction | None = None,
         sections: Sections | None = None,
         **kwargs: Any) -> CrossSection
```

Returns copy of the cross_section with new parameters.

**Arguments**:

- `width` - of the section (um). Defaults to current width.
- `layer` - layer spec. Defaults to current layer.
- `width_function` - parameterized function from 0 to 1.
- `offset_function` - parameterized function from 0 to 1.
- `sections` - a tuple of Sections, to replace the original sections
- `kwargs` - additional parameters to update.
  

**Arguments**:

- `sections` - tuple of Sections(width, offset, layer, ports).
- `components_along_path` - tuple of ComponentAlongPaths.
- `radius` - route bend radius (um).
- `bbox_layers` - layer to add as bounding box.
- `bbox_offsets` - offset to add to the bounding box.
- `_name` - name of the cross_section.

<a id="gdsfactory.cross_section.CrossSection.mirror"></a>

#### mirror

```python
def mirror() -> CrossSection
```

Returns a mirrored copy of the cross_section.

<a id="gdsfactory.cross_section.CrossSection.add_bbox"></a>

#### add\_bbox

```python
def add_bbox(component: typings.AnyComponentT,
             top: float | None = None,
             bottom: float | None = None,
             right: float | None = None,
             left: float | None = None) -> typings.AnyComponentT
```

Add bounding box layers to a component.

**Arguments**:

- `component` - to add layers.
- `top` - top padding.
- `bottom` - bottom padding.
- `right` - right padding.
- `left` - left padding.

<a id="gdsfactory.cross_section.CrossSection.get_xmin_xmax"></a>

#### get\_xmin\_xmax

```python
def get_xmin_xmax() -> tuple[float, float]
```

Returns the min and max extent of the cross_section across all sections.

<a id="gdsfactory.cross_section.Transition"></a>

## Transition Objects

```python
class Transition(BaseModel)
```

Waveguide information to extrude a path between two CrossSection.

cladding_layers follow path shape

**Arguments**:

- `cross_section1` - input cross_section.
- `cross_section2` - output cross_section.
- `width_type` - 'sine', 'linear', 'parabolic' or Callable. Sets the type of width                 transition used if widths are different between the two input CrossSections.
- `offset_type` - 'sine', 'linear', 'parabolic' or Callable. Sets the type of offset                 transition used if offsets are different between the two input CrossSections.

<a id="gdsfactory.cross_section.xsection"></a>

#### xsection

```python
def xsection(func: CrossSectionCallable[P]) -> CrossSectionCallable[P]
```

Decorator to register a cross section function.

Ensures that the cross-section name matches the name of the function that generated it when created using default parameters

.. code-block:: python

    @xsection
    def xs_sc(width=TECH.width_sc, radius=TECH.radius_sc):
        return gf.cross_section.cross_section(width=width, radius=radius)

<a id="gdsfactory.cross_section.cross_section"></a>

#### cross\_section

```python
def cross_section(width: float = 0.5,
                  offset: float = 0,
                  layer: typings.LayerSpec = "WG",
                  sections: Sections | None = None,
                  port_names: typings.IOPorts = ("o1", "o2"),
                  port_types: typings.IOPorts = ("optical", "optical"),
                  bbox_layers: typings.LayerSpecs | None = None,
                  bbox_offsets: typings.Floats | None = None,
                  cladding_layers: typings.LayerSpecs | None = None,
                  cladding_offsets: typings.Floats | None = None,
                  cladding_simplify: typings.Floats | None = None,
                  cladding_centers: typings.Floats | None = None,
                  radius: float | None = 10.0,
                  radius_min: float | None = None,
                  main_section_name: str = "_default") -> CrossSection
```

Return CrossSection.

**Arguments**:

- `width` - main Section width (um).
- `offset` - main Section center offset (um).
- `layer` - main section layer.
- `sections` - list of Sections(width, offset, layer, ports).
- `port_names` - for input and output ('o1', 'o2').
- `port_types` - for input and output: electrical, optical, vertical_te ...
- `bbox_layers` - list of layers bounding boxes to extrude.
- `bbox_offsets` - list of offset from bounding box edge.
- `cladding_layers` - list of layers to extrude.
- `cladding_offsets` - list of offset from main Section edge.
- `cladding_simplify` - Optional Tolerance value for the simplification algorithm.                 All points that can be removed without changing the resulting.                 polygon by more than the value listed here will be removed.
- `cladding_centers` - center offset for each cladding layer. Defaults to 0.
- `radius` - routing bend radius (um).
- `radius_min` - min acceptable bend radius.
- `main_section_name` - name of the main section. Defaults to _default
  
  .. plot::
  :include-source:
  
  import gdsfactory as gf
  
  xs = gf.cross_section.cross_section(width=0.5, offset=0, layer='WG')
  p = gf.path.arc(radius=10, angle=45)
  c = p.extrude(xs)
  c.plot()
  
  .. code::
  
  
  ┌────────────────────────────────────────────────────────────┐
  │                                                            │
  │                                                            │
  │                   boox_layer                               │
  │                                                            │
  │         ┌──────────────────────────────────────┐           │
  │         │                            ▲         │bbox_offset│
  │         │                            │         ├──────────►│
  │         │           cladding_offset  │         │           │
  │         │                            │         │           │
  │         ├─────────────────────────▲──┴─────────┤           │
  │         │                         │            │           │
  ─ ─┤         │           core   width  │            │           ├─ ─ center
  │         │                         │            │           │
  │         ├─────────────────────────▼────────────┤           │
  │         │                                      │           │
  │         │                                      │           │
  │         │                                      │           │
  │         │                                      │           │
  │         └──────────────────────────────────────┘           │
  │                                                            │
  │                                                            │
  │                                                            │
  └────────────────────────────────────────────────────────────┘

<a id="gdsfactory.cross_section.strip"></a>

#### strip

```python
@xsection
def strip(width: float = 0.5,
          layer: typings.LayerSpec = "WG",
          radius: float = 10.0,
          radius_min: float = 5,
          **kwargs: Any) -> CrossSection
```

Return Strip cross_section.

<a id="gdsfactory.cross_section.strip_no_ports"></a>

#### strip\_no\_ports

```python
@xsection
def strip_no_ports(width: float = 0.5,
                   layer: typings.LayerSpec = "WG",
                   radius: float = 10.0,
                   radius_min: float = 5,
                   port_names: typings.IOPorts = ("", ""),
                   **kwargs: Any) -> CrossSection
```

Return Strip cross_section.

<a id="gdsfactory.cross_section.rib"></a>

#### rib

```python
@xsection
def rib(width: float = 0.5,
        layer: typings.LayerSpec = "WG",
        radius: float = radius_rib,
        radius_min: float | None = None,
        cladding_layers: typings.LayerSpecs = ("SLAB90", ),
        cladding_offsets: typings.Floats = (3, ),
        cladding_simplify: typings.Floats = (50 * nm, ),
        **kwargs: Any) -> CrossSection
```

Return Rib cross_section.

<a id="gdsfactory.cross_section.rib_bbox"></a>

#### rib\_bbox

```python
@xsection
def rib_bbox(width: float = 0.5,
             layer: typings.LayerSpec = "WG",
             radius: float = radius_rib,
             radius_min: float | None = None,
             bbox_layers: typings.LayerSpecs = ("SLAB90", ),
             bbox_offsets: typings.Floats = (3, ),
             **kwargs: Any) -> CrossSection
```

Return Rib cross_section.

<a id="gdsfactory.cross_section.rib2"></a>

#### rib2

```python
@xsection
def rib2(width: float = 0.5,
         layer: typings.LayerSpec = "WG",
         layer_slab: typings.LayerSpec = "SLAB90",
         radius: float = radius_rib,
         radius_min: float | None = None,
         width_slab: float = 6,
         **kwargs: Any) -> CrossSection
```

Return Rib cross_section.

<a id="gdsfactory.cross_section.nitride"></a>

#### nitride

```python
@xsection
def nitride(width: float = 1.0,
            layer: typings.LayerSpec = "WGN",
            radius: float = radius_nitride,
            radius_min: float | None = None,
            **kwargs: Any) -> CrossSection
```

Return Strip cross_section.

<a id="gdsfactory.cross_section.strip_rib_tip"></a>

#### strip\_rib\_tip

```python
@xsection
def strip_rib_tip(width: float = 0.5,
                  width_tip: float = 0.2,
                  layer: typings.LayerSpec = "WG",
                  layer_slab: typings.LayerSpec = "SLAB90",
                  radius: float = 10.0,
                  radius_min: float | None = 5,
                  **kwargs: Any) -> CrossSection
```

Return Strip cross_section.

<a id="gdsfactory.cross_section.strip_nitride_tip"></a>

#### strip\_nitride\_tip

```python
@xsection
def strip_nitride_tip(width: float = 1.0,
                      layer: typings.LayerSpec = "WGN",
                      layer_silicon: typings.LayerSpec = "WG",
                      width_tip_nitride: float = 0.2,
                      width_tip_silicon: float = 0.1,
                      radius: float = radius_nitride,
                      radius_min: float | None = None,
                      **kwargs: Any) -> CrossSection
```

Return Strip cross_section.

<a id="gdsfactory.cross_section.slot"></a>

#### slot

```python
@xsection
def slot(width: float = 0.5,
         layer: typings.LayerSpec = "WG",
         slot_width: float = 0.04,
         sections: Sections | None = None) -> CrossSection
```

Return CrossSection Slot (with an etched region in the center).

**Arguments**:

- `width` - main Section width (um) or function parameterized from 0 to 1.                 the width at t==0 is the width at the beginning of the Path.                 the width at t==1 is the width at the end.
- `layer` - main section layer.
- `slot_width` - in um.
- `sections` - list of Sections(width, offset, layer, ports).
  
  .. plot::
  :include-source:
  
  import gdsfactory as gf
  
  xs = gf.cross_section.slot(width=0.5, slot_width=0.05, layer='WG')
  p = gf.path.arc(radius=10, angle=45)
  c = p.extrude(xs)
  c.plot()

<a id="gdsfactory.cross_section.rib_with_trenches"></a>

#### rib\_with\_trenches

```python
@xsection
def rib_with_trenches(width: float = 0.5,
                      width_trench: float = 2.0,
                      slab_offset: float | None = 0.3,
                      width_slab: float | None = None,
                      simplify_slab: float | None = None,
                      layer: typings.LayerSpec = "WG",
                      layer_trench: typings.LayerSpec = "DEEP_ETCH",
                      wg_marking_layer: typings.LayerSpec = "WG_ABSTRACT",
                      sections: Sections | None = None,
                      **kwargs: Any) -> CrossSection
```

Return CrossSection of rib waveguide defined by trenches.

**Arguments**:

- `width` - main Section width (um) or function parameterized from 0 to 1.                 the width at t==0 is the width at the beginning of the Path.                 the width at t==1 is the width at the end.
- `width_trench` - in um.
- `slab_offset` - from the edge of the trench to the edge of the slab.
- `width_slab` - in um.
- `simplify_slab` - Optional Tolerance value for the simplification algorithm.                 All points that can be removed without changing the resulting                polygon by more than the value listed here will be removed.
- `layer` - slab layer.
- `layer_trench` - layer to etch trenches.
- `wg_marking_layer` - layer to draw over the actual waveguide.                 This can be useful for booleans, routing, placement ...
- `sections` - list of Sections(width, offset, layer, ports).
- `kwargs` - cross_section settings.
  
  .. code::
  
  ┌─────────┐
  │         │ wg_marking_layer
  └─────────┘
  
  ┌────────┐         ┌────────┐
  │        │         │        │layer_trench
  └────────┘         └────────┘
  
  ┌─────────────────────────────────────────┐
  │                                  layer  │
  │                                         │
  └─────────────────────────────────────────┘
  ◄─────────►
  width
  ┌─────┐         ┌────────┐        ┌───────┐
  │     │         │        │        │       │
  │     └─────────┘        └────────┘       │
  │     ◄---------►         ◄-------►       │
  └─────────────────────────────────────────┘
  slab_offset
  width_trench                  ──────►
  |
  ◄────────────────────────────────────────►
  width_slab
  
  
  .. plot::
  :include-source:
  
  import gdsfactory as gf
  
  xs = gf.cross_section.rib_with_trenches(width=0.5)
  p = gf.path.arc(radius=10, angle=45)
  c = p.extrude(xs)
  c.plot()

<a id="gdsfactory.cross_section.l_with_trenches"></a>

#### l\_with\_trenches

```python
@xsection
def l_with_trenches(width: float = 0.5,
                    width_trench: float = 2.0,
                    width_slab: float = 7.0,
                    layer: typings.LayerSpec = "WG",
                    layer_slab: typings.LayerSpec = "WG",
                    layer_trench: typings.LayerSpec = "DEEP_ETCH",
                    mirror: bool = False,
                    sections: Sections | None = None,
                    **kwargs: Any) -> CrossSection
```

Return CrossSection of l waveguide defined by trenches.

**Arguments**:

- `width` - main Section width (um) or function parameterized from 0 to 1.                 the width at t==0 is the width at the beginning of the Path.                 the width at t==1 is the width at the end.
- `width_trench` - in um.
- `width_slab` - in um.
- `layer` - ridge layer. None adds only ridge.
- `layer_slab` - slab layer.
- `layer_trench` - layer to etch trenches.
- `mirror` - this cross section is not symmetric and you can switch orientation.
- `sections` - list of Sections(width, offset, layer, ports).
- `kwargs` - cross_section settings.
  
  
  .. code::
  x = 0
  |
  |
  _____         __________
  |        |         |
  |________|         |
  
  _________________________
  <------->          |
  width_trench
  <-------->
  width
  |
  <------------------------>
  width_slab
  
  
  
  .. plot::
  :include-source:
  
  import gdsfactory as gf
  
  xs = gf.cross_section.l_with_trenches(width=0.5)
  p = gf.path.arc(radius=10, angle=45)
  c = p.extrude(xs)
  c.plot()

<a id="gdsfactory.cross_section.metal1"></a>

#### metal1

```python
@xsection
def metal1(width: float = 10,
           layer: typings.LayerSpec = "M1",
           radius: float | None = None,
           port_names: typings.IOPorts = port_names_electrical,
           port_types: typings.IOPorts = port_types_electrical,
           **kwargs: Any) -> CrossSection
```

Return Metal Strip cross_section.

<a id="gdsfactory.cross_section.metal2"></a>

#### metal2

```python
@xsection
def metal2(width: float = 10,
           layer: typings.LayerSpec = "M2",
           radius: float | None = None,
           port_names: typings.IOPorts = port_names_electrical,
           port_types: typings.IOPorts = port_types_electrical,
           **kwargs: Any) -> CrossSection
```

Return Metal Strip cross_section.

<a id="gdsfactory.cross_section.metal3"></a>

#### metal3

```python
@xsection
def metal3(width: float = 10,
           layer: typings.LayerSpec = "M3",
           radius: float | None = None,
           port_names: typings.IOPorts = port_names_electrical,
           port_types: typings.IOPorts = port_types_electrical,
           **kwargs: Any) -> CrossSection
```

Return Metal Strip cross_section.

<a id="gdsfactory.cross_section.metal_routing"></a>

#### metal\_routing

```python
@xsection
def metal_routing(width: float = 10,
                  layer: typings.LayerSpec = "M3",
                  radius: float | None = None,
                  port_names: typings.IOPorts = port_names_electrical,
                  port_types: typings.IOPorts = port_types_electrical,
                  **kwargs: Any) -> CrossSection
```

Return Metal Strip cross_section.

<a id="gdsfactory.cross_section.heater_metal"></a>

#### heater\_metal

```python
@xsection
def heater_metal(width: float = 2.5,
                 layer: typings.LayerSpec = "HEATER",
                 radius: float | None = None,
                 port_names: typings.IOPorts = port_names_electrical,
                 port_types: typings.IOPorts = port_types_electrical,
                 **kwargs: Any) -> CrossSection
```

Return Metal Strip cross_section.

<a id="gdsfactory.cross_section.npp"></a>

#### npp

```python
@xsection
def npp(width: float = 0.5,
        layer: typings.LayerSpec = "NPP",
        radius: float | None = None,
        port_names: typings.IOPorts = port_names_electrical,
        port_types: typings.IOPorts = port_types_electrical,
        **kwargs: Any) -> CrossSection
```

Return Doped NPP cross_section.

<a id="gdsfactory.cross_section.pin"></a>

#### pin

```python
@xsection
def pin(width: float = 0.5,
        layer: typings.LayerSpec = "WG",
        layer_slab: typings.LayerSpec = "SLAB90",
        layers_via_stack1: typings.LayerSpecs = ("PPP", ),
        layers_via_stack2: typings.LayerSpecs = ("NPP", ),
        bbox_offsets_via_stack1: tuple[float, ...] = (0, -0.2),
        bbox_offsets_via_stack2: tuple[float, ...] = (0, -0.2),
        via_stack_width: float = 9.0,
        via_stack_gap: float = 0.55,
        slab_gap: float = -0.2,
        layer_via: typings.LayerSpec | None = None,
        via_width: float = 1,
        via_offsets: tuple[float, ...] | None = None,
        sections: Sections | None = None,
        **kwargs: Any) -> CrossSection
```

Rib PIN doped cross_section.

**Arguments**:

- `width` - ridge width.
- `layer` - ridge layer.
- `layer_slab` - slab layer.
- `layers_via_stack1` - list of bot layer.
- `layers_via_stack2` - list of top layer.
- `bbox_offsets_via_stack1` - for bot.
- `bbox_offsets_via_stack2` - for top.
- `via_stack_width` - in um.
- `via_stack_gap` - offset from via_stack to ridge edge.
- `slab_gap` - extra slab gap (negative: via_stack goes beyond slab).
- `layer_via` - for via.
- `via_width` - in um.
- `via_offsets` - in um.
- `sections` - cross_section sections.
- `kwargs` - cross_section settings.
  
  
  https://doi.org/10.1364/OE.26.029983
  
  .. code::
  
  layer
  |<----width--->|
  _______________ via_stack_gap           slab_gap
  |              |<----------->|             <-->
  ___ ____________________|              |__________________________|___
  |   |         |                                       |            |   |
  |   |    P++  |         undoped silicon               |     N++    |   |
  |___|_________|_______________________________________|____________|___|
  <----------->
  via_stack_width
  <---------------------------------------------------------------------->
  slab_width
  
  .. plot::
  :include-source:
  
  import gdsfactory as gf
  
  xs = gf.cross_section.pin(width=0.5, via_stack_gap=1, via_stack_width=1)
  p = gf.path.arc(radius=10, angle=45)
  c = p.extrude(xs)
  c.plot()

<a id="gdsfactory.cross_section.pn"></a>

#### pn

```python
@xsection
def pn(width: float = 0.5,
       layer: typings.LayerSpec = "WG",
       layer_slab: typings.LayerSpec = "SLAB90",
       gap_low_doping: float = 0.0,
       gap_medium_doping: float = 0.5,
       gap_high_doping: float = 1.0,
       offset_low_doping: float = 0.0,
       width_doping: float = 8.0,
       width_slab: float = 7.0,
       layer_p: typings.LayerSpec | None = "P",
       layer_pp: typings.LayerSpec | None = "PP",
       layer_ppp: typings.LayerSpec | None = "PPP",
       layer_n: typings.LayerSpec | None = "N",
       layer_np: typings.LayerSpec | None = "NP",
       layer_npp: typings.LayerSpec | None = "NPP",
       layer_via: typings.LayerSpec | None = None,
       width_via: float = 1.0,
       layer_metal: typings.LayerSpec | None = None,
       width_metal: float = 1.0,
       port_names: tuple[str, str] = ("o1", "o2"),
       sections: Sections | None = None,
       cladding_layers: typings.LayerSpecs | None = None,
       cladding_offsets: typings.Floats | None = None,
       cladding_simplify: typings.Floats | None = None,
       slab_inset: float | None = None,
       **kwargs: Any) -> CrossSection
```

Rib PN doped cross_section.

**Arguments**:

- `width` - width of the ridge in um.
- `layer` - ridge layer.
- `layer_slab` - slab layer.
- `gap_low_doping` - from waveguide center to low doping. Only used for PIN.
- `gap_medium_doping` - from waveguide center to medium doping. None removes it.
- `gap_high_doping` - from center to high doping. None removes it.
- `offset_low_doping` - from center to junction center.
- `width_doping` - in um.
- `width_slab` - in um.
- `layer_p` - p doping layer.
- `layer_pp` - p+ doping layer.
- `layer_ppp` - p++ doping layer.
- `layer_n` - n doping layer.
- `layer_np` - n+ doping layer.
- `layer_npp` - n++ doping layer.
- `layer_via` - via layer.
- `width_via` - via width in um.
- `layer_metal` - metal layer.
- `width_metal` - metal width in um.
- `port_names` - input and output port names.
- `sections` - optional list of sections.
- `cladding_layers` - optional list of cladding layers.
- `cladding_offsets` - optional list of cladding offsets.
- `cladding_simplify` - Optional Tolerance value for the simplification algorithm.                 All points that can be removed without changing the resulting                polygon by more than the value listed here will be removed.
- `slab_inset` - slab inset in um.
- `kwargs` - cross_section settings.
  
  .. code::
  
  offset_low_doping
  <------>
  |       |
  wg     junction
  center   center
  |       |
  ______________|_______|______
  |             |       |     |
  _________|             |       |     |_________________|
  P                |       |               N       |
  width_p              |       |            width_n    |
  <----------------------------->|<--------------------->|
  |               |       N+      |
  |               |    width_n    |
  |               |<------------->|
  |<------------->|
  gap_medium_doping
  
  .. plot::
  :include-source:
  
  import gdsfactory as gf
  
  xs = gf.cross_section.pn(width=0.5, gap_low_doping=0, width_doping=2.)
  p = gf.path.arc(radius=10, angle=45)
  c = p.extrude(xs)
  c.plot()

<a id="gdsfactory.cross_section.pn_with_trenches"></a>

#### pn\_with\_trenches

```python
@xsection
def pn_with_trenches(width: float = 0.5,
                     layer: typings.LayerSpec = "WG",
                     layer_trench: typings.LayerSpec = "DEEP_ETCH",
                     gap_low_doping: float = 0.0,
                     gap_medium_doping: float | None = 0.5,
                     gap_high_doping: float | None = 1.0,
                     offset_low_doping: float = 0.0,
                     width_doping: float = 8.0,
                     slab_offset: float | None = 0.3,
                     width_slab: float | None = None,
                     width_trench: float = 2.0,
                     layer_p: typings.LayerSpec | None = "P",
                     layer_pp: typings.LayerSpec | None = "PP",
                     layer_ppp: typings.LayerSpec | None = "PPP",
                     layer_n: typings.LayerSpec | None = "N",
                     layer_np: typings.LayerSpec | None = "NP",
                     layer_npp: typings.LayerSpec | None = "NPP",
                     layer_via: typings.LayerSpec | None = None,
                     width_via: float = 1.0,
                     layer_metal: typings.LayerSpec | None = None,
                     width_metal: float = 1.0,
                     port_names: typings.IOPorts = ("o1", "o2"),
                     cladding_layers: typings.Layers
                     | None = cladding_layers_optical,
                     cladding_offsets: typings.Floats
                     | None = cladding_offsets_optical,
                     cladding_simplify: typings.Floats
                     | None = cladding_simplify_optical,
                     wg_marking_layer: typings.LayerSpec | None = None,
                     sections: Sections | None = None,
                     **kwargs: Any) -> CrossSection
```

Rib PN doped cross_section.

**Arguments**:

- `width` - width of the ridge in um.
- `layer` - ridge layer. None adds only ridge.
- `layer_trench` - layer to etch trenches.
- `gap_low_doping` - from waveguide center to low doping. Only used for PIN.
- `gap_medium_doping` - from waveguide center to medium doping. None removes it.
- `gap_high_doping` - from center to high doping. None removes it.
- `offset_low_doping` - from center to junction center.
- `width_doping` - in um.
- `slab_offset` - from the edge of the trench to the edge of the slab.
- `width_slab` - in um.
- `width_trench` - in um.
- `layer_p` - p doping layer.
- `layer_pp` - p+ doping layer.
- `layer_ppp` - p++ doping layer.
- `layer_n` - n doping layer.
- `layer_np` - n+ doping layer.
- `layer_npp` - n++ doping layer.
- `layer_via` - via layer.
- `width_via` - via width in um.
- `layer_metal` - metal layer.
- `width_metal` - metal width in um.
- `port_names` - input and output port names.
- `cladding_layers` - optional list of cladding layers.
- `cladding_offsets` - optional list of cladding offsets.
- `cladding_simplify` - Optional Tolerance value for the simplification algorithm.                All points that can be removed without changing the resulting.                 polygon by more than the value listed here will be removed.
- `wg_marking_layer` - layer to draw over the actual waveguide.
- `sections` - optional list of sections.
- `kwargs` - cross_section settings.
  
  .. code::
  
  offset_low_doping
  <------>
  |       |
  wg     junction
  center   center             slab_offset
  |       |               <------>
  _____         ______________|_______ ______         ________
  |        |             |       |     |         |       |
  |________|             |             |_________|       |
  P                |       |               N       |
  width_p              |                    width_n    |
  <-------------------------------->|<--------------------->|
  <------->              |               |       N+      |
  width_trench            |               |    width_n    |
  |               |<------------->|
  |<------------->|
  gap_medium_doping
  <------------------------------------------------------------>
  width_slab
  
  .. plot::
  :include-source:
  
  import gdsfactory as gf
  
  xs = gf.cross_section.pn_with_trenches(width=0.5, gap_low_doping=0, width_doping=2.)
  p = gf.path.arc(radius=10, angle=45)
  c = p.extrude(xs)
  c.plot()

<a id="gdsfactory.cross_section.pn_with_trenches_asymmetric"></a>

#### pn\_with\_trenches\_asymmetric

```python
@xsection
def pn_with_trenches_asymmetric(width: float = 0.5,
                                layer: typings.LayerSpec = "WG",
                                layer_trench: typings.LayerSpec = "DEEP_ETCH",
                                gap_low_doping: float
                                | tuple[float, float] = (0.0, 0.0),
                                gap_medium_doping: float | tuple[float, float]
                                | None = (0.5, 0.2),
                                gap_high_doping: float | tuple[float, float]
                                | None = (1.0, 0.8),
                                width_doping: float = 8.0,
                                slab_offset: float | None = 0.3,
                                width_slab: float | None = None,
                                width_trench: float = 2.0,
                                layer_p: typings.LayerSpec | None = "P",
                                layer_pp: typings.LayerSpec | None = "PP",
                                layer_ppp: typings.LayerSpec | None = "PPP",
                                layer_n: typings.LayerSpec | None = "N",
                                layer_np: typings.LayerSpec | None = "NP",
                                layer_npp: typings.LayerSpec | None = "NPP",
                                layer_via: typings.LayerSpec | None = None,
                                width_via: float = 1.0,
                                layer_metal: typings.LayerSpec | None = None,
                                width_metal: float = 1.0,
                                port_names: tuple[str, str] = ("o1", "o2"),
                                cladding_layers: typings.Layers
                                | None = cladding_layers_optical,
                                cladding_offsets: typings.Floats
                                | None = cladding_offsets_optical,
                                wg_marking_layer: typings.LayerSpec
                                | None = None,
                                sections: Sections | None = None,
                                **kwargs: Any) -> CrossSection
```

Rib PN doped cross_section with asymmetric dimensions left and right.

**Arguments**:

- `width` - width of the ridge in um.
- `layer` - ridge layer. None adds only ridge.
- `layer_trench` - layer to etch trenches.
- `gap_low_doping` - from waveguide center to low doping. Only used for PIN.                 If a list, it considers the first element is [p_side, n_side]. If a number,                 it assumes the same for both sides.
- `gap_medium_doping` - from waveguide center to medium doping. None removes it.                 If a list, it considers the first element is [p_side, n_side].                 If a number, it assumes the same for both sides.
- `gap_high_doping` - from center to high doping. None removes it.                 If a list, it considers the first element is [p_side, n_side].                If a number, it assumes the same for both sides.
- `width_doping` - in um.
- `slab_offset` - from the edge of the trench to the edge of the slab.
- `width_slab` - in um.
- `width_trench` - in um.
- `layer_p` - p doping layer.
- `layer_pp` - p+ doping layer.
- `layer_ppp` - p++ doping layer.
- `layer_n` - n doping layer.
- `layer_np` - n+ doping layer.
- `layer_npp` - n++ doping layer.
- `layer_via` - via layer.
- `width_via` - via width in um.
- `layer_metal` - metal layer.
- `width_metal` - metal width in um.
- `port_names` - input and output port names.
- `cladding_layers` - optional list of cladding layers.
- `cladding_offsets` - optional list of cladding offsets.
- `wg_marking_layer` - layer to draw over the actual waveguide.
- `sections` - optional list of sections.
- `kwargs` - cross_section settings.
  
  .. code::
  
  gap_low_doping[1]
  <------>
  |       |
  wg     junction
  center   center           slab_offset
  |       |               <------>
  _____         ______________|_______ ______         ________
  |        |             |       |     |         |       |
  |________|             |             |_________|       |
  P                |       |               N       |
  width_p              |                    width_n    |
  <-------------------------------->|<--------------------->|
  <------->              |               |       N+      |
  width_trench            |               |    width_n    |
  |               |<------------->|
  |<------------->|
  gap_medium_doping[1]
  <------------------------------------------------------------>
  width_slab
  
  .. plot::
  :include-source:
  
  import gdsfactory as gf
  
  xs = gf.cross_section.pn_with_trenches_assymmetric(width=0.5, gap_low_doping=0, width_doping=2.)
  p = gf.path.arc(radius=10, angle=45)
  c = p.extrude(xs)
  c.plot()

<a id="gdsfactory.cross_section.l_wg_doped_with_trenches"></a>

#### l\_wg\_doped\_with\_trenches

```python
@xsection
def l_wg_doped_with_trenches(width: float = 0.5,
                             layer: typings.LayerSpec = "WG",
                             layer_trench: typings.LayerSpec = "DEEP_ETCH",
                             gap_low_doping: float = 0.0,
                             gap_medium_doping: float | None = 0.5,
                             gap_high_doping: float | None = 1.0,
                             width_doping: float = 8.0,
                             slab_offset: float | None = 0.3,
                             width_slab: float | None = None,
                             width_trench: float = 2.0,
                             layer_low: typings.LayerSpec = "P",
                             layer_mid: typings.LayerSpec = "PP",
                             layer_high: typings.LayerSpec = "PPP",
                             layer_via: typings.LayerSpec | None = None,
                             width_via: float = 1.0,
                             layer_metal: typings.LayerSpec | None = None,
                             width_metal: float = 1.0,
                             port_names: tuple[str, str] = ("o1", "o2"),
                             cladding_layers: typings.Layers
                             | None = cladding_layers_optical,
                             cladding_offsets: typings.Floats
                             | None = cladding_offsets_optical,
                             wg_marking_layer: typings.LayerSpec | None = None,
                             sections: Sections | None = None,
                             **kwargs: Any) -> CrossSection
```

L waveguide PN doped cross_section.

**Arguments**:

- `width` - width of the ridge in um.
- `layer` - ridge layer. None adds only ridge.
- `layer_trench` - layer to etch trenches.
- `gap_low_doping` - from waveguide outer edge to low doping. Only used for PIN.
- `gap_medium_doping` - from waveguide edge to medium doping. None removes it.
- `gap_high_doping` - from edge to high doping. None removes it.
- `width_doping` - in um.
- `slab_offset` - from the edge of the trench to the edge of the slab.
- `width_slab` - in um.
- `width_trench` - in um.
- `layer_low` - low doping layer.
- `layer_mid` - mid doping layer.
- `layer_high` - high doping layer.
- `layer_via` - via layer.
- `width_via` - via width in um.
- `layer_metal` - metal layer.
- `width_metal` - metal width in um.
- `port_names` - input and output port names.
- `cladding_layers` - optional list of cladding layers.
- `cladding_offsets` - optional list of cladding offsets.
- `wg_marking_layer` - layer to mark where the actual guiding section is.
- `sections` - optional list of sections.
- `kwargs` - cross_section settings.
  
  .. code::
  
  gap_low_doping
  <------>
  |
  wg
  edge
  |
  _____                       _______ ______
  |                     |              |
  |_____________________|              |
  |
  |
  <------------>
  width
  <--------------------->               |
  width_trench       |                   |
  |                   |
  |<----------------->|
  gap_medium_doping
  |<--------------------------->|
  gap_high_doping
  <------------------------------------------->
  width_slab
  
  .. plot::
  :include-source:
  
  import gdsfactory as gf
  
  xs = gf.cross_section.pn_with_trenches(width=0.5, gap_low_doping=0, width_doping=2.)
  p = gf.path.arc(radius=10, angle=45)
  c = p.extrude(xs)
  c.plot()

<a id="gdsfactory.cross_section.strip_heater_metal_undercut"></a>

#### strip\_heater\_metal\_undercut

```python
@xsection
def strip_heater_metal_undercut(width: float = 0.5,
                                layer: typings.LayerSpec = "WG",
                                heater_width: float = 2.5,
                                trench_width: float = 6.5,
                                trench_gap: float = 2.0,
                                layer_heater: typings.LayerSpec = "HEATER",
                                layer_trench: typings.LayerSpec = "DEEPTRENCH",
                                sections: Sections | None = None,
                                **kwargs: Any) -> CrossSection
```

Returns strip cross_section with top metal and undercut trenches on both.

sides.

dimensions from https://doi.org/10.1364/OE.18.020298

**Arguments**:

- `width` - waveguide width.
- `layer` - waveguide layer.
- `heater_width` - of metal heater.
- `trench_width` - in um.
- `trench_gap` - from waveguide edge to trench edge.
- `layer_heater` - heater layer.
- `layer_trench` - tench layer.
- `sections` - cross_section sections.
- `kwargs` - cross_section settings.
  
  .. code::
  
  |<-------heater_width--------->|
  ______________________________
  |                              |
  |         layer_heater         |
  |______________________________|
  
  |<------width------>|
  ____________________ trench_gap
  |                   |<----------->|              |
  |                   |             |   undercut   |
  |       width       |             |              |
  |                   |             |<------------>|
  |___________________|             | trench_width |
  |              |
  |              |
  
  .. plot::
  :include-source:
  
  import gdsfactory as gf
  
  xs = gf.cross_section.strip_heater_metal_undercut(width=0.5, heater_width=2, trench_width=4, trench_gap=4)
  p = gf.path.arc(radius=10, angle=45)
  c = p.extrude(xs)
  c.plot()

<a id="gdsfactory.cross_section.strip_heater_metal"></a>

#### strip\_heater\_metal

```python
@xsection
def strip_heater_metal(width: float = 0.5,
                       layer: typings.LayerSpec = "WG",
                       heater_width: float = 2.5,
                       layer_heater: typings.LayerSpec = "HEATER",
                       sections: Sections | None = None,
                       insets: tuple[float, float] | None = None,
                       **kwargs: Any) -> CrossSection
```

Returns strip cross_section with top heater metal.

dimensions from https://doi.org/10.1364/OE.18.020298

**Arguments**:

- `width` - waveguide width (um).
- `layer` - waveguide layer.
- `heater_width` - of metal heater.
- `layer_heater` - for the metal.
- `sections` - cross_section sections.
- `insets` - for the heater.
- `kwargs` - cross_section settings.
  
  .. plot::
  :include-source:
  
  import gdsfactory as gf
  
  xs = gf.cross_section.strip_heater_metal(width=0.5, heater_width=2)
  p = gf.path.arc(radius=10, angle=45)
  c = p.extrude(xs)
  c.plot()

<a id="gdsfactory.cross_section.strip_heater_doped"></a>

#### strip\_heater\_doped

```python
@xsection
def strip_heater_doped(width: float = 0.5,
                       layer: typings.LayerSpec = "WG",
                       heater_width: float = 2.0,
                       heater_gap: float = 0.8,
                       layers_heater: typings.LayerSpecs = ("WG", "NPP"),
                       bbox_offsets_heater: tuple[float, ...] = (0, 0.1),
                       sections: Sections | None = None,
                       **kwargs: Any) -> CrossSection
```

Returns strip cross_section with N++ doped heaters on both sides.

**Arguments**:

- `width` - in um.
- `layer` - waveguide spec.
- `heater_width` - in um.
- `heater_gap` - in um.
- `layers_heater` - for doped heater.
- `bbox_offsets_heater` - for each layers_heater.
- `sections` - cross_section sections.
- `kwargs` - cross_section settings.
  
  .. code::
  
  |<------width------>|
  ____________             ___________________               ______________
  |            |           |     undoped Si    |             |              |
  |layer_heater|           |  intrinsic region |<----------->| layer_heater |
  |____________|           |___________________|             |______________|
  <------------>
  heater_gap     heater_width
  
  .. plot::
  :include-source:
  
  import gdsfactory as gf
  
  xs = gf.cross_section.strip_heater_doped(width=0.5, heater_width=2, heater_gap=0.5)
  p = gf.path.arc(radius=10, angle=45)
  c = p.extrude(xs)
  c.plot()

<a id="gdsfactory.cross_section.rib_heater_doped"></a>

#### rib\_heater\_doped

```python
@xsection
def rib_heater_doped(width: float = 0.5,
                     layer: typings.LayerSpec = "WG",
                     heater_width: float = 2.0,
                     heater_gap: float = 0.8,
                     layer_heater: typings.LayerSpec = "NPP",
                     layer_slab: typings.LayerSpec = "SLAB90",
                     slab_gap: float = 0.2,
                     with_top_heater: bool = True,
                     with_bot_heater: bool = True,
                     sections: Sections | None = None,
                     **kwargs: Any) -> CrossSection
```

Returns rib cross_section with N++ doped heaters on both sides.

dimensions from https://doi.org/10.1364/OE.27.010456

.. code::

                                |<------width------>|
                                 ____________________  heater_gap           slab_gap
                                |                   |<----------->|             <-->
     ___ _______________________|                   |__________________________|___
    |   |            |                undoped Si                  |            |   |
    |   |layer_heater|                intrinsic region            |layer_heater|   |
    |___|____________|____________________________________________|____________|___|
                                                                   <---------->
                                                                    heater_width
    <------------------------------------------------------------------------------>
                                    slab_width

.. plot::
    :include-source:

    import gdsfactory as gf

    xs = gf.cross_section.rib_heater_doped(width=0.5, heater_width=2, heater_gap=0.5, layer_heater='NPP')
    p = gf.path.arc(radius=10, angle=45)
    c = p.extrude(xs)
    c.plot()

<a id="gdsfactory.cross_section.rib_heater_doped_via_stack"></a>

#### rib\_heater\_doped\_via\_stack

```python
@xsection
def rib_heater_doped_via_stack(width: float = 0.5,
                               layer: typings.LayerSpec = "WG",
                               heater_width: float = 1.0,
                               heater_gap: float = 0.8,
                               layer_slab: typings.LayerSpec = "SLAB90",
                               layer_heater: typings.LayerSpec = "NPP",
                               via_stack_width: float = 2.0,
                               via_stack_gap: float = 0.8,
                               layers_via_stack: typings.LayerSpecs = ("NPP",
                                                                       "VIAC"),
                               bbox_offsets_via_stack: tuple[float,
                                                             ...] = (0, -0.2),
                               slab_gap: float = 0.2,
                               slab_offset: float = 0,
                               with_top_heater: bool = True,
                               with_bot_heater: bool = True,
                               sections: Sections | None = None,
                               **kwargs: Any) -> CrossSection
```

Returns rib cross_section with N++ doped heaters on both sides.

dimensions from https://doi.org/10.1364/OE.27.010456

**Arguments**:

- `width` - in um.
- `layer` - for main waveguide section.
- `heater_width` - in um.
- `heater_gap` - in um.
- `layer_slab` - for pedestal.
- `layer_heater` - for doped heater.
- `via_stack_width` - for the contact.
- `via_stack_gap` - in um.
- `layers_via_stack` - for the contact.
- `bbox_offsets_via_stack` - for the contact.
- `slab_gap` - from heater edge.
- `slab_offset` - over the center of the slab.
- `with_top_heater` - adds top/left heater.
- `with_bot_heater` - adds bottom/right heater.
- `sections` - list of sections to add to the cross_section.
- `kwargs` - cross_section settings.
  
  .. code::
  
  |<----width------>|
  slab_gap                     __________________ via_stack_gap     via_stack width
  <-->                        |                 |<------------>|<--------------->
  |                 | heater_gap |
  |                 |<---------->|
  ___ _______________________|                 |___________________________ ____
  |   |            |              undoped Si                 |              |    |
  |   |layer_heater|              intrinsic region           |layer_heater  |    |
  |___|____________|_________________________________________|______________|____|
  <------------>
  heater_width
  <------------------------------------------------------------------------------>
  slab_width
  
  .. plot::
  :include-source:
  
  import gdsfactory as gf
  
  xs = gf.cross_section.rib_heater_doped_via_stack(width=0.5, heater_width=2, heater_gap=0.5, layer_heater='NPP')
  p = gf.path.arc(radius=10, angle=45)
  c = p.extrude(xs)
  c.plot()

<a id="gdsfactory.cross_section.pn_ge_detector_si_contacts"></a>

#### pn\_ge\_detector\_si\_contacts

```python
@xsection
def pn_ge_detector_si_contacts(width_si: float = 6.0,
                               layer_si: typings.LayerSpec = "WG",
                               width_ge: float = 3.0,
                               layer_ge: typings.LayerSpec = "GE",
                               gap_low_doping: float = 0.6,
                               gap_medium_doping: float = 0.9,
                               gap_high_doping: float = 1.1,
                               width_doping: float = 8.0,
                               layer_p: typings.LayerSpec = "P",
                               layer_pp: typings.LayerSpec = "PP",
                               layer_ppp: typings.LayerSpec = "PPP",
                               layer_n: typings.LayerSpec = "N",
                               layer_np: typings.LayerSpec = "NP",
                               layer_npp: typings.LayerSpec = "NPP",
                               layer_via: typings.LayerSpec | None = None,
                               width_via: float = 1.0,
                               layer_metal: typings.LayerSpec | None = None,
                               port_names: tuple[str, str] = ("o1", "o2"),
                               cladding_layers: typings.Layers
                               | None = cladding_layers_optical,
                               cladding_offsets: typings.Floats
                               | None = cladding_offsets_optical,
                               cladding_simplify: typings.Floats | None = None,
                               **kwargs: Any) -> CrossSection
```

Linear Ge detector cross section based on a lateral p(i)n junction.

It has silicon contacts (no contact on the Ge). The contacts need to be
created in the component generating function (they can't be created here).

See Chen et al., "High-Responsivity Low-Voltage 28-Gb/s Ge p-i-n Photodetector
With Silicon Contacts", Journal of Lightwave Technology 33(4), 2015.

Notice it is possible to have dopings going beyond the ridge waveguide. This
is fine, and it is to account for the
presence of the contacts. Such contacts can be subwavelength or not.

**Arguments**:

- `width_si` - width of the full etch si in um.
- `layer_si` - si ridge layer.
- `width_ge` - width of the ge in um.
- `layer_ge` - ge layer.
- `gap_low_doping` - from waveguide center to low doping.
- `gap_medium_doping` - from waveguide center to medium doping. None removes it.
- `gap_high_doping` - from center to high doping. None removes it.
- `width_doping` - distance from waveguide center to doping edge in um.
- `layer_p` - p doping layer.
- `layer_pp` - p+ doping layer.
- `layer_ppp` - p++ doping layer.
- `layer_n` - n doping layer.
- `layer_np` - n+ doping layer.
- `layer_npp` - n++ doping layer.
- `layer_via` - via layer.
- `width_via` - via width in um.
- `layer_metal` - metal layer.
- `port_names` - for input and output ('o1', 'o2').
- `cladding_layers` - list of layers to extrude.
- `cladding_offsets` - list of offset from main Section edge.
- `cladding_simplify` - Optional Tolerance value for the simplification algorithm.                 All points that can be removed without changing the resulting.                 polygon by more than the value listed here will be removed.
- `kwargs` - cross_section settings.
  
  .. code::
  
  layer_si
  |<------width_si---->|
  
  layer_ge
  |<--width_ge->|
  ______________
  |             |
  __|_____________|___
  |     |       |     |
  |     |       |     |
  P      |     |       |     |         N                |
  width_p   |_____|_______|_____|           width_n        |
  <----------------------->|       |<------------------------------>|
  |<->|
  gap_low_doping
  |         |        N+                |
  |         |     width_np             |
  |         |<------------------------>|
  |<------->|
  |     gap_medium_doping
  |
  |<---------------------------------->|
  width_doping
  
  .. plot::
  :include-source:
  
  import gdsfactory as gf
  
  xs = gf.cross_section.pn()
  p = gf.path.straight()
  c = p.extrude(xs)
  c.plot()

<a id="gdsfactory.cross_section.get_cross_sections"></a>

#### get\_cross\_sections

```python
def get_cross_sections(
        modules: Sequence[ModuleType] | ModuleType,
        verbose: bool = False) -> dict[str, CrossSectionFactory]
```

Returns cross_sections from a module or list of modules.

**Arguments**:

- `modules` - module or iterable of modules.
- `verbose` - prints in case any errors occur.

<a id="gdsfactory._cell"></a>

# gdsfactory.\_cell

<a id="gdsfactory._cell.cell"></a>

#### cell

```python
def cell(
    _func: ComponentFunc[ComponentParams] | None = None,
    *,
    set_settings: bool = True,
    set_name: bool = True,
    check_ports: bool = True,
    check_instances: CheckInstances | None = None,
    snap_ports: bool = True,
    add_port_layers: bool = True,
    cache: Cache[int, Any] | dict[int, Any] | None = None,
    basename: str | None = None,
    drop_params: list[str] | None = None,
    register_factory: bool = True,
    overwrite_existing: bool | None = None,
    layout_cache: bool | None = None,
    info: dict[str, MetaData] | None = None,
    post_process: Iterable[Callable[[Component], None]] | None = None,
    debug_names: bool | None = None,
    tags: list[str] | None = None,
    with_module_name: bool = False
) -> (ComponentFunc[ComponentParams]
      | Callable[[ComponentFunc[ComponentParams]],
                 ComponentFunc[ComponentParams]])
```

Decorator to convert a function into a Component.

<a id="gdsfactory._cell.cell_with_module_name"></a>

#### cell\_with\_module\_name

type: ignore

<a id="gdsfactory._deprecation"></a>

# gdsfactory.\_deprecation

<a id="gdsfactory.add_pins"></a>

# gdsfactory.add\_pins

Add_pin adds a Pin to a port, add_pins adds Pins to all ports.

- pins
- outline

Some functions modify a component without changing its name.
Make sure these functions are inside a new Component or called as a decorator
They without modifying the cell name

<a id="gdsfactory.add_pins.add_bbox"></a>

#### add\_bbox

```python
def add_bbox(component: Component,
             bbox_layer: typings.LayerSpec = "DEVREC",
             top: float = 0,
             bottom: float = 0,
             left: float = 0,
             right: float = 0) -> Component
```

Add bbox on outline.

**Arguments**:

- `component` - component to add bbox.
- `bbox_layer` - bbox layer.
- `top` - padding.
- `bottom` - padding.
- `left` - padding.
- `right` - padding.

<a id="gdsfactory.add_pins.add_bbox_siepic"></a>

#### add\_bbox\_siepic

```python
def add_bbox_siepic(
    component: Component,
    bbox_layer: typings.LayerSpec = "DEVREC",
    remove_layers: typings.LayerSpecs = ("PORT", "PORTE")
) -> Component
```

Add bounding box device recognition layer.

**Arguments**:

- `component` - to add bbox.
- `bbox_layer` - bounding box.
- `remove_layers` - remove other layers.

<a id="gdsfactory.add_pins.get_pin_triangle_polygon_tip"></a>

#### get\_pin\_triangle\_polygon\_tip

```python
def get_pin_triangle_polygon_tip(
    port: typings.Port
) -> tuple[npt.NDArray[np.floating[Any]], tuple[float, float]]
```

Returns triangle polygon and tip position.

<a id="gdsfactory.add_pins.add_pin_triangle"></a>

#### add\_pin\_triangle

```python
def add_pin_triangle(component: Component,
                     port: typings.Port,
                     layer: typings.LayerSpec = "PORT",
                     layer_label: typings.LayerSpec | None = "TEXT") -> None
```

Add triangle pin with a right angle, pointing out of the port.

**Arguments**:

- `component` - to add pin.
- `port` - Port.
- `layer` - for the pin marker.
- `layer_label` - for the label.

<a id="gdsfactory.add_pins.add_pin_rectangle_inside"></a>

#### add\_pin\_rectangle\_inside

```python
def add_pin_rectangle_inside(
        component: Component,
        port: typings.Port,
        pin_length: float = 0.1,
        layer: typings.LayerSpec = "PORT",
        layer_label: typings.LayerSpec | None = "TEXT") -> None
```

Add square pin towards the inside of the port.

**Arguments**:

- `component` - to add pins.
- `port` - Port.
- `pin_length` - length of the pin marker for the port.
- `layer` - layer to place the pin rectangle on.
- `layer_label` - layer to place the text label on.
  
  .. code::
  
  _______________
  |               |
  |               |
  |               |
  ||              |
  ||              |
  |               |
  |      __       |
  |_______________|

<a id="gdsfactory.add_pins.add_pin_rectangle"></a>

#### add\_pin\_rectangle

```python
def add_pin_rectangle(component: Component,
                      port: typings.Port,
                      pin_length: float = 0.1,
                      layer: typings.LayerSpec | None = "PORT",
                      layer_label: typings.LayerSpec | None = "TEXT",
                      port_margin: float = 0.0) -> None
```

Add half out pin to a component.

**Arguments**:

- `component` - to add pin.
- `port` - Port.
- `pin_length` - length of the pin marker for the port.
- `layer` - for the pin marker.
- `layer_label` - for the label.
- `port_margin` - margin to port edge.
  
  .. code::
  
  _______________
  |               |
  |               |
  |               |
  |||              |
  |||              |
  |               |
  |      __       |
  |_______________|
  __

<a id="gdsfactory.add_pins.add_pin_path"></a>

#### add\_pin\_path

```python
def add_pin_path(component: Component,
                 port: typings.Port,
                 pin_length: float = 2 * nm,
                 layer: typings.LayerSpec = "PORT",
                 layer_label: typings.LayerSpec | None = None) -> None
```

Add half out path pin to a component.

This port type is compatible with SiEPIC pdk.

**Arguments**:

- `component` - to add pin.
- `port` - Port.
- `pin_length` - length of the pin marker for the port.
- `layer` - for the pin marker.
- `layer_label` - optional layer label. Defaults to layer.
  
  .. code::
  
  _______________
  |               |
  |               |
  |               |
  |||              |
  |||              |
  |               |
  |      __       |
  |_______________|
  __

<a id="gdsfactory.add_pins.add_outline"></a>

#### add\_outline

```python
def add_outline(component: Component,
                reference: ComponentReference | None = None,
                layer: typings.LayerSpec = "DEVREC",
                **kwargs: Any) -> None
```

Adds devices outline bounding box in layer.

**Arguments**:

- `component` - where to add the markers.
- `reference` - to read outline from.
- `layer` - to add padding.
- `kwargs` - padding settings.
  

**Arguments**:

- `default` - default padding.
- `top` - North padding.
- `bottom` - padding.
- `right` - padding.
- `left` - padding.

<a id="gdsfactory.add_pins.add_pins_siepic"></a>

#### add\_pins\_siepic

```python
def add_pins_siepic(component: Component,
                    function: AddPinPathFunction = add_pin_path,
                    port_type: str = "optical",
                    layer: typings.LayerSpec = "PORT",
                    pin_length: float = 10 * nm,
                    **kwargs: Any) -> Component
```

Add pins.

Enables you to run SiEPIC verification tools:
To Run verification install SiEPIC-tools KLayout package
then hit V shortcut in KLayout to run verification

- ensure no disconnected pins
- netlist extraction

**Arguments**:

- `component` - to add pins.
- `function` - to add pin.
- `port_type` - optical, electrical, ...
- `layer` - pin layer.
- `pin_length` - length of the pin marker for the port.
- `kwargs` - add pins function settings.

<a id="gdsfactory.add_pins.add_pins"></a>

#### add\_pins

```python
def add_pins(component: Component,
             port_type: str | None = None,
             function: AddPinFunction = add_pin_rectangle_inside,
             **kwargs: Any) -> None
```

Add Pin port markers.

**Arguments**:

- `component` - to add ports to.
- `port_type` - Which port type do you want to add pins to. optical, electrical, ...  If None, it will add to all.
- `layer` - layer for the pin marker.
- `function` - to add each pin.
- `kwargs` - add pins function settings.

<a id="gdsfactory.add_pins.add_pins_triangle"></a>

#### add\_pins\_triangle

type: ignore[arg-type]

<a id="gdsfactory.add_pins.add_pins_center"></a>

#### add\_pins\_center

type: ignore[arg-type]

<a id="gdsfactory.add_pins.add_settings_label"></a>

#### add\_settings\_label

```python
def add_settings_label(component: Component,
                       reference: ComponentReference | None = None,
                       layer_label: typings.LayerSpec = "LABEL_SETTINGS",
                       with_yaml_format: bool = False) -> None
```

Add settings in label.

**Arguments**:

- `component` - to add pins.
- `reference` - ComponentReference.
- `layer_label` - layer spec.
- `with_yaml_format` - add yaml format, False uses json.

<a id="gdsfactory.add_pins.add_instance_label"></a>

#### add\_instance\_label

```python
def add_instance_label(component: Component,
                       reference: ComponentReference,
                       layer: typings.LayerSpec | None = None,
                       instance_name: str | None = None) -> None
```

Adds label to a reference in a component.

**Arguments**:

- `component` - to add instance label.
- `reference` - to add label.
- `layer` - layer for the label.
- `instance_name` - label name.

<a id="gdsfactory.add_pins.add_pins_and_outline"></a>

#### add\_pins\_and\_outline

```python
def add_pins_and_outline(
    component: Component,
    reference: ComponentReference | None = None,
    add_outline_function: AddInstanceLabelFunction | None = add_outline,
    add_pins_function: AddPinsFunction | None = add_pins,
    add_settings_function: AddInstanceLabelFunction
    | None = add_settings_label,
    add_instance_label_function: AddInstanceLabelFunction
    | None = add_settings_label
) -> None
```

Add pins component outline.

**Arguments**:

- `component` - where to add the markers.
- `reference` - to add pins.
- `add_outline_function` - to add outline around the component.
- `add_pins_function` - to add pins to ports.
- `add_settings_function` - to add outline around the component.
- `add_instance_label_function` - labels each instance.

<a id="gdsfactory.config"></a>

# gdsfactory.config

Gdsfactory configuration.

<a id="gdsfactory.config.print_version_plugins"></a>

#### print\_version\_plugins

```python
def print_version_plugins(packages: list[str] | None = None) -> None
```

Print gdsfactory plugin versions and paths.

**Arguments**:

- `packages` - list of packages to print versions for.

<a id="gdsfactory.config.print_version_plugins_raw"></a>

#### print\_version\_plugins\_raw

```python
def print_version_plugins_raw() -> None
```

Print gdsfactory plugin versions and paths.

<a id="gdsfactory.config.CONF"></a>

#### CONF

type: ignore[assignment]

<a id="gdsfactory.config.Paths"></a>

## Paths Objects

```python
class Paths()
```

<a id="gdsfactory.config.Paths.sparameters_repo"></a>

#### sparameters\_repo

repo with some demo sparameters

<a id="gdsfactory.config.rich_output"></a>

#### rich\_output

```python
def rich_output() -> None
```

Enables rich output.

<a id="gdsfactory.grid"></a>

# gdsfactory.grid

pack a list of components into a grid.

Adapted from PHIDL https://github.com/amccaugh/phidl/ by Adam McCaughan

<a id="gdsfactory.grid.grid"></a>

#### grid

```python
def grid(components: ComponentSpecs = ("rectangle", "triangle"),
         spacing: Spacing | float = (5.0, 5.0),
         shape: tuple[int, int] | None = None,
         align_x: Literal["origin", "xmin", "xmax", "center"] = "center",
         align_y: Literal["origin", "ymin", "ymax", "center"] = "center",
         rotation: int = 0,
         mirror: bool = False) -> Component
```

Returns Component with a 1D or 2D grid of components.

**Arguments**:

- `components` - Iterable to be placed onto a grid. (can be 1D or 2D).
- `spacing` - between adjacent elements on the grid, can be a tuple for                 different distances in height and width or a single float.
- `shape` - x, y shape of the grid (see np.reshape).                 If no shape and the list is 1D, if np.reshape were run with (1, -1).
- `align_x` - x alignment along (origin, xmin, xmax, center).
- `align_y` - y alignment along (origin, ymin, ymax, center).
- `rotation` - for each component in degrees.
- `mirror` - horizontal mirror y axis (x, 1) (1, 0). most common mirror.
  

**Returns**:

  Component containing components grid.
  
  .. plot::
  :include-source:
  
  import gdsfactory as gf
  
  components = [gf.components.triangle(x=i) for i in range(1, 10)]
  c = gf.grid(
  components,
  shape=(1, len(components)),
  rotation=0,
  mirror=False,
  spacing=(100, 100),
  )
  c.plot()

<a id="gdsfactory.grid.grid_with_text"></a>

#### grid\_with\_text

```python
def grid_with_text(components: Sequence[ComponentSpec] = ("rectangle",
                                                          "triangle"),
                   text_prefix: str = "",
                   text_offsets: Sequence[Float2] | None = None,
                   text_anchors: Sequence[Anchor] | None = None,
                   text_mirror: bool = False,
                   text_rotation: int = 0,
                   text: ComponentSpec | None = "text_rectangular",
                   spacing: Spacing | float = (5.0, 5.0),
                   shape: tuple[int, int] | None = None,
                   align_x: Literal["origin", "xmin", "xmax",
                                    "center"] = "center",
                   align_y: Literal["origin", "ymin", "ymax",
                                    "center"] = "center",
                   rotation: int = 0,
                   mirror: bool = False,
                   labels: Sequence[str] | None = None) -> Component
```

Returns Component with 1D or 2D grid of components with text labels.

**Arguments**:

- `components` - Iterable to be placed onto a grid. (can be 1D or 2D).
- `text_prefix` - for labels. For example. 'A' will produce 'A1', 'A2', ...
- `text_offsets` - relative to component anchor. Defaults to center.
- `text_anchors` - relative to component (ce cw nc ne nw sc se sw center cc).
- `text_mirror` - if True mirrors text.
- `text_rotation` - Optional text rotation.
- `text` - function to add text labels.
- `spacing` - between adjacent elements on the grid, can be a tuple for                 different distances in height and width.
- `shape` - x, y shape of the grid (see np.reshape).
- `align_x` - x alignment along (origin, xmin, xmax, center).
- `align_y` - y alignment along (origin, ymin, ymax, center).
- `rotation` - for each component in degrees.
- `mirror` - horizontal mirror y axis (x, 1) (1, 0). most common mirror.
- `labels` - list of labels for each component.
  
  
  .. plot::
  :include-source:
  
  import gdsfactory as gf
  
  components = [gf.components.triangle(x=i) for i in range(1, 10)]
  c = gf.grid_with_text(
  components,
  shape=(1, len(components)),
  rotation=0,
  mirror=False,
  spacing=(100, 100),
  text_offsets=((0, 100), (0, -100)),
  text_anchors=("nc", "sc"),
  )
  c.plot()

<a id="gdsfactory.difftest_git"></a>

# gdsfactory.difftest\_git

<a id="gdsfactory.difftest_git.gdsdiff_git"></a>

#### gdsdiff\_git

```python
def gdsdiff_git(path: str = "",
                curr_file: str = "",
                old_file: str = "",
                old_hex: str = "",
                old_mode: str = "",
                new_file: str = "",
                new_hex: str = "",
                new_mode: str = "") -> None
```

Show diffs for two files when running git diff.

**Arguments**:

- `path` - script to run path.
- `curr_file` - current GDS file.
- `old_file` - old GDS.
- `old_hex` - ignore.
- `old_mode` - ignore.
- `new_file` - new GDS file.
- `new_hex` - ignore.
- `new_mode` - ignore.

<a id="gdsfactory.typings"></a>

# gdsfactory.typings

In programming, a factory is a function that returns an object.

Functions are easy to understand because they have clear inputs and outputs.
Most gdsfactory functions take some inputs and return a Component object.
Some of these inputs parameters are also functions.

- Component: Object with.
    - name.
    - references: to other components (x, y, rotation).
    - polygons in different layers.
    - ports dict.


Specs:

- ComponentSpec: Component, function, string or dict
    (component=mzi, settings=dict(delta_length=20)).
- LayerSpec: (3, 0), 3 (assumes 0 as datatype) or string.

<a id="gdsfactory.typings.Step"></a>

## Step Objects

```python
@dataclasses.dataclass
class Step()
```

Manhattan Step.

**Arguments**:

- `x` - absolute.
- `y` - absolute.
- `dx` - x-displacement.
- `dy` - y-displacement.

<a id="gdsfactory.typings.TypedArray"></a>

## TypedArray Objects

```python
class TypedArray(np.ndarray[Any, np.dtype[Any]])
```

based on https://github.com/samuelcolvin/pydantic/issues/380.

<a id="gdsfactory.add_padding"></a>

# gdsfactory.add\_padding

<a id="gdsfactory.add_padding.get_padding_points"></a>

#### get\_padding\_points

```python
def get_padding_points(component: ComponentBase | ComponentReference
                       | kf.kcell.ProtoKCell[float, Any],
                       default: float = 50.0,
                       top: float | None = None,
                       bottom: float | None = None,
                       right: float | None = None,
                       left: float | None = None) -> list[Coordinate]
```

Returns padding points for a component outline.

**Arguments**:

- `component` - to add padding.
- `default` - default padding in um.
- `top` - north padding in um.
- `bottom` - south padding in um.
- `right` - east padding in um.
- `left` - west padding in um.

<a id="gdsfactory.add_padding.add_padding"></a>

#### add\_padding

```python
def add_padding(component: ComponentSpec = "mmi2x2",
                layers: LayerSpecs = ("PADDING", ),
                default: float = 50.0,
                top: float | None = None,
                bottom: float | None = None,
                right: float | None = None,
                left: float | None = None) -> Component
```

Adds padding layers to component. Returns same component.

**Arguments**:

- `component` - to add padding.
- `layers` - list of layers.
- `default` - default padding.
- `top` - north padding in um.
- `bottom` - south padding in um.
- `right` - east padding in um.
- `left` - west padding in um.

<a id="gdsfactory.add_padding.add_padding_to_size"></a>

#### add\_padding\_to\_size

```python
def add_padding_to_size(component: ComponentSpec,
                        layers: LayerSpecs = ("PADDING", ),
                        xsize: float | None = None,
                        ysize: float | None = None,
                        left: float = 0,
                        bottom: float = 0) -> Component
```

Returns component with padding layers on each side.

New size is multiple of grid size.

**Arguments**:

- `component` - to add padding.
- `layers` - list of layers.
- `xsize` - x size to fill up in um.
- `ysize` - y size to fill up in um.
- `left` - left padding in um to fill up in um.
- `bottom` - bottom padding in um to fill up in um.

<a id="gdsfactory.pdk"></a>

# gdsfactory.pdk

PDK stores layers, cross_sections, cell functions ...

<a id="gdsfactory.pdk.evanescent_coupler_sample"></a>

#### evanescent\_coupler\_sample

```python
def evanescent_coupler_sample() -> None
```

Evanescent coupler example.

**Arguments**:

- `coupler_length` - length of coupling (min: 0.0, max: 200.0, um).

<a id="gdsfactory.pdk.extract_args_from_docstring"></a>

#### extract\_args\_from\_docstring

```python
def extract_args_from_docstring(docstring: str) -> dict[str, Any]
```

This function extracts settings from a function's docstring for uPDK format.

**Arguments**:

- `docstring` - The function from which to extract YAML in the docstring.
  

**Returns**:

- `settings` _dict_ - The extracted YAML data as a dictionary.

<a id="gdsfactory.pdk.Pdk"></a>

## Pdk Objects

```python
class Pdk(BaseModel)
```

Store layers, cross_sections, cell functions, simulation_settings ...

only one Pdk can be active at a given time.

**Arguments**:

- `name` - PDK name.
- `version` - PDK version.
- `cross_sections` - dict of cross_sections factories.
- `cells` - dict of parametric cells that return Components.
- `containers` - dict of containers that return Components. A container is a cell that contains other cells.
- `models` - dict of models names to functions.
- `symbols` - dict of symbols names to functions.
  default_symbol_factory:
- `base_pdk` - a pdk to copy from and extend.
- `default_decorator` - decorate all cells, if not otherwise defined on the cell.
- `layers` - maps name to gdslayer/datatype.
  For example dict(si=(1, 0), sin=(34, 0)).
- `layer_stack` - maps name to layer numbers, thickness, zmin, sidewall_angle.
  if can also contain material properties
  (refractive index, nonlinear coefficient, sheet resistance ...).
- `layer_views` - includes layer name to color, opacity and pattern.
- `layer_transitions` - transitions between different cross_sections.
- `constants` - dict of constants for the PDK.
- `materials_index` - material spec names to material spec, which can be:
- `string` - material name.
- `float` - refractive index.
  float, float: refractive index real and imaginary part.
- `function` - function of wavelength.
- `routing_strategies` - functions enabled to route.
- `bend_points_distance` - default points distance for bends in um.
- `connectivity` - defines connectivity between layers through vias.

<a id="gdsfactory.pdk.Pdk.xsection"></a>

#### xsection

```python
def xsection(func: Callable[..., CrossSection]) -> Callable[..., CrossSection]
```

Decorator to register a cross section function.

Ensures that the cross-section name matches the name of the function
that generated it when created using default parameters.

.. code-block:: python

    @pdk.xsection
    def xs_sc(width=TECH.width_sc, radius=TECH.radius_sc):
        return gf.cross_section.cross_section(width=width, radius=radius)

<a id="gdsfactory.pdk.Pdk.activate"></a>

#### activate

```python
def activate(force: bool = False) -> None
```

Set current pdk to the active pdk (if not already active).

<a id="gdsfactory.pdk.Pdk.register_cells"></a>

#### register\_cells

```python
def register_cells(**kwargs: Any) -> None
```

Register cell factories.

<a id="gdsfactory.pdk.Pdk.register_cross_sections"></a>

#### register\_cross\_sections

```python
def register_cross_sections(**kwargs: Any) -> None
```

Register cross_sections factories.

<a id="gdsfactory.pdk.Pdk.register_cells_yaml"></a>

#### register\_cells\_yaml

```python
def register_cells_yaml(dirpath: PathType | None = None,
                        update: bool = False,
                        **kwargs: Any) -> None
```

Load *.pic.yml YAML files and register them as cells.

**Arguments**:

- `dirpath` - directory to recursive search for YAML cells.
- `update` - does not raise ValueError if cell already registered.
- `kwargs` - cell_name: cell function. To update cells dict.
  

**Arguments**:

- `cell_name` - cell function. To update cells dict.

<a id="gdsfactory.pdk.Pdk.remove_cell"></a>

#### remove\_cell

```python
def remove_cell(name: str) -> None
```

Removes cell from a PDK.

<a id="gdsfactory.pdk.Pdk.get_cell"></a>

#### get\_cell

```python
def get_cell(cell: CellSpec, **kwargs: Any) -> ComponentFactory
```

Returns ComponentFactory from a cell spec.

<a id="gdsfactory.pdk.Pdk.get_component"></a>

#### get\_component

```python
def get_component(component: ComponentSpec,
                  settings: Mapping[str, Any] | None = None,
                  include_containers: bool = True,
                  **kwargs: Any) -> Component
```

Returns component from a component spec.

<a id="gdsfactory.pdk.Pdk.get_symbol"></a>

#### get\_symbol

```python
def get_symbol(component: ComponentSpec, **kwargs: Any) -> Component
```

Returns a component's symbol from a component spec.

<a id="gdsfactory.pdk.Pdk.get_cross_section"></a>

#### get\_cross\_section

```python
def get_cross_section(cross_section: CrossSectionSpec,
                      **kwargs: Any) -> CrossSection
```

Returns cross_section from a cross_section spec.

**Arguments**:

- `cross_section` - CrossSection, CrossSectionFactory, Transition, string or dict.
- `kwargs` - settings to override.

<a id="gdsfactory.pdk.Pdk.get_layer"></a>

#### get\_layer

```python
def get_layer(layer: LayerSpec | kf.kdb.LayerInfo) -> LayerEnum | int
```

Returns layer from a layer spec.

<a id="gdsfactory.pdk.Pdk.to_updk"></a>

#### to\_updk

```python
def to_updk(exclude: Sequence[str] | None = None) -> str
```

Export to uPDK YAML definition.

<a id="gdsfactory.pdk.Pdk.klayout_technology"></a>

#### klayout\_technology

```python
@cached_property
def klayout_technology() -> klayout_tech.KLayoutTechnology
```

Returns a KLayoutTechnology from the PDK.

**Raises**:

  UserWarning if required properties for generating a KLayoutTechnology are not defined.

<a id="gdsfactory.pdk.get_active_pdk"></a>

#### get\_active\_pdk

```python
def get_active_pdk(name: str | None = None) -> Pdk
```

Returns active PDK.

By default it will return the PDK defined in the name or config file.
Otherwise it will return the generic PDK.

<a id="gdsfactory.pdk.get_layer_tuple"></a>

#### get\_layer\_tuple

```python
def get_layer_tuple(layer: LayerSpec) -> tuple[int, int]
```

Returns layer tuple (layer, datatype) from a layer spec.

<a id="gdsfactory.pdk.get_constant"></a>

#### get\_constant

```python
def get_constant(constant_name: Any) -> Any
```

If constant_name is a string returns a the value from the dict.

<a id="gdsfactory.pdk.get_routing_strategies"></a>

#### get\_routing\_strategies

```python
def get_routing_strategies() -> RoutingStrategies
```

Gets a dictionary of named routing functions available to the PDK, if defined, or gdsfactory defaults otherwise.

<a id="gdsfactory.components.shapes.cross"></a>

# gdsfactory.components.shapes.cross

<a id="gdsfactory.components.shapes.cross.cross"></a>

#### cross

```python
@gf.cell_with_module_name
def cross(length: float = 10.0,
          width: float = 3.0,
          layer: LayerSpec = "WG",
          port_type: str | None = None) -> Component
```

Returns a cross from two rectangles of length and width.

**Arguments**:

- `length` - float Length of the cross from one end to the other.
- `width` - float Width of the arms of the cross.
- `layer` - layer for geometry.
- `port_type` - None, optical, electrical.

<a id="gdsfactory.components.shapes.L"></a>

# gdsfactory.components.shapes.L

<a id="gdsfactory.components.shapes.L.L"></a>

#### L

```python
@gf.cell_with_module_name
def L(width: int | float = 1,
      size: tuple[int, int] = (10, 20),
      layer: LayerSpec = "MTOP",
      port_type: str = "electrical") -> Component
```

Generates an 'L' geometry with ports on both ends.

Based on phidl.

**Arguments**:

- `width` - of the line.
- `size` - length and height of the base.
- `layer` - spec.
- `port_type` - for port.

<a id="gdsfactory.components.shapes.triangles"></a>

# gdsfactory.components.shapes.triangles

<a id="gdsfactory.components.shapes.triangles.triangle"></a>

#### triangle

```python
@gf.cell_with_module_name
def triangle(x: float = 10,
             xtop: float = 0,
             y: float = 20,
             ybot: float = 0,
             layer: LayerSpec = "WG") -> Component
```

Return triangle.

**Arguments**:

- `x` - base xsize.
- `xtop` - top xsize.
- `y` - ysize.
- `ybot` - bottom ysize.
- `layer` - layer.
  
  .. code::
  
  xtop
  _
  | \
  |  \
  |   \
  y|    \
  |     \
  |      \
  |______|ybot
  x

<a id="gdsfactory.components.shapes.triangles.triangle2"></a>

#### triangle2

```python
@gf.cell_with_module_name
def triangle2(spacing: float = 3, **kwargs: Any) -> Component
```

Return 2 triangles (bot, top).

**Arguments**:

- `spacing` - between top and bottom.
- `kwargs` - triangle arguments.
  

**Arguments**:

- `x` - base xsize.
- `xtop` - top xsize.
- `y` - ysize.
- `ybot` - bottom ysize.
- `layer` - layer.
  
  .. code::
  
  _
  | \
  |  \
  |   \
  |    \
  |     \
  |      \
  |       \
  |       |  spacing
  |      /
  |     /
  |    /
  |   /
  |  /
  |_/

<a id="gdsfactory.components.shapes.triangles.triangle4"></a>

#### triangle4

```python
@gf.cell_with_module_name
def triangle4(**kwargs: Any) -> Component
```

Return 4 triangles.

**Arguments**:

- `kwargs` - triangle arguments.
  

**Arguments**:

- `x` - base xsize.
- `xtop` - top xsize.
- `y` - ysize.
- `ybot` - bottom ysize.
- `layer` - layer.
  
  .. code::
  
  / | \
  /  |  \
  /   |   \
  /    |    \
  /     |     \
  /      |      \
  /       |       \
  |       |       |
  \       |      /
  \      |     /
  \     |    /
  \    |   /
  \   |  /
  \  |_/

<a id="gdsfactory.components.shapes.ellipse"></a>

# gdsfactory.components.shapes.ellipse

<a id="gdsfactory.components.shapes.ellipse.ellipse"></a>

#### ellipse

```python
@gf.cell_with_module_name
def ellipse(radii: tuple[float, float] = (10.0, 5.0),
            angle_resolution: float = 2.5,
            layer: LayerSpec = "WG") -> Component
```

Returns ellipse component.

**Arguments**:

- `radii` - Semimajor and semiminor axis lengths of the ellipse.
- `angle_resolution` - number of degrees per point.
- `layer` - Specific layer(s) to put polygon geometry on.
  
  The orientation of the ellipse is determined by the order of the radii variables;
  if the first element is larger, the ellipse will be horizontal and if the second
  element is larger, the ellipse will be vertical.

<a id="gdsfactory.components.shapes.rectangle"></a>

# gdsfactory.components.shapes.rectangle

<a id="gdsfactory.components.shapes.rectangle.rectangle"></a>

#### rectangle

```python
@gf.cell_with_module_name
def rectangle(
    size: Size = (4.0, 2.0),
    layer: LayerSpec = "WG",
    centered: bool = False,
    port_type: str | None = "electrical",
    port_orientations: Ints | None = (180, 90, 0, -90)
) -> Component
```

Returns a rectangle.

**Arguments**:

- `size` - (tuple) Width and height of rectangle.
- `layer` - Specific layer to put polygon geometry on.
- `centered` - True sets center to (0, 0), False sets south-west to (0, 0).
- `port_type` - optical, electrical.
- `port_orientations` - list of port_orientations to add. None adds no ports.

<a id="gdsfactory.components.shapes.rectangle.rectangles"></a>

#### rectangles

```python
@gf.cell_with_module_name
def rectangles(size: Size = (4.0, 2.0),
               offsets: Sequence[float] | None = None,
               layers: LayerSpecs = ("WG", "SLAB150"),
               centered: bool = True,
               **kwargs: Any) -> Component
```

Returns overimposed rectangles.

**Arguments**:

- `size` - (tuple) Width and height of rectangle.
- `layers` - Specific layer to put polygon geometry on.
- `offsets` - list of offsets. If None, all rectangles have a zero offset.
- `centered` - True sets center to (0, 0), False sets south-west of first rectangle to (0, 0).
- `kwargs` - additional arguments to pass to rectangle.
  

**Arguments**:

- `port_type` - optical, electrical.
- `port_orientations` - list of port_orientations to add.
  
  .. code::
  
  ┌──────────────┐
  │              │
  │   ┌──────┐   │
  │   │      │   │
  │   │      ├───►
  │   │      │offset
  │   └──────┘   │
  │              │
  └──────────────┘

<a id="gdsfactory.components.shapes.nxn"></a>

# gdsfactory.components.shapes.nxn

<a id="gdsfactory.components.shapes.nxn.nxn"></a>

#### nxn

```python
@gf.cell_with_module_name
def nxn(west: int = 1,
        east: int = 4,
        north: int = 0,
        south: int = 0,
        xsize: float = 8.0,
        ysize: float = 8.0,
        wg_width: float = 0.5,
        layer: LayerSpec = "WG",
        wg_margin: float = 1.0,
        **kwargs: Any) -> Component
```

Returns a nxn component with nxn ports (west, east, north, south).

**Arguments**:

- `west` - number of west ports.
- `east` - number of east ports.
- `north` - number of north ports.
- `south` - number of south ports.
- `xsize` - size in X.
- `ysize` - size in Y.
- `wg_width` - width of the straight ports.
- `layer` - layer.
- `wg_margin` - margin from straight to component edge.
- `kwargs` - port_settings.
  
  .. code::
  
  3   4
  |___|_
  2 -|      |- 5
  |      |
  1 -|______|- 6
  |   |
  8   7

<a id="gdsfactory.components.shapes"></a>

# gdsfactory.components.shapes

<a id="gdsfactory.components.shapes.regular_polygon"></a>

# gdsfactory.components.shapes.regular\_polygon

<a id="gdsfactory.components.shapes.regular_polygon.regular_polygon"></a>

#### regular\_polygon

```python
@gf.cell_with_module_name
def regular_polygon(sides: int = 6,
                    side_length: float = 10,
                    layer: LayerSpec = "WG",
                    port_type: str | None = "placement") -> Component
```

Returns a regular N-sided polygon, with ports on each edge.

**Arguments**:

- `sides` - number of sides for the polygon.
- `side_length` - of the edges.
- `layer` - Specific layer to put polygon geometry on.
- `port_type` - optical, electrical.

<a id="gdsfactory.components.shapes.bbox"></a>

# gdsfactory.components.shapes.bbox

<a id="gdsfactory.components.shapes.bbox.bbox_to_points"></a>

#### bbox\_to\_points

```python
def bbox_to_points(bbox: gf.kdb.DBox,
                   top: float = 0,
                   bottom: float = 0,
                   left: float = 0,
                   right: float = 0) -> list[tuple[float, float]]
```

Returns bounding box rectangle with offsets.

**Arguments**:

- `bbox` - DBbox.
- `top` - north offset.
- `bottom` - south offset.
- `left` - west offset.
- `right` - east offset.

<a id="gdsfactory.components.shapes.bbox.bbox"></a>

#### bbox

```python
@gf.cell_with_module_name
def bbox(component: gf.Component | ComponentReference,
         layer: LayerSpec,
         top: float = 0,
         bottom: float = 0,
         left: float = 0,
         right: float = 0) -> gf.Component
```

Returns bounding box rectangle from coordinates.

**Arguments**:

- `component` - component or instance to get bbox from.
- `layer` - for bbox.
- `top` - north offset.
- `bottom` - south offset.
- `left` - west offset.
- `right` - east offset.

<a id="gdsfactory.components.shapes.C"></a>

# gdsfactory.components.shapes.C

<a id="gdsfactory.components.shapes.C.C"></a>

#### C

```python
@gf.cell_with_module_name
def C(width: float = 1.0,
      size: Size = (10.0, 20.0),
      layer: LayerSpec = "WG",
      port_type: str = "electrical") -> Component
```

C geometry with ports on both ends.

based on phidl.

**Arguments**:

- `width` - of the line.
- `size` - length and height of the base.
- `layer` - layer spec.
- `port_type` - optical or electrical.
  
  .. code::
  
  ______
  |       o1
  |   ___
  |  |
  |  |___
  ||<---> size[0]
  |______ o2

<a id="gdsfactory.components.shapes.fiducial_squares"></a>

# gdsfactory.components.shapes.fiducial\_squares

<a id="gdsfactory.components.shapes.fiducial_squares.fiducial_squares"></a>

#### fiducial\_squares

```python
@gf.cell_with_module_name
def fiducial_squares(layers: Layers = ((1, 0), ),
                     size: Float2 = (5, 5),
                     offset: float = 0.14) -> gf.Component
```

Returns fiducials with two squares.

**Arguments**:

- `layers` - list of layers.
- `size` - in um.
- `offset` - in um.

<a id="gdsfactory.components.shapes.circle"></a>

# gdsfactory.components.shapes.circle

<a id="gdsfactory.components.shapes.circle.circle"></a>

#### circle

```python
@gf.cell_with_module_name
def circle(radius: float = 10.0,
           angle_resolution: float = 2.5,
           layer: LayerSpec = "WG") -> Component
```

Generate a circle geometry.

**Arguments**:

- `radius` - of the circle.
- `angle_resolution` - number of degrees per point.
- `layer` - layer.

<a id="gdsfactory.components.shapes.compass"></a>

# gdsfactory.components.shapes.compass

<a id="gdsfactory.components.shapes.compass.compass"></a>

#### compass

```python
@gf.cell_with_module_name
def compass(size: Size = (4.0, 2.0),
            layer: LayerSpec = "WG",
            port_type: str | None = "electrical",
            port_inclusion: float = 0.0,
            port_orientations: Ints | None = (180, 90, 0, -90),
            auto_rename_ports: bool = True) -> Component
```

Rectangle with ports on each edge (north, south, east, and west).

**Arguments**:

- `size` - rectangle size.
- `layer` - tuple (int, int).
- `port_type` - optical, electrical.
- `port_inclusion` - from edge.
- `port_orientations` - list of port_orientations to add. None does not add ports.
- `auto_rename_ports` - auto rename ports.

<a id="gdsfactory.components.couplers.coupler90bend"></a>

# gdsfactory.components.couplers.coupler90bend

<a id="gdsfactory.components.couplers.coupler90bend.coupler90bend"></a>

#### coupler90bend

```python
@gf.cell_with_module_name
def coupler90bend(
        radius: float = 10.0,
        gap: float = 0.2,
        bend: ComponentSpec = "bend_euler",
        cross_section_inner: CrossSectionSpec = "strip",
        cross_section_outer: CrossSectionSpec = "strip") -> Component
```

Returns 2 coupled bends.

**Arguments**:

- `radius` - um.
- `gap` - um.
- `bend` - for bend.
- `cross_section_inner` - spec inner bend.
- `cross_section_outer` - spec outer bend.
  
  
  .. code::
  
  r   3 4
  |   | |
  |  / /
  | / /
  2____/ /
  1_____/

<a id="gdsfactory.components.couplers.coupler_full"></a>

# gdsfactory.components.couplers.coupler\_full

<a id="gdsfactory.components.couplers.coupler_full.coupler_full"></a>

#### coupler\_full

```python
@gf.cell_with_module_name
def coupler_full(coupling_length: float = 40.0,
                 dx: Delta = 10.0,
                 dy: Delta = 4.8,
                 gap: float = 0.5,
                 dw: float = 0.1,
                 cross_section: CrossSectionSpec = "strip",
                 width: float | None = None) -> Component
```

Adiabatic Full coupler.

Design based on asymmetric adiabatic full
coupler designs, such as the one reported in 'Integrated Optic Adiabatic
Devices on Silicon' by Y. Shani, et al (IEEE Journal of Quantum
Electronics, Vol. 27, No. 3 March 1991).

1. is the first half of the input S-bend straight where the
input straights widths taper by +dw and -dw,
2. is the second half of the S-bend straight with constant,
unbalanced widths,
3. is the coupling region where the straights from unbalanced widths to
balanced widths to reverse polarity unbalanced widths,
4. is the fixed width straight that curves away from the coupling region,
5.is the final curve where the straights taper back to the regular width
specified in the straight template.

**Arguments**:

- `coupling_length` - Length of the coupling region in um.
- `dx` - Length of the bend regions in um.
- `dy` - Port-to-port distance between the bend regions in um.
- `gap` - Distance between the two straights in um.
- `dw` - delta width. Top arm tapers to width - dw, bottom to width + dw in um.
- `cross_section` - cross-section spec.
- `width` - width of the waveguide. If None, it will use the width of the cross_section.

<a id="gdsfactory.components.couplers.coupler_bent"></a>

# gdsfactory.components.couplers.coupler\_bent

<a id="gdsfactory.components.couplers.coupler_bent.coupler_bent_half"></a>

#### coupler\_bent\_half

```python
@gf.cell_with_module_name
def coupler_bent_half(gap: float = 0.200,
                      radius: float = 26,
                      length: float = 8.6,
                      width1: float = 0.400,
                      width2: float = 0.400,
                      length_straight: float = 10,
                      length_straight_exit: float = 18,
                      cross_section: str = "strip") -> gf.Component
```

Returns Broadband SOI curved / straight directional coupler.

**Arguments**:

- `gap` - gap.
- `radius` - radius coupling.
- `length` - coupler_length.
- `width1` - width1.
- `width2` - width2.
- `length_straight` - input and output straight length.
- `length_straight_exit` - length straight exit.
- `cross_section` - cross_section.

<a id="gdsfactory.components.couplers.coupler_bent.coupler_bent"></a>

#### coupler\_bent

```python
@gf.cell_with_module_name
def coupler_bent(gap: float = 0.200,
                 radius: float = 26,
                 length: float = 8.6,
                 width1: float = 0.400,
                 width2: float = 0.400,
                 length_straight: float = 10,
                 cross_section: str = "strip") -> gf.Component
```

Returns Broadband SOI curved / straight directional coupler.

based on: https://doi.org/10.1038/s41598-017-07618-6.

**Arguments**:

- `gap` - gap.
- `radius` - radius coupling.
- `length` - coupler_length.
- `width1` - width1.
- `width2` - width2.
- `length_straight` - input and output straight length.
- `cross_section` - cross_section.

<a id="gdsfactory.components.couplers.coupler_broadband"></a>

# gdsfactory.components.couplers.coupler\_broadband

<a id="gdsfactory.components.couplers.coupler_broadband.coupler_broadband"></a>

#### coupler\_broadband

```python
@gf.cell_with_module_name
def coupler_broadband(w_sc: float = 0.5,
                      gap_sc: float = 0.2,
                      w_top: float = 0.6,
                      gap_pc: float = 0.3,
                      legnth_taper: float = 1.0,
                      bend: ComponentSpec = "bend_euler",
                      coupler_straight: ComponentSpec = "coupler_straight",
                      length_coupler_straight: float = 12.4,
                      lenght_coupler_big_gap: float = 4.7,
                      cross_section: CrossSectionSpec = "strip",
                      radius: float = 10.0) -> Component
```

Returns broadband coupler component.

https://docs.flexcompute.com/projects/tidy3d/en/latest/notebooks/BroadbandDirectionalCoupler.html
proposed in Zeqin Lu, Han Yun, Yun Wang, Zhitian Chen, Fan Zhang, Nicolas A. F. Jaeger, and Lukas Chrostowski,
"Broadband silicon photonic directional coupler using asymmetric-waveguide based phase control,"
Opt. Express 23, 3795-3808 (2015), DOI: 10.1364/OE.23.003795.

**Arguments**:

- `w_sc` - width of waveguides in the symmetric coupler section.
- `gap_sc` - gap size between the waveguides in the symmetric coupler section.
- `w_top` - width of the top waveguide in the phase control section.
- `gap_pc` - gap size in the phase control section.
- `legnth_taper` - length of the tapers.
- `bend` - bend factory.
- `coupler_straight` - coupler_straight factory.
- `length_coupler_straight` - optimal L_1 from the 3d fdtd analysis.
- `lenght_coupler_big_gap` - optimal L_2 from the 3d fdtd analysis.
- `cross_section` - cross_section of the waveguides.
- `radius` - bend radius.

<a id="gdsfactory.components.couplers"></a>

# gdsfactory.components.couplers

<a id="gdsfactory.components.couplers.coupler_asymmetric"></a>

# gdsfactory.components.couplers.coupler\_asymmetric

<a id="gdsfactory.components.couplers.coupler_asymmetric.coupler_asymmetric"></a>

#### coupler\_asymmetric

```python
@gf.cell_with_module_name
def coupler_asymmetric(gap: float = 0.234,
                       dy: Delta = 2.5,
                       dx: Delta = 10.0,
                       cross_section: CrossSectionSpec = "strip") -> Component
```

Bend coupled to straight waveguide.

**Arguments**:

- `gap` - um.
- `dy` - port to port vertical spacing.
- `dx` - bend length in x direction.
- `cross_section` - spec.
  
  .. code::
  
  dx
  |-----|
  _____ o2
  /         |
  _____/          |
  gap o1____________    |  dy
  o3

<a id="gdsfactory.components.couplers.coupler"></a>

# gdsfactory.components.couplers.coupler

<a id="gdsfactory.components.couplers.coupler.coupler_symmetric"></a>

#### coupler\_symmetric

```python
@gf.cell_with_module_name
def coupler_symmetric(bend: ComponentSpec = "bend_s",
                      gap: float = 0.234,
                      dy: Delta = 4.0,
                      dx: Delta = 10.0,
                      cross_section: CrossSectionSpec = "strip") -> Component
```

Two coupled straights with bends.

**Arguments**:

- `bend` - bend spec.
- `gap` - in um.
- `dy` - port to port vertical spacing.
- `dx` - bend length in x direction.
- `cross_section` - section.
  
  .. code::
  
  dx
  |-----|
  ___ o3
  /       |
  o2 _____/        |
  |
  o1 _____         |  dy
  \        |
  \___    |
  o4

<a id="gdsfactory.components.couplers.coupler.coupler_straight"></a>

#### coupler\_straight

```python
@gf.cell_with_module_name
def coupler_straight(length: float = 10.0,
                     gap: float = 0.27,
                     cross_section: CrossSectionSpec = "strip") -> Component
```

Coupler_straight with two parallel straights.

**Arguments**:

- `length` - of straight.
- `gap` - between straights.
- `cross_section` - specification (CrossSection, string or dict).
  
  .. code::
  
  o2──────▲─────────o3
  │gap
  o1──────▼─────────o4

<a id="gdsfactory.components.couplers.coupler.coupler"></a>

#### coupler

```python
@gf.cell_with_module_name
def coupler(gap: float = 0.236,
            length: float = 20.0,
            dy: Delta = 4.0,
            dx: Delta = 10.0,
            cross_section: CrossSectionSpec = "strip",
            allow_min_radius_violation: bool = False,
            bend: ComponentSpec = "bend_s") -> Component
```

Symmetric coupler.

**Arguments**:

- `gap` - between straights in um.
- `length` - of coupling region in um.
- `dy` - port to port vertical spacing in um.
- `dx` - length of bend in x direction in um.
- `cross_section` - spec (CrossSection, string or dict).
- `allow_min_radius_violation` - if True does not check for min bend radius.
- `bend` - input and output sbend components.
  
  .. code::
  
  dx                                 dx
  |------|                           |------|
  o2 ________                           ______o3
  \                         /           |
  \        length         /            |
  ======================= gap         | dy
  /                       \            |
  ________/                         \_______    |
  o1                                          o4
  
  coupler_straight  coupler_symmetric

<a id="gdsfactory.components.couplers.coupler_ring"></a>

# gdsfactory.components.couplers.coupler\_ring

<a id="gdsfactory.components.couplers.coupler_ring.coupler_ring"></a>

#### coupler\_ring

```python
@gf.cell_with_module_name
def coupler_ring(gap: float = 0.2,
                 radius: float = 5.0,
                 length_x: float = 4.0,
                 bend: ComponentSpec = "bend_euler",
                 straight: ComponentSpec = "straight",
                 cross_section: CrossSectionSpec = "strip",
                 cross_section_bend: CrossSectionSpec | None = None,
                 length_extension: float = 3) -> Component
```

Coupler for ring.

**Arguments**:

- `gap` - spacing between parallel coupled straight waveguides.
- `radius` - of the bends.
- `length_x` - length of the parallel coupled straight waveguides.
- `bend` - 90 degrees bend spec.
- `straight` - straight spec.
- `cross_section` - cross_section spec.
- `cross_section_bend` - optional bend cross_section spec.
- `length_extension` - for the ports.
  
  .. code::
  
  o2            o3
  |             |
  \           /
  \         /
  ---=========---
  o1    length_x   o4

<a id="gdsfactory.components.couplers.coupler_straight_asymmetric"></a>

# gdsfactory.components.couplers.coupler\_straight\_asymmetric

<a id="gdsfactory.components.couplers.coupler_straight_asymmetric.coupler_straight_asymmetric"></a>

#### coupler\_straight\_asymmetric

```python
@gf.cell_with_module_name
def coupler_straight_asymmetric(
        length: float = 10.0,
        gap: float = 0.27,
        width_top: float = 0.5,
        width_bot: float = 1,
        cross_section: CrossSectionSpec = "strip") -> Component
```

Coupler with two parallel straights of different widths.

**Arguments**:

- `length` - of straight.
- `gap` - between straights.
- `width_top` - of top straight.
- `width_bot` - of bottom straight.
- `cross_section` - cross_section spec.

<a id="gdsfactory.components.couplers.coupler_adiabatic"></a>

# gdsfactory.components.couplers.coupler\_adiabatic

<a id="gdsfactory.components.couplers.coupler_adiabatic.coupler_adiabatic"></a>

#### coupler\_adiabatic

```python
@gf.cell_with_module_name
def coupler_adiabatic(length1: float = 20.0,
                      length2: float = 50.0,
                      length3: float = 30.0,
                      wg_sep: float = 1.0,
                      input_wg_sep: float = 3.0,
                      output_wg_sep: float = 3.0,
                      dw: float = 0.1,
                      cross_section: CrossSectionSpec = "strip") -> Component
```

Returns 50/50 adiabatic coupler.

Design based on asymmetric adiabatic 3dB coupler designs, such as those.
- https://doi.org/10.1364/CLEO.2010.CThAA2,
- https://doi.org/10.1364/CLEO_SI.2017.SF1I.5
- https://doi.org/10.1364/CLEO_SI.2018.STh4B.4

input Bezier curves, with poles set to half of the x-length of the S-bend.
1. is the first half of input S-bend where input widths taper by +dw and -dw
2. is the second half of the S-bend straight with constant, unbalanced widths
3. is the region where the two asymmetric straights gradually come together
4. straights taper back to the original width at a fixed distance from one another
5. is the output S-bend straight.

**Arguments**:

- `length1` - region that gradually brings the two asymmetric straights together.
  In this region the straight widths gradually change to be different by `dw`.
- `length2` - coupling region, where asymmetric straights gradually
  become the same width.
- `length3` - output region where the two straights separate.
- `wg_sep` - Distance between center-to-center in the coupling region (Region 2).
- `input_wg_sep` - Separation of the two straights at the input, center-to-center.
- `output_wg_sep` - Separation of the two straights at the output, center-to-center.
- `dw` - Change in straight width.
  In Region 1, top arm tapers to width+dw/2.0, bottom taper to width-dw/2.0.
- `cross_section` - cross_section spec.

<a id="gdsfactory.components.couplers.coupler90"></a>

# gdsfactory.components.couplers.coupler90

<a id="gdsfactory.components.couplers.coupler90.coupler90"></a>

#### coupler90

```python
@gf.cell_with_module_name
def coupler90(gap: float = 0.2,
              radius: float | None = None,
              bend: ComponentSpec = "bend_euler",
              straight: ComponentSpec = "straight",
              cross_section: CrossSectionSpec = "strip",
              cross_section_bend: CrossSectionSpec | None = None) -> Component
```

Straight coupled to a bend.

**Arguments**:

- `gap` - um.
- `radius` - um.
- `straight` - for straight.
- `bend` - bend spec.
- `cross_section` - cross_section spec.
- `cross_section_bend` - optional bend cross_section spec.
  
  .. code::
  
  o3
  |
  /
  /
  o2_/
  o1___o4

<a id="gdsfactory.components.rings.disk"></a>

# gdsfactory.components.rings.disk

<a id="gdsfactory.components.rings.disk.disk"></a>

#### disk

```python
@gf.cell_with_module_name
def disk(radius: float = 10.0,
         gap: float = 0.2,
         wrap_angle_deg: float = 180.0,
         parity: int = 1,
         cross_section: CrossSectionSpec = "strip") -> Component
```

Disk Resonator.

**Arguments**:

- `radius` - disk resonator radius.
- `gap` - Distance between the bus straight and resonator.
- `wrap_angle_deg` - Angle in degrees between 0 and 180.
  determines how much the bus straight wraps along the resonator.
  0 corresponds to a straight bus straight.
  180 corresponds to a bus straight wrapped around half of the resonator.
- `parity` _1 or -1_ - 1, resonator left from bus straight, -1 resonator to the right.
- `cross_section` - cross_section spec.

<a id="gdsfactory.components.rings.disk.disk_heater"></a>

#### disk\_heater

```python
@gf.cell_with_module_name
def disk_heater(radius: float = 10.0,
                gap: float = 0.2,
                wrap_angle_deg: float = 180.0,
                parity: int = 1,
                cross_section: CrossSectionSpec = "strip",
                heater_layer: LayerSpec = "HEATER",
                via_stack: ComponentSpec = "via_stack_heater_mtop",
                heater_width: float = 5.0,
                heater_extent: float = 2.0,
                via_width: float = 10.0,
                port_orientation: AngleInDegrees | None = 90) -> Component
```

Disk Resonator with top metal heater.

**Arguments**:

- `radius` - disk resonator radius.
- `gap` - Distance between the bus straight and resonator.
- `wrap_angle_deg` - Angle in degrees between 0 and 180.
  determines how much the bus straight wraps along the resonator.
  0 corresponds to a straight bus straight.
  180 corresponds to a bus straight wrapped around half of the resonator.
- `parity` _1 or -1_ - 1, resonator left from bus straight, -1 resonator to the right.
- `cross_section` - cross_section spec.
- `heater_layer` - layer of the heater.
- `via_stack` - via stack component.
- `heater_width` - width of the heater.
- `heater_extent` - length of heater beyond disk.
- `via_width` - size of the square via at the end of the heater.
- `port_orientation` - in degrees.

<a id="gdsfactory.components.rings.ring_crow_couplers"></a>

# gdsfactory.components.rings.ring\_crow\_couplers

<a id="gdsfactory.components.rings.ring_crow_couplers.ring_crow_couplers"></a>

#### ring\_crow\_couplers

```python
@gf.cell_with_module_name
def ring_crow_couplers(
        radius: Sequence[float] = (10.0, ) * 3,
        bends: Sequence[ComponentSpec] = ("bend_circular", ) * 3,
        ring_cross_sections: Sequence[CrossSectionSpec] = ("strip", ) * 3,
        couplers: Sequence[ComponentSpec] = ("coupler", ) * 4) -> Component
```

Coupled ring resonators with coupler components between gaps.

**Arguments**:

- `radius` - for the bend and coupler.
- `bends` - bend specs.
- `ring_cross_sections` - cross_section for the ring.
- `couplers` - coupling component between rings and bus.
  
  .. code::
  
  --==ct==-- gap[N-1]   <------- couplers[N-1]
  |      |
  sl     sr ring[N-1]
  |      |
  --==cb==-- gap[N-2]   <------- couplers[N-2]
  
  .
  .
  .
  
  --==ct==--
  |      |
  sl     sr lengths_y[1], ring[1]
  |      |
  --==cb==-- gap[1]
  <------- couplers[1]
  --==ct==--
  |      |
  sl     sr lengths_y[0], ring[0]
  |      |
  --==cb==-- gap[0]      <------- couplers[0]
  
  length_x

<a id="gdsfactory.components.rings.ring_heater"></a>

# gdsfactory.components.rings.ring\_heater

<a id="gdsfactory.components.rings.ring_heater.ring_double_heater"></a>

#### ring\_double\_heater

```python
@gf.cell_with_module_name
def ring_double_heater(
        gap: float = 0.2,
        gap_top: float | None = None,
        gap_bot: float | None = None,
        radius: float = 10.0,
        length_x: float = 1.0,
        length_y: float = 0.01,
        coupler_ring: ComponentSpec = "coupler_ring",
        coupler_ring_top: ComponentSpec | None = None,
        straight: ComponentSpec = "straight",
        bend: ComponentSpec = "bend_euler",
        cross_section_heater: CrossSectionSpec = "heater_metal",
        cross_section_waveguide_heater: CrossSectionSpec = "strip_heater_metal",
        cross_section: CrossSectionSpec = "strip",
        via_stack: ComponentSpec = "via_stack_heater_mtop_mini",
        port_orientation: AngleInDegrees | None = None,
        via_stack_offset: Float2 = (1, 0),
        with_drop: bool = True) -> Component
```

Returns a double bus ring with heater on top.

two couplers (ct: top, cb: bottom)
connected with two vertical straights (sl: left, sr: right)

**Arguments**:

- `gap` - gap between for coupler.
- `gap_top` - gap for the top coupler. Defaults to gap.
- `gap_bot` - gap for the bottom coupler. Defaults to gap.
- `radius` - for the bend and coupler.
- `length_x` - ring coupler length.
- `length_y` - vertical straight length.
- `coupler_ring` - ring coupler spec.
- `coupler_ring_top` - ring coupler spec for coupler away from vias (defaults to coupler_ring)
- `straight` - straight spec.
- `bend` - bend spec.
- `cross_section_heater` - for heater.
- `cross_section_waveguide_heater` - for waveguide with heater.
- `cross_section` - for regular waveguide.
- `via_stack` - for heater to routing metal.
- `port_orientation` - for electrical ports to promote from via_stack.
- `via_stack_offset` - x,y offset for via_stack.
- `with_drop` - adds drop ports.
  
  .. code::
  
  o2──────▲─────────o3
  │gap_top
  xx──────▼─────────xxx
  xxx                   xxx
  xxx                       xxx
  xx                           xxx
  x                             xxx
  xx                              xx▲
  xx                              xx│length_y
  xx                              xx▼
  xx                             xx
  xx          length_x          x
  xx     ◄───────────────►    x
  xx                       xxx
  xx                   xxx
  xxx──────▲─────────xxx
  │gap
  o1──────▼─────────o4

<a id="gdsfactory.components.rings.ring_pn"></a>

# gdsfactory.components.rings.ring\_pn

<a id="gdsfactory.components.rings.ring_pn.ring_double_pn"></a>

#### ring\_double\_pn

```python
@gf.cell_with_module_name
def ring_double_pn(add_gap: float = 0.3,
                   drop_gap: float = 0.3,
                   radius: float = 5.0,
                   doping_angle: float = 85,
                   cross_section: CrossSectionFactory = rib,
                   pn_cross_section: CrossSectionFactory = cross_section_pn,
                   doped_heater: bool = True,
                   doped_heater_angle_buffer: float = 10,
                   doped_heater_layer: LayerSpec = "NPP",
                   doped_heater_width: float = 0.5,
                   doped_heater_waveguide_offset: float = 2.175,
                   heater_vias: ComponentSpec = _heater_vias,
                   with_drop: bool = True,
                   **kwargs: Any) -> gf.Component
```

Returns add-drop pn ring with optional doped heater.

**Arguments**:

- `add_gap` - gap to add waveguide. Bottom gap.
- `drop_gap` - gap to drop waveguide. Top gap.
- `radius` - for the bend and coupler.
- `doping_angle` - angle in degrees representing portion of ring that is doped.
- `length_x` - ring coupler length.
- `length_y` - vertical straight length.
- `cross_section` - cross_section spec for non-PN doped rib waveguide sections.
- `pn_cross_section` - cross section of pn junction.
- `doped_heater` - boolean for if we include doped heater or not.
- `doped_heater_angle_buffer` - angle in degrees buffering heater from pn junction.
- `doped_heater_layer` - doping layer for heater.
- `doped_heater_width` - width of doped heater.
- `doped_heater_waveguide_offset` - distance from the center of the ring waveguide to the center of the doped heater.
- `heater_vias` - components specifications for heater vias
- `with_drop` - boolean for if we include drop waveguide or not.
- `kwargs` - cross_section settings.

<a id="gdsfactory.components.rings.ring_pn.ring_single_pn"></a>

#### ring\_single\_pn

```python
@gf.cell_with_module_name
def ring_single_pn(gap: float = 0.3,
                   radius: float = 5.0,
                   doping_angle: float = 250,
                   cross_section: CrossSectionSpec = rib,
                   pn_cross_section: CrossSectionSpec = cross_section_pn,
                   doped_heater: bool = True,
                   doped_heater_angle_buffer: float = 10,
                   doped_heater_layer: LayerSpec = "NPP",
                   doped_heater_width: float = 0.5,
                   doped_heater_waveguide_offset: float = 1.175,
                   heater_vias: ComponentSpec = _heater_vias,
                   pn_vias: ComponentSpec = "via_stack_slab_m3",
                   pn_vias_width: float = 3) -> gf.Component
```

Returns single pn ring with optional doped heater.

**Arguments**:

- `gap` - gap between for coupler.
- `radius` - for the bend and coupler.
- `doping_angle` - angle in degrees representing portion of ring that is doped.
- `length_x` - ring coupler length.
- `length_y` - vertical straight length.
- `cross_section` - cross_section spec for non-PN doped rib waveguide sections.
- `pn_cross_section` - cross section of pn junction.
- `doped_heater` - boolean for if we include doped heater or not.
- `doped_heater_angle_buffer` - angle in degrees buffering heater from pn junction.
- `doped_heater_layer` - doping layer for heater.
- `doped_heater_width` - width of doped heater.
- `doped_heater_waveguide_offset` - distance from the center of the ring waveguide to the center of the doped heater.
- `heater_vias` - components specifications for heater vias.
- `pn_vias` - components specifications for pn vias.
- `pn_vias_width` - width of pn vias.

<a id="gdsfactory.components.rings.ring"></a>

# gdsfactory.components.rings.ring

<a id="gdsfactory.components.rings.ring.ring"></a>

#### ring

```python
@gf.cell_with_module_name
def ring(radius: float = 10.0,
         width: float = 0.5,
         angle_resolution: float = 2.5,
         layer: LayerSpec = "WG",
         angle: float = 360) -> Component
```

Returns a ring.

**Arguments**:

- `radius` - ring radius.
- `width` - of the ring.
- `angle_resolution` - number of points per degree.
- `layer` - layer.
- `angle` - angular coverage of the ring

<a id="gdsfactory.components.rings.ring_single_array"></a>

# gdsfactory.components.rings.ring\_single\_array

<a id="gdsfactory.components.rings.ring_single_array.ring_single_array"></a>

#### ring\_single\_array

```python
@gf.cell_with_module_name
def ring_single_array(ring: ComponentSpec = "ring_single",
                      spacing: float = 5.0,
                      list_of_dicts: tuple[dict[str, Any], ...] | None = None,
                      cross_section: CrossSectionSpec = "strip") -> Component
```

Ring of single bus connected with straights.

**Arguments**:

- `ring` - ring function.
- `spacing` - between rings.
- `list_of_dicts` - settings for each ring.
- `cross_section` - spec.
  
  .. code::
  
  ______               ______
  |      |             |      |
  |      |  length_y   |      |
  |      |             |      |
  --======-- spacing ----==gap==--
  
  length_x

<a id="gdsfactory.components.rings.ring_single_bend_coupler"></a>

# gdsfactory.components.rings.ring\_single\_bend\_coupler

<a id="gdsfactory.components.rings.ring_single_bend_coupler.coupler_bend"></a>

#### coupler\_bend

```python
@gf.cell_with_module_name
def coupler_bend(radius: float = 10.0,
                 coupler_gap: float = 0.2,
                 coupling_angle_coverage: float = 120.0,
                 cross_section_inner: CrossSectionSpec = "strip",
                 cross_section_outer: CrossSectionSpec = "strip",
                 bend: AnyComponentFactory = bend_circular_all_angle,
                 bend_output: ComponentSpec = "bend_euler") -> Component
```

Compact curved coupler with bezier escape.

TODO: fix for euler bends.

**Arguments**:

- `radius` - um.
- `coupler_gap` - um.
- `coupling_angle_coverage` - degrees.
- `cross_section_inner` - spec inner bend.
- `cross_section_outer` - spec outer bend.
- `bend` - for bend.
- `bend_output` - for bend.
  
  .. code::
  
  r   4
  |   |
  |  / ___3
  | / /
  2____/ /
  1_____/

<a id="gdsfactory.components.rings.ring_single_bend_coupler.coupler_ring_bend"></a>

#### coupler\_ring\_bend

```python
@gf.cell_with_module_name
def coupler_ring_bend(radius: float = 10.0,
                      coupler_gap: float = 0.2,
                      coupling_angle_coverage: float = 90.0,
                      length_x: float = 0.0,
                      cross_section_inner: CrossSectionSpec = "strip",
                      cross_section_outer: CrossSectionSpec = "strip",
                      bend: AnyComponentFactory = bend_circular_all_angle,
                      bend_output: ComponentSpec = "bend_euler",
                      straight: ComponentSpec = "straight") -> Component
```

Two back-to-back coupler_bend.

**Arguments**:

- `radius` - um.
- `coupler_gap` - um.
- `angle_inner` - of the inner bend, from beginning to end. Depending on the bend chosen, gap may not be preserved.
- `angle_outer` - of the outer bend, from beginning to end. Depending on the bend chosen, gap may not be preserved.
- `coupling_angle_coverage` - degrees.
- `length_x` - horizontal straight length.
- `cross_section_inner` - spec inner bend.
- `cross_section_outer` - spec outer bend.
- `bend` - for bend.
- `bend_output` - for bend.
- `straight` - for straight.

<a id="gdsfactory.components.rings.ring_single_bend_coupler.ring_single_bend_coupler"></a>

#### ring\_single\_bend\_coupler

```python
@gf.cell_with_module_name
def ring_single_bend_coupler(
        radius: float = 5.0,
        gap: float = 0.2,
        coupling_angle_coverage: float = 180.0,
        bend_all_angle: AnyComponentFactory = bend_circular_all_angle,
        bend: ComponentSpec = "bend_circular",
        bend_output: ComponentSpec = "bend_euler",
        length_x: float = 0.6,
        length_y: float = 0.6,
        cross_section_inner: CrossSectionSpec = "strip",
        cross_section_outer: CrossSectionSpec = "strip",
        **kwargs: Any) -> Component
```

Returns ring with curved coupler.

TODO: enable euler bends.

**Arguments**:

- `radius` - um.
- `gap` - um.
- `coupling_angle_coverage` - degrees.
- `angle_inner` - of the inner bend, from beginning to end. Depending on the bend chosen, gap may not be preserved.
- `angle_outer` - of the outer bend, from beginning to end. Depending on the bend chosen, gap may not be preserved.
- `bend_all_angle` - for bend.
- `bend` - for bend.
- `bend_output` - for bend.
- `length_x` - horizontal straight length.
- `length_y` - vertical straight length.
- `cross_section_inner` - spec inner bend.
- `cross_section_outer` - spec outer bend.
- `kwargs` - cross_section settings.

<a id="gdsfactory.components.rings"></a>

# gdsfactory.components.rings

<a id="gdsfactory.components.rings.ring_double_bend_coupler"></a>

# gdsfactory.components.rings.ring\_double\_bend\_coupler

<a id="gdsfactory.components.rings.ring_double_bend_coupler.ring_double_bend_coupler"></a>

#### ring\_double\_bend\_coupler

```python
@gf.cell_with_module_name
def ring_double_bend_coupler(
        radius: float = 5.0,
        gap: float = 0.2,
        coupling_angle_coverage: float = 70.0,
        bend: ComponentAllAngleFactory = bend_circular_all_angle,
        length_x: float = 0.6,
        length_y: float = 0.6,
        cross_section_inner: CrossSectionSpec = "strip",
        cross_section_outer: CrossSectionSpec = "strip") -> Component
```

Returns ring with double curved couplers.

**Arguments**:

- `radius` - um.
- `gap` - um.
- `coupling_angle_coverage` - degrees.
- `bend` - for bend.
- `length_x` - horizontal straight length.
- `length_y` - vertical straight length.
- `cross_section_inner` - spec inner bend.
- `cross_section_outer` - spec outer bend.

<a id="gdsfactory.components.rings.ring_double"></a>

# gdsfactory.components.rings.ring\_double

<a id="gdsfactory.components.rings.ring_double.ring_double"></a>

#### ring\_double

```python
@gf.cell_with_module_name
def ring_double(gap: float = 0.2,
                gap_top: float | None = None,
                gap_bot: float | None = None,
                radius: float = 10.0,
                length_x: float = 0.01,
                length_y: float = 0.01,
                bend: ComponentSpec = "bend_euler",
                straight: ComponentSpec = "straight",
                coupler_ring: ComponentSpec = "coupler_ring",
                coupler_ring_top: ComponentSpec | None = None,
                cross_section: CrossSectionSpec = "strip") -> Component
```

Returns a double bus ring.

two couplers (ct: top, cb: bottom)
connected with two vertical straights (sl: left, sr: right)

**Arguments**:

- `gap` - gap between for coupler.
- `gap_top` - gap for the top coupler. Defaults to gap.
- `gap_bot` - gap for the bottom coupler. Defaults to gap.
- `radius` - for the bend and coupler.
- `length_x` - ring coupler length.
- `length_y` - vertical straight length.
- `bend` - 90 degrees bend spec.
- `straight` - straight spec.
- `coupler_ring` - ring coupler spec.
- `coupler_ring_top` - top ring coupler spec. Defaults to coupler_ring.
- `cross_section` - cross_section spec.
  
  .. code::
  
  o2──────▲─────────o3
  │gap_top
  xx──────▼─────────xxx
  xxx                   xxx
  xxx                       xxx
  xx                           xxx
  x                             xxx
  xx                              xx▲
  xx                              xx│length_y
  xx                              xx▼
  xx                             xx
  xx          length_x          x
  xx     ◄───────────────►    x
  xx                       xxx
  xx                   xxx
  xxx──────▲─────────xxx
  │gap
  o1──────▼─────────o4

<a id="gdsfactory.components.rings.ring_single"></a>

# gdsfactory.components.rings.ring\_single

<a id="gdsfactory.components.rings.ring_single.ring_single"></a>

#### ring\_single

```python
@gf.cell_with_module_name
def ring_single(gap: float = 0.2,
                radius: float = 10.0,
                length_x: float = 4.0,
                length_y: float = 0.6,
                bend: ComponentSpec = "bend_euler",
                straight: ComponentSpec = "straight",
                coupler_ring: ComponentSpec = "coupler_ring",
                cross_section: CrossSectionSpec = "strip") -> gf.Component
```

Returns a single ring.

ring coupler (cb: bottom) connects to two vertical straights (sl: left, sr: right),
two bends (bl, br) and horizontal straight (wg: top)

**Arguments**:

- `gap` - gap between for coupler.
- `radius` - for the bend and coupler.
- `length_x` - ring coupler length.
- `length_y` - vertical straight length.
- `coupler_ring` - ring coupler spec.
- `bend` - 90 degrees bend spec.
- `straight` - straight spec.
- `coupler_ring` - ring coupler spec.
- `cross_section` - cross_section spec.
  
  .. code::
  
  xxxxxxxxxxxxx
  xxxxx           xxxx
  xxx                   xxx
  xxx                       xxx
  xx                           xxx
  x                             xxx
  xx                              xx▲
  xx                              xx│length_y
  xx                              xx▼
  xx                             xx
  xx          length_x          x
  xx     ◄───────────────►    x
  xx                       xxx
  xx                   xxx
  xxx──────▲─────────xxx
  │gap
  o1──────▼─────────o2

<a id="gdsfactory.components.rings.ring_crow"></a>

# gdsfactory.components.rings.ring\_crow

<a id="gdsfactory.components.rings.ring_crow.ring_crow"></a>

#### ring\_crow

```python
@gf.cell_with_module_name
def ring_crow(gaps: tuple[float, ...] = (0.2, 0.2, 0.2, 0.2),
              radius: tuple[float, ...] = (10.0, 10.0, 10.0),
              bends: tuple[ComponentSpec, ...] | None = None,
              ring_cross_sections: tuple[CrossSectionSpec,
                                         ...] = ("strip", "strip", "strip"),
              length_x: float = 0,
              lengths_y: tuple[float, ...] = (0, 0, 0),
              input_straight_cross_section: CrossSectionSpec | None = None,
              output_straight_cross_section: CrossSectionSpec | None = None,
              cross_section: CrossSectionSpec = "strip") -> Component
```

Coupled ring resonators.

**Arguments**:

- `gaps` - gap between rings.
- `radius` - for each ring.
- `bends` - bend spec for each ring.
- `ring_cross_sections` - cross_section spec for each ring.
- `length_x` - ring coupler length.
- `lengths_y` - vertical straight length.
- `input_straight_cross_section` - cross_section spec for input and output straight. Defaults to cross_section.
- `output_straight_cross_section` - cross_section spec for input and output straight. Defaults to cross_section.
- `cross_section` - cross_section spec for input and output straight.
  
  .. code::
  
  --==ct==-- gap[N-1]
  |      |
  sl     sr ring[N-1]
  |      |
  --==cb==-- gap[N-2]
  
  .
  .
  .
  
  --==ct==--
  |      |
  sl     sr lengths_y[1], ring[1]
  |      |
  --==cb==-- gap[1]
  
  --==ct==--
  |      |
  sl     sr lengths_y[0], ring[0]
  |      |
  --==cb==-- gap[0]
  
  length_x

<a id="gdsfactory.components.rings.ring_single_dut"></a>

# gdsfactory.components.rings.ring\_single\_dut

<a id="gdsfactory.components.rings.ring_single_dut.ring_single_dut"></a>

#### ring\_single\_dut

```python
@gf.cell_with_module_name
def ring_single_dut(component: ComponentSpec = "straight",
                    gap: float = 0.2,
                    length_x: float = 4,
                    length_y: float = 0,
                    radius: float = 5.0,
                    coupler: ComponentSpec = "coupler_ring",
                    bend: ComponentSpec = "bend_euler",
                    with_component: bool = True,
                    port_name: str = "o1",
                    **kwargs: Any) -> Component
```

Single bus ring made of two couplers (ct: top, cb: bottom) connected.

with two vertical straights (wyl: left, wyr: right) (Component Under Test) in
the middle to extract loss from quality factor.

**Arguments**:

- `component` - device under test.
- `gap` - in um.
- `length_x` - in um.
- `length_y` - in um.
- `radius` - in um.
- `coupler` - coupler function.
- `bend` - bend function.
- `with_component` - True adds component. False adds waveguide.
- `port_name` - for component input.
- `kwargs` - cross_section settings.
  

**Arguments**:

- `with_component` - if False changes component for just a straight.
  
  .. code::
  
  bl-wt-br
  |      | length_y
  wl     component
  |      |
  --==cb==-- gap
  
  length_x

<a id="gdsfactory.components.pcms.greek_cross"></a>

# gdsfactory.components.pcms.greek\_cross

Greek cross test structure.

<a id="gdsfactory.components.pcms.greek_cross.greek_cross"></a>

#### greek\_cross

```python
@gf.cell_with_module_name
def greek_cross(length: float = 30,
                layers: LayerSpecs = ("WG", "N"),
                widths: Floats = (2.0, 3.0),
                offsets: Floats | None = None,
                via_stack: ComponentSpec = "via_stack_npp_m1",
                layer_index: int = 0) -> gf.Component
```

Simple greek cross with via stacks at the endpoints.

Process control monitor for dopant sheet resistivity and linewidth variation.

**Arguments**:

- `length` - length of cross arms.
- `layers` - list of layers.
- `widths` - list of widths (same order as layers).
- `offsets` - how much to extend each layer beyond the cross length
  negative shorter, positive longer.
- `via_stack` - via component to attach to the cross.
- `layer_index` - index of the layer to connect the via_stack to.
  
  .. code::
  
  via_stack
  <------->
  _________       length          ________
  |       |<-------------------->|
  2x  |       |     |   ↓       |<-->|
  |       |======== width =======|
  |_______|<--> |   ↑       |<-->|________
  offset            offset
  
  

**References**:

  - Walton, Anthony J.. “MICROELECTRONIC TEST STRUCTURES.” (1999).
  - W. Versnel, Analysis of the Greek cross, a Van der Pauw structure with finite
  contacts, Solid-State Electronics, Volume 22, Issue 11, 1979, Pages 911-914,
  ISSN 0038-1101, https://doi.org/10.1016/0038-1101(79)90061-3.
  - S. Enderling et al., "Sheet resistance measurement of non-standard cleanroom
  materials using suspended Greek cross test structures," IEEE Transactions on
  Semiconductor Manufacturing, vol. 19, no. 1, pp. 2-9, Feb. 2006,
- `doi` - 10.1109/TSM.2005.863248.
  - https://download.tek.com/document/S530_VanDerPauwSheetRstnce.pdf

<a id="gdsfactory.components.pcms.greek_cross.greek_cross_with_pads"></a>

#### greek\_cross\_with\_pads

```python
@gf.cell_with_module_name
def greek_cross_with_pads(pad: ComponentSpec = "pad",
                          pad_pitch: float = 150.0,
                          greek_cross_component: ComponentSpec = "greek_cross",
                          pad_via: ComponentSpec = "via_stack_m1_mtop",
                          cross_section: CrossSectionSpec = metal1,
                          pad_port_name: str = "e4") -> gf.Component
```

Greek cross under 4 DC pads, ready to test.

**Arguments**:

- `pad` - component to use for probe pads.
- `pad_pitch` - spacing between pads.
- `greek_cross_component` - component to use for greek cross.
- `pad_via` - via to add to the pad.
- `cross_section` - cross-section for cross via to pad via wiring.
- `pad_port_name` - name of the port to connect to the greek cross.

<a id="gdsfactory.components.pcms.version_stamp"></a>

# gdsfactory.components.pcms.version\_stamp

<a id="gdsfactory.components.pcms.version_stamp.qrcode"></a>

#### qrcode

```python
@gf.cell_with_module_name
def qrcode(data: str = "mask01",
           psize: int = 1,
           layer: LayerSpec = "WG") -> Component
```

Returns QRCode.

**Arguments**:

- `data` - string to encode.
- `psize` - pixel size.
- `layer` - layer to use.

<a id="gdsfactory.components.pcms.version_stamp.version_stamp"></a>

#### version\_stamp

```python
@gf.cell_with_module_name
def version_stamp(labels: tuple[str, ...] = ("demo_label", ),
                  with_qr_code: bool = False,
                  layer: LayerSpec = "WG",
                  pixel_size: int = 1,
                  version: str | None = None,
                  text_size: int = 10) -> Component
```

Component with module version and date.

**Arguments**:

- `labels` - Iterable of labels.
- `with_qr_code` - Whether to add a QR code with the date.
- `layer` - Layer to use.
- `pixel_size` - Pixel size.
- `version` - Version string.
- `text_size` - Text size.

<a id="gdsfactory.components.pcms.cutback_component"></a>

# gdsfactory.components.pcms.cutback\_component

<a id="gdsfactory.components.pcms.cutback_component.cutback_component"></a>

#### cutback\_component

```python
@gf.cell_with_module_name
def cutback_component(component: ComponentSpec = "taper_0p5_to_3_l36",
                      cols: int = 4,
                      rows: int = 5,
                      port1: str = "o1",
                      port2: str = "o2",
                      bend180: ComponentSpec = "bend_euler180",
                      mirror: bool = False,
                      mirror1: bool = False,
                      mirror2: bool = False,
                      straight_length: float | None = None,
                      straight_length_pair: float | None = None,
                      straight: ComponentSpec = "straight",
                      cross_section: CrossSectionSpec = "strip",
                      **kwargs: Any) -> Component
```

Returns a daisy chain of components for measuring their loss.

Works only for components with 2 ports (input, output).

**Arguments**:

- `component` - for cutback.
- `cols` - number of columns.
- `rows` - number of rows.
- `port1` - name of first optical port.
- `port2` - name of second optical port.
- `bend180` - ubend.
- `mirror` - Flips component. Useful when 'o2' is the port that you want to route to.
- `mirror1` - mirrors first component.
- `mirror2` - mirrors second component.
- `straight_length` - length of the straight section between cutbacks.
- `straight_length_pair` - length of the straight section between each component pair.
- `cross_section` - specification (CrossSection, string or dict).
- `straight` - straight spec.
- `kwargs` - component settings.

<a id="gdsfactory.components.pcms.cdsem_all"></a>

# gdsfactory.components.pcms.cdsem\_all

CD SEM structures.

<a id="gdsfactory.components.pcms.cdsem_all.cdsem_all"></a>

#### cdsem\_all

```python
@gf.cell_with_module_name
def cdsem_all(widths: tuple[float, ...] = (0.4, 0.45, 0.5, 0.6, 0.8, 1.0),
              dense_lines_width: float | None = 0.3,
              dense_lines_width_difference: float = 20e-3,
              dense_lines_gap: float = 0.3,
              dense_lines_labels: tuple[str, ...] = ("DL", "DM", "DH"),
              straight: ComponentSpec = "straight",
              bend90: ComponentSpec | None = "bend_circular",
              cross_section: CrossSectionSpec = "strip",
              text: ComponentSpec = "text_rectangular",
              spacing: float = 5,
              cdsem_bend180: ComponentSpec = "cdsem_bend180",
              text_size: float = 1) -> Component
```

Column with all optical PCMs.

**Arguments**:

- `widths` - for straight lines.
- `dense_lines_width` - in um.
- `dense_lines_width_difference` - in um.
- `dense_lines_gap` - in um.
- `dense_lines_labels` - strings.
- `straight` - spec.
- `bend90` - spec.
- `cross_section` - spec.
- `text` - spec.
- `spacing` - from group to group.
- `cdsem_bend180` - spec.
- `text_size` - in um.

<a id="gdsfactory.components.pcms.cdsem_bend180"></a>

# gdsfactory.components.pcms.cdsem\_bend180

CD SEM structures.

<a id="gdsfactory.components.pcms.cdsem_bend180.cdsem_bend180"></a>

#### cdsem\_bend180

```python
@gf.cell_with_module_name
def cdsem_bend180(width: float = 0.5,
                  radius: float = 10.0,
                  wg_length: float | None = LINE_LENGTH,
                  straight: ComponentSpec = "straight",
                  bend90: ComponentSpec = "bend_circular",
                  cross_section: CrossSectionSpec = "strip",
                  text: ComponentSpec = "text_rectangular",
                  text_size: float = 1.0) -> Component
```

Returns CDSEM structures.

**Arguments**:

- `width` - of the line.
- `radius` - um.
- `wg_length` - in um.
- `straight` - spec.
- `bend90` - spec.
- `cross_section` - spec.
- `text` - spec.
- `text_size` - um.

<a id="gdsfactory.components.pcms.litho_ruler"></a>

# gdsfactory.components.pcms.litho\_ruler

<a id="gdsfactory.components.pcms.litho_ruler.litho_ruler"></a>

#### litho\_ruler

```python
@gf.cell_with_module_name
def litho_ruler(height: float = 2,
                width: float = 0.5,
                spacing: float = 2.0,
                scale: tuple[float, ...] = (3, 1, 1, 1, 1, 2, 1, 1, 1, 1),
                num_marks: int = 21,
                layer: LayerSpec = "WG") -> gf.Component
```

Ruler structure for lithographic measurement.

Includes marks of varying scales to allow for easy reading by eye.

based on phidl.geometry

**Arguments**:

- `height` - Height of the ruling marks in um.
- `width` - Width of the ruling marks in um.
- `spacing` - Center-to-center spacing of the ruling marks in um.
- `scale` - Height scale pattern of marks.
- `num_marks` - Total number of marks to generate.
- `layer` - Specific layer to put the ruler geometry on.

<a id="gdsfactory.components.pcms"></a>

# gdsfactory.components.pcms

<a id="gdsfactory.components.pcms.cdsem_straight_density"></a>

# gdsfactory.components.pcms.cdsem\_straight\_density

CD SEM structures.

<a id="gdsfactory.components.pcms.cdsem_straight_density.cdsem_straight_density"></a>

#### cdsem\_straight\_density

```python
@gf.cell_with_module_name
def cdsem_straight_density(widths: Floats = widths,
                           gaps: Floats = gaps,
                           length: float = 420.0,
                           label: str = "",
                           cross_section: CrossSectionSpec = "strip_no_ports",
                           text: ComponentSpec | None = "text_rectangular",
                           text_size: float = 1.0) -> Component
```

Returns sweep of dense straight lines.

**Arguments**:

- `widths` - list of widths.
- `gaps` - list of gaps.
- `length` - of the lines.
- `label` - defaults to widths[0] gaps[0].
- `cross_section` - spec.
- `text` - optional function for text.
- `text_size` - size of the text.

<a id="gdsfactory.components.pcms.cutback_splitter"></a>

# gdsfactory.components.pcms.cutback\_splitter

<a id="gdsfactory.components.pcms.cutback_splitter.cutback_splitter"></a>

#### cutback\_splitter

```python
@gf.cell_with_module_name
def cutback_splitter(component: ComponentSpec = "mmi1x2",
                     cols: int = 4,
                     rows: int = 5,
                     port1: str = "o1",
                     port2: str = "o2",
                     port3: str = "o3",
                     bend180: ComponentSpec = "bend_euler180",
                     mirror: bool = False,
                     straight: ComponentSpec = "straight",
                     straight_length: float | None = None,
                     cross_section: CrossSectionSpec = "strip",
                     **kwargs: Any) -> Component
```

Returns a daisy chain of splitters for measuring their loss.

**Arguments**:

- `component` - for cutback.
- `cols` - number of columns.
- `rows` - number of rows.
- `port1` - name of first optical port.
- `port2` - name of second optical port.
- `port3` - name of third optical port.
- `bend180` - ubend.
- `mirror` - Flips component. Useful when 'o2' is the port that you want to route to.
- `straight` - waveguide spec to connect both sides.
- `straight_length` - length of the straight section between cutbacks.
- `cross_section` - specification (CrossSection, string or dict).
- `kwargs` - cross_section settings.

<a id="gdsfactory.components.pcms.litho_calipers"></a>

# gdsfactory.components.pcms.litho\_calipers

<a id="gdsfactory.components.pcms.litho_calipers.litho_calipers"></a>

#### litho\_calipers

```python
@gf.cell_with_module_name
def litho_calipers(notch_size: Size = (2.0, 5.0),
                   notch_spacing: float = 2.0,
                   num_notches: int = 11,
                   offset_per_notch: float = 0.1,
                   row_spacing: float = 0.0,
                   layer1: LayerSpec = "WG",
                   layer2: LayerSpec = "SLAB150") -> Component
```

Vernier caliper structure to test lithography alignment.

Only the middle finger is aligned and the rest are offset.
adapted from phidl

**Arguments**:

- `notch_size` - [xwidth, yheight].
- `notch_spacing` - in um.
- `num_notches` - number of notches.
- `offset_per_notch` - in um.
- `row_spacing` - 0
- `layer1` - layer.
- `layer2` - layer.

<a id="gdsfactory.components.pcms.cdsem_straight"></a>

# gdsfactory.components.pcms.cdsem\_straight

CD SEM structures.

<a id="gdsfactory.components.pcms.cdsem_straight.cdsem_straight"></a>

#### cdsem\_straight

```python
@gf.cell_with_module_name
def cdsem_straight(widths: Sequence[float] = (0.4, 0.45, 0.5, 0.6, 0.8, 1.0),
                   length: float = LINE_LENGTH,
                   cross_section: CrossSectionSpec = "strip_no_ports",
                   text: ComponentSpec | None = "text_rectangular",
                   spacing: float = 7.0,
                   positions: Sequence[float | None] | None = None,
                   text_size: float = 1) -> Component
```

Returns straight waveguide lines width sweep.

**Arguments**:

- `widths` - for the sweep.
- `length` - for the line.
- `cross_section` - for the lines.
- `text` - optional text for labels.
- `spacing` - Optional center to center spacing.
- `positions` - Optional positions for the text labels.
- `text_size` - in um.

<a id="gdsfactory.components.pcms.cdsem_coupler"></a>

# gdsfactory.components.pcms.cdsem\_coupler

CD SEM structures.

<a id="gdsfactory.components.pcms.cdsem_coupler.cdsem_coupler"></a>

#### cdsem\_coupler

```python
@gf.cell_with_module_name
def cdsem_coupler(length: float = 420.0,
                  gaps: Sequence[float] = (0.15, 0.2, 0.25),
                  cross_section: CrossSectionSpec = "strip_no_ports",
                  text: ComponentSpec | None = "text_rectangular",
                  spacing: float = 7.0,
                  positions: Sequence[float | None] | None = None,
                  width: float | None = None,
                  text_size: float = 1.0) -> Component
```

Returns 2 coupled waveguides gap sweep.

**Arguments**:

- `length` - for the line.
- `gaps` - list of gaps for the sweep.
- `cross_section` - for the lines.
- `text` - optional text for labels.
- `spacing` - Optional center to center spacing.
- `positions` - Optional positions for the text labels.
- `width` - width of the waveguide. If None, it will use the width of the cross_section.
- `text_size` - size of the text.

<a id="gdsfactory.components.pcms.litho_steps"></a>

# gdsfactory.components.pcms.litho\_steps

<a id="gdsfactory.components.pcms.litho_steps.litho_steps"></a>

#### litho\_steps

```python
@gf.cell_with_module_name
def litho_steps(line_widths: tuple[float, ...] = (1.0, 2.0, 4.0, 8.0, 16.0),
                line_spacing: float = 10.0,
                height: float = 100.0,
                layer: LayerSpec = "WG") -> Component
```

Positive + negative tone linewidth test.

used for lithography resolution test patterning
based on phidl

**Arguments**:

- `line_widths` - in um.
- `line_spacing` - in um.
- `height` - in um.
- `layer` - Specific layer to put the ruler geometry on.

<a id="gdsfactory.components.pcms.resistance_meander"></a>

# gdsfactory.components.pcms.resistance\_meander

<a id="gdsfactory.components.pcms.resistance_meander.resistance_meander"></a>

#### resistance\_meander

```python
@gf.cell_with_module_name
def resistance_meander(pad_size: Size = (50.0, 50.0),
                       num_squares: int = 1000,
                       width: float = 1.0,
                       res_layer: LayerSpec = "MTOP",
                       pad_layer: LayerSpec = "MTOP") -> Component
```

Return meander to test resistance.

based on phidl.geometry

**Arguments**:

- `pad_size` - Size of the two matched impedance pads (microns).
- `num_squares` - Number of squares comprising the resonator wire.
- `width` - The width of the squares (microns).
- `res_layer` - resistance layer.
- `pad_layer` - pad layer.

<a id="gdsfactory.components.pcms.cutback_2x2"></a>

# gdsfactory.components.pcms.cutback\_2x2

<a id="gdsfactory.components.pcms.cutback_2x2.cutback_2x2"></a>

#### cutback\_2x2

```python
@gf.cell_with_module_name
def cutback_2x2(component: ComponentSpec = "mmi2x2",
                cols: int = 4,
                rows: int = 5,
                port1: str = "o1",
                port2: str = "o2",
                port3: str = "o3",
                port4: str = "o4",
                bend180: ComponentSpec = "bend_circular180",
                mirror: bool = False,
                straight_length: float | None = None,
                cross_section: CrossSectionSpec = "strip",
                straight: ComponentSpec = "straight") -> Component
```

Returns a daisy chain of splitters for measuring their loss.

**Arguments**:

- `component` - for cutback.
- `cols` - number of columns.
- `rows` - number of rows.
- `port1` - name of first optical port.
- `port2` - name of second optical port.
- `port3` - name of third optical port.
- `port4` - name of fourth optical port.
- `bend180` - ubend.
- `mirror` - Flips component. Useful when 'o2' is the port that you want to route to.
- `straight_length` - length of the straight section between cutbacks.
- `cross_section` - specification (CrossSection, string or dict).
- `straight` - straight spec.

<a id="gdsfactory.components.pcms.verniers"></a>

# gdsfactory.components.pcms.verniers

<a id="gdsfactory.components.pcms.verniers.verniers"></a>

#### verniers

```python
@gf.cell_with_module_name
def verniers(widths: Floats = (0.1, 0.2, 0.3, 0.4, 0.5),
             gap: float = 0.1,
             xsize: float = 100.0,
             layer_label: LayerSpec = "TEXT",
             straight: ComponentSpec = "straight",
             cross_section: CrossSectionSpec = "strip_no_ports",
             **kwargs: Any) -> Component
```

Returns a component with verniers.

**Arguments**:

- `widths` - list of widths.
- `gap` - gap between verniers.
- `xsize` - size of the component.
- `layer_label` - layer for the labels.
- `straight` - straight function.
- `cross_section` - cross_section spec.
- `kwargs` - straight settings.

<a id="gdsfactory.components.pcms.cutback_bend"></a>

# gdsfactory.components.pcms.cutback\_bend

<a id="gdsfactory.components.pcms.cutback_bend.cutback_bend"></a>

#### cutback\_bend

```python
@gf.cell_with_module_name
def cutback_bend(component: ComponentSpec = "bend_euler",
                 straight: ComponentSpec = "straight",
                 straight_length: float = 5.0,
                 rows: int = 6,
                 cols: int = 5,
                 **kwargs: Any) -> Component
```

We recommend using cutback_bend90 instead for a smaller footprint.

**Arguments**:

- `component` - bend spec.
- `straight` - straight spec.
- `straight_length` - in um.
- `rows` - number of rows.
- `cols` - number of cols.
- `kwargs` - cross_section settings.
  
  .. code::
  
  this is a column
  _
  _|
  _|
  
  _ this is a row

<a id="gdsfactory.components.pcms.cutback_bend.cutback_bend90"></a>

#### cutback\_bend90

```python
@gf.cell_with_module_name
def cutback_bend90(component: ComponentSpec = "bend_euler",
                   straight: ComponentSpec = "straight",
                   straight_length: float = 5.0,
                   rows: int = 6,
                   cols: int = 6,
                   spacing: int = 5,
                   **kwargs: Any) -> Component
```

Returns bend90 cutback.

**Arguments**:

- `component` - bend spec.
- `straight` - straight spec.
- `straight_length` - in um.
- `rows` - number of rows.
- `cols` - number of cols.
- `spacing` - in um.
- `kwargs` - cross_section settings.
  
  .. code::
  
  _
  |_| |

<a id="gdsfactory.components.pcms.cutback_bend.staircase"></a>

#### staircase

```python
@gf.cell_with_module_name
def staircase(component: ComponentSpec | Component = "bend_euler",
              straight: ComponentSpec = "straight",
              length_v: float = 5.0,
              length_h: float = 5.0,
              rows: int = 4,
              **kwargs: Any) -> Component
```

Returns staircase.

**Arguments**:

- `component` - bend spec.
- `straight` - straight spec.
- `length_v` - vertical length.
- `length_h` - vertical length.
- `rows` - number of rows.
- `cols` - number of cols.
- `kwargs` - cross_section settings.

<a id="gdsfactory.components.pcms.cutback_bend.cutback_bend180"></a>

#### cutback\_bend180

```python
@gf.cell_with_module_name
def cutback_bend180(component: ComponentSpec = "bend_euler180",
                    straight: ComponentSpec = "straight",
                    straight_length: float = 5.0,
                    rows: int = 6,
                    cols: int = 6,
                    spacing: float = 3.0,
                    **kwargs: Any) -> Component
```

Returns cutback to measure u bend loss.

**Arguments**:

- `component` - bend spec.
- `straight` - straight spec.
- `straight_length` - in um.
- `rows` - number of rows.
- `cols` - number of cols.
- `spacing` - in um.
- `kwargs` - cross_section settings.
  
  .. code::
  
  _
  _| |_  this is a row
  
  _ this is a column

<a id="gdsfactory.components.pcms.cutback_loss"></a>

# gdsfactory.components.pcms.cutback\_loss

<a id="gdsfactory.components.pcms.cutback_loss.cutback_loss"></a>

#### cutback\_loss

```python
def cutback_loss(component: ComponentSpec = "mmi1x2",
                 cutback: ComponentSpec = "cutback_component",
                 loss: Sequence[float] = (1.0, 2.0, 3.0),
                 loss_dB: float = 10e-3,
                 cols: int | None = 4,
                 rows: int | None = None,
                 **kwargs: Any) -> list[gf.Component]
```

Returns a list of component cutbacks.

**Arguments**:

- `component` - component factory.
- `cutback` - cutback function.
- `loss` - list of target loss in dB.
- `loss_dB` - loss per component.
- `cols` - number of columns.
- `rows` - number of rows.
  

**Arguments**:

- `port1` - name of first optical port.
- `port2` - name of second optical port.
- `bend180` - ubend.
- `mirror` - Flips component. Useful when 'o2' is the port that you want to route to.
- `mirror1` - mirrors first component.
- `mirror2` - mirrors second component.
- `straight_length` - length of the straight section between cutbacks.
- `straight_length_pair` - length of the straight section between each component pair.
- `cross_section` - specification (CrossSection, string or dict).
- `kwargs` - component settings.

<a id="gdsfactory.components.pcms.cutback_loss.cutback_loss_spirals"></a>

#### cutback\_loss\_spirals

```python
def cutback_loss_spirals(spiral: ComponentSpec = "spiral",
                         loss: Sequence[float] = _loss_default,
                         cross_section: CrossSectionSpec = "strip",
                         loss_dB_per_m: float = 300,
                         **kwargs: Any) -> list[gf.Component]
```

Returns a list of spirals.

**Arguments**:

- `spiral` - spiral factory.
- `loss` - list of target loss in dB.
- `cross_section` - strip or rib.
- `loss_dB_per_m` - loss per meter.
- `kwargs` - additional spiral arguments.

<a id="gdsfactory.components.pcms.resistance_sheet"></a>

# gdsfactory.components.pcms.resistance\_sheet

<a id="gdsfactory.components.pcms.resistance_sheet.resistance_sheet"></a>

#### resistance\_sheet

```python
@gf.cell_with_module_name
def resistance_sheet(width: float = 10.0,
                     layers: LayerSpecs = ("HEATER", ),
                     layer_offsets: Floats = (0, 0.2),
                     pad: ComponentSpec = "via_stack_heater_mtop",
                     pad_size: Size = (50.0, 50.0),
                     pad_pitch: float = 100.0,
                     ohms_per_square: float | None = None,
                     pad_port_name: str = "e4") -> Component
```

Returns Sheet resistance.

keeps connectivity for pads and first layer in layers

**Arguments**:

- `width` - in um.
- `layers` - for the middle part.
- `layer_offsets` - from edge, positive: over, negative: inclusion.
- `pad` - function to create a pad.
- `pad_size` - in um.
- `pad_pitch` - in um.
- `ohms_per_square` - optional sheet resistance to compute info.resistance.
- `pad_port_name` - port name for the pad.

<a id="gdsfactory.components.pcms.cavity"></a>

# gdsfactory.components.pcms.cavity

<a id="gdsfactory.components.pcms.cavity.cavity"></a>

#### cavity

```python
@gf.cell_with_module_name
def cavity(component: ComponentSpec = "dbr",
           coupler: ComponentSpec = "coupler",
           length: float = 0.1,
           gap: float = 0.2,
           **kwargs: Any) -> Component
```

Returns  cavity from a coupler and a mirror.

connects the W0 port of the mirror to E1 and W1 coupler ports
creating a resonant cavity

**Arguments**:

- `component` - mirror.
- `coupler` - coupler library.
- `length` - coupler length.
- `gap` - coupler gap.
- `kwargs` - coupler_settings.
  
  .. code::
  
  ml (mirror left)              mr (mirror right)
  |                               |
  |o1 - o2__             __o3 - o1|
  |         \           /         |
  \         /
  ---=========---
  o1  o1    length      o4    o2

<a id="gdsfactory.components.superconductors.optimal_hairpin"></a>

# gdsfactory.components.superconductors.optimal\_hairpin

<a id="gdsfactory.components.superconductors.optimal_hairpin.optimal_hairpin"></a>

#### optimal\_hairpin

```python
@gf.cell_with_module_name
def optimal_hairpin(width: float = 0.2,
                    pitch: float = 0.6,
                    length: float = 10,
                    turn_ratio: float = 4,
                    num_pts: int = 50,
                    layer: LayerSpec = (1, 0)) -> Component
```

Returns an optimally-rounded hairpin geometry, with a 180 degree turn.

based on phidl.geometry

**Arguments**:

- `width` - Width of the hairpin leads.
- `pitch` - Distance between the two hairpin leads. Must be greater than width.
- `length` - Length of the hairpin from the connectors to the opposite end of the curve.
- `turn_ratio` - int or float
  Specifies how much of the hairpin is dedicated to the 180 degree turn.
  A turn_ratio of 10 will result in 20% of the hairpin being comprised of the turn.
- `num_pts` - Number of points constituting the 180 degree turn.
- `layer` - Specific layer(s) to put polygon geometry on.
  

**Notes**:

  Hairpin pitch must be greater than width.
  
  Optimal structure from https://doi.org/10.1103/PhysRevB.84.174510
  Clem, J., & Berggren, K. (2011). Geometry-dependent critical currents in
  superconducting nanocircuits. Physical Review B, 84(17), 1-27.

<a id="gdsfactory.components.superconductors"></a>

# gdsfactory.components.superconductors

<a id="gdsfactory.components.superconductors.hline"></a>

# gdsfactory.components.superconductors.hline

<a id="gdsfactory.components.superconductors.hline.hline"></a>

#### hline

```python
@gf.cell_with_module_name
def hline(length: float = 10.0,
          width: float = 0.5,
          layer: LayerSpec = "WG",
          port_type: str = "optical") -> Component
```

Horizontal line straight, with ports on east and west sides.

<a id="gdsfactory.components.superconductors.optimal_step"></a>

# gdsfactory.components.superconductors.optimal\_step

<a id="gdsfactory.components.superconductors.optimal_step.optimal_step"></a>

#### optimal\_step

```python
@gf.cell_with_module_name
def optimal_step(
    start_width: float = 10,
    end_width: float = 22,
    num_pts: int = 50,
    width_tol: float = 1e-3,
    anticrowding_factor: float = 1.2,
    symmetric: bool = False,
    layer: LayerSpec = (1, 0)) -> Component
```

Returns an optimally-rounded step geometry.

**Arguments**:

- `start_width` - Width of the connector on the left end of the step.
- `end_width` - Width of the connector on the right end of the step.
- `num_pts` - number of points comprising the entire step geometry.
- `width_tol` - Point at which to terminate the calculation of the optimal step
- `anticrowding_factor` - Factor to reduce current crowding by elongating
  the structure and reducing the curvature
- `symmetric` - If True, adds a mirrored copy of the step across the x-axis to the
  geometry and adjusts the width of the ports.
- `layer` - layer spec to put polygon geometry on.
  
  based on phidl.geometry
  Optimal structure from https://doi.org/10.1103/PhysRevB.84.174510
  Clem, J., & Berggren, K. (2011). Geometry-dependent critical currents in
  superconducting nanocircuits. Physical Review B, 84(17), 1-27.

<a id="gdsfactory.components.superconductors.snspd"></a>

# gdsfactory.components.superconductors.snspd

<a id="gdsfactory.components.superconductors.snspd.snspd"></a>

#### snspd

```python
@gf.cell_with_module_name
def snspd(wire_width: float = 0.2,
          wire_pitch: float = 0.6,
          size: Size = (10, 8),
          num_squares: int | None = None,
          turn_ratio: float = 4,
          terminals_same_side: bool = False,
          layer: LayerSpec = (1, 0),
          port_type: str = "electrical") -> Component
```

Creates an optimally-rounded SNSPD.

**Arguments**:

- `wire_width` - Width of the wire.
- `wire_pitch` - Distance between two adjacent wires. Must be greater than `width`.
- `size` - Float2
  (width, height) of the rectangle formed by the outer boundary of the
  SNSPD.
- `num_squares` - int | None = None
  Total number of squares inside the SNSPD length.
- `turn_ratio` - float
  Specifies how much of the SNSPD width is dedicated to the 180 degree
  turn. A `turn_ratio` of 10 will result in 20% of the width being
  comprised of the turn.
- `terminals_same_side` - If True, both ports will be located on the same side of the SNSPD.
- `layer` - layer spec to put polygon geometry on.
- `port_type` - type of port to add to the component.

<a id="gdsfactory.components.superconductors.optimal_90deg"></a>

# gdsfactory.components.superconductors.optimal\_90deg

<a id="gdsfactory.components.superconductors.optimal_90deg.optimal_90deg"></a>

#### optimal\_90deg

```python
@gf.cell_with_module_name
def optimal_90deg(
    width: float = 100,
    num_pts: int = 15,
    length_adjust: float = 1,
    layer: LayerSpec = (1, 0)) -> Component
```

Returns optimally-rounded 90 degree bend that is sharp on the outer corner.

**Arguments**:

- `width` - Width of the ports on either side of the bend.
- `num_pts` - The number of points comprising the curved section of the bend.
- `length_adjust` - Adjusts the length of the non-curved portion of the bend.
- `layer` - Specific layer(s) to put polygon geometry on.
  

**Notes**:

  Optimal structure from https://doi.org/10.1103/PhysRevB.84.174510
  Clem, J., & Berggren, K. (2011). Geometry-dependent critical currents in
  superconducting nanocircuits. Physical Review B, 84(17), 1-27.

<a id="gdsfactory.components.tapers.ramp"></a>

# gdsfactory.components.tapers.ramp

<a id="gdsfactory.components.tapers.ramp.ramp"></a>

#### ramp

```python
@gf.cell_with_module_name
def ramp(length: float = 10.0,
         width1: float = 5.0,
         width2: float | None = 8.0,
         layer: LayerSpec = "WG") -> Component
```

Return a ramp component.

Based on phidl.

**Arguments**:

- `length` - Length of the ramp section.
- `width1` - Width of the start of the ramp section.
- `width2` - Width of the end of the ramp section (defaults to width1).
- `layer` - Specific layer to put polygon geometry on.

<a id="gdsfactory.components.tapers.taper_cross_section"></a>

# gdsfactory.components.tapers.taper\_cross\_section

<a id="gdsfactory.components.tapers.taper_cross_section.taper_cross_section"></a>

#### taper\_cross\_section

```python
@gf.cell_with_module_name
def taper_cross_section(cross_section1: CrossSectionSpec = "strip_rib_tip",
                        cross_section2: CrossSectionSpec = "rib2",
                        length: float = 10,
                        npoints: int = 100,
                        linear: bool = False,
                        width_type: str = "sine") -> Component
```

Returns taper transition between cross_section1 and cross_section2.

**Arguments**:

- `cross_section1` - start cross_section factory.
- `cross_section2` - end cross_section factory.
- `length` - transition length.
- `npoints` - number of points.
- `linear` - shape of the transition, sine when False.
- `width_type` - shape of the transition ONLY IF linear is False
  
  
  .. code::
  
  _____________________
  /
  _______/______________________
  /
  cross_section1  |        cross_section2
  ______\_______________________
  \
  \_____________________

<a id="gdsfactory.components.tapers.taper_adiabatic"></a>

# gdsfactory.components.tapers.taper\_adiabatic

<a id="gdsfactory.components.tapers.taper_adiabatic.neff_TE1550SOI_220nm"></a>

#### neff\_TE1550SOI\_220nm

```python
def neff_TE1550SOI_220nm(w: float) -> float
```

Returns the effective index of the fundamental TE mode for a 220nm-thick core with 3.45 index, fully clad with 1.44 index.

**Arguments**:

- `w` - width in um.
  

**Returns**:

  effective index.

<a id="gdsfactory.components.tapers.taper_adiabatic.taper_adiabatic"></a>

#### taper\_adiabatic

```python
@gf.cell_with_module_name
def taper_adiabatic(width1: float = 0.5,
                    width2: float = 5.0,
                    length: float = 0,
                    neff_w: Callable[[float], float] = neff_TE1550SOI_220nm,
                    alpha: float = 1,
                    wavelength: float = 1.55,
                    npoints: int = 200,
                    cross_section: CrossSectionSpec = "strip",
                    max_length: float = 200) -> gf.Component
```

Returns a straight adiabatic_taper from an effective index callable.

**Arguments**:

- `width1` - initial width.
- `width2` - final width.
- `length` - 0 uses the optimized length, and otherwise the optimal shape is compressed/stretched to the specified length.
- `neff_w` - a callable that returns the effective index as a function of width
  - By default, will use a compact model of neff(y) for fundamental 1550 nm TE mode of 220nm-thick core with 3.45 index, fully clad with 1.44 index. Many coefficients are needed to capture the behaviour.
- `alpha` - parameter that scales the rate of width change.
  - closer to 0 means longer and more adiabatic;
  - 1 is the intuitive limit beyond which higher order modes are excited;
  - [2] reports good performance up to 1.4 for fundamental TE in SOI (for multiple core thicknesses)
- `wavelength` - wavelength in um.
- `npoints` - number of points for sampling.
- `cross_section` - cross_section specification.
- `max_length` - maximum length for the taper.
  

**References**:

  [1] Burns, W. K., et al. "Optical waveguide parabolic coupling horns." Appl. Phys. Lett., vol. 30, no. 1, 1 Jan. 1977, pp. 28-30, doi:10.1063/1.89199.
  [2] Fu, Yunfei, et al. "Efficient adiabatic silicon-on-insulator waveguide taper." Photonics Res., vol. 2, no. 3, 1 June 2014, pp. A41-A44, doi:10.1364/PRJ.2.000A41.
- `npoints` - number of points for sampling

<a id="gdsfactory.components.tapers.taper_parabolic"></a>

# gdsfactory.components.tapers.taper\_parabolic

<a id="gdsfactory.components.tapers.taper_parabolic.taper_parabolic"></a>

#### taper\_parabolic

```python
@gf.cell_with_module_name
def taper_parabolic(length: float = 20,
                    width1: float = 0.5,
                    width2: float = 5.0,
                    exp: float = 0.5,
                    npoints: int = 100,
                    layer: LayerSpec = "WG") -> gf.Component
```

Returns a parabolic_taper.

**Arguments**:

- `length` - in um.
- `width1` - in um.
- `width2` - in um.
- `exp` - exponent.
- `npoints` - number of points.
- `layer` - layer spec.

<a id="gdsfactory.components.tapers"></a>

# gdsfactory.components.tapers

<a id="gdsfactory.components.tapers.taper"></a>

# gdsfactory.components.tapers.taper

<a id="gdsfactory.components.tapers.taper.taper"></a>

#### taper

```python
@gf.cell_with_module_name
def taper(length: float = 10.0,
          width1: float = 0.5,
          width2: float | None = None,
          layer: LayerSpec | None = None,
          port: Port | None = None,
          with_two_ports: bool = True,
          cross_section: CrossSectionSpec = "strip",
          port_names: tuple[str, str] = ("o1", "o2"),
          port_types: tuple[str, str] = ("optical", "optical"),
          with_bbox: bool = True) -> Component
```

Linear taper, which tapers only the main cross section section.

**Arguments**:

- `length` - taper length.
- `width1` - width of the west/left port.
- `width2` - width of the east/right port. Defaults to width1.
- `layer` - layer for the taper.
- `port` - can taper from a port instead of defining width1.
- `with_two_ports` - includes a second port.
  False for terminator and edge coupler fiber interface.
- `cross_section` - specification (CrossSection, string, CrossSectionFactory dict).
- `port_names` - input and output port names. Second name only used if with_two_ports.
- `port_types` - input and output port types. Second type only used if with_two_ports.
- `with_bbox` - box in bbox_layers and bbox_offsets to avoid DRC sharp edges.

<a id="gdsfactory.components.tapers.taper.taper_strip_to_ridge"></a>

#### taper\_strip\_to\_ridge

```python
@gf.cell_with_module_name
def taper_strip_to_ridge(length: float = 10.0,
                         width1: float = 0.5,
                         width2: float = 0.5,
                         w_slab1: float = 0.15,
                         w_slab2: float = 6.0,
                         layer_wg: LayerSpec = "WG",
                         layer_slab: LayerSpec = "SLAB90",
                         cross_section: CrossSectionSpec = "strip",
                         use_slab_port: bool = False) -> Component
```

Linear taper from strip to rib.

**Arguments**:

- `length` - taper length (um).
- `width1` - in um.
- `width2` - in um.
- `w_slab1` - slab width in um.
- `w_slab2` - slab width in um.
- `layer_wg` - for input waveguide.
- `layer_slab` - for output waveguide with slab.
- `cross_section` - for input waveguide.
- `use_slab_port` - if True adds a second port for the slab.
  
  .. code::
  
  __________________________
  /           |
  _______/____________|______________
  /             |
  width1     |w_slab1       | w_slab2  width2
  ______\_____________|______________
  \            |
  \__________________________

<a id="gdsfactory.components.tapers.taper.taper_strip_to_ridge_trenches"></a>

#### taper\_strip\_to\_ridge\_trenches

```python
@gf.cell_with_module_name
def taper_strip_to_ridge_trenches(length: float = 10.0,
                                  width: float = 0.5,
                                  slab_offset: float = 3.0,
                                  trench_width: float = 2.0,
                                  trench_layer: LayerSpec = "DEEP_ETCH",
                                  layer_wg: LayerSpec = "WG",
                                  trench_offset: float = 0.1) -> gf.Component
```

Defines taper using trenches to define the etch.

**Arguments**:

- `length` - in um.
- `width` - in um.
- `slab_offset` - in um.
- `trench_width` - in um.
- `trench_layer` - trench layer.
- `layer_wg` - waveguide layer.
- `trench_offset` - after waveguide in um.

<a id="gdsfactory.components.tapers.taper.taper_sc_nc"></a>

#### taper\_sc\_nc

```python
@gf.cell_with_module_name
def taper_sc_nc(width1: float = 0.5,
                width2: float = 1,
                length: float = 20,
                layer_wg: LayerSpec = "WG",
                layer_nitride: LayerSpec = "WGN",
                width_tip_nitride: float = 0.15,
                width_tip_silicon: float = 0.15,
                cross_section: CrossSectionSpec = "strip") -> Component
```

Taper from strip to nitride.

**Arguments**:

- `width1` - strip width.
- `width2` - nitride width.
- `length` - taper length.
- `layer_wg` - strip layer.
- `layer_nitride` - nitride layer.
- `width_tip_nitride` - tip width for nitride.
- `width_tip_silicon` - tip width for strip.
- `cross_section` - cross_section specification.

<a id="gdsfactory.components.tapers.taper.taper_nc_sc"></a>

#### taper\_nc\_sc

```python
@gf.cell_with_module_name
def taper_nc_sc(width1: float = 1,
                width2: float = 0.5,
                length: float = 20,
                layer_wg: LayerSpec = "WG",
                layer_nitride: LayerSpec = "WGN",
                width_tip_nitride: float = 0.15,
                width_tip_silicon: float = 0.15,
                cross_section: CrossSectionSpec = "strip") -> Component
```

Taper from nitride to strip.

**Arguments**:

- `width1` - nitride width.
- `width2` - silicon width.
- `length` - taper length.
- `layer_wg` - nitride layer.
- `layer_nitride` - strip layer.
- `width_tip_nitride` - tip width for nitride.
- `width_tip_silicon` - tip width for strip.
- `cross_section` - cross_section specification.

<a id="gdsfactory.components.tapers.taper_from_csv"></a>

# gdsfactory.components.tapers.taper\_from\_csv

Adiabatic tapers from CSV files.

<a id="gdsfactory.components.tapers.taper_from_csv.taper_from_csv"></a>

#### taper\_from\_csv

```python
@gf.cell_with_module_name
def taper_from_csv(filepath: Path = data / "taper_strip_0p5_3_36.csv",
                   cross_section: CrossSectionSpec = "strip") -> Component
```

Returns taper from CSV file.

**Arguments**:

- `filepath` - for CSV file.
- `cross_section` - specification (CrossSection, string, CrossSectionFactory dict).

<a id="gdsfactory.components"></a>

# gdsfactory.components

<a id="gdsfactory.components.bends.bend_euler"></a>

# gdsfactory.components.bends.bend\_euler

<a id="gdsfactory.components.bends.bend_euler.bend_euler_s"></a>

#### bend\_euler\_s

```python
@gf.cell_with_module_name
def bend_euler_s(radius: float | None = None,
                 p: float = 0.5,
                 with_arc_floorplan: bool = True,
                 npoints: int | None = None,
                 layer: LayerSpec | None = None,
                 width: float | None = None,
                 cross_section: CrossSectionSpec = "strip",
                 allow_min_radius_violation: bool = False,
                 port1: str = "o1",
                 port2: str = "o2") -> Component
```

Sbend made of 2 euler bends.

**Arguments**:

- `radius` - in um. Defaults to cross_section_radius.
- `p` - Proportion of the curve that is an Euler curve.
- `with_arc_floorplan` - If False: `radius` is the minimum radius of curvature.
- `npoints` - Number of points used per 360 degrees.
- `layer` - layer to use. Defaults to cross_section.layer.
- `width` - width to use. Defaults to cross_section.width.
- `cross_section` - specification (CrossSection, string, CrossSectionFactory dict).
- `allow_min_radius_violation` - if True allows radius to be smaller than cross_section radius.
- `port1` - input port name.
- `port2` - output port name.
  
  
  .. code::
  
  _____ o2
  /
  /
  /
  /
  |
  /
  /
  /
  o1_____/

<a id="gdsfactory.components.bends.bend_euler.bend_euler"></a>

#### bend\_euler

```python
@gf.cell_with_module_name
def bend_euler(radius: float | None = None,
               angle: float = 90.0,
               p: float = 0.5,
               with_arc_floorplan: bool = True,
               npoints: int | None = None,
               layer: LayerSpec | None = None,
               width: float | None = None,
               cross_section: CrossSectionSpec = "strip",
               allow_min_radius_violation: bool = False) -> Component
```

Regular degree euler bend.

**Arguments**:

- `radius` - in um. Defaults to cross_section_radius.
- `angle` - total angle of the curve.
- `p` - Proportion of the curve that is an Euler curve.
- `with_arc_floorplan` - if True the size of the bend will be adjusted to match an arc bend with the specified radius. If False: `radius` is the minimum radius of curvature.
- `npoints` - Number of points used per 360 degrees.
- `layer` - layer to use. Defaults to cross_section.layer.
- `width` - width to use. Defaults to cross_section.width.
- `cross_section` - specification (CrossSection, string, CrossSectionFactory dict).
- `allow_min_radius_violation` - if True allows radius to be smaller than cross_section radius.

<a id="gdsfactory.components.bends.bend_euler.bend_euler_all_angle"></a>

#### bend\_euler\_all\_angle

```python
@gf.vcell
def bend_euler_all_angle(
        radius: float | None = None,
        angle: float = 90.0,
        p: float = 0.5,
        with_arc_floorplan: bool = True,
        npoints: int | None = None,
        layer: gf.typings.LayerSpec | None = None,
        width: float | None = None,
        cross_section: CrossSectionSpec = "strip",
        allow_min_radius_violation: bool = False) -> ComponentAllAngle
```

Regular degree euler bend.

**Arguments**:

- `radius` - in um. Defaults to cross_section_radius.
- `angle` - total angle of the curve.
- `p` - Proportion of the curve that is an Euler curve.
- `with_arc_floorplan` - If False: `radius` is the minimum radius of curvature
- `npoints` - Number of points used per 360 degrees.
- `layer` - layer to use. Defaults to cross_section.layer.
- `width` - width to use. Defaults to cross_section.width.
- `cross_section` - specification (CrossSection, string, CrossSectionFactory dict).
- `allow_min_radius_violation` - if True allows radius to be smaller than cross_section radius.

<a id="gdsfactory.components.bends"></a>

# gdsfactory.components.bends

<a id="gdsfactory.components.bends.bend_circular"></a>

# gdsfactory.components.bends.bend\_circular

<a id="gdsfactory.components.bends.bend_circular.bend_circular"></a>

#### bend\_circular

```python
@gf.cell_with_module_name
def bend_circular(radius: float | None = None,
                  angle: float = 90.0,
                  npoints: int | None = None,
                  layer: gf.typings.LayerSpec | None = None,
                  width: float | None = None,
                  cross_section: CrossSectionSpec = "strip",
                  allow_min_radius_violation: bool = False) -> Component
```

Returns a radial arc.

**Arguments**:

- `radius` - in um. Defaults to cross_section_radius.
- `angle` - angle of arc (degrees).
- `npoints` - number of points.
- `layer` - layer to use. Defaults to cross_section.layer.
- `width` - width to use. Defaults to cross_section.width.
- `cross_section` - spec (CrossSection, string or dict).
- `allow_min_radius_violation` - if True allows radius to be smaller than cross_section radius.

<a id="gdsfactory.components.bends.bend_circular.bend_circular_all_angle"></a>

#### bend\_circular\_all\_angle

```python
@gf.vcell
def bend_circular_all_angle(
        radius: float | None = None,
        angle: float = 90.0,
        npoints: int | None = None,
        layer: gf.typings.LayerSpec | None = None,
        width: float | None = None,
        cross_section: CrossSectionSpec = "strip",
        allow_min_radius_violation: bool = False) -> ComponentAllAngle
```

Returns a radial arc.

**Arguments**:

- `radius` - in um. Defaults to cross_section_radius.
- `angle` - angle of arc (degrees).
- `npoints` - number of points.
- `layer` - layer to use. Defaults to cross_section.layer.
- `width` - width to use. Defaults to cross_section.width.
- `cross_section` - spec (CrossSection, string or dict).
- `allow_min_radius_violation` - if True allows radius to be smaller than cross_section radius.

<a id="gdsfactory.components.bends.bend_s"></a>

# gdsfactory.components.bends.bend\_s

<a id="gdsfactory.components.bends.bend_s.bezier_curve"></a>

#### bezier\_curve

```python
def bezier_curve(t: npt.NDArray[np.floating[Any]],
                 control_points: Coordinates) -> npt.NDArray[np.floating[Any]]
```

Returns bezier coordinates.

**Arguments**:

- `t` - 1D array of points varying between 0 and 1.
- `control_points` - for the bezier curve.

<a id="gdsfactory.components.bends.bend_s.bezier"></a>

#### bezier

```python
@gf.cell_with_module_name
def bezier(control_points: Coordinates = ((0.0, 0.0), (5.0, 0.0), (5.0, 1.8),
                                          (10.0, 1.8)),
           npoints: int = 201,
           with_manhattan_facing_angles: bool = True,
           start_angle: int | None = None,
           end_angle: int | None = None,
           cross_section: CrossSectionSpec = "strip",
           bend_radius_error_type: ErrorType | None = None,
           allow_min_radius_violation: bool = False,
           width: float | None = None) -> Component
```

Returns Bezier bend.

**Arguments**:

- `control_points` - list of points.
- `npoints` - number of points varying between 0 and 1.
- `with_manhattan_facing_angles` - bool.
- `start_angle` - optional start angle in deg.
- `end_angle` - optional end angle in deg.
- `cross_section` - spec.
- `bend_radius_error_type` - error type.
- `allow_min_radius_violation` - bool.
- `width` - width to use. Defaults to cross_section.width.

<a id="gdsfactory.components.bends.bend_s.find_min_curv_bezier_control_points"></a>

#### find\_min\_curv\_bezier\_control\_points

```python
def find_min_curv_bezier_control_points(start_point: Coordinate,
                                        end_point: Coordinate,
                                        start_angle: float,
                                        end_angle: float,
                                        npoints: int = 201,
                                        alpha: float = 0.05,
                                        nb_pts: int = 2) -> Coordinates
```

Returns bezier control points that minimize curvature.

**Arguments**:

- `start_point` - start point.
- `end_point` - end point.
- `start_angle` - start angle in deg.
- `end_angle` - end angle in deg.
- `npoints` - number of points varying between 0 and 1.
- `alpha` - weight for angle mismatch.
- `nb_pts` - number of control points.

<a id="gdsfactory.components.bends.bend_s.bend_s"></a>

#### bend\_s

```python
@gf.cell_with_module_name
def bend_s(size: Size = (11.0, 1.8),
           npoints: int = 99,
           cross_section: CrossSectionSpec = "strip",
           allow_min_radius_violation: bool = False,
           width: float | None = None) -> Component
```

Return S bend with bezier curve.

stores min_bend_radius property in self.info['min_bend_radius']
min_bend_radius depends on height and length

**Arguments**:

- `size` - in x and y direction.
- `npoints` - number of points.
- `cross_section` - spec.
- `allow_min_radius_violation` - bool.
- `width` - width to use. Defaults to cross_section.width.

<a id="gdsfactory.components.bends.bend_s.bend_s_offset"></a>

#### bend\_s\_offset

```python
@gf.cell_with_module_name
def bend_s_offset(offset: float = 40.0,
                  radius: float | None = 10.0,
                  cross_section: CrossSectionSpec = "strip",
                  width: float | None = None,
                  with_euler: bool = True) -> gf.Component
```

Return S bend made of two euler bends with a straight section.

stores min_bend_radius property in self.info['min_bend_radius']
min_bend_radius depends on height and length

**Arguments**:

- `offset` - in um.
- `radius` - in um. if None, uses cross_section_radius.
- `cross_section` - spec.
- `width` - width to use. Defaults to cross_section.width.
- `with_euler` - use euler bend instead of arc bend.

<a id="gdsfactory.components.bends.bend_s.get_min_sbend_size"></a>

#### get\_min\_sbend\_size

```python
def get_min_sbend_size(size: tuple[float | None, float | None] = (None, 10.0),
                       cross_section: CrossSectionSpec = "strip",
                       num_points: int = 100) -> float
```

Returns the minimum sbend size to comply with bend radius requirements.

**Arguments**:

- `size` - in x and y direction. One of them is None, which is the size we need to figure out.
- `cross_section` - spec.
- `num_points` - number of points to iterate over between max_size and 0.1 * max_size.

<a id="gdsfactory.components.bends.bend_circular_heater"></a>

# gdsfactory.components.bends.bend\_circular\_heater

<a id="gdsfactory.components.bends.bend_circular_heater.bend_circular_heater"></a>

#### bend\_circular\_heater

```python
@gf.cell_with_module_name
def bend_circular_heater(
        radius: float | None = None,
        angle: float = 90,
        npoints: int | None = None,
        heater_to_wg_distance: float = 1.2,
        heater_width: float = 0.5,
        layer_heater: LayerSpec = "HEATER",
        cross_section: CrossSectionSpec = "strip",
        allow_min_radius_violation: bool = False) -> Component
```

Creates an arc of arclength `theta` starting at angle `start_angle`.

**Arguments**:

- `radius` - in um. Defaults to cross_section.radius.
- `angle` - angle of arc (degrees).
- `npoints` - Number of points used per 360 degrees.
- `heater_to_wg_distance` - in um.
- `heater_width` - in um.
- `layer_heater` - for heater.
- `cross_section` - specification (CrossSection, string, CrossSectionFactory dict).
- `allow_min_radius_violation` - if True allows radius to be smaller than cross_section radius.

<a id="gdsfactory.components.texts"></a>

# gdsfactory.components.texts

<a id="gdsfactory.components.texts.text"></a>

# gdsfactory.components.texts.text

<a id="gdsfactory.components.texts.text.text"></a>

#### text

```python
@gf.cell_with_module_name
def text(text: str = "abcd",
         size: float = 10.0,
         position: Coordinate = (0, 0),
         justify: str = "left",
         layer: LayerSpec = "WG") -> Component
```

Text shapes.

**Arguments**:

- `text` - string.
- `size` - in um.
- `position` - x, y position.
- `justify` - left, right, center.
- `layer` - for the text.

<a id="gdsfactory.components.texts.text.text_lines"></a>

#### text\_lines

```python
@gf.cell_with_module_name
def text_lines(text: tuple[str, ...] = ("Chip", "01"),
               size: float = 0.4,
               layer: LayerSpec = "WG") -> Component
```

Returns a Component from a text lines.

**Arguments**:

- `text` - list of strings.
- `size` - text size.
- `layer` - text layer.

<a id="gdsfactory.components.texts.text.text_klayout"></a>

#### text\_klayout

```python
@gf.cell_with_module_name
def text_klayout(text: str = "a",
                 layer: LayerSpec = "WG",
                 layers: LayerSpecs | None = None,
                 bbox_layers: LayerSpecs | None = None) -> Component
```

Returns a text component.

**Arguments**:

- `text` - string.
- `layer` - text layer.
- `layers` - layers for the text.
- `bbox_layers` - layers for the text bounding box.

<a id="gdsfactory.components.texts.text_rectangular_font"></a>

# gdsfactory.components.texts.text\_rectangular\_font

<a id="gdsfactory.components.texts.text_rectangular_font.pixel_array"></a>

#### pixel\_array

```python
@gf.cell_with_module_name
def pixel_array(pixels: str = character_a,
                pixel_size: float = 10.0,
                layer: LayerSpec = "M1") -> Component
```

Returns a pixel component from a string representing the pixels.

**Arguments**:

- `pixels` - string representing the pixels
- `pixel_size` - width/height for each pixel
- `layer` - layer for each pixel

<a id="gdsfactory.components.texts.text_rectangular_font.rectangular_font"></a>

#### rectangular\_font

```python
@cache
def rectangular_font() -> dict[str, str]
```

Returns a rectangular font dict The keys of the dictionary are the.

characters The values are the pixel representation of the character.

<a id="gdsfactory.components.texts.text_rectangular"></a>

# gdsfactory.components.texts.text\_rectangular

<a id="gdsfactory.components.texts.text_rectangular.text_rectangular"></a>

#### text\_rectangular

```python
@gf.cell_with_module_name
def text_rectangular(
        text: str = "abcd",
        size: float = 10.0,
        position: tuple[float, float] = (0.0, 0.0),
        justify: str = "left",
        layer: LayerSpec | None = "WG",
        layers: LayerSpecs | None = None,
        font: Callable[..., dict[str, str]] = rectangular_font) -> Component
```

Pixel based font, guaranteed to be manhattan, without acute angles.

**Arguments**:

- `text` - string.
- `size` - pixel size.
- `position` - coordinate.
- `justify` - left, right or center.
- `layer` - for text.
- `layers` - optional for duplicating the text.
- `font` - function that returns dictionary of characters.

<a id="gdsfactory.components.texts.text_rectangular.text_rectangular_multi_layer"></a>

#### text\_rectangular\_multi\_layer

```python
@gf.cell_with_module_name
def text_rectangular_multi_layer(
        text: str = "abcd",
        layers: LayerSpecs = ("WG", "M1", "M2", "MTOP"),
        text_factory: ComponentSpec = text_rectangular,
        **kwargs: Any) -> Component
```

Returns rectangular text in different layers.

**Arguments**:

- `text` - string of text.
- `layers` - list of layers to replicate the text.
- `text_factory` - function to create the text Components.
- `kwargs` - keyword arguments for text_factory.
  

**Arguments**:

- `size` - pixel size.
- `position` - coordinate.
- `justify` - left, right or center.
- `font` - function that returns dictionary of characters.

<a id="gdsfactory.components.texts.text_freetype"></a>

# gdsfactory.components.texts.text\_freetype

<a id="gdsfactory.components.texts.text_freetype.text_freetype"></a>

#### text\_freetype

```python
@gf.cell_with_module_name
def text_freetype(text: str = "a",
                  size: int = 10,
                  justify: str = "left",
                  font: PathType = PATH.font_ocr,
                  layer: LayerSpec = "WG",
                  layers: LayerSpecs | None = None) -> Component
```

Returns text Component.

**Arguments**:

- `text` - string.
- `size` - in um.
- `justify` - left, right, center.
- `font` - Font face to use. Default DEPLOF does not require additional libraries,
  otherwise freetype load fonts. You can choose font by name
  (e.g. "Times New Roman"), or by file OTF or TTF filepath.
- `layer` - list of layers to use for the text.
- `layers` - list of layers to use for the text.

<a id="gdsfactory.components.mzis"></a>

# gdsfactory.components.mzis

<a id="gdsfactory.components.mzis.mzit"></a>

# gdsfactory.components.mzis.mzit

<a id="gdsfactory.components.mzis.mzit.mzit"></a>

#### mzit

```python
@gf.cell_with_module_name
def mzit(w0: float = 0.5,
         w1: float = 0.45,
         w2: float = 0.55,
         dy: Delta = 2.0,
         delta_length: float = 10.0,
         length: float = 1.0,
         coupler_length1: float = 5.0,
         coupler_length2: float = 10.0,
         coupler_gap1: float = 0.2,
         coupler_gap2: float = 0.3,
         taper: ComponentSpec = "taper",
         taper_length: float = 5.0,
         bend90: ComponentSpec = "bend_euler",
         straight: ComponentSpec = "straight",
         coupler1: ComponentSpec | None = "coupler",
         coupler2: ComponentSpec = "coupler",
         cross_section: str = "strip") -> Component
```

Mzi tolerant to fabrication variations.

based on Yufei Xing thesis
http://photonics.intec.ugent.be/publications/PhD.asp?ID=250

**Arguments**:

- `w0` - input waveguide width (um).
- `w1` - narrow waveguide width (um).
- `w2` - wide waveguide width (um).
- `dy` - port to port vertical spacing.
- `delta_length` - length difference between arms (um).
- `length` - shared length for w1 and w2.
- `coupler_length1` - length of coupler1.
- `coupler_length2` - length of coupler2.
- `coupler_gap1` - coupler1.
- `coupler_gap2` - coupler2.
- `taper` - taper spec.
- `taper_length` - from w0 to w1.
- `bend90` - bend spec.
- `straight` - spec.
- `coupler1` - coupler1 spec (optional).
- `coupler2` - coupler2 spec.
- `cross_section` - cross_section spec.
  
  .. code::
  
  cp1
  4   2 __                  __  3___w0_t2   _w2___
  \                /                      \
  \    length1   /                        |
  ============== gap1                    |
  /              \                        |
  __/                \_____w0___t1   _w1     |
  3   1                        4               \   |
  |   |
  2   2                                        |   |
  __                  __w0____t1____w1___/   |
  \                /                       |
  \    length2   /                        |
  ============== gap2                    |
  /               \                       |                       |
  __/                 \ E0_w0__t2 __w1______/
  1   1
  cp2

<a id="gdsfactory.components.mzis.mzit.mzit_lattice"></a>

#### mzit\_lattice

```python
@gf.cell_with_module_name
def mzit_lattice(coupler_lengths: Sequence[float] = (10.0, 20.0),
                 coupler_gaps: Sequence[float] = (0.2, 0.3),
                 delta_lengths: Sequence[float] = (10.0, ),
                 mzi: ComponentSpec = mzit) -> Component
```

Mzi fab tolerant lattice filter.

.. code::

                       cp1
       o4  o2 __                  __ o3___w0_t2   _w2___
                \                /                      \
                 \    length1   /                        |
                  ============== gap1                    |
                 /              \                        |
              __/                \_____w0___t1   _w1     |
       o3  o1                       o4               \   | .
                        ...                          |   | .
       o2  o2                    o3                  |   | .
              __                  _____w0___t1___w1__/   |
                \                /                       |
                 \    lengthN   /                        |
                  ============== gapN                    |
                 /               \                       |
              __/                 \_                     |
       o1  o1                      \___w0___t2___w1_____/
                       cpN       o4

<a id="gdsfactory.components.mzis.mzi_lattice"></a>

# gdsfactory.components.mzis.mzi\_lattice

<a id="gdsfactory.components.mzis.mzi_lattice.mzi_lattice"></a>

#### mzi\_lattice

```python
@gf.cell_with_module_name
def mzi_lattice(coupler_lengths: Sequence[float] = (10.0, 20.0),
                coupler_gaps: Sequence[float] = (0.2, 0.3),
                delta_lengths: Sequence[float] = (10.0, ),
                mzi: str = "mzi_coupler",
                splitter: str = "coupler",
                **kwargs: Any) -> Component
```

Mzi lattice filter.

**Arguments**:

- `coupler_lengths` - list of length for each coupler.
- `coupler_gaps` - list of coupler gaps.
- `delta_lengths` - list of length differences.
- `mzi` - function for the mzi.
- `splitter` - splitter function.
- `kwargs` - additional settings.
  

**Arguments**:

- `length_y` - vertical length for both and top arms.
- `length_x` - horizontal length.
- `bend` - 90 degrees bend library.
- `straight` - straight function.
- `straight_y` - straight for length_y and delta_length.
- `straight_x_top` - top straight for length_x.
- `straight_x_bot` - bottom straight for length_x.
- `cross_section` - for routing (sxtop/sxbot to combiner).
  
  .. code::
  
  ______             ______
  |      |           |      |
  |      |           |      |
  cp1==|      |===cp2=====|      |=== .... ===cp_last===
  |      |           |      |
  |      |           |      |
  DL1     |          DL2     |
  |      |           |      |
  |______|           |      |
  |______|

<a id="gdsfactory.components.mzis.mzi_lattice.mzi_lattice_mmi"></a>

#### mzi\_lattice\_mmi

```python
@gf.cell_with_module_name
def mzi_lattice_mmi(coupler_widths: tuple[float | None,
                                          float | None] = (None, None),
                    coupler_widths_tapers: tuple[float, ...] = (
                        1.0,
                        1.0,
                    ),
                    coupler_lengths_tapers: tuple[float, ...] = (
                        10.0,
                        10.0,
                    ),
                    coupler_lengths_mmis: tuple[float, ...] = (
                        5.5,
                        5.5,
                    ),
                    coupler_widths_mmis: tuple[float, ...] = (
                        2.5,
                        2.5,
                    ),
                    coupler_gaps_mmis: tuple[float, ...] = (
                        0.25,
                        0.25,
                    ),
                    taper_functions_mmis: tuple[str, ...] = (
                        "taper",
                        "taper",
                    ),
                    straight_functions_mmis: tuple[str, ...] = ("straight",
                                                                "straight"),
                    cross_sections_mmis: tuple[str, ...] = ("strip", "strip"),
                    delta_lengths: tuple[float, ...] = (10.0, ),
                    mzi: str = "mzi2x2_2x2",
                    splitter: str = "mmi2x2",
                    **kwargs: Any) -> Component
```

Mzi lattice filter, with MMI couplers.

**Arguments**:

- `coupler_widths` - (for each MMI coupler, list of) input and output straight width.
- `coupler_widths_tapers` - (for each MMI coupler, list of) interface between input straights and mmi region.
- `coupler_lengths_tapers` - (for each MMI coupler, list of) into the mmi region.
- `coupler_lengths_mmis` - (for each MMI coupler, list of) in x direction.
- `coupler_widths_mmis` - (for each MMI coupler, list of) in y direction.
- `coupler_gaps_mmis` - (for each MMI coupler, list of) (width_taper + gap between tapered wg)/2.
- `taper_functions_mmis` - (for each MMI coupler, list of) taper function.
- `straight_functions_mmis` - (for each MMI coupler, list of) straight function.
- `cross_sections_mmis` - (for each MMI coupler, list of) spec.
- `delta_lengths` - list of length differences.
- `mzi` - function for the mzi.
- `splitter` - splitter function.
- `kwargs` - additional settings.
  

**Arguments**:

- `length_y` - vertical length for both and top arms.
- `length_x` - horizontal length.
- `bend` - 90 degrees bend library.
- `straight` - straight function.
- `straight_y` - straight for length_y and delta_length.
- `straight_x_top` - top straight for length_x.
- `straight_x_bot` - bottom straight for length_x.
- `cross_section` - for routing (sxtop/sxbot to combiner).
  
  .. code::
  
  ______             ______
  |      |           |      |
  |      |           |      |
  cp1==|      |===cp2=====|      |=== .... ===cp_last===
  |      |           |      |
  |      |           |      |
  DL1     |          DL2     |
  |      |           |      |
  |______|           |      |
  |______|

<a id="gdsfactory.components.mzis.mzi_pads_center"></a>

# gdsfactory.components.mzis.mzi\_pads\_center

<a id="gdsfactory.components.mzis.mzi_pads_center.mzi_pads_center"></a>

#### mzi\_pads\_center

```python
@gf.cell_with_module_name
def mzi_pads_center(ps_top: ComponentSpec = "straight_heater_metal",
                    ps_bot: ComponentSpec = "straight_heater_metal",
                    mzi: ComponentSpec = "mzi",
                    pad: ComponentSpec = "pad_small",
                    length_x: float = 500,
                    length_y: float = 40,
                    mzi_sig_top: str | None = "top_r_e2",
                    mzi_gnd_top: str | None = "top_l_e2",
                    mzi_sig_bot: str | None = "bot_l_e2",
                    mzi_gnd_bot: str | None = "bot_r_e2",
                    pad_sig_bot: str = "e1_1_1",
                    pad_sig_top: str = "e3_1_3",
                    pad_gnd_bot: str = "e4_1_2",
                    pad_gnd_top: str = "e2_1_2",
                    delta_length: float = 40.0,
                    cross_section: CrossSectionSpec = "strip",
                    cross_section_metal: CrossSectionSpec = "metal_routing",
                    pad_pitch: float | str = "pad_pitch",
                    **kwargs: Any) -> gf.Component
```

Return Mzi phase shifter with pads in the middle.

GND is the middle pad and is shared between top and bottom phase shifters.

**Arguments**:

- `ps_top` - phase shifter top.
- `ps_bot` - phase shifter bottom.
- `mzi` - interferometer.
- `pad` - pad function.
- `length_x` - horizontal length.
- `length_y` - vertical length.
- `mzi_sig_top` - port name for top phase shifter signal. None if no connection.
- `mzi_gnd_top` - port name for top phase shifter GND. None if no connection.
- `mzi_sig_bot` - port name for top phase shifter signal. None if no connection.
- `mzi_gnd_bot` - port name for top phase shifter GND. None if no connection.
- `pad_sig_bot` - port name for top pad.
- `pad_sig_top` - port name for top pad.
- `pad_gnd_bot` - port name for top pad.
- `pad_gnd_top` - port name for top pad.
- `delta_length` - mzi length imbalance.
- `cross_section` - for the mzi.
- `cross_section_metal` - for routing metal.
- `pad_pitch` - pad pitch in um.
- `kwargs` - routing settings.

<a id="gdsfactory.components.mzis.mzi"></a>

# gdsfactory.components.mzis.mzi

<a id="gdsfactory.components.mzis.mzi.mzi"></a>

#### mzi

```python
@gf.cell_with_module_name
def mzi(delta_length: float = 10.0,
        length_y: float = 2.0,
        length_x: float | None = 0.1,
        bend: ComponentSpec = "bend_euler",
        straight: ComponentSpec = "straight",
        straight_y: ComponentSpec | None = None,
        straight_x_top: ComponentSpec | None = None,
        straight_x_bot: ComponentSpec | None = None,
        splitter: ComponentSpec = "mmi1x2",
        combiner: ComponentSpec | None = None,
        with_splitter: bool = True,
        port_e1_splitter: str = "o2",
        port_e0_splitter: str = "o3",
        port_e1_combiner: str = "o2",
        port_e0_combiner: str = "o3",
        port1: str = "o1",
        port2: str = "o2",
        nbends: int = 2,
        cross_section: CrossSectionSpec = "strip",
        cross_section_x_top: CrossSectionSpec | None = None,
        cross_section_x_bot: CrossSectionSpec | None = None,
        mirror_bot: bool = False,
        add_optical_ports_arms: bool = False,
        min_length: float = 10e-3,
        auto_rename_ports: bool = True) -> Component
```

Mzi.

**Arguments**:

- `delta_length` - bottom arm vertical extra length.
- `length_y` - vertical length for both and top arms.
- `length_x` - horizontal length. None uses to the straight_x_bot/top defaults.
- `bend` - 90 degrees bend library.
- `straight` - straight function.
- `straight_y` - straight for length_y and delta_length.
- `straight_x_top` - top straight for length_x.
- `straight_x_bot` - bottom straight for length_x.
- `splitter` - splitter function.
- `combiner` - combiner function.
- `with_splitter` - if False removes splitter.
- `port_e1_splitter` - east top splitter port.
- `port_e0_splitter` - east bot splitter port.
- `port_e1_combiner` - east top combiner port.
- `port_e0_combiner` - east bot combiner port.
- `port1` - input port name.
- `port2` - output port name.
- `nbends` - from straight top/bot to combiner (at least 2).
- `cross_section` - for routing (sxtop/sxbot to combiner).
- `cross_section_x_top` - optional top cross_section (defaults to cross_section).
- `cross_section_x_bot` - optional bottom cross_section (defaults to cross_section).
- `mirror_bot` - if true, mirrors the bottom arm.
- `add_optical_ports_arms` - add all other optical ports in the arms
  with top_ and bot_ prefix.
- `min_length` - minimum length for the straight.
- `auto_rename_ports` - if True, renames ports.
  
  .. code::
  
  b2______b3
  |  sxtop  |
  straight_y        |
  |         |
  b1        b4
  splitter==|         |==combiner
  b5        b8
  |         |
  straight_y        |
  |         |
  delta_length/2          |
  |         |
  b6__sxbot__b7
  Lx

<a id="gdsfactory.components.analog.interdigital_capacitor"></a>

# gdsfactory.components.analog.interdigital\_capacitor

<a id="gdsfactory.components.analog.interdigital_capacitor.interdigital_capacitor"></a>

#### interdigital\_capacitor

```python
@gf.cell_with_module_name
def interdigital_capacitor(fingers: int = 4,
                           finger_length: float | int = 20.0,
                           finger_gap: float | int = 2.0,
                           thickness: float | int = 5.0,
                           layer: LayerSpec = "WG") -> Component
```

Generates an interdigital capacitor with ports on both ends.

See for example Zhu et al., `Accurate circuit model of interdigital
capacitor and its application to design of new uasi-lumped miniaturized
filters with suppression of harmonic resonance`, doi: 10.1109/22.826833.

**Notes**:

  ``finger_length=0`` effectively provides a plate capacitor.
  

**Arguments**:

- `fingers` - total fingers of the capacitor.
- `finger_length` - length of the probing fingers.
- `finger_gap` - length of gap between the fingers.
- `thickness` - Thickness of fingers and section before the fingers.
- `layer` - spec.

<a id="gdsfactory.components.analog"></a>

# gdsfactory.components.analog

<a id="gdsfactory.components.containers.copy_layers"></a>

# gdsfactory.components.containers.copy\_layers

<a id="gdsfactory.components.containers.copy_layers.copy_layers"></a>

#### copy\_layers

```python
@gf.cell_with_module_name
def copy_layers(factory: ComponentSpec = "cross",
                layers: LayerSpecs = ((1, 0), (2, 0)),
                **kwargs: Any) -> Component
```

Returns a component with the geometry copied in different layers.

**Arguments**:

- `factory` - component spec.
- `layers` - iterable of layers.
- `kwargs` - keyword arguments.

<a id="gdsfactory.components.containers.extend_ports_list"></a>

# gdsfactory.components.containers.extend\_ports\_list

<a id="gdsfactory.components.containers.extend_ports_list.extend_ports_list"></a>

#### extend\_ports\_list

```python
@gf.cell(set_name=False)
def extend_ports_list(component_spec: ComponentSpec,
                      extension: ComponentSpec,
                      extension_port_name: str | None = None,
                      ignore_ports: Strs | None = None) -> Component
```

Returns a component with an extension attached to a list of ports.

**Arguments**:

- `component_spec` - component from which to get ports.
- `extension` - function for extension.
- `extension_port_name` - to connect extension.
- `ignore_ports` - list of port names to ignore.

<a id="gdsfactory.components.containers.add_trenches"></a>

# gdsfactory.components.containers.add\_trenches

<a id="gdsfactory.components.containers.add_trenches.add_trenches"></a>

#### add\_trenches

```python
@gf.cell_with_module_name
def add_trenches(component: ComponentSpec = "coupler",
                 layer_component: LayerSpec = "WG",
                 layer_trench: LayerSpec = "DEEP_ETCH",
                 width_trench: float = 2.0,
                 cross_section: CrossSectionSpec = "rib_with_trenches",
                 top: float | None = None,
                 bot: float | None = None,
                 right: float | None = 0,
                 left: float | None = 0,
                 **kwargs: Any) -> gf.Component
```

Return component with trenches.

**Arguments**:

- `component` - component to add to the trenches.
- `layer_component` - layer of the component.
- `layer_trench` - layer of the trenches.
- `width_trench` - width of the trenches.
- `cross_section` - spec (CrossSection, string or dict).
- `top` - width of the trench on the top. If None uses width_trench.
- `bot` - width of the trench on the bottom. If None uses width_trench.
- `right` - width of the trench on the right. If None uses width_trench.
- `left` - width of the trench on the left. If None uses width_trench.
- `kwargs` - component settings.

<a id="gdsfactory.components.containers.add_fiber_array_optical_south_electrical_north"></a>

# gdsfactory.components.containers.add\_fiber\_array\_optical\_south\_electrical\_north

<a id="gdsfactory.components.containers.add_fiber_array_optical_south_electrical_north.add_fiber_array_optical_south_electrical_north"></a>

#### add\_fiber\_array\_optical\_south\_electrical\_north

```python
@gf.cell_with_module_name
def add_fiber_array_optical_south_electrical_north(
        component: ComponentSpec,
        pad: ComponentSpec,
        grating_coupler: ComponentSpec,
        cross_section_metal: CrossSectionSpec,
        with_loopback: bool = True,
        pad_pitch: float = 100.0,
        pitch: float = 127.0,
        pad_gc_spacing: float = 250.0,
        electrical_port_names: list[str] | None = None,
        electrical_port_orientation: AngleInDegrees | None = 90,
        npads: int | None = None,
        port_types_grating_couplers: list[str] | None = None,
        **kwargs: Any) -> Component
```

Returns a fiber array with Optical gratings on South and Electrical pads on North.

This a test configuration for DC pads.

**Arguments**:

- `component` - component spec to add fiber and pads.
- `pad` - pad spec.
- `grating_coupler` - grating coupler function.
- `cross_section_metal` - metal cross section.
- `with_loopback` - whether to add a loopback port.
- `pad_pitch` - spacing between pads.
- `pitch` - spacing between grating couplers.
- `pad_gc_spacing` - spacing between pads and grating couplers.
- `electrical_port_names` - list of electrical port names. Defaults to all.
- `electrical_port_orientation` - orientation of electrical ports. Defaults to 90.
- `npads` - number of pads. Defaults to one per electrical_port_names.
- `port_types_grating_couplers` - port types for grating couplers. Defaults to vertical TE, TM, and dual.
- `kwargs` - additional arguments.
  

**Arguments**:

- `layer_label` - layer for settings label.
- `measurement` - measurement name.
- `measurement_settings` - measurement settings.
- `analysis` - analysis name.
- `doe` - Design of Experiment.
- `anchor` - anchor point for the label. Defaults to south-west "sw".             Valid options are: "n", "s", "e", "w", "ne", "nw", "se", "sw", "c".
- `gc_port_name` - grating coupler input port name.
- `gc_port_labels` - grating coupler list of labels.
- `component_name` - optional for the label.
- `select_ports` - function to select ports.
- `cross_section` - cross_section function.
- `get_input_labels_function` - function to get input labels. None skips labels.
- `layer_label` - optional layer for grating coupler label.
- `bend` - bend spec.
- `straight` - straight spec.
- `taper` - taper spec.
- `get_input_label_text_loopback_function` - function to get input label test.
- `get_input_label_text_function` - for labels.
- `fanout_length` - if None, automatic calculation of fanout length.
- `max_y0_optical` - in um.
- `with_loopback` - True, adds loopback structures.
- `straight_separation` - from edge to edge.
- `list_port_labels` - None, adds TM labels to port indices in this list.
- `connected_port_list_ids` - names of ports only for type 0 optical routing.
- `nb_optical_ports_lines` - number of grating coupler lines.
- `force_manhattan` - False
- `excluded_ports` - list of port names to exclude when adding gratings.
- `grating_indices` - list of grating coupler indices.
- `routing_straight` - function to route.
- `routing_method` - route_single.
- `gc_rotation` - fiber coupler rotation in degrees. Defaults to -90.
- `input_port_indexes` - to connect.

<a id="gdsfactory.components.containers.array_component"></a>

# gdsfactory.components.containers.array\_component

<a id="gdsfactory.components.containers.array_component.array"></a>

#### array

```python
@gf.cell_with_module_name
def array(component: ComponentSpec = "pad",
          columns: int = 6,
          rows: int = 1,
          column_pitch: float = 150,
          row_pitch: float = 150,
          add_ports: bool = True,
          size: Size | None = None,
          centered: bool = False,
          post_process: PostProcesses | None = None,
          auto_rename_ports: bool = False) -> Component
```

Returns an array of components.

**Arguments**:

- `component` - to replicate.
- `columns` - in x.
- `rows` - in y.
- `column_pitch` - pitch between columns.
- `row_pitch` - pitch between rows.
- `auto_rename_ports` - True to auto rename ports.
- `add_ports` - add ports from component into the array.
- `size` - Optional x, y size. Overrides columns and rows.
- `centered` - center the array around the origin.
- `post_process` - function to apply to the array after creation.
  

**Raises**:

- `ValueError` - If columns > 1 and spacing[0] = 0.
- `ValueError` - If rows > 1 and spacing[1] = 0.
  
  .. code::
  
  2 rows x 4 columns
  
  column_pitch
  <---------->
  ___        ___       ___        ___
  |   |      |   |     |   |      |   |
  |___|      |___|     |___|      |___|
  
  ___        ___       ___        ___
  |   |      |   |     |   |      |   |
  |___|      |___|     |___|      |___|

<a id="gdsfactory.components.containers"></a>

# gdsfactory.components.containers

<a id="gdsfactory.components.containers.splitter_chain"></a>

# gdsfactory.components.containers.splitter\_chain

<a id="gdsfactory.components.containers.splitter_chain.splitter_chain"></a>

#### splitter\_chain

```python
@gf.cell_with_module_name
def splitter_chain(splitter: ComponentSpec = "mmi1x2",
                   columns: int = 3,
                   bend: ComponentSpec = "bend_s") -> Component
```

Chain of splitters.

**Arguments**:

- `splitter` - splitter to chain.
- `columns` - number of splitters to chain.
- `bend` - bend to connect splitters.
  
  .. code::
  
  __o5
  __|
  __|  |__o4
  o1 _|  |__o3
  |__o2
  
  __o2
  o1 _|
  |__o3

<a id="gdsfactory.components.containers.extension"></a>

# gdsfactory.components.containers.extension

<a id="gdsfactory.components.containers.extension.move_polar_rad_copy"></a>

#### move\_polar\_rad\_copy

```python
def move_polar_rad_copy(pos: Coordinate, angle: float,
                        length: float) -> npt.NDArray[np.floating[Any]]
```

Returns the points of a position (pos) with angle, shifted by length.

**Arguments**:

- `pos` - position.
- `angle` - in radians.
- `length` - extension length in um.

<a id="gdsfactory.components.containers.extension.extend_ports"></a>

#### extend\_ports

```python
@gf.cell_with_module_name
def extend_ports(component: ComponentSpec = "mmi1x2",
                 port_names: PortNames | None = None,
                 length: float = 5.0,
                 extension: ComponentSpec | None = None,
                 port1: str | None = None,
                 port2: str | None = None,
                 port_type: str = "optical",
                 centered: bool = False,
                 cross_section: CrossSectionSpec | None = None,
                 extension_port_names: list[str] | None = None,
                 allow_width_mismatch: bool = False,
                 auto_taper: bool = True,
                 **kwargs: Any) -> Component
```

Returns a new component with some ports extended.

You can define extension Spec
defaults to port cross_section of each port to extend.

**Arguments**:

- `component` - component to extend ports.
- `port_names` - list of ports names to extend, if None it extends all ports.
- `length` - extension length.
- `extension` - function to extend ports (defaults to a straight).
- `port1` - extension input port name.
- `port2` - extension output port name.
- `port_type` - type of the ports to extend.
- `centered` - if True centers rectangle at (0, 0).
- `cross_section` - extension cross_section, defaults to port cross_section
  if port has no cross_section it creates one using width and layer.
- `extension_port_names` - extension port names add to the new component.
- `allow_width_mismatch` - allow width mismatches.
- `auto_taper` - if True adds automatic tapers.
- `kwargs` - cross_section settings.
  

**Arguments**:

- `layer` - port GDS layer.
- `prefix` - port name prefix.
- `orientation` - in degrees.
- `width` - port width.
- `layers_excluded` - List of layers to exclude.
- `port_type` - optical, electrical, ....
- `clockwise` - if True, sort ports clockwise, False: counter-clockwise.

<a id="gdsfactory.components.containers.pack_doe"></a>

# gdsfactory.components.containers.pack\_doe

<a id="gdsfactory.components.containers.pack_doe.generate_doe"></a>

#### generate\_doe

```python
def generate_doe(
    doe: ComponentSpec,
    settings: Mapping[str, Sequence[Any]],
    do_permutations: bool = False,
    function: CellSpec | None = None
) -> tuple[list[Component], list[dict[str, Any]]]
```

Generates a component DOE (Design of Experiment).

which can then be packed, or used elsewhere.

**Arguments**:

- `doe` - function to return Components.
- `settings` - component settings.
- `do_permutations` - for each setting.
- `function` - for the component (add padding, grating couplers ...)

<a id="gdsfactory.components.containers.pack_doe.pack_doe"></a>

#### pack\_doe

```python
@gf.cell_with_module_name
def pack_doe(doe: ComponentSpec,
             settings: Mapping[str, Sequence[kf.typings.MetaData]],
             do_permutations: bool = False,
             function: CellSpec | None = None,
             **kwargs: Any) -> Component
```

Packs a component DOE (Design of Experiment) using pack.

**Arguments**:

- `doe` - function to return Components.
- `settings` - component settings.
- `do_permutations` - for each setting.
- `function` - to apply (add padding, grating couplers).
- `kwargs` - for pack.
  

**Arguments**:

- `spacing` - Minimum distance between adjacent shapes.
- `aspect_ratio` - (width, height) ratio of the rectangular bin.
- `max_size` - Limits the size into which the shapes will be packed.
- `sort_by_area` - Pre-sorts the shapes by area.
- `density` - Values closer to 1 pack tighter but require more computation.
- `precision` - Desired precision for rounding vertex coordinates.
- `text` - Optional function to add text labels.
- `text_prefix` - for labels. For example. 'A' for 'A1', 'A2'...
- `text_offsets` - relative to component size info anchor. Defaults to center.
- `text_anchors` - relative to component (ce cw nc ne nw sc se sw center cc).
- `name_prefix` - for each packed component (avoids the Unnamed cells warning).
  Note that the suffix contains a uuid so the name will not be deterministic.
- `rotation` - for each component in degrees.
- `h_mirror` - horizontal mirror in y axis (x, 1) (1, 0). This is the most common.
- `v_mirror` - vertical mirror using x axis (1, y) (0, y).

<a id="gdsfactory.components.containers.pack_doe.pack_doe_grid"></a>

#### pack\_doe\_grid

```python
@gf.cell_with_module_name
def pack_doe_grid(doe: ComponentSpec,
                  settings: Mapping[str, Sequence[kf.typings.MetaData]],
                  do_permutations: bool = False,
                  function: CellSpec | None = None,
                  with_text: bool = False,
                  **kwargs: Any) -> Component
```

Packs a component DOE (Design of Experiment) using grid.

**Arguments**:

- `doe` - function to return Components.
- `settings` - component settings.
- `do_permutations` - for each setting.
- `function` - to apply to component (add padding, grating couplers).
- `with_text` - includes text label.
- `kwargs` - for grid.
  

**Arguments**:

- `spacing` - between adjacent elements on the grid, can be a tuple for
  different distances in height and width.
- `separation` - If True, guarantees elements are separated with fixed spacing
  if False, elements are spaced evenly along a grid.
- `shape` - x, y shape of the grid (see np.reshape).
  If no shape and the list is 1D, if np.reshape were run with (1, -1).
- `align_x` - {'x', 'xmin', 'xmax'} for x (column) alignment along.
- `align_y` - {'y', 'ymin', 'ymax'} for y (row) alignment along.
- `edge_x` - {'x', 'xmin', 'xmax'} for x (column) (ignored if separation = True).
- `edge_y` - {'y', 'ymin', 'ymax'} for y (row) (ignored if separation = True).
- `rotation` - for each component in degrees.
- `h_mirror` - horizontal mirror y axis (x, 1) (1, 0). most common mirror.
- `v_mirror` - vertical mirror using x axis (1, y) (0, y).

<a id="gdsfactory.components.containers.component_sequence"></a>

# gdsfactory.components.containers.component\_sequence

<a id="gdsfactory.components.containers.component_sequence.SequenceGenerator"></a>

## SequenceGenerator Objects

```python
class SequenceGenerator()
```

<a id="gdsfactory.components.containers.component_sequence.SequenceGenerator.__init__"></a>

#### \_\_init\_\_

```python
def __init__(start_sequence: str = "IL",
             repeated_sequence: str = "ASASBSBS",
             end_sequence: str = "LO") -> None
```

Sequence generator.

Main use case: any type of cascade of components with repeating patterns
such as serpentine, cutbacks etc...
Component sequences have two ports by default.
it adds aliases for the components forming the sequence.
They use the component symbol with a suffix index starting from 1,
so you may access the ports from any subcomponent.

Usually we can break these components in 3 parts:
- there is a starting pattern with input and possibly some special
connections
- then a repeating pattern
- An ending pattern with an output

Example of symbol meaning

A: bend connected with input W0
B: bend connected with input N0
I: taper with input '1'
O: taper with input '2'
S: short straight waveguide
L: long straight waveguide

**Arguments**:

- `start_sequence` - starting sequence.
- `end_sequence` - ending sequence.
- `repeated_sequence` - repeating sequence.

<a id="gdsfactory.components.containers.component_sequence.parse_component_name"></a>

#### parse\_component\_name

```python
def parse_component_name(name: str) -> tuple[str, bool]
```

If the component name has more than one character and starts with "!".

then we need to flip along the axis given by the input port angle.

<a id="gdsfactory.components.containers.component_sequence.component_sequence"></a>

#### component\_sequence

```python
def component_sequence(sequence: str,
                       symbol_to_component: dict[str, tuple[Component, str,
                                                            str]],
                       ports_map: dict[str, tuple[str, str]] | None = None,
                       port_name1: str = "o1",
                       port_name2: str = "o2",
                       start_orientation: AngleInDegrees = 0.0) -> Component
```

Returns component from ASCII sequence.

if you prefix a symbol with ! it mirrors the component

**Arguments**:

- `sequence` - a string or a list of symbols.
- `symbol_to_component` - maps symbols to (component, input, output).
- `ports_map` - (optional) extra port mapping using the convention.
- `{port_name` - (alias_name, port_name)}
- `port_name1` - input port_name.
- `port_name2` - output port_name.
- `start_orientation` - in degrees.
  

**Returns**:

- `component` - containing the sequence of sub-components
  instantiated and connected together in the sequence order.
  
  .. plot::
  :include-source:
  
  import gdsfactory as gf
  
  bend180 = gf.components.bend_circular180()
  wg_pin = gf.components.straight_pin(length=40)
  wg = gf.components.straight()
  
  # Define a map between symbols and (component, input port, output port)
  symbol_to_component = {
- `"A"` - (bend180, 'o1', 'o2'),
- `"B"` - (bend180, 'o2', 'o1'),
- `"H"` - (wg_pin, 'o1', 'o2'),
- `"-"` - (wg, 'o1', 'o2'),
  }
  
  # Each character in the sequence represents a component
  s = "AB-H-H-H-H-BA"
  c = gf.components.component_sequence(sequence=s, symbol_to_component=symbol_to_component)
  c.plot()

<a id="gdsfactory.components.containers.add_termination"></a>

# gdsfactory.components.containers.add\_termination

<a id="gdsfactory.components.containers.add_termination.add_termination"></a>

#### add\_termination

```python
@gf.cell_with_module_name
def add_termination(component: ComponentSpec = "straight",
                    port_names: tuple[str, ...] | None = None,
                    terminator: ComponentSpec = _terminator_function,
                    terminator_port_name: str | None = None) -> Component
```

Returns component with terminator on some ports.

**Arguments**:

- `component` - to add terminator.
- `port_names` - ports to add terminator.
- `terminator` - factory for the terminator.
- `terminator_port_name` - for the terminator to connect to the component ports.

<a id="gdsfactory.components.containers.splitter_tree"></a>

# gdsfactory.components.containers.splitter\_tree

Returns a switch_tree.

          __
        _|  |_
  __   | |  |_   _
 |  |__| |__|    |
_|  |__          |dy
 |__|  |  __     |
       |_|  |_   |
         |  |_   -
         |__|

   |<-dx->|

<a id="gdsfactory.components.containers.splitter_tree.splitter_tree"></a>

#### splitter\_tree

```python
@gf.cell_with_module_name
def splitter_tree(coupler: ComponentSpec = "mmi1x2",
                  noutputs: int = 4,
                  spacing: Spacing = (90.0, 50.0),
                  bend_s: ComponentSpec | None = "bend_s",
                  bend_s_xsize: float | None = None,
                  cross_section: CrossSectionSpec = "strip") -> gf.Component
```

Tree of power splitters.

**Arguments**:

- `coupler` - coupler factory.
- `noutputs` - number of outputs.
- `spacing` - x, y spacing between couplers.
- `bend_s` - Sbend function for termination.
- `bend_s_xsize` - xsize for the sbend.
- `cross_section` - cross_section.
  
  .. code::
  
  __|
  __|  |__
  _|  |__
  |__        dy
  
  dx

<a id="gdsfactory.components.vias.via_corner"></a>

# gdsfactory.components.vias.via\_corner

<a id="gdsfactory.components.vias.via_corner.via_corner"></a>

#### via\_corner

```python
@gf.cell_with_module_name
def via_corner(cross_section: MultiCrossSectionAngleSpec = (
    (metal2, (0, 180)),
    (metal3, (90, 270)),
),
               vias: tuple[ComponentSpec] = ("via1", ),
               layers_labels: tuple[str, ...] = ("m2", "m3"),
               **kwargs: Any) -> gf.Component
```

Returns Corner via.

Use in place of wire_corner to route between two layers.

**Arguments**:

- `cross_section` - list of cross_section, orientation pairs.
- `vias` - vias to use to fill the rectangles.
- `layers_labels` - Labels to use for each layer.
- `kwargs` - cross_section settings.

<a id="gdsfactory.components.vias.via_stack"></a>

# gdsfactory.components.vias.via\_stack

<a id="gdsfactory.components.vias.via_stack.via_stack"></a>

#### via\_stack

```python
@gf.cell_with_module_name
def via_stack(
    size: Size = (11.0, 11.0),
    layers: LayerSpecs = ("M1", "M2", "MTOP"),
    layer_offsets: Floats | tuple[float | tuple[float, float], ...]
    | None = None,
    vias: Sequence[ComponentSpec | None] = ("via1", "via2", None),
    layer_to_port_orientations: dict[LayerSpec, list[int]] | None = None,
    correct_size: bool = True,
    slot_horizontal: bool = False,
    slot_vertical: bool = False,
    port_orientations: Ints | None = (180, 90, 0, -90)
) -> Component
```

Rectangular via array stack.

You can use it to connect different metal layers or metals to silicon.
You can use the naming convention via_stack_layerSource_layerDestination
contains 4 ports (e1, e2, e3, e4)

also know as Via array
http://www.vlsi-expert.com/2017/12/vias.html

**Arguments**:

- `size` - of the layers.
- `layers` - layers on which to draw rectangles.
- `layer_offsets` - Optional offsets for each layer with respect to size.
  positive grows, negative shrinks the size. If a tuple, it is the offset in x and y.
- `vias` - vias to use to fill the rectangles.
- `layer_to_port_orientations` - dictionary of layer to port_orientations.
- `correct_size` - if True, if the specified dimensions are too small it increases
  them to the minimum possible to fit a via.
- `slot_horizontal` - if True, then vias are horizontal.
- `slot_vertical` - if True, then vias are vertical.
- `port_orientations` - list of port_orientations to add. None does not add ports.

<a id="gdsfactory.components.vias.via_stack.via_stack_corner45"></a>

#### via\_stack\_corner45

```python
@gf.cell_with_module_name
def via_stack_corner45(width: float = 10,
                       layers: Sequence[LayerSpec | None] = ("M1", "M2",
                                                             "MTOP"),
                       layer_offsets: Floats | None = None,
                       vias: Sequence[ComponentSpec | None] = ("via1", "via2",
                                                               None),
                       layer_port: LayerSpec | None = None,
                       correct_size: bool = True) -> Component
```

Rectangular via array stack at a 45 degree angle.

**Arguments**:

- `width` - of the corner45.
- `layers` - layers on which to draw rectangles.
- `layer_offsets` - Optional offsets for each layer with respect to size.
  positive grows, negative shrinks the size.
- `vias` - vias to use to fill the rectangles.
- `layer_port` - if None assumes port is on the last layer.
- `correct_size` - if True, if the specified dimensions are too small it increases
  them to the minimum possible to fit a via.

<a id="gdsfactory.components.vias.via_stack.via_stack_corner45_extended"></a>

#### via\_stack\_corner45\_extended

```python
@gf.cell_with_module_name
def via_stack_corner45_extended(corner: ComponentSpec = "via_stack_corner45",
                                via_stack: ComponentSpec = "via_stack",
                                width: float = 3,
                                length: float = 10) -> Component
```

Rectangular via array stack at a 45 degree angle.

**Arguments**:

- `corner` - corner component.
- `via_stack` - for the via stack.
- `width` - of the corner45.
- `length` - of the straight.

<a id="gdsfactory.components.vias"></a>

# gdsfactory.components.vias

<a id="gdsfactory.components.vias.via"></a>

# gdsfactory.components.vias.via

<a id="gdsfactory.components.vias.via.via"></a>

#### via

```python
@gf.cell_with_module_name
def via(size: Size = (0.7, 0.7),
        enclosure: float = 1.0,
        layer: LayerSpec = "VIAC",
        bbox_layers: Sequence[LayerSpec] | None = None,
        bbox_offset: float = 0,
        bbox_offsets: Sequence[float] | None = None,
        pitch: float = 2,
        column_pitch: float | None = None,
        row_pitch: float | None = None) -> Component
```

Rectangular via.

**Arguments**:

- `size` - in x and y direction.
- `enclosure` - inclusion of via.
- `layer` - via layer.
- `bbox_layers` - layers for the bounding box.
- `bbox_offset` - in um.
- `bbox_offsets` - List of offsets for each bbox_layer.
- `pitch` - pitch between vias.
- `column_pitch` - Optional pitch between columns of vias. Default is pitch.
- `row_pitch` - Optional pitch between rows of vias. Default is pitch.
  
  .. code::
  
  enclosure
  _________________________________________
  |<--->                                  |
  |             gap[0]    size[0]         |
  |             <------> <----->          |
  |      ______          ______           |
  |     |      |        |      |          |
  |     |      |        |      |  size[1] |
  |     |______|        |______|          |
  |      <------------->                  |
  |           pitch                       |
  |_______________________________________|

<a id="gdsfactory.components.vias.via.via_circular"></a>

#### via\_circular

```python
@gf.cell_with_module_name
def via_circular(radius: float = 0.35,
                 enclosure: float = 1.0,
                 layer: LayerSpec = "VIAC",
                 pitch: float | None = 2,
                 column_pitch: float | None = None,
                 row_pitch: float | None = None,
                 angle_resolution: float = 2.5) -> Component
```

Circular via.

**Arguments**:

- `radius` - in um.
- `enclosure` - inclusion of via in um for the layer above.
- `layer` - via layer.
- `pitch` - pitch between vias.
- `column_pitch` - Optional pitch between columns of vias. Default is pitch.
- `row_pitch` - Optional pitch between rows of vias. Default is pitch.
- `angle_resolution` - number of degrees per point.

<a id="gdsfactory.components.vias.via_chain"></a>

# gdsfactory.components.vias.via\_chain

Via chain.

<a id="gdsfactory.components.vias.via_chain.via_chain"></a>

#### via\_chain

```python
@gf.cell_with_module_name
def via_chain(num_vias: int = 100,
              cols: int = 10,
              via: ComponentSpec = "via1",
              contact: ComponentSpec = "via_stack_m2_m3",
              layers_bot: LayerSpecs = ("M1", ),
              layers_top: LayerSpecs = ("M2", ),
              offsets_top: tuple[float, ...] = (0, ),
              offsets_bot: tuple[float, ...] = (0, ),
              via_min_enclosure: float = 1.0,
              min_metal_spacing: float = 1.0,
              contact_offset: float = 0.0) -> Component
```

Via chain to extract via resistance.

**Arguments**:

- `num_vias` - number of vias.
- `cols` - number of column pairs.
- `via` - via component.
- `contact` - contact component.
- `layers_bot` - list of bottom layers.
- `layers_top` - list of top layers.
- `offsets_top` - list of top layer offsets.
- `offsets_bot` - list of bottom layer offsets.
- `via_min_enclosure` - via_min_enclosure.
- `min_metal_spacing` - min_metal_spacing.
- `contact_offset` - contact offset.
  
  .. code::
  
  side view:
  min_metal_spacing
  ┌────────────────────────────────────┐              ┌────────────────────────────────────┐
  │  layers_top                        │              │                                    │
  │                                    │◄───────────► │                                    │
  └─────────────┬─────┬────────────────┘              └───────────────┬─────┬──────────────┘
  │     │         via_enclosure                         │     │
  │     │◄───────────────►                              │     │
  │     │                                               │     │
  │     │                                               │     │
  │width│                                               │     │
  ◄─────►                                               │     │
  │     │                                               │     │
  ┌─────────────┴─────┴───────────────────────────────────────────────┴─────┴───────────────┐
  │ layers_bot                                                                              │
  │                                                                                         │
  └─────────────────────────────────────────────────────────────────────────────────────────┘
  
  ◄─────────────────────────────────────────────────────────────────────────────────────────►
  2*e + w + min_metal_spacing + 2*e + w

<a id="gdsfactory.components.vias.via_stack_with_offset"></a>

# gdsfactory.components.vias.via\_stack\_with\_offset

<a id="gdsfactory.components.vias.via_stack_with_offset.via_stack_with_offset"></a>

#### via\_stack\_with\_offset

```python
@gf.cell_with_module_name
def via_stack_with_offset(
    layers: LayerSpecs = ("PPP", "M1"),
    size: Size | None = (10, 10),
    sizes: Sequence[Size] | None = None,
    layer_offsets: Sequence[float] | None = None,
    vias: Sequence[ComponentSpec | None] = (None, "viac"),
    offsets: Sequence[float] | None = None,
    layer_to_port_orientations: dict[LayerSpec, list[int]] | None = None
) -> Component
```

Rectangular layer transition with offset between layers.

**Arguments**:

- `layers` - layer specs between vias.
- `size` - for all vias array.
- `sizes` - Optional size for each via array. Overrides size.
- `layer_offsets` - Optional offsets for each layer with respect to size.
  positive grows, negative shrinks the size.
- `vias` - via spec for previous layer. None for no via.
- `offsets` - optional offset for each layer relatively to the previous one.
  By default it only offsets by size[1] if there is a via.
- `layer_to_port_orientations` - Optional dictionary with layer to port orientations.
  
  .. code::
  
  side view
  
  __________________________
  |                          |
  |                          | layers[2]
  |__________________________|           vias[2] = None
  |                          |
  | layer_offsets[1]+size    | layers[1]
  |__________________________|
  |     |
  vias[1]
  ___|_____|__
  |            |
  |  sizes[0]  |  layers[0]
  |____________|
  
  vias[0] = None

<a id="gdsfactory.components.grating_couplers.grating_coupler_array"></a>

# gdsfactory.components.grating\_couplers.grating\_coupler\_array

<a id="gdsfactory.components.grating_couplers.grating_coupler_array.grating_coupler_array"></a>

#### grating\_coupler\_array

```python
@gf.cell_with_module_name
def grating_coupler_array(
        grating_coupler: ComponentSpec = "grating_coupler_elliptical",
        pitch: float = 127.0,
        n: int = 6,
        port_name: str = "o1",
        rotation: int = -90,
        with_loopback: bool = False,
        cross_section: CrossSectionSpec = "strip",
        straight_to_grating_spacing: float = 10.0,
        centered: bool = True,
        radius: float | None = None) -> Component
```

Array of grating couplers.

**Arguments**:

- `grating_coupler` - ComponentSpec.
- `pitch` - x spacing.
- `n` - number of grating couplers.
- `port_name` - port name.
- `rotation` - rotation angle for each reference.
- `with_loopback` - if True, adds a loopback between edge GCs. Only works for rotation = 90 for now.
- `cross_section` - cross_section for the routing.
- `straight_to_grating_spacing` - spacing between the last grating coupler and the loopback.
- `centered` - if True, centers the array around the origin.
- `radius` - optional radius for routing the loopback.

<a id="gdsfactory.components.grating_couplers.grating_coupler_elliptical_trenches"></a>

# gdsfactory.components.grating\_couplers.grating\_coupler\_elliptical\_trenches

<a id="gdsfactory.components.grating_couplers.grating_coupler_elliptical_trenches.grating_coupler_elliptical_trenches"></a>

#### grating\_coupler\_elliptical\_trenches

```python
@gf.cell_with_module_name
def grating_coupler_elliptical_trenches(
        polarization: str = "te",
        taper_length: float = 16.6,
        taper_angle: float = 30.0,
        trenches_extra_angle: float = 9.0,
        wavelength: float = 1.53,
        fiber_angle: float = 15.0,
        grating_line_width: float = 0.343,
        neff: float = 2.638,
        ncladding: float = 1.443,
        layer_trench: LayerSpec = "SHALLOW_ETCH",
        p_start: int = 26,
        n_periods: int = 30,
        end_straight_length: float = 0.2,
        taper: ComponentSpec = "taper",
        cross_section: CrossSectionSpec = "strip") -> Component
```

Returns Grating coupler with defined trenches.

Some foundries define the grating coupler by a shallow etch step (trenches)
Others define the slab that they keep (see grating_coupler_elliptical)

**Arguments**:

- `polarization` - 'te' or 'tm'.
- `taper_length` - taper length from straight I/O.
- `taper_angle` - grating flare angle.
- `trenches_extra_angle` - extra angle for the trenches.
- `wavelength` - grating transmission central wavelength.
- `fiber_angle` - fibre polish angle in degrees.
- `grating_line_width` - of the 220 ridge.
- `neff` - tooth effective index.
- `ncladding` - cladding index.
- `layer_trench` - for the trench.
- `p_start` - first tooth.
- `n_periods` - number of grating teeth.
- `end_straight_length` - at the end of straight.
- `taper` - taper function.
- `cross_section` - cross_section spec.
  
  
  .. code::
  
  fiber
  
  /  /  /  /
  /  /  /  /
  _|-|_|-|_|-|___
  WG  o1  ______________|

<a id="gdsfactory.components.grating_couplers.grating_coupler_rectangular"></a>

# gdsfactory.components.grating\_couplers.grating\_coupler\_rectangular

<a id="gdsfactory.components.grating_couplers.grating_coupler_rectangular.grating_coupler_rectangular"></a>

#### grating\_coupler\_rectangular

```python
@gf.cell_with_module_name
def grating_coupler_rectangular(
        n_periods: int = 20,
        period: float = 0.75,
        fill_factor: float = 0.5,
        width_grating: float = 11.0,
        length_taper: float = 150.0,
        polarization: str = "te",
        wavelength: float = 1.55,
        taper: ComponentSpec = "taper",
        layer_slab: LayerSpec | None = "SLAB150",
        layer_grating: LayerSpec | None = None,
        fiber_angle: float = 15,
        slab_xmin: float = -1.0,
        slab_offset: float = 1.0,
        cross_section: CrossSectionSpec = "strip") -> Component
```

Grating coupler with rectangular shapes (not elliptical).

Needs longer taper than elliptical.
Grating teeth are straight.
For a focusing grating take a look at grating_coupler_elliptical.

**Arguments**:

- `n_periods` - number of grating teeth.
- `period` - grating pitch.
- `fill_factor` - ratio of grating width vs gap.
- `width_grating` - 11.
- `length_taper` - 150.
- `polarization` - 'te' or 'tm'.
- `wavelength` - in um.
- `taper` - function.
- `layer_slab` - layer that protects the slab under the grating.
- `layer_grating` - layer for the grating.
- `fiber_angle` - in degrees.
- `slab_xmin` - where 0 is at the start of the taper.
- `slab_offset` - from edge of grating to edge of the slab.
- `cross_section` - for input waveguide port.
  
  .. code::
  
  side view
  fiber
  
  /  /  /  /
  /  /  /  /
  
  _|-|_|-|_|-|___ layer
  layer_slab |
  o1  ______________|
  
  
  top view     _________
  /| | | | |
  / | | | | |
  /taper_angle
  /_ _| | | | |
  wg_width |   | | | | |
  \   | | | | |
  \  | | | | |
  \ | | | | |
  \|_|_|_|_|
  <-->
  taper_length

<a id="gdsfactory.components.grating_couplers.grating_coupler_dual_pol"></a>

# gdsfactory.components.grating\_couplers.grating\_coupler\_dual\_pol

<a id="gdsfactory.components.grating_couplers.grating_coupler_dual_pol.grating_coupler_dual_pol"></a>

#### grating\_coupler\_dual\_pol

```python
@gf.cell_with_module_name
def grating_coupler_dual_pol(
        unit_cell: ComponentSpec = _unit_cell,
        period_x: float = 0.58,
        period_y: float = 0.58,
        x_span: float = 11,
        y_span: float = 11,
        length_taper: float = 150.0,
        width_taper: float = 10.0,
        polarization: str = "te",
        wavelength: float = 1.55,
        taper: ComponentSpec = "taper",
        base_layer: LayerSpec = "WG",
        cross_section: CrossSectionSpec = "strip") -> Component
```

2 dimensional, dual polarization grating coupler.

Based on a photonic crystal with a unit cell that is usually an ellipse,
a rectangle or a circle.
# The default values are loosely based on Taillaert et al,
# "A Compact Two-Dimensional Grating Coupler Used as a Polarization Splitter", IEEE Phot. Techn. Lett. 15(9), 2003

**Arguments**:

- `unit_cell` - component describing the unit cell of the photonic crystal.
- `period_x` - spacing between unit cells in the x direction [um].
- `period_y` - spacing between unit cells in the y direction [um].
- `x_span` - full x span of the photonic crystal.
- `y_span` - full y span of the photonic crystal.
- `length_taper` - taper length [um].
- `width_taper` - width of the taper at the grating coupler side [um].
- `polarization` - polarization of the grating coupler.
- `wavelength` - operation wavelength [um]
- `taper` - function to generate the tapers.
- `base_layer` - layer to draw over the whole photonic crystal \
  (necessary if the unit cells are etched into a base layer).
- `cross_section` - for the routing waveguides.
  
  .. code::
  
  side view
  fiber
  
  /  /  /  /
  /  /  /  /
  
  _|-|_|-|_|-|___  --> unit_cells
  base_layer |
  o1  ______________|
  
  
  top view
  
  -------------
  // | o   o   o  |
  o1 __ //  | o   o   o  |
  \\  | o   o   o  |
  \\ | o   o   o  |
  -------------
  \\         //
  \\       //
  |
  o2

<a id="gdsfactory.components.grating_couplers.functions"></a>

# gdsfactory.components.grating\_couplers.functions

<a id="gdsfactory.components.grating_couplers.functions.ellipse_arc"></a>

#### ellipse\_arc

```python
def ellipse_arc(a: float,
                b: float,
                x0: float,
                theta_min: float,
                theta_max: float,
                angle_step: float = 0.5) -> npt.NDArray[np.floating[Any]]
```

Returns an elliptical arc.

b = a *sqrt(1-e**2)

An ellipse with a = b has zero eccentricity (is a circle)

**Arguments**:

- `a` - ellipse semi-major axis.
- `b` - semi-minor axis.
- `x0` - in um.
- `theta_min` - in rad.
- `theta_max` - in rad.
- `angle_step` - in rad.

<a id="gdsfactory.components.grating_couplers.functions.grating_taper_points"></a>

#### grating\_taper\_points

```python
def grating_taper_points(
        a: float,
        b: float,
        x0: float,
        taper_length: float,
        taper_angle: float,
        wg_width: float,
        angle_step: float = 1.0) -> npt.NDArray[np.floating[Any]]
```

Returns a taper for a grating coupler.

**Arguments**:

- `a` - ellipse semi-major axis.
- `b` - semi-minor axis.
- `x0` - in um.
- `taper_length` - in um.
- `taper_angle` - in degrees.
- `wg_width` - in um.
- `angle_step` - in degrees.

<a id="gdsfactory.components.grating_couplers.functions.get_grating_period_curved"></a>

#### get\_grating\_period\_curved

```python
def get_grating_period_curved(fiber_angle: float = 15.0,
                              wavelength: float = 1.55,
                              n_slab: float = (neff_ridge + neff_shallow) / 2,
                              n_clad: float = 1.0) -> tuple[float, float]
```

The following function calculates the confocal grating periods n_slab is.

the "average slab index" of the grating. For 220nm silicon it is 2.8, for
150nm it is 2.5. The average is approximately 2.65. n_clad is the cladding
index in which the fiber is located, not the index of the layer above the
straight. If the fiber is in air, then it is 1.0. If you use an index
matching fluid or glue, then it should be 1.45.

**Arguments**:

- `fiber_angle` - in degrees.
- `wavelength` - um.
- `n_slab` - slab refractive index.
- `n_clad` - cladding refractive index.

<a id="gdsfactory.components.grating_couplers.functions.get_grating_period"></a>

#### get\_grating\_period

```python
def get_grating_period(fiber_angle: float = 13.45,
                       wavelength: float = 1.55,
                       neff_high: float = neff_ridge,
                       neff_low: float = neff_shallow,
                       n_clad: float = 1.45) -> float
```

Return grating coupler period based on lumerical slides.

**Arguments**:

- `fiber_angle` - in degrees.
- `wavelength` - um.
- `neff_high` - high index.
- `neff_low` - low index.
- `n_clad` - cladding index.

<a id="gdsfactory.components.grating_couplers"></a>

# gdsfactory.components.grating\_couplers

<a id="gdsfactory.components.grating_couplers.grating_coupler_tree"></a>

# gdsfactory.components.grating\_couplers.grating\_coupler\_tree

<a id="gdsfactory.components.grating_couplers.grating_coupler_tree.grating_coupler_tree"></a>

#### grating\_coupler\_tree

```python
@gf.cell_with_module_name
def grating_coupler_tree(
        n: int = 4,
        straight_spacing: float = 4.0,
        grating_coupler: ComponentSpec = "grating_coupler_elliptical_te",
        with_loopback: bool = False,
        bend: ComponentSpec = "bend_euler",
        fanout_length: float = 0.0,
        cross_section: CrossSectionSpec = "strip",
        **kwargs: Any) -> Component
```

Array of straights connected with grating couplers.

useful to align the 4 corners of the chip

**Arguments**:

- `n` - number of gratings.
- `straight_spacing` - in um.
- `grating_coupler` - spec.
- `with_loopback` - adds loopback.
- `bend` - bend spec.
- `fanout_length` - in um.
- `cross_section` - cross_section function.
- `kwargs` - additional arguments.

<a id="gdsfactory.components.grating_couplers.grating_coupler_loss"></a>

# gdsfactory.components.grating\_couplers.grating\_coupler\_loss

<a id="gdsfactory.components.grating_couplers.grating_coupler_loss.grating_coupler_loss"></a>

#### grating\_coupler\_loss

```python
@gf.cell_with_module_name
def grating_coupler_loss(
        pitch: float = 127.0,
        grating_coupler: ComponentSpec = "grating_coupler_elliptical_trenches",
        cross_section: CrossSectionSpec = "strip",
        port_name: str = "o1",
        rotation: float = -90,
        nfibers: int = 10,
        grating_coupler_spacing: float = 5.0) -> Component
```

Grating coupler test structure for de-embeding fiber array.

Connects channel 1->3, 1->5 ... 1->nfibers with grating couplers.

Only odd channels are connected to the grating couplers as even channels in the align_tree.

**Arguments**:

- `pitch` - um.
- `grating_coupler` - spec.
- `cross_section` - spec.
- `port_name` - for the grating_coupler port.
- `rotation` - degrees.
- `nfibers` - number of fibers to connect.
- `grating_coupler_spacing` - um.

<a id="gdsfactory.components.grating_couplers.grating_coupler_rectangular_arbitrary"></a>

# gdsfactory.components.grating\_couplers.grating\_coupler\_rectangular\_arbitrary

<a id="gdsfactory.components.grating_couplers.grating_coupler_rectangular_arbitrary.grating_coupler_rectangular_arbitrary"></a>

#### grating\_coupler\_rectangular\_arbitrary

```python
@gf.cell_with_module_name
def grating_coupler_rectangular_arbitrary(
        gaps: Floats = _gaps,
        widths: Floats = _widths,
        width_grating: float = 11.0,
        length_taper: float = 150.0,
        polarization: str = "te",
        wavelength: float = 1.55,
        layer_grating: LayerSpec | None = None,
        layer_slab: LayerSpec | None = None,
        slab_xmin: float = -1.0,
        slab_offset: float = 1.0,
        fiber_angle: float = 15,
        cross_section: CrossSectionSpec = "strip") -> Component
```

Grating coupler uniform with rectangular shape (not elliptical).

Therefore it needs a longer taper.
Grating teeth are straight instead of elliptical.

**Arguments**:

- `gaps` - list of gaps between grating teeth.
- `widths` - list of grating widths.
- `width_grating` - grating teeth width.
- `length_taper` - taper length (um).
- `polarization` - 'te' or 'tm'.
- `wavelength` - in um.
- `layer_grating` - Optional layer for grating. \
  by default None uses cross_section.layer. \
  if different from cross_section.layer expands taper.
- `layer_slab` - layer that protects the slab under the grating.
- `slab_xmin` - where 0 is at the start of the taper.
- `slab_offset` - from edge of grating to edge of the slab.
- `fiber_angle` - in degrees.
- `cross_section` - for input waveguide port.
  
  .. code::
  
  fiber
  
  /  /  /  /
  /  /  /  /
  
  _|-|_|-|_|-|___ layer
  layer_slab |
  o1  ______________|
  
  
  
  top view     _________
  /| | | | |
  / | | | | |
  /taper_angle
  /_ _| | | | |
  wg_width |   | | | | |
  \   | | | | |
  \  | | | | |
  \ | | | | |
  \|_|_|_|_|
  <-->
  taper_length

<a id="gdsfactory.components.grating_couplers.grating_coupler_elliptical_arbitrary"></a>

# gdsfactory.components.grating\_couplers.grating\_coupler\_elliptical\_arbitrary

<a id="gdsfactory.components.grating_couplers.grating_coupler_elliptical_arbitrary.grating_coupler_elliptical_arbitrary"></a>

#### grating\_coupler\_elliptical\_arbitrary

```python
@gf.cell_with_module_name
def grating_coupler_elliptical_arbitrary(
        gaps: Floats = _gaps,
        widths: Floats = _widths,
        taper_length: float = 16.6,
        taper_angle: float = 60.0,
        wavelength: float = 1.554,
        fiber_angle: float = 15.0,
        nclad: float = 1.443,
        layer_slab: LayerSpec | None = "SLAB150",
        layer_grating: LayerSpec | None = None,
        taper_to_slab_offset: float = -3.0,
        polarization: str = "te",
        spiked: bool = True,
        bias_gap: float = 0,
        cross_section: CrossSectionSpec = "strip") -> Component
```

Grating coupler with parametrization based on Lumerical FDTD simulation.

The ellipticity is derived from Lumerical knowledge base
it depends on fiber_angle (degrees), neff, and nclad

**Arguments**:

- `gaps` - list of gaps.
- `widths` - list of widths.
- `taper_length` - taper length from input.
- `taper_angle` - grating flare angle.
- `wavelength` - grating transmission central wavelength (um).
- `fiber_angle` - fibre angle in degrees determines ellipticity.
- `nclad` - cladding effective index to compute ellipticity.
- `layer_slab` - Optional slab.
- `layer_grating` - Optional layer for grating.
  by default None uses cross_section.layer.
  if different from cross_section.layer expands taper.
- `taper_to_slab_offset` - 0 is where taper ends.
- `polarization` - te or tm.
- `spiked` - grating teeth have spikes to avoid drc errors.
- `bias_gap` - etch gap (um).
  Positive bias increases gap and reduces width to keep period constant.
- `cross_section` - cross_section spec for waveguide port.
  
  https://en.wikipedia.org/wiki/Ellipse
  c = (a1 ** 2 - b1 ** 2) ** 0.5
  e = (1 - (b1 / a1) ** 2) ** 0.5
  print(e)
  
  .. code::
  
  fiber
  
  /  /  /  /
  /  /  /  /
  
  _|-|_|-|_|-|___ layer
  layer_slab |
  o1  ______________|

<a id="gdsfactory.components.grating_couplers.grating_coupler_elliptical_arbitrary.grating_coupler_elliptical_uniform"></a>

#### grating\_coupler\_elliptical\_uniform

```python
@gf.cell_with_module_name
def grating_coupler_elliptical_uniform(n_periods: int = 20,
                                       period: float = 0.75,
                                       fill_factor: float = 0.5,
                                       **kwargs: Any) -> Component
```

Grating coupler with parametrization based on Lumerical FDTD simulation.

The ellipticity is derived from Lumerical knowledge base
it depends on fiber_angle (degrees), neff, and nclad

**Arguments**:

- `n_periods` - number of grating periods.
- `period` - grating pitch in um.
- `fill_factor` - ratio of grating width vs gap.
  

**Arguments**:

- `taper_length` - taper length from input.
- `taper_angle` - grating flare angle.
- `wavelength` - grating transmission central wavelength (um).
- `fiber_angle` - fibre angle in degrees determines ellipticity.
- `neff` - tooth effective index to compute ellipticity.
- `nclad` - cladding effective index to compute ellipticity.
- `layer_slab` - Optional slab.
- `taper_to_slab_offset` - where 0 is at the start of the taper.
- `polarization` - te or tm.
- `spiked` - grating teeth have spikes to avoid drc errors..
- `bias_gap` - etch gap (um).
  Positive bias increases gap and reduces width to keep period constant.
- `cross_section` - cross_section spec for waveguide port.
- `kwargs` - cross_section settings.
  
  .. code::
  
  fiber
  
  /  /  /  /
  /  /  /  /
  
  _|-|_|-|_|-|___ layer
  layer_slab |
  o1  ______________|

<a id="gdsfactory.components.grating_couplers.grating_coupler_elliptical"></a>

# gdsfactory.components.grating\_couplers.grating\_coupler\_elliptical

<a id="gdsfactory.components.grating_couplers.grating_coupler_elliptical.grating_coupler_elliptical"></a>

#### grating\_coupler\_elliptical

```python
@gf.cell_with_module_name
def grating_coupler_elliptical(
        polarization: str = "te",
        taper_length: float = 16.6,
        taper_angle: float = 40.0,
        wavelength: float = 1.554,
        fiber_angle: float = 15.0,
        grating_line_width: float = 0.343,
        neff: float = 2.638,
        nclad: float = 1.443,
        n_periods: int = 30,
        big_last_tooth: bool = False,
        layer_slab: LayerSpec | None = "SLAB150",
        slab_xmin: float = -1.0,
        slab_offset: float = 2.0,
        spiked: bool = True,
        cross_section: CrossSectionSpec = "strip") -> Component
```

Grating coupler with parametrization based on Lumerical FDTD simulation.

**Arguments**:

- `polarization` - te or tm.
- `taper_length` - taper length from input.
- `taper_angle` - grating flare angle.
- `wavelength` - grating transmission central wavelength (um).
- `fiber_angle` - fibre angle in degrees determines ellipticity.
- `grating_line_width` - in um.
- `neff` - tooth effective index.
- `nclad` - cladding effective index.
- `n_periods` - number of periods.
- `big_last_tooth` - adds a big_last_tooth.
- `layer_slab` - layer that protects the slab under the grating.
- `slab_xmin` - where 0 is at the start of the taper.
- `slab_offset` - in um.
- `spiked` - grating teeth have sharp spikes to avoid non-manhattan drc errors.
- `cross_section` - specification (CrossSection, string or dict).
  
  .. code::
  
  fiber
  
  /  /  /  /
  /  /  /  /
  
  _|-|_|-|_|-|___ layer
  layer_slab |
  o1  ______________|

<a id="gdsfactory.components.grating_couplers.grating_coupler_elliptical_lumerical"></a>

# gdsfactory.components.grating\_couplers.grating\_coupler\_elliptical\_lumerical

<a id="gdsfactory.components.grating_couplers.grating_coupler_elliptical_lumerical.grating_coupler_elliptical_lumerical"></a>

#### grating\_coupler\_elliptical\_lumerical

```python
@gf.cell_with_module_name
def grating_coupler_elliptical_lumerical(
        parameters: Floats = parameters,
        layer_slab: LayerSpec | None = "SLAB150",
        taper_angle: float = 55,
        taper_length: float = 12.24 + 0.36,
        fiber_angle: float = 5,
        info: dict[str, Any] | None = None,
        bias_gap: float = 0,
        cross_section: CrossSectionSpec = "strip") -> Component
```

Returns a grating coupler from lumerical inverse design 3D optimization.

this is a wrapper of components.grating_coupler_elliptical_arbitrary
https://support.lumerical.com/hc/en-us/articles/1500000306621
https://support.lumerical.com/hc/en-us/articles/360042800573

Here are the simulation settings used in lumerical

n_bg=1.44401 `Refractive` index of the background material (cladding)
wg=3.47668   # Refractive index of the waveguide material (core)
lambda0=1550e-9
bandwidth = 0e-9
polarization = 'TE'
wg_width=500e-9 # Waveguide width
wg_height=220e-9 # Waveguide height
etch_depth=80e-9 # etch depth
theta_fib_mat = 5 # Angle of the fiber mode in material
theta_taper=30
efficiency=0.55 # 5.2 dB

**Arguments**:

- `parameters` - xinput, gap1, width1, gap2, width2 ...
- `layer` - for waveguide.
- `layer_slab` - for slab.
- `taper_angle` - in deg.
- `taper_length` - in um.
- `fiber_angle` - used to compute ellipticity.
- `info` - optional simulation settings.
- `bias_gap` - gap/trenches bias (um) to compensate for etching bias.
  

**Arguments**:

- `taper_length` - taper length from input in um.
- `taper_angle` - grating flare angle in degrees.
- `wavelength` - grating transmission central wavelength (um).
- `fiber_angle` - fibre angle in degrees determines ellipticity.
- `neff` - tooth effective index.
- `nclad` - cladding effective index.
- `polarization` - te or tm.
- `spiked` - grating teeth include sharp spikes to avoid non-manhattan drc errors.
- `cross_section` - cross_section spec for waveguide port.

<a id="gdsfactory.components.spirals.spiral_double"></a>

# gdsfactory.components.spirals.spiral\_double

<a id="gdsfactory.components.spirals.spiral_double.spiral_double"></a>

#### spiral\_double

```python
@gf.cell_with_module_name
def spiral_double(min_bend_radius: float = 10.0,
                  separation: float = 2.0,
                  number_of_loops: float = 3,
                  npoints: int = 1000,
                  cross_section: CrossSectionSpec = "strip",
                  bend: ComponentSpec = "bend_circular") -> gf.Component
```

Returns a spiral double (spiral in, and then out).

**Arguments**:

- `min_bend_radius` - inner radius of the spiral.
- `separation` - separation between the loops.
- `number_of_loops` - number of loops per spiral.
- `npoints` - points for the spiral.
- `cross_section` - cross-section to extrude the structure with.
- `bend` - factory for the bends in the middle of the double spiral.

<a id="gdsfactory.components.spirals.spiral_inductor"></a>

# gdsfactory.components.spirals.spiral\_inductor

<a id="gdsfactory.components.spirals.spiral_inductor.spiral_inductor"></a>

#### spiral\_inductor

```python
@gf.cell_with_module_name
def spiral_inductor(width: float = 3.0,
                    pitch: float = 3.0,
                    turns: int = 16,
                    outer_diameter: float = 800,
                    tail: float = 50.0) -> Component
```

Generates a spiral inductor to make superconducting resonator for qubit readout.

See J. M. Hornibrook, J. I. Colless, A. C. Mahoney, X. G. Croot, S. Blanvillain, H. Lu, A. C. Gossard, D. J. Reilly;
Frequency multiplexing for readout of spin qubits. Appl. Phys. Lett. 10 March 2014; 104 (10): 103108. https://doi.org/10.1063/1.4868107

**Arguments**:

- `width` - width of the inductor track.
- `pitch` - distance between the inductor tracks.
- `turns` - number of full spriral turns.
- `outer_diameter` - size of the inductor.
- `tail` - length of the inner and outer tail.

<a id="gdsfactory.components.spirals.delay_snake"></a>

# gdsfactory.components.spirals.delay\_snake

<a id="gdsfactory.components.spirals.delay_snake.delay_snake"></a>

#### delay\_snake

```python
@gf.cell_with_module_name
def delay_snake(length: float = 1600.0,
                length0: float = 0.0,
                length2: float = 0.0,
                n: int = 2,
                bend180: ComponentSpec = bend_euler180,
                cross_section: CrossSectionSpec = "strip",
                width: float | None = None) -> Component
```

Returns Snake with a starting bend and 180 bends.

**Arguments**:

- `length` - total length.
- `length0` - start length.
- `length2` - end length.
- `n` - number of loops.
- `bend180` - ubend spec.
- `cross_section` - cross_section spec.
- `width` - width of the waveguide. If None, it will use the width of the cross_section.
  
  .. code::
  
  | length0   |
  
  >---------\
  \bend180.info['length']
  /
  |-------------------/
  |
  |------------------->------->|
  length2
  |   delta_length    |        |

<a id="gdsfactory.components.spirals"></a>

# gdsfactory.components.spirals

<a id="gdsfactory.components.spirals.spiral_heater"></a>

# gdsfactory.components.spirals.spiral\_heater

<a id="gdsfactory.components.spirals.spiral_heater.spiral_racetrack"></a>

#### spiral\_racetrack

```python
@gf.cell_with_module_name
def spiral_racetrack(min_radius: float | None = None,
                     straight_length: float = 20.0,
                     spacings: Floats = (2, 2, 3, 3, 2, 2),
                     straight: ComponentSpec = straight,
                     bend: ComponentSpec = bend_euler,
                     bend_s: ComponentSpec = "bend_s",
                     cross_section: CrossSectionSpec = "strip",
                     cross_section_s: CrossSectionSpec | None = None,
                     extra_90_deg_bend: bool = False,
                     allow_min_radius_violation: bool = False) -> Component
```

Returns Racetrack-Spiral.

**Arguments**:

- `min_radius` - smallest radius in um.
- `straight_length` - length of the straight segments in um.
- `spacings` - space between the center of neighboring waveguides in um.
- `straight` - factory to generate the straight segments.
- `bend` - factory to generate the bend segments.
- `bend_s` - factory to generate the s-bend segments.
- `cross_section` - cross-section of the waveguides.
- `cross_section_s` - cross-section of the s bend waveguide (optional).
- `extra_90_deg_bend` - if True, we add an additional straight + 90 degree bent at the output, so the output port is looking down.
- `allow_min_radius_violation` - if True, will allow the s-bend to have a smaller radius than the minimum radius.

<a id="gdsfactory.components.spirals.spiral_heater.spiral_racetrack_fixed_length"></a>

#### spiral\_racetrack\_fixed\_length

```python
@gf.cell_with_module_name
def spiral_racetrack_fixed_length(
        length: float = 1000,
        in_out_port_spacing: float = 150,
        n_straight_sections: int = 8,
        min_radius: float | None = None,
        min_spacing: float = 5.0,
        straight: ComponentSpec = straight,
        bend: ComponentSpec = "bend_circular",
        bend_s: ComponentSpec = "bend_s",
        cross_section: CrossSectionSpec = "strip",
        cross_section_s: CrossSectionSpec | None = None) -> Component
```

Returns Racetrack-Spiral with a specified total length.

The input and output ports are aligned in y. This class is meant to
be used for generating interferometers with long waveguide lengths, where
the most important parameter is the length difference between the arms.

**Arguments**:

- `length` - total length of the spiral from input to output ports in um.
- `in_out_port_spacing` - spacing between input and output ports of the spiral in um.
- `n_straight_sections` - total number of straight sections for the racetrack spiral. Has to be even.
- `min_radius` - smallest radius in um.
- `min_spacing` - minimum center-center spacing between adjacent waveguides.
- `straight` - factory to generate the straight segments.
- `bend` - factory to generate the bend segments.
- `bend_s` - factory to generate the s-bend segments.
- `cross_section` - cross-section of the waveguides.
- `cross_section_s` - cross-section of the s bend waveguide (optional).

<a id="gdsfactory.components.spirals.spiral_heater.spiral_racetrack_heater_metal"></a>

#### spiral\_racetrack\_heater\_metal

```python
@gf.cell_with_module_name
def spiral_racetrack_heater_metal(
        min_radius: float | None = None,
        straight_length: float = 30,
        spacing: float = 2,
        num: int = 8,
        straight: ComponentSpec = straight,
        bend: ComponentSpec = bend_euler,
        bend_s: ComponentSpec = "bend_s",
        waveguide_cross_section: CrossSectionSpec = "strip",
        heater_cross_section: CrossSectionSpec = "heater_metal",
        via_stack: ComponentSpec | None = "via_stack_heater_mtop"
) -> Component
```

Returns spiral racetrack with a heater above.

based on https://doi.org/10.1364/OL.400230 .

**Arguments**:

- `min_radius` - smallest radius. Defaults to the radius of the cross-section.
- `straight_length` - length of the straight segments.
- `spacing` - space between the center of neighboring waveguides.
- `num` - number of loops.
- `straight` - factory to generate the straight segments.
- `bend` - factory to generate the bend segments.
- `bend_s` - factory to generate the s-bend segments.
- `waveguide_cross_section` - cross-section of the waveguides.
- `heater_cross_section` - cross-section of the heater.
- `via_stack` - via stack to connect the heater to the metal layer.

<a id="gdsfactory.components.spirals.spiral_heater.spiral_racetrack_heater_doped"></a>

#### spiral\_racetrack\_heater\_doped

```python
@gf.cell_with_module_name
def spiral_racetrack_heater_doped(
        min_radius: float | None = None,
        straight_length: float = 30,
        spacing: float = 2,
        num: int = 8,
        straight: ComponentSpec = straight,
        bend: ComponentSpec = bend_euler,
        bend_s: ComponentSpec = "bend_s",
        waveguide_cross_section: CrossSectionSpec = "strip",
        heater_cross_section: CrossSectionSpec = "npp") -> Component
```

Returns spiral racetrack with a heater between the loops.

based on https://doi.org/10.1364/OL.400230 but with the heater between the loops.

**Arguments**:

- `min_radius` - smallest radius in um. Defaults to the radius of the cross-section.
- `straight_length` - length of the straight segments in um.
- `spacing` - space between the center of neighboring waveguides in um.
- `num` - number.
- `straight` - factory to generate the straight segments.
- `bend` - factory to generate the bend segments.
- `bend_s` - factory to generate the s-bend segments.
- `waveguide_cross_section` - cross-section of the waveguides.
- `heater_cross_section` - cross-section of the heater.

<a id="gdsfactory.components.spirals.spiral"></a>

# gdsfactory.components.spirals.spiral

<a id="gdsfactory.components.spirals.spiral.spiral"></a>

#### spiral

```python
@gf.cell_with_module_name
def spiral(length: float = 100,
           bend: ComponentSpec = "bend_euler",
           straight: ComponentSpec = "straight",
           cross_section: CrossSectionSpec = "strip",
           spacing: float = 3.0,
           n_loops: int = 6) -> gf.Component
```

Returns a spiral double (spiral in, and then out).

**Arguments**:

- `length` - length of the spiral straight section.
- `bend` - bend component.
- `straight` - straight component.
- `cross_section` - cross_section component.
- `spacing` - spacing between the spiral loops.
- `n_loops` - number of loops.

<a id="gdsfactory.components.spirals.delay_snake_sbend"></a>

# gdsfactory.components.spirals.delay\_snake\_sbend

<a id="gdsfactory.components.spirals.delay_snake_sbend.delay_snake_sbend"></a>

#### delay\_snake\_sbend

```python
@gf.cell_with_module_name
def delay_snake_sbend(length: float = 100.0,
                      length1: float = 0.0,
                      length4: float = 0.0,
                      radius: float = 5.0,
                      waveguide_spacing: float = 5.0,
                      bend: ComponentSpec = "bend_euler",
                      sbend: ComponentSpec = "bend_s",
                      sbend_xsize: float = 100.0,
                      cross_section: CrossSectionSpec = "strip") -> Component
```

Returns compact Snake with sbend in the middle.

Input port faces west and output port faces east.

**Arguments**:

- `length` - total length.
- `length1` - first straight section length in um.
- `length4` - fourth straight section length in um.
- `radius` - u bend radius in um.
- `waveguide_spacing` - waveguide pitch in um.
- `bend` - bend spec.
- `sbend` - sbend spec.
- `sbend_xsize` - sbend size.
- `cross_section` - cross_section spec.
  
  .. code::
  
  length1
  <----------------------------
  length2    spacing    |
  _______              |
  |        \            |
  |          \          | bend1 radius
  |            \sbend   |
  bend2|              \      |
  |                \    |
  |                  \__|
  |
  ---------------------->----------->
  length3              length4
  
  We adjust length2 and length3

<a id="gdsfactory.components.spirals.delay_snake2"></a>

# gdsfactory.components.spirals.delay\_snake2

<a id="gdsfactory.components.spirals.delay_snake2.delay_snake2"></a>

#### delay\_snake2

```python
@gf.cell_with_module_name
def delay_snake2(length: float = 1600.0,
                 length0: float = 0.0,
                 length2: float = 0.0,
                 n: int = 2,
                 bend180: ComponentSpec = "bend_euler180",
                 cross_section: CrossSectionSpec = "strip",
                 width: float | None = None) -> Component
```

Returns Snake with a starting straight and 180 bends.

Input faces west output faces east.

**Arguments**:

- `length` - total length.
- `length0` - start length.
- `length2` - end length.
- `n` - number of loops.
- `bend180` - ubend spec.
- `cross_section` - cross_section spec.
- `width` - width of the waveguide. If None, it will use the width of the cross_section.
  
  .. code::
  
  | length0 | length1 |
  
  >---------|
  | bend180.length
  |-------------------|
  |
  |------------------->------- |
  length2
  |   delta_length    |        |

<a id="gdsfactory.components.edge_couplers"></a>

# gdsfactory.components.edge\_couplers

<a id="gdsfactory.components.edge_couplers.edge_coupler_array"></a>

# gdsfactory.components.edge\_couplers.edge\_coupler\_array

<a id="gdsfactory.components.edge_couplers.edge_coupler_array.edge_coupler_silicon"></a>

#### edge\_coupler\_silicon

```python
@gf.cell_with_module_name
def edge_coupler_silicon(
        length: float = 100,
        width1: float = 0.5,
        width2: float = 0.2,
        with_two_ports: bool = True,
        port_names: tuple[str, str] = ("o1", "o2"),
        port_types: tuple[str, str] = ("optical", "edge_coupler"),
        cross_section: CrossSectionSpec = "strip") -> Component
```

Edge coupler for silicon photonics.

**Arguments**:

- `length` - length of the taper.
- `width1` - width1 of the taper.
- `width2` - width2 of the taper.
- `with_two_ports` - add two ports.
- `port_names` - tuple with port names.
- `port_types` - tuple with port types.
- `cross_section` - cross_section spec.

<a id="gdsfactory.components.edge_couplers.edge_coupler_array.edge_coupler_array"></a>

#### edge\_coupler\_array

```python
@gf.cell_with_module_name
def edge_coupler_array(edge_coupler: ComponentSpec = "edge_coupler_silicon",
                       n: int = 5,
                       pitch: float = 127.0,
                       x_reflection: bool = False,
                       text: ComponentSpec | None = "text_rectangular",
                       text_offset: Float2 = (10, 20),
                       text_rotation: float = 0) -> Component
```

Fiber array edge coupler based on an inverse taper.

Each edge coupler adds a ruler for polishing.

**Arguments**:

- `edge_coupler` - edge coupler spec.
- `n` - number of channels.
- `pitch` - Fiber pitch.
- `x_reflection` - horizontal mirror.
- `text` - text spec.
- `text_offset` - from edge coupler.
- `text_rotation` - text rotation in degrees.

<a id="gdsfactory.components.edge_couplers.edge_coupler_array.edge_coupler_array_with_loopback"></a>

#### edge\_coupler\_array\_with\_loopback

```python
@gf.cell_with_module_name
def edge_coupler_array_with_loopback(
        edge_coupler: ComponentSpec = "edge_coupler_silicon",
        cross_section: CrossSectionSpec = "strip",
        radius: float = 30,
        n: int = 8,
        pitch: float = 127.0,
        extension_length: float = 1.0,
        x_reflection: bool = False,
        text: ComponentSpec | None = "text_rectangular",
        text_offset: Float2 = (0, 10),
        text_rotation: float = 0) -> Component
```

Fiber array edge coupler.

**Arguments**:

- `edge_coupler` - edge coupler.
- `cross_section` - spec.
- `radius` - bend radius loopback (um).
- `n` - number of channels.
- `pitch` - Fiber pitch (um).
- `extension_length` - in um.
- `x_reflection` - horizontal mirror.
- `text` - Optional text spec.
- `text_offset` - x, y.
- `text_rotation` - text rotation in degrees.

<a id="gdsfactory.components.detectors"></a>

# gdsfactory.components.detectors

<a id="gdsfactory.components.detectors.detector_ge"></a>

# gdsfactory.components.detectors.detector\_ge

Straight Ge photodetector.

<a id="gdsfactory.components.detectors.detector_ge.ge_detector_straight_si_contacts"></a>

#### ge\_detector\_straight\_si\_contacts

```python
@gf.cell_with_module_name
def ge_detector_straight_si_contacts(
        length: float = 40.0,
        cross_section: CrossSectionSpec = "pn_ge_detector_si_contacts",
        via_stack: ComponentSpec = "via_stack_slab_m3",
        via_stack_width: float = 10.0,
        via_stack_spacing: float = 5.0,
        via_stack_offset: float = 0.0,
        taper_length: float = 20.0,
        taper_width: float = 0.8,
        taper_cros_section: CrossSectionSpec = "strip") -> Component
```

Returns a straight Ge on Si detector with silicon contacts.

There are no contacts on the Ge. These detectors could have lower
dark current and sensitivity compared to those with contacts in the
Ge. See Chen et al., "High-Responsivity Low-Voltage 28-Gb/s Ge p-i-n
Photodetector With Silicon Contacts", Journal of Lightwave Technology 33(4), 2015.

https://doi.org/10.1109/JLT.2014.2367134

**Arguments**:

- `length` - pd length.
- `cross_section` - for the waveguide.
- `via_stack` - for the via_stacks. First element
- `via_stack_width` - width of the via_stack.
- `via_stack_spacing` - spacing between via_stacks.
- `via_stack_offset` - with respect to the detector
- `taper_length` - length of the taper.
- `taper_width` - width of the taper.
- `taper_cros_section` - cross_section of the taper.

<a id="gdsfactory.components.waveguides.straight_pin_slot"></a>

# gdsfactory.components.waveguides.straight\_pin\_slot

Straight Doped PIN waveguide.

<a id="gdsfactory.components.waveguides.straight_pin_slot.straight_pin_slot"></a>

#### straight\_pin\_slot

```python
@gf.cell_with_module_name
def straight_pin_slot(length: float = 500.0,
                      cross_section: CrossSectionSpec = "pin",
                      via_stack: ComponentSpec | None = "via_stack_m1_mtop",
                      via_stack_width: float = 10.0,
                      via_stack_slab: ComponentSpec
                      | None = "via_stack_slab_m1_horizontal",
                      via_stack_slab_top: ComponentSpec | None = None,
                      via_stack_slab_bot: ComponentSpec | None = None,
                      via_stack_slab_width: float | None = None,
                      via_stack_spacing: float = 3.0,
                      via_stack_slab_spacing: float = 2.0,
                      taper: ComponentSpec | None = "taper_strip_to_ridge",
                      width: float | None = None) -> Component
```

Returns a PIN straight waveguide with slotted via.

https://doi.org/10.1364/OE.26.029983

500um length for PI phase shift
https://ieeexplore.ieee.org/document/8268112

to go beyond 2PI, you will need at least 1mm
https://ieeexplore.ieee.org/document/8853396/

**Arguments**:

- `length` - of the waveguide.
- `cross_section` - for the waveguide.
- `via_stack` - for via_stacking the metal.
- `via_stack_width` - in um.
- `via_stack_slab` - function for the component via_stacking the slab.
- `via_stack_slab_top` - Optional, defaults to via_stack_slab.
- `via_stack_slab_bot` - Optional, defaults to via_stack_slab.
- `via_stack_slab_width` - defaults to via_stack_width.
- `via_stack_spacing` - spacing between via_stacks.
- `via_stack_slab_spacing` - spacing between via_stacks slabs.
- `taper` - optional taper.
- `width` - width of the waveguide. If None, it will use the width of the cross_section.

<a id="gdsfactory.components.waveguides.straight_heater_meander_doped"></a>

# gdsfactory.components.waveguides.straight\_heater\_meander\_doped

Straight heater meander doped.

<a id="gdsfactory.components.waveguides.straight_heater_meander_doped.straight_heater_meander_doped"></a>

#### straight\_heater\_meander\_doped

```python
@gf.cell_with_module_name
def straight_heater_meander_doped(length: float = 300.0,
                                  spacing: float = 2.0,
                                  cross_section: CrossSectionSpec = "strip",
                                  heater_width: float = 1.5,
                                  extension_length: float = 15.0,
                                  layers_doping: LayerSpecs = ("P", "PP",
                                                               "PPP"),
                                  radius: float = 5.0,
                                  via_stack: ComponentSpec | None = _via_stack,
                                  port_orientation1: float | None = None,
                                  port_orientation2: float | None = None,
                                  straight_widths: Floats = (0.8, 0.9, 0.8),
                                  taper_length: float = 10) -> Component
```

Returns a meander based heater.

based on SungWon Chung, Makoto Nakai, and Hossein Hashemi,
Low-power thermo-optic silicon modulator for large-scale photonic integrated systems
Opt. Express 27, 13430-13459 (2019)
https://www.osapublishing.org/oe/abstract.cfm?URI=oe-27-9-13430

**Arguments**:

- `length` - total length of the optical path.
- `spacing` - waveguide spacing (center to center).
- `cross_section` - for waveguide.
- `heater_width` - for heater.
- `extension_length` - of input and output optical ports.
- `layers_doping` - doping layers to be used for heater.
- `radius` - for the meander bends.
- `via_stack` - for the heater to via_stack metal.
- `port_orientation1` - in degrees. None adds all orientations.
- `port_orientation2` - in degrees. None adds all orientations.
- `straight_widths` - width of the straight sections.
- `taper_length` - from the cross_section.

<a id="gdsfactory.components.waveguides.straight_heater_meander"></a>

# gdsfactory.components.waveguides.straight\_heater\_meander

<a id="gdsfactory.components.waveguides.straight_heater_meander.straight_heater_meander"></a>

#### straight\_heater\_meander

```python
@gf.cell_with_module_name
def straight_heater_meander(length: float = 300.0,
                            spacing: float = 2.0,
                            cross_section: CrossSectionSpec = "strip",
                            heater_width: float = 2.5,
                            extension_length: float = 15.0,
                            layer_heater: LayerSpec = "HEATER",
                            radius: float | None = None,
                            via_stack: ComponentSpec
                            | None = "via_stack_heater_mtop",
                            port_orientation1: float | None = None,
                            port_orientation2: float | None = None,
                            heater_taper_length: float = 10.0,
                            straight_widths: Floats | None = None,
                            taper_length: float = 10.0,
                            n: int | None = 3) -> Component
```

Returns a meander based heater.

based on SungWon Chung, Makoto Nakai, and Hossein Hashemi,
Low-power thermo-optic silicon modulator for large-scale photonic integrated systems
Opt. Express 27, 13430-13459 (2019)
https://www.osapublishing.org/oe/abstract.cfm?URI=oe-27-9-13430

**Arguments**:

- `length` - total length of the optical path.
- `spacing` - waveguide spacing (center to center).
- `cross_section` - for waveguide.
- `heater_width` - for heater.
- `extension_length` - of input and output optical ports.
- `layer_heater` - for top heater, if None, it does not add a heater.
- `radius` - for the meander bends. Defaults to cross_section radius.
- `via_stack` - for the heater to via_stack metal.
- `port_orientation1` - in degrees. None adds all orientations.
- `port_orientation2` - in degrees. None adds all orientations.
- `heater_taper_length` - minimizes current concentrations from heater to via_stack.
- `straight_widths` - widths of the straight sections.
- `taper_length` - from the cross_section.
- `n` - number of straight sections.

<a id="gdsfactory.components.waveguides.wire"></a>

# gdsfactory.components.waveguides.wire

Wires for electrical manhattan routes.

<a id="gdsfactory.components.waveguides.wire.wire_corner"></a>

#### wire\_corner

```python
@gf.cell_with_module_name
def wire_corner(cross_section: CrossSectionSpec = "metal_routing",
                port_names: "PortNames" = port_names_electrical,
                port_types: "PortTypes" = port_types_electrical,
                width: float | None = None,
                radius: None | float = None) -> Component
```

Returns 45 degrees electrical corner wire.

**Arguments**:

- `cross_section` - spec.
- `port_names` - port names.
- `port_types` - port types.
- `width` - optional width. Defaults to cross_section width.
- `radius` - ignored.

<a id="gdsfactory.components.waveguides.wire.wire_corner45"></a>

#### wire\_corner45

```python
@gf.cell_with_module_name
def wire_corner45(cross_section: CrossSectionSpec = "metal_routing",
                  radius: float = 10,
                  width: float | None = None,
                  layer: LayerSpec | None = None,
                  with_corner90_ports: bool = True) -> Component
```

Returns 90 degrees electrical corner wire.

**Arguments**:

- `cross_section` - spec.
- `radius` - in um.
- `width` - optional width.
- `layer` - optional layer.
- `with_corner90_ports` - if True adds ports at 90 degrees.

<a id="gdsfactory.components.waveguides.wire.wire_corner_sections"></a>

#### wire\_corner\_sections

```python
@gf.cell_with_module_name
def wire_corner_sections(
        cross_section: CrossSectionSpec = "metal_routing") -> Component
```

Returns 90 degrees electrical corner wire, where all cross_section sections properly represented.

Works well with symmetric cross_sections, not quite ready for asymmetric.

**Arguments**:

- `cross_section` - spec.

<a id="gdsfactory.components.waveguides.crossing_waveguide"></a>

# gdsfactory.components.waveguides.crossing\_waveguide

Waveguide crossings.

<a id="gdsfactory.components.waveguides.crossing_waveguide.crossing_arm"></a>

#### crossing\_arm

```python
@gf.cell_with_module_name
def crossing_arm(r1: float = 3.0,
                 r2: float = 1.1,
                 w: float = 1.2,
                 L: float = 3.4,
                 layer_slab: LayerSpec = "SLAB150",
                 cross_section: CrossSectionSpec = "strip") -> Component
```

Returns crossing arm.

**Arguments**:

- `r1` - ellipse radius1.
- `r2` - ellipse radius2.
- `w` - width in um.
- `L` - length in um.
- `layer_slab` - for the shallow etch.
- `cross_section` - spec.

<a id="gdsfactory.components.waveguides.crossing_waveguide.crossing"></a>

#### crossing

```python
@gf.cell_with_module_name
def crossing(arm: ComponentSpec = crossing_arm) -> gf.Component
```

Waveguide crossing.

**Arguments**:

- `arm` - arm spec.

<a id="gdsfactory.components.waveguides.crossing_waveguide.crossing_linear_taper"></a>

#### crossing\_linear\_taper

```python
@gf.cell_with_module_name
def crossing_linear_taper(width1: float = 2.5,
                          width2: float = 0.5,
                          length: float = 3,
                          cross_section: CrossSectionSpec = "strip",
                          taper: ComponentSpec = "taper") -> Component
```

Returns Crossing based on a taper.

The default is a dummy taper.

**Arguments**:

- `width1` - input width.
- `width2` - output width.
- `length` - taper length.
- `cross_section` - cross_section spec.
- `taper` - taper spec.

<a id="gdsfactory.components.waveguides.crossing_waveguide.crossing_etched"></a>

#### crossing\_etched

```python
@gf.cell_with_module_name
def crossing_etched(width: float = 0.5,
                    r1: float = 3.0,
                    r2: float = 1.1,
                    w: float = 1.2,
                    L: float = 3.4,
                    layer_wg: LayerSpec = "WG",
                    layer_slab: LayerSpec = "SLAB150") -> Component
```

Waveguide crossing.

Full crossing has to be on WG layer (to start with a 220nm slab).
Then we etch the ellipses down to 150nm slabs and we keep linear taper at 220nm.

**Arguments**:

- `width` - input waveguides width.
- `r1` - radii.
- `r2` - radii.
- `w` - wide width.
- `L` - length.
- `layer_wg` - waveguide layer.
- `layer_slab` - shallow etch layer.

<a id="gdsfactory.components.waveguides.crossing_waveguide.crossing45"></a>

#### crossing45

```python
@gf.cell(check_instances=CheckInstances.IGNORE, with_module_name=True)
def crossing45(crossing: ComponentSpec = crossing,
               port_spacing: float = 40.0,
               dx: Delta | None = None,
               alpha: float = 0.08,
               npoints: int = 101,
               cross_section: CrossSectionSpec = "strip",
               cross_section_bends: CrossSectionSpec = "strip") -> Component
```

Returns 45deg crossing with bends.

**Arguments**:

- `crossing` - crossing function.
- `port_spacing` - target I/O port spacing.
- `dx` - target length.
- `alpha` - optimization parameter. diminish it for tight bends,
  increase it if raises assertion angle errors
- `npoints` - number of points.
- `cross_section` - cross_section spec.
- `cross_section_bends` - cross_section spec.
  
  
  The 45 Degree crossing CANNOT be kept as an SRef since
  we only allow for multiples of 90Deg rotations in SRef.
  
  .. code::
  
  ----   ----
  \ /
  X
  / \
  ---    ----

<a id="gdsfactory.components.waveguides"></a>

# gdsfactory.components.waveguides

<a id="gdsfactory.components.waveguides.straight_piecewise"></a>

# gdsfactory.components.waveguides.straight\_piecewise

<a id="gdsfactory.components.waveguides.straight_piecewise.straight_piecewise"></a>

#### straight\_piecewise

```python
@gf.cell_with_module_name
def straight_piecewise(x: Sequence[float] | Path,
                       widths: Sequence[float],
                       layer: LayerSpec,
                       sections: Sequence[Section] | None = None,
                       port_names: tuple[str | None,
                                         str | None] = ("o1", "o2"),
                       name: str = "core",
                       **kwargs: Any) -> Component
```

Create a component with a piecewise-defined straight waveguide.

**Arguments**:

- `x` - X coordinates or a custom Path object.
- `widths` - Waveguide widths at each corresponding x.
- `layer` - Layer to extrude.
- `sections` - Additional cross-section sections to extrude.
- `port_names` - Port names for the waveguide.
- `name` - Name for the core (main) Section.
- `**kwargs` - Additional keyword arguments for the Section.

<a id="gdsfactory.components.waveguides.straight_heater_metal"></a>

# gdsfactory.components.waveguides.straight\_heater\_metal

<a id="gdsfactory.components.waveguides.straight_heater_metal.straight_heater_metal_undercut"></a>

#### straight\_heater\_metal\_undercut

```python
@gf.cell_with_module_name
def straight_heater_metal_undercut(
        length: float = 320.0,
        length_undercut_spacing: float = 6.0,
        length_undercut: float = 30.0,
        length_straight: float = 0.1,
        length_straight_input: float = 15.0,
        cross_section: CrossSectionSpec = "strip",
        cross_section_heater: CrossSectionSpec = "heater_metal",
        cross_section_waveguide_heater: CrossSectionSpec = "strip_heater_metal",
        cross_section_heater_undercut:
    CrossSectionSpec = "strip_heater_metal_undercut",
        with_undercut: bool = True,
        via_stack: ComponentSpec | None = "via_stack_heater_mtop",
        port_orientation1: int | None = None,
        port_orientation2: int | None = None,
        heater_taper_length: float = 5.0,
        ohms_per_square: float | None = None) -> Component
```

Returns a thermal phase shifter.

dimensions from https://doi.org/10.1364/OE.27.010456

**Arguments**:

- `length` - of the waveguide.
- `length_undercut_spacing` - from undercut regions.
- `length_undercut` - length of each undercut section.
- `length_straight` - length of the straight waveguide.
- `length_straight_input` - from input port to where trenches start.
- `cross_section` - for waveguide ports.
- `cross_section_heater` - for heated sections. heater metal only.
- `cross_section_waveguide_heater` - for heated sections.
- `cross_section_heater_undercut` - for heated sections with undercut.
- `with_undercut` - isolation trenches for higher efficiency.
- `via_stack` - via stack.
- `port_orientation1` - left via stack port orientation. None adds all orientations.
- `port_orientation2` - right via stack port orientation. None adds all orientations.
- `heater_taper_length` - minimizes current concentrations from heater to via_stack.
- `ohms_per_square` - to calculate resistance.

<a id="gdsfactory.components.waveguides.straight_heater_metal.straight_heater_metal_simple"></a>

#### straight\_heater\_metal\_simple

```python
@gf.cell_with_module_name
def straight_heater_metal_simple(
        length: float = 320.0,
        cross_section_heater: CrossSectionSpec = "heater_metal",
        cross_section_waveguide_heater: CrossSectionSpec = "strip_heater_metal",
        via_stack: ComponentSpec | None = "via_stack_heater_mtop",
        port_orientation1: int | None = None,
        port_orientation2: int | None = None,
        heater_taper_length: float = 5.0,
        ohms_per_square: float | None = None) -> Component
```

Returns a thermal phase shifter that has properly fixed electrical connectivity to extract a suitable electrical netlist and models.

dimensions from https://doi.org/10.1364/OE.27.010456.

**Arguments**:

- `length` - of the waveguide.
- `length_undercut` - length of each undercut section.
- `cross_section_heater` - for heated sections. heater metal only.
- `cross_section_waveguide_heater` - for heated sections.
- `via_stack` - via stack.
- `port_orientation1` - left via stack port orientation. None adds all orientations.
- `port_orientation2` - right via stack port orientation. None adds all orientations.
- `heater_taper_length` - minimizes current concentrations from heater to via_stack.
- `ohms_per_square` - to calculate resistance.

<a id="gdsfactory.components.waveguides.straight_heater_doped"></a>

# gdsfactory.components.waveguides.straight\_heater\_doped

<a id="gdsfactory.components.waveguides.straight_heater_doped.straight_heater_doped_rib"></a>

#### straight\_heater\_doped\_rib

```python
@gf.cell_with_module_name
def straight_heater_doped_rib(
        length: float = 320.0,
        nsections: int = 3,
        cross_section: CrossSectionSpec = "strip_rib_tip",
        cross_section_heater: CrossSectionSpec = "rib_heater_doped",
        via_stack: ComponentSpec | None = "via_stack_slab_npp_m3",
        via_stack_metal: ComponentSpec | None = "via_stack_m1_mtop",
        via_stack_metal_size: Size = (10.0, 10.0),
        via_stack_size: Size = (10.0, 10.0),
        taper: ComponentSpec | None = "taper_cross_section",
        heater_width: float = 2.0,
        heater_gap: float = 0.8,
        via_stack_gap: float = 0.0,
        width: float = 0.5,
        xoffset_tip1: float = 0.2,
        xoffset_tip2: float = 0.4) -> Component
```

Returns a doped thermal phase shifter.

dimensions from https://doi.org/10.1364/OE.27.010456

**Arguments**:

- `length` - of the waveguide in um.
- `nsections` - between via_stacks.
- `cross_section` - for the input/output ports.
- `cross_section_heater` - for the heater.
- `via_stack` - optional function to connect the heater strip.
- `via_stack_metal` - function to connect the metal area.
- `via_stack_metal_size` - x, y size in um.
- `via_stack_size` - x, y size in um.
- `taper` - optional taper spec.
- `heater_width` - in um.
- `heater_gap` - in um.
- `via_stack_gap` - from edge of via_stack to waveguide.
- `width` - waveguide width on the ridge.
- `xoffset_tip1` - distance in um from input taper to via_stack.
- `xoffset_tip2` - distance in um from output taper to via_stack.
  
  .. code::
  
  
  length
  |<--------------------------------------------->|
  |              length_section                   |
  |    <--------------------------->              |
  |  length_via_stack                             |
  |    <------->                             taper|
  |    __________                   _________     |
  |   |          |                  |        |    |
  |   | via_stack|__________________|        |    |
  |   |  size    |  heater width    |        |    |
  |  /|__________|__________________|________|\   |
  | / |             heater_gap               | \  |
  |/  |______________________________________|  \ |
  \  |_______________width__________________|  /
  \ |                                      | /
  \|_____________heater_gap______________ |/
  |        |                    |        |
  |        |____heater_width____|        |
  |        |                    |        |
  |________|                    |________|
  
  taper         cross_section_heater
  
  
  
  |<------width------>|
  ____________________ heater_gap             slab_gap
  top_via_stack         |                   |<---------->| bot_via_stack   <-->
  ___ ______________________|                   |___________________________|___
  |   |            |               undoped Si                 |              |   |
  |   |layer_heater|               intrinsic region           |layer_heater  |   |
  |___|____________|__________________________________________|______________|___|
  <------------>
  heater_width
  <------------------------------------------------------------------------------>
  slab_width

<a id="gdsfactory.components.waveguides.straight_heater_doped.straight_heater_doped_strip"></a>

#### straight\_heater\_doped\_strip

```python
@gf.cell_with_module_name
def straight_heater_doped_strip(
        length: float = 320.0,
        nsections: int = 3,
        cross_section: CrossSectionSpec = "strip_heater_doped",
        cross_section_heater: CrossSectionSpec = "rib_heater_doped",
        via_stack: ComponentSpec | None = "via_stack_npp_m1",
        via_stack_metal: ComponentSpec | None = "via_stack_m1_mtop",
        via_stack_metal_size: Size = (10.0, 10.0),
        via_stack_size: Size = (10.0, 10.0),
        taper: ComponentSpec | None = "taper_cross_section",
        heater_width: float = 2.0,
        heater_gap: float = 0.8,
        via_stack_gap: float = 0.0,
        width: float = 0.5,
        xoffset_tip1: float = 0.2,
        xoffset_tip2: float = 0.4) -> Component
```

Top view.

**Arguments**:

- `length` - of the waveguide in um.
- `nsections` - between via_stacks.
- `cross_section` - for the input/output ports.
- `cross_section_heater` - for the heater.
- `via_stack` - optional function to connect the heater strip.
- `via_stack_metal` - function to connect the metal area.
- `via_stack_metal_size` - x, y size in um.
- `via_stack_size` - x, y size in um.
- `taper` - optional taper spec.
- `heater_width` - in um.
- `heater_gap` - in um.
- `via_stack_gap` - from edge of via_stack to waveguide.
- `width` - waveguide width on the ridge.
- `xoffset_tip1` - distance in um from input taper to via_stack.
- `xoffset_tip2` - distance in um from output taper to via_stack.
  
  .. code::
  length
  <-|--------|--------------------------------->
  |        | length_section
  |<--------------------------->
  length_via_stack
  |<------>|
  |________|_______________________________
  /|        |____________________|          |
  / |viastack|                    |via_stack |
  \ | size   |____________________|          |
  \|________|____________________|__________|
  |          |
  cross_section_heater|          |
  |          |
  |          |
  |__________|
  cross_section
  .. code::
  |<------width------>|
  ____________             ___________________               ______________
  |            |           |     undoped Si    |             |              |
  |layer_heater|           |  intrinsic region |<----------->| layer_heater |
  |____________|           |___________________|             |______________|
  <------------>
  heater_gap     heater_width

<a id="gdsfactory.components.waveguides.straight"></a>

# gdsfactory.components.waveguides.straight

Straight waveguide.

<a id="gdsfactory.components.waveguides.straight.straight"></a>

#### straight

```python
@gf.cell_with_module_name
def straight(length: float = 10.0,
             npoints: int = 2,
             cross_section: CrossSectionSpec = "strip",
             width: float | None = None) -> Component
```

Returns a Straight waveguide.

**Arguments**:

- `length` - straight length (um).
- `npoints` - number of points.
- `cross_section` - specification (CrossSection, string or dict).
- `width` - width of the waveguide. If None, it will use the width of the cross_section.
  
  .. code::
  
  o1 -------------- o2
  length

<a id="gdsfactory.components.waveguides.straight.straight_all_angle"></a>

#### straight\_all\_angle

```python
@gf.vcell
def straight_all_angle(length: float = 10.0,
                       npoints: int = 2,
                       cross_section: CrossSectionSpec = "strip",
                       width: float | None = None) -> ComponentAllAngle
```

Returns a Straight waveguide with offgrid ports.

**Arguments**:

- `length` - straight length (um).
- `npoints` - number of points.
- `cross_section` - specification (CrossSection, string or dict).
- `width` - width of the waveguide. If None, it will use the width of the cross_section.
  
  .. code::
  
  o1 -------------- o2
  length

<a id="gdsfactory.components.waveguides.straight.straight_array"></a>

#### straight\_array

```python
@gf.cell_with_module_name
def straight_array(n: int = 4,
                   spacing: float = 4.0,
                   length: float = 10.0,
                   cross_section: CrossSectionSpec = "strip") -> Component
```

Array of straights connected with grating couplers.

useful to align the 4 corners of the chip

**Arguments**:

- `n` - number of straights.
- `spacing` - edge to edge straight spacing.
- `length` - straight length (um).
- `cross_section` - specification (CrossSection, string or dict).

<a id="gdsfactory.components.waveguides.straight.wire_straight"></a>

#### wire\_straight

```python
@gf.cell_with_module_name
def wire_straight(length: float = 10.0,
                  npoints: int = 2,
                  cross_section: CrossSectionSpec = "metal_routing",
                  width: float | None = None) -> Component
```

Returns a Straight waveguide.

**Arguments**:

- `length` - straight length (um).
- `npoints` - number of points.
- `cross_section` - specification (CrossSection, string or dict).
- `width` - width of the waveguide. If None, it will use the width of the cross_section.
  
  .. code::
  
  o1 -------------- o2
  length

<a id="gdsfactory.components.waveguides.straight_pin"></a>

# gdsfactory.components.waveguides.straight\_pin

Straight Doped PIN waveguide.

<a id="gdsfactory.components.waveguides.straight_pin.straight_pin"></a>

#### straight\_pin

```python
@gf.cell_with_module_name
def straight_pin(
        length: float = 500.0,
        cross_section: CrossSectionSpec = pin,
        via_stack: ComponentSpec = "via_stack_slab_m3",
        via_stack_width: float = 10.0,
        via_stack_spacing: float = 2,
        taper: ComponentSpec | None = "taper_strip_to_ridge") -> Component
```

Returns rib waveguide with doping and via_stacks used for PN and PIN modulators.

For PIN:
https://doi.org/10.1364/OE.26.029983

500um length for PI phase shift
https://ieeexplore.ieee.org/document/8268112

to go beyond 2PI, you will need at least 1mm
https://ieeexplore.ieee.org/document/8853396/

For PN:
Typical lengths in practice are 2-5mm depending on doping,engineering and application:
https://opg.optica.org/oe/fulltext.cfm?uri=oe-21-25-30350&id=275107
https://opg.optica.org/oe/fulltext.cfm?uri=oe-20-11-12014&id=233271

**Arguments**:

- `length` - of the waveguide.
- `cross_section` - for the waveguide.
- `via_stack` - for the via_stacks.
- `via_stack_width` - width of the via_stack.
- `via_stack_spacing` - spacing between via_stacks.
- `taper` - optional taper.

<a id="gdsfactory.components.dies.die"></a>

# gdsfactory.components.dies.die

based on phidl.geometry.

<a id="gdsfactory.components.dies.die.die"></a>

#### die

```python
@gf.cell_with_module_name
def die(size: Size = (10000.0, 10000.0),
        street_width: float = 100.0,
        street_length: float = 1000.0,
        die_name: str | None = "chip99",
        text_size: float = 100.0,
        text_location: str | Float2 = "SW",
        layer: LayerSpec | None = "FLOORPLAN",
        bbox_layer: LayerSpec | None = "FLOORPLAN",
        text: ComponentSpec = "text",
        draw_corners: bool = False) -> gf.Component
```

Returns die with optional markers marking the boundary of the die.

**Arguments**:

- `size` - x, y dimensions of the die.
- `street_width` - Width of the corner marks for die-sawing.
- `street_length` - Length of the corner marks for die-sawing.
- `die_name` - Label text. If None, no label is added.
- `text_size` - Label text size.
- `text_location` - {'NW', 'N', 'NE', 'SW', 'S', 'SE'} or (x, y) coordinate.
- `layer` - For street widths. None to not draw the street widths.
- `bbox_layer` - optional bbox layer drawn bounding box around the die.
- `text` - function use for generating text. Needs to accept text, size, layer.
- `draw_corners` - True draws only corners. False draws a square die.

<a id="gdsfactory.components.dies.align"></a>

# gdsfactory.components.dies.align

<a id="gdsfactory.components.dies.align.align_wafer"></a>

#### align\_wafer

```python
@gf.cell_with_module_name
def align_wafer(width: float = 10.0,
                spacing: float = 10.0,
                cross_length: float = 80.0,
                layer: LayerSpec = "WG",
                layer_cladding: tuple[int, int] | None = None,
                square_corner: str = "bottom_left") -> Component
```

Returns cross inside a frame to align wafer.

**Arguments**:

- `width` - in um.
- `spacing` - in um.
- `cross_length` - for the cross.
- `layer` - for the cross.
- `layer_cladding` - optional.
- `square_corner` - bottom_left, bottom_right, top_right, top_left.

<a id="gdsfactory.components.dies.align.add_frame"></a>

#### add\_frame

```python
@gf.cell_with_module_name
def add_frame(component: ComponentSpec = "rectangle",
              width: float = 10.0,
              spacing: float = 10.0,
              layer: LayerSpec = "WG") -> Component
```

Returns component with a frame around it.

**Arguments**:

- `component` - Component to frame.
- `width` - of the frame.
- `spacing` - of component to frame.
- `layer` - frame layer.

<a id="gdsfactory.components.dies.die_with_pads"></a>

# gdsfactory.components.dies.die\_with\_pads

<a id="gdsfactory.components.dies.die_with_pads.die_with_pads"></a>

#### die\_with\_pads

```python
@gf.cell_with_module_name
def die_with_pads(size: Size = (11470.0, 4900.0),
                  ngratings: int = 14,
                  npads: int = 31,
                  grating_pitch: float = 250.0,
                  pad_pitch: float = 300.0,
                  grating_coupler: ComponentSpec = "grating_coupler_te",
                  cross_section: CrossSectionSpec = "strip",
                  pad: ComponentSpec = "pad",
                  layer_floorplan: LayerSpec = "FLOORPLAN",
                  edge_to_pad_distance: float = 150.0,
                  edge_to_grating_distance: float = 150.0,
                  with_loopback: bool = True,
                  loopback_radius: float | None = None) -> Component
```

A die with grating couplers and pads.

**Arguments**:

- `size` - the size of the die, in um.
- `ngratings` - the number of grating couplers.
- `npads` - the number of pads.
- `grating_pitch` - the pitch of the grating couplers, in um.
- `pad_pitch` - the pitch of the pads, in um.
- `grating_coupler` - the grating coupler component.
- `cross_section` - the cross section.
- `pad` - the pad component.
- `layer_floorplan` - the layer of the floorplan.
- `edge_to_pad_distance` - the distance from the edge to the pads, in um.
- `edge_to_grating_distance` - the distance from the edge to the grating couplers, in um.
- `with_loopback` - if True, adds a loopback between edge GCs. Only works for rotation = 90 for now.
- `loopback_radius` - optional radius for loopback.

<a id="gdsfactory.components.dies"></a>

# gdsfactory.components.dies

<a id="gdsfactory.components.dies.wafer"></a>

# gdsfactory.components.dies.wafer

<a id="gdsfactory.components.dies.wafer.wafer"></a>

#### wafer

```python
@gf.cell_with_module_name
def wafer(reticle: ComponentSpec = "die",
          cols: tuple[int, ...] = _cols_200mm_wafer,
          xspacing: float | None = None,
          yspacing: float | None = None,
          die_name_col_row: bool = False) -> Component
```

Returns complete wafer. Useful for mask aligner steps.

**Arguments**:

- `reticle` - spec for each wafer reticle.
- `cols` - how many columns per row.
- `xspacing` - optional spacing, defaults to reticle.xsize.
- `yspacing` - optional spacing, defaults to reticle.ysize.
- `die_name_col_row` - if True, die name is row_col, otherwise is a number

<a id="gdsfactory.components.dies.seal_ring"></a>

# gdsfactory.components.dies.seal\_ring

<a id="gdsfactory.components.dies.seal_ring.seal_ring"></a>

#### seal\_ring

```python
@gf.cell_with_module_name
def seal_ring(size: Float2 = (500, 500),
              seal: ComponentSpec = "via_stack",
              width: float = 10,
              padding: float = 10.0,
              with_north: bool = True,
              with_south: bool = True,
              with_east: bool = True,
              with_west: bool = True) -> gf.Component
```

Returns a continuous seal ring boundary at the chip/die.

Prevents cracks from spreading and shields when connected to ground.

**Arguments**:

- `size` - of the seal.
- `seal` - function for the seal.
- `width` - of the seal.
- `padding` - from component to seal.
- `with_north` - includes seal.
- `with_south` - includes seal.
- `with_east` - includes seal.
- `with_west` - includes seal.

<a id="gdsfactory.components.dies.seal_ring.seal_ring_segmented"></a>

#### seal\_ring\_segmented

```python
@gf.cell_with_module_name
def seal_ring_segmented(size: Float2 = (500, 500),
                        length_segment: float = 10,
                        width_segment: float = 3,
                        spacing_segment: float = 2,
                        corner: ComponentSpec = "via_stack_corner45_extended",
                        via_stack: ComponentSpec = "via_stack_m1_mtop",
                        with_north: bool = True,
                        with_south: bool = True,
                        with_east: bool = True,
                        with_west: bool = True) -> gf.Component
```

Segmented Seal ring.

**Arguments**:

- `size` - of the seal ring.
- `length_segment` - length of each segment.
- `width_segment` - width of each segment.
- `spacing_segment` - spacing between segments.
- `corner` - corner component.
- `via_stack` - via_stack component.
- `with_north` - includes seal.
- `with_south` - includes seal.
- `with_east` - includes seal.
- `with_west` - includes seal.

<a id="gdsfactory.components.filters.fiber_array"></a>

# gdsfactory.components.filters.fiber\_array

<a id="gdsfactory.components.filters.fiber_array.fiber_array"></a>

#### fiber\_array

```python
@gf.cell_with_module_name
def fiber_array(n: int = 8,
                pitch: float = 127.0,
                core_diameter: float = 10,
                cladding_diameter: float = 125,
                layer_core: LayerSpec = "WG",
                layer_cladding: LayerSpec = "WGCLAD") -> Component
```

Returns a fiber array.

**Arguments**:

- `n` - number of fibers.
- `pitch` - spacing.
- `core_diameter` - 10um.
- `cladding_diameter` - in um.
- `layer_core` - layer spec for fiber core.
- `layer_cladding` - layer spec for fiber cladding.
  
  .. code::
  
  pitch
  <->
  _________
  |         | lid
  | o o o o |
  |         | base
  |_________|
  length

<a id="gdsfactory.components.filters.fiber"></a>

# gdsfactory.components.filters.fiber

<a id="gdsfactory.components.filters.fiber.fiber"></a>

#### fiber

```python
@gf.cell_with_module_name
def fiber(core_diameter: float = 10,
          cladding_diameter: float = 125,
          layer_core: LayerSpec = "WG",
          layer_cladding: LayerSpec = "WGCLAD") -> Component
```

Returns a fiber.

**Arguments**:

- `core_diameter` - in um.
- `cladding_diameter` - in um.
- `layer_core` - layer spec for fiber core.
- `layer_cladding` - layer spec for fiber cladding.

<a id="gdsfactory.components.filters.polarization_splitter_rotator"></a>

# gdsfactory.components.filters.polarization\_splitter\_rotator

<a id="gdsfactory.components.filters.polarization_splitter_rotator.polarization_splitter_rotator"></a>

#### polarization\_splitter\_rotator

```python
@gf.cell_with_module_name
def polarization_splitter_rotator(
        width_taper_in: Float3 = (0.54, 0.69, 0.83),
        length_taper_in: Float2 | Float3 = (4.0, 44.0),
        width_coupler: Float2 = (0.9, 0.404),
        length_coupler: float = 7.0,
        gap: float = 0.15,
        width_out: float = 0.54,
        length_out: float = 14.33,
        dy: Delta = 5.0,
        cross_section: CrossSectionSpec = "strip") -> Component
```

Returns polarization splitter rotator.

"Novel concept for ultracompact polarization splitter-rotator
based on silicon nanowires." By D. Dai, and J. E. Bowers
(Optics express vol 19, no. 11 pp. 10940-10949 (2011)).

**Arguments**:

- `width_taper_in` - Three west widths of the input tapers in um.
- `length_taper_in` - Two or three length of the bend regions in um.
- `width_coupler` - Top and bottom widths of the coupling region in um.
- `length_coupler` - Length of the coupling region in um.
- `gap` - Distance between the coupler in um.
- `width_out` - Width of the splitter region in um.
- `length_out` - Length of the splitter region in um.
- `dy` - Port-to-port distance between the splitter region in um.
- `cross_section` - cross-section spec.
  
  

**Notes**:

  The length of third input taper is automatically determined
  if only two lengths are in arguments.

<a id="gdsfactory.components.filters.terminator"></a>

# gdsfactory.components.filters.terminator

<a id="gdsfactory.components.filters.terminator.terminator"></a>

#### terminator

```python
@gf.cell_with_module_name
def terminator(length: float | None = 50,
               cross_section_input: CrossSectionSpec = strip,
               cross_section_tip: CrossSectionSpec | None = None,
               tapered_width: float = 0.2,
               doping_layers: LayerSpecs = ("NPP", ),
               doping_offset: float = 1.0) -> gf.Component
```

Returns doped taper to terminate waveguides.

**Arguments**:

- `length` - distance between input and narrow tapered end.
- `cross_section_input` - input cross-section.
- `cross_section_tip` - cross-section at the end of the termination.
- `tapered_width` - width of the default cross-section at the end of the termination.
  Only used if cross_section_tip is not None.
- `doping_layers` - doping layers to superimpose on the taper. Default N++.
- `doping_offset` - offset of the doping layer beyond the bbox

<a id="gdsfactory.components.filters"></a>

# gdsfactory.components.filters

<a id="gdsfactory.components.filters.mode_converter"></a>

# gdsfactory.components.filters.mode\_converter

<a id="gdsfactory.components.filters.mode_converter.mode_converter"></a>

#### mode\_converter

```python
@gf.cell_with_module_name
def mode_converter(gap: float = 0.3,
                   length: float = 10,
                   coupler_straight_asymmetric:
                   ComponentSpec = "coupler_straight_asymmetric",
                   bend: ComponentSpec = partial(bend_s, size=(25, 3)),
                   taper: ComponentSpec = "taper",
                   mm_width: float = 1.2,
                   mc_mm_width: float = 1,
                   sm_width: float = 0.5,
                   taper_length: float = 25,
                   cross_section: CrossSectionSpec = "strip") -> Component
```

Returns Mode converter from TE0 to TE1.

By matching the effective indices of two waveguides with different widths,
light can couple from different transverse modes e.g. TE0 <-> TE1.
https://doi.org/10.1109/JPHOT.2019.2941742

**Arguments**:

- `gap` - directional coupler gap.
- `length` - coupler length interaction.
- `coupler_straight_asymmetric` - spec.
- `bend` - spec.
- `taper` - spec.
- `mm_width` - input/output multimode waveguide width.
- `mc_mm_width` - mode converter multimode waveguide width
- `sm_width` - single mode waveguide width.
- `taper_length` - taper length.
- `cross_section` - cross_section spec.
  
  .. code::
  
  o2 ---           --- o4
  \         /
  \       /
  -------
  o1 -----=======----- o3
  |-----|
  length
  
  = : multimode width
  - : singlemode width

<a id="gdsfactory.components.filters.dbr_tapered"></a>

# gdsfactory.components.filters.dbr\_tapered

<a id="gdsfactory.components.filters.dbr_tapered.dbr_tapered"></a>

#### dbr\_tapered

```python
@gf.cell_with_module_name
def dbr_tapered(length: float = 10.0,
                period: float = 0.85,
                dc: float = 0.5,
                w1: float = 0.4,
                w2: float = 1.0,
                taper_length: float = 20.0,
                fins: bool = False,
                fin_size: Size = (0.2, 0.05),
                cross_section: CrossSectionSpec = "strip") -> Component
```

Distributed Bragg Reflector Cell class.

Tapers the input straight to a
periodic straight structure with varying width (1-D photonic crystal).

**Arguments**:

- `length` - Length of the DBR region.
- `period` - Period of the repeated unit.
- `dc` - Duty cycle of the repeated unit (must be a float between 0 and 1.0).
- `w1` - thin section width. w1 = 0 corresponds to disconnected periodic blocks.
- `w2` - wide section width.
- `taper_length` - between the input/output straight and the DBR region.
- `fins` - If `True`, adds fins to the input/output straights.
- `fin_size` - Specifies the x- and y-size of the `fins`. Defaults to 200 nm x 50 nm
- `cross_section` - cross_section spec.
  
  .. code::
  
  period
  <-----><-------->
  _________
  _______|
  
  w1       w2       ...  n times
  _______
  |_________

<a id="gdsfactory.components.filters.awg"></a>

# gdsfactory.components.filters.awg

Sample AWG.

<a id="gdsfactory.components.filters.awg.free_propagation_region"></a>

#### free\_propagation\_region

```python
@gf.cell_with_module_name
def free_propagation_region(
        width1: float = 2.0,
        width2: float = 20.0,
        length: float = 20.0,
        wg_width: float = 0.5,
        inputs: int = 1,
        outputs: int = 10,
        cross_section: CrossSectionSpec = "strip") -> Component
```

Free propagation region.

**Arguments**:

- `width1` - width of the input region.
- `width2` - width of the output region.
- `length` - length of the free propagation region.
- `wg_width` - waveguide width.
- `inputs` - number of inputs.
- `outputs` - number of outputs.
- `cross_section` - cross_section function.
  
  .. code::
  
  length
  <-->
  /|
  / |
  width1|  | width2
  \ |
  \|

<a id="gdsfactory.components.filters.awg.awg"></a>

#### awg

```python
@gf.cell_with_module_name
def awg(arms: int = 10,
        outputs: int = 3,
        free_propagation_region_input_function:
        ComponentSpec = free_propagation_region_input,
        free_propagation_region_output_function:
        ComponentSpec = free_propagation_region_output,
        fpr_spacing: float = 50.0,
        arm_spacing: float = 1.0,
        cross_section: CrossSectionSpec = "strip") -> Component
```

Returns a basic Arrayed Waveguide grating.

To simulate you can use
https://github.com/dnrobin/awg-python

**Arguments**:

- `arms` - number of arms.
- `outputs` - number of outputs.
- `free_propagation_region_input_function` - for input.
- `free_propagation_region_output_function` - for output.
- `fpr_spacing` - x separation between input/output free propagation region.
- `arm_spacing` - y separation between arms.
- `cross_section` - cross_section function.

<a id="gdsfactory.components.filters.dbr"></a>

# gdsfactory.components.filters.dbr

DBR gratings.

wavelength = 2*period*neff
period = wavelength/2/neff

dbr default parameters are from Stephen Lin thesis
https://open.library.ubc.ca/cIRcle/collections/ubctheses/24/items/1.0388871

Period: 318nm, width: 500nm, dw: 20 ~ 120 nm.

<a id="gdsfactory.components.filters.dbr.dbr_cell"></a>

#### dbr\_cell

```python
@gf.cell_with_module_name
def dbr_cell(w1: float = w1,
             w2: float = w2,
             l1: float = period / 2,
             l2: float = period / 2,
             cross_section: CrossSectionSpec = "strip") -> Component
```

Distributed Bragg Reflector unit cell.

**Arguments**:

- `w1` - thin width in um.
- `l1` - thin length in um.
- `w2` - thick width in um.
- `l2` - thick length in um.
- `n` - number of periods.
- `cross_section` - cross_section spec.
  
  .. code::
  
  l1      l2
  <-----><-------->
  _________
  _______|
  
  w1       w2
  _______
  |_________

<a id="gdsfactory.components.filters.dbr.dbr"></a>

#### dbr

```python
@gf.cell_with_module_name
def dbr(w1: float = w1,
        w2: float = w2,
        l1: float = period / 2,
        l2: float = period / 2,
        n: int = 10,
        cross_section: CrossSectionSpec = "strip",
        straight_length: float = 10e-3) -> Component
```

Distributed Bragg Reflector.

**Arguments**:

- `w1` - thin width in um.
- `w2` - thick width in um.
- `l1` - thin length in um.
- `l2` - thick length in um.
- `n` - number of periods.
- `cross_section` - cross_section spec.
- `straight_length` - length of the straight section between cutbacks.
  
  .. code::
  
  l1      l2
  <-----><-------->
  _________
  _______|
  
  w1       w2       ...  n times
  _______
  |_________

<a id="gdsfactory.components.filters.loop_mirror"></a>

# gdsfactory.components.filters.loop\_mirror

Sagnac loop_mirror.

<a id="gdsfactory.components.filters.loop_mirror.loop_mirror"></a>

#### loop\_mirror

```python
@gf.cell_with_module_name
def loop_mirror(component: ComponentSpec = "mmi1x2",
                bend90: ComponentSpec = "bend_euler",
                cross_section: CrossSectionSpec = "strip") -> Component
```

Returns Sagnac loop_mirror.

**Arguments**:

- `component` - 1x2 splitter.
- `bend90` - 90 deg bend.
- `cross_section` - cross_section settings.

<a id="gdsfactory.components.filters.terminator_spiral"></a>

# gdsfactory.components.filters.terminator\_spiral

<a id="gdsfactory.components.filters.terminator_spiral.terminator_spiral"></a>

#### terminator\_spiral

```python
@gf.cell_with_module_name
def terminator_spiral(
        separation: float = 3.0,
        width_tip: float = 0.2,
        number_of_loops: float = 1,
        npoints: int = 1000,
        min_bend_radius: float | None = None,
        cross_section: CrossSectionSpec = "strip") -> gf.Component
```

Returns doped taper to terminate waveguides.

**Arguments**:

- `separation` - separation between the loops.
- `width_tip` - width of the default cross-section at the end of the termination.
  Only used if cross_section_tip is not None.
- `number_of_loops` - number of loops in the spiral.
- `npoints` - points for the spiral.
- `min_bend_radius` - minimum bend radius for the spiral.
- `cross_section` - input cross-section.

<a id="gdsfactory.components.pads.pads_shorted"></a>

# gdsfactory.components.pads.pads\_shorted

<a id="gdsfactory.components.pads.pads_shorted.pads_shorted"></a>

#### pads\_shorted

```python
@gf.cell_with_module_name
def pads_shorted(pad: ComponentSpec = "pad",
                 columns: int = 8,
                 pad_pitch: float = 150.0,
                 layer_metal: LayerSpec = "MTOP",
                 metal_width: float = 10) -> Component
```

Returns a 1D array of shorted_pads.

**Arguments**:

- `pad` - pad spec.
- `columns` - number of columns.
- `pad_pitch` - in um
- `layer_metal` - for the short.
- `metal_width` - for the short.

<a id="gdsfactory.components.pads.pad_gsg"></a>

# gdsfactory.components.pads.pad\_gsg

High speed GSG pads.

<a id="gdsfactory.components.pads.pad_gsg.pad_gsg_short"></a>

#### pad\_gsg\_short

```python
@gf.cell_with_module_name
def pad_gsg_short(size: Float2 = (22, 7),
                  layer_metal: LayerSpec = "MTOP",
                  metal_spacing: float = 5.0,
                  short: bool = True,
                  pad: ComponentSpec = "pad",
                  pad_pitch: float = 150,
                  route_xsize: float = 50) -> gf.Component
```

Returns high speed GSG pads for calibrating the RF probes.

**Arguments**:

- `size` - for the short.
- `layer_metal` - for the short.
- `metal_spacing` - in um.
- `short` - if False returns an open.
- `pad` - function for pad.
- `pad_pitch` - in um.
- `route_xsize` - in um.

<a id="gdsfactory.components.pads"></a>

# gdsfactory.components.pads

<a id="gdsfactory.components.pads.rectangle_with_slits"></a>

# gdsfactory.components.pads.rectangle\_with\_slits

<a id="gdsfactory.components.pads.rectangle_with_slits.rectangle_with_slits"></a>

#### rectangle\_with\_slits

```python
@gf.cell_with_module_name
def rectangle_with_slits(size: Size = (100.0, 200.0),
                         layer: LayerSpec = "WG",
                         layer_slit: LayerSpec = "SLAB150",
                         centered: bool = False,
                         port_type: str | None = None,
                         slit_size: Size = (1.0, 1.0),
                         slit_column_pitch: float = 20,
                         slit_row_pitch: float = 20,
                         slit_enclosure: float = 10) -> Component
```

Returns a rectangle with slits.

Metal slits reduce stress.

**Arguments**:

- `size` - (tuple) Width and height of rectangle.
- `layer` - Specific layer to put polygon geometry on.
- `layer_slit` - does a boolean NOT when None.
- `centered` - True sets center to (0, 0), False sets south-west to (0, 0)
- `port_type` - for the rectangle.
- `slit_size` - x, y slit size.
- `slit_column_pitch` - pitch for columns of slits.
- `slit_row_pitch` - pitch for rows of slits.
- `slit_enclosure` - from slit to rectangle edge.
  
  .. code::
  
  slit_enclosure
  _____________________________________
  |<--->                              |
  |                                   |
  |      ______________________       |
  |     |                      |      |
  |     |                      | slit_size[1]
  |  _  |______________________|      |
  |  |                                |
  |  | slit_row_pitch                 |
  |  |                                |  size[1]
  |  |   ______________________       |
  |  |  |                      |      |
  |  |  |                      |      |
  |  _  |______________________|      |
  |     <--------------------->       |
  |            slit_size[0]           |
  |___________________________________|
  size[0]

<a id="gdsfactory.components.pads.pad"></a>

# gdsfactory.components.pads.pad

<a id="gdsfactory.components.pads.pad.pad"></a>

#### pad

```python
@gf.cell_with_module_name
def pad(size: Size | str = (100.0, 100.0),
        layer: LayerSpec = "MTOP",
        bbox_layers: tuple[LayerSpec, ...] | None = None,
        bbox_offsets: tuple[float, ...] | None = None,
        port_inclusion: float = 0,
        port_orientation: AngleInDegrees | None = 0,
        port_orientations: Ints | None = (180, 90, 0, -90),
        port_type: str = "pad") -> Component
```

Returns rectangular pad with ports.

**Arguments**:

- `size` - x, y size.
- `layer` - pad layer.
- `bbox_layers` - list of layers.
- `bbox_offsets` - Optional offsets for each layer with respect to size.
  positive grows, negative shrinks the size.
- `port_inclusion` - from edge.
- `port_orientation` - in degrees for the center port.
- `port_orientations` - list of port_orientations to add. None does not add ports.
- `port_type` - port type for pad port.

<a id="gdsfactory.components.pads.pad.pad_array"></a>

#### pad\_array

```python
@gf.cell_with_module_name
def pad_array(pad: ComponentSpec = "pad",
              columns: int = 6,
              rows: int = 1,
              column_pitch: float = 150.0,
              row_pitch: float = 150.0,
              port_orientation: AngleInDegrees = 0,
              size: Float2 | None = None,
              layer: LayerSpec | None = "MTOP",
              centered_ports: bool = False,
              auto_rename_ports: bool = False) -> Component
```

Returns 2D array of pads.

**Arguments**:

- `pad` - pad element.
- `columns` - number of columns.
- `rows` - number of rows.
- `column_pitch` - x pitch.
- `row_pitch` - y pitch.
- `port_orientation` - port orientation in deg. None for low speed DC ports.
- `size` - pad size.
- `layer` - pad layer.
- `centered_ports` - True add ports to center. False add ports to the edge.
- `auto_rename_ports` - True to auto rename ports.

<a id="gdsfactory.components.mmis.mmi"></a>

# gdsfactory.components.mmis.mmi

<a id="gdsfactory.components.mmis.mmi.mmi"></a>

#### mmi

```python
@gf.cell_with_module_name
def mmi(inputs: int = 1,
        outputs: int = 4,
        width: float | None = None,
        width_taper: float = 1.0,
        length_taper: float = 10.0,
        length_mmi: float = 5.5,
        width_mmi: float = 5,
        gap_input_tapers: float = 0.25,
        gap_output_tapers: float = 0.25,
        taper: ComponentSpec = "taper",
        straight: ComponentSpec = "straight",
        cross_section: CrossSectionSpec = "strip",
        input_positions: list[float] | None = None,
        output_positions: list[float] | None = None) -> Component
```

Mxn MultiMode Interferometer (MMI).

**Arguments**:

- `inputs` - number of inputs.
- `outputs` - number of outputs.
- `width` - input and output straight width. Defaults to cross_section.
- `width_taper` - interface between input straights and mmi region.
- `length_taper` - into the mmi region.
- `length_mmi` - in x direction.
- `width_mmi` - in y direction.
- `gap_input_tapers` - gap between input tapers from edge to edge.
- `gap_output_tapers` - gap between output tapers from edge to edge.
- `taper` - taper function.
- `straight` - straight function.
- `cross_section` - specification (CrossSection, string or dict).
- `input_positions` - optional positions of the inputs.
- `output_positions` - optional positions of the outputs.
  
  .. code::
  
  length_mmi
  <------>
  ________
  |        |
  __/          \__
  o2  __            __  o3
  \          /_ _ _ _
  |         | _ _ _ _| gap_output_tapers
  __/          \__
  o1  __            __  o4
  \          /
  |________|
  | |
  <->
  length_taper

<a id="gdsfactory.components.mmis.mmi1x2"></a>

# gdsfactory.components.mmis.mmi1x2

<a id="gdsfactory.components.mmis.mmi1x2.mmi1x2"></a>

#### mmi1x2

```python
@gf.cell_with_module_name
def mmi1x2(width: float | None = None,
           width_taper: float = 1.0,
           length_taper: float = 10.0,
           length_mmi: float = 5.5,
           width_mmi: float = 2.5,
           gap_mmi: float = 0.25,
           taper: ComponentSpec = taper_function,
           straight: ComponentSpec = straight_function,
           cross_section: CrossSectionSpec = "strip") -> Component
```

1x2 MultiMode Interferometer (MMI).

**Arguments**:

- `width` - input and output straight width. Defaults to cross_section width.
- `width_taper` - interface between input straights and mmi region.
- `length_taper` - into the mmi region.
- `length_mmi` - in x direction.
- `width_mmi` - in y direction.
- `gap_mmi` - gap between tapered wg.
- `taper` - taper function.
- `straight` - straight function.
- `cross_section` - specification (CrossSection, string or dict).
  
  
  .. code::
  
  length_mmi
  <------>
  ________
  |        |
  |         \__
  |          __  o2
  __/          /_ _ _ _
  o1 __          | _ _ _ _| gap_mmi
  \          \__
  |          __  o3
  |         /
  |________|
  
  <->
  length_taper

<a id="gdsfactory.components.mmis.mmi_90degree_hybrid"></a>

# gdsfactory.components.mmis.mmi\_90degree\_hybrid

<a id="gdsfactory.components.mmis.mmi_90degree_hybrid.mmi_90degree_hybrid"></a>

#### mmi\_90degree\_hybrid

```python
@gf.cell_with_module_name
def mmi_90degree_hybrid(
        width: float = 0.5,
        width_taper: float = 1.7,
        length_taper: float = 40.0,
        length_mmi: float = 175.0,
        width_mmi: float = 10.0,
        gap_mmi: float = 0.8,
        straight: ComponentSpec = "straight",
        cross_section: CrossSectionSpec = "strip") -> Component
```

90 degree hybrid based on a 4x4 MMI.

Default values from Watanabe et al.,
"Coherent few mode demultiplexer realized as a
2D grating coupler array in silicon", Optics Express 28(24), 2020

It could be interesting to consider the design in Guan et al.,
"Compact and low loss 90° optical hybrid on a silicon-on-insulator
platform", Optics Express 25(23), 2017

**Arguments**:

- `width` - input and output straight width.
- `width_taper` - interface between input straights and mmi region.
- `length_taper` - into the mmi region.
- `length_mmi` - in x direction.
- `width_mmi` - in y direction.
- `gap_mmi` - (width_taper + gap between tapered wg)/2.
- `straight` - straight function.
- `with_bbox` - box in bbox_layers and bbox_offsets avoid DRC sharp edges.
- `cross_section` - spec.
  
  
  .. code::
  
  length_mmi
  <------>
  ________
  |        |
  __/          \__
  signal_in  __            __  I_out1
  \          /_ _ _ _
  |         | _ _ _ _| gap_mmi
  |          \__
  |           __  Q_out1
  |          /
  |        |
  |
  __/          \__
  LO_in   __            __  Q_out2
  \          /_ _ _ _
  |         | _ _ _ _| gap_mmi
  |          \__
  |           __  I_out2
  |          /
  | ________|
  
  
  <->
  length_taper

<a id="gdsfactory.components.mmis.mmi_tapered"></a>

# gdsfactory.components.mmis.mmi\_tapered

<a id="gdsfactory.components.mmis.mmi_tapered.mmi_tapered"></a>

#### mmi\_tapered

```python
@gf.cell_with_module_name
def mmi_tapered(inputs: int = 1,
                outputs: int = 2,
                width: float | None = None,
                width_taper_in: float = 2.0,
                length_taper_in: float = 1.0,
                width_taper_out: float | None = None,
                length_taper_out: float | None = None,
                width_taper: float = 1.0,
                length_taper: float = 10.0,
                length_taper_start: float | None = None,
                length_taper_end: float | None = None,
                length_mmi: float = 5.5,
                width_mmi: float = 5,
                width_mmi_inner: float | None = None,
                gap_input_tapers: float = 0.25,
                gap_output_tapers: float = 0.25,
                taper: ComponentFactory = taper_function,
                cross_section: CrossSectionSpec = "strip",
                input_positions: list[float] | None = None,
                output_positions: list[float] | None = None) -> Component
```

Mxn MultiMode Interferometer (MMI).

This is jut a more general version of the mmi component.
Make sure you simulate and optimize the component before using it.

**Arguments**:

- `inputs` - number of inputs.
- `outputs` - number of outputs.
- `width` - input and output straight width. Defaults to cross_section.
- `width_taper_in` - interface between input straights and mmi region.
- `length_taper_in` - into the mmi region.
- `width_taper_out` - interface between mmi region and output straights.
- `length_taper_out` - into the mmi region.
- `width_taper` - interface between mmi region and output straights.
- `length_taper` - into the mmi region.
- `length_taper_start` - length of the taper at the start. Defaults to length_taper.
- `length_taper_end` - length of the taper at the end. Defaults to length_taper.
- `length_mmi` - in x direction.
- `width_mmi` - in y direction.
- `width_mmi_inner` - allows adding a different width for the inner mmi region.
- `gap_input_tapers` - gap between input tapers from edge to edge.
- `gap_output_tapers` - gap between output tapers from edge to edge.
- `taper` - taper function.
- `cross_section` - specification (CrossSection, string or dict).
- `input_positions` - optional positions of the inputs.
- `output_positions` - optional positions of the outputs.
  
  .. code::
  
  ┌───────────┐
  │           ├───────────────┐
  │           │               ├────────────┐
  width_taper             │           │               │            │
  ▲ ┌────────────────┤           │               ├────────────┘
  │ │                │           ├───────────────┘
  ┌───────────┼─┤                │           │
  │           │ │                │           │
  ◄───────────┼─►                │           ├───────────────┐
  └───────────┼─┐                │           │               ├─────────────┐
  ▼ └────────────────┤           │               │             │
  ◄───────────────►│           │               ├─────────────┘
  length_taper    length_taper_in│           ├───────────────┘ length_taper
  ◄────────────►                 └───────────┘◄────────────►  ◄────────────►
  start                                  length_taper_out      end
  ◄───────────►
  length_mmi

<a id="gdsfactory.components.mmis.mmi1x2_with_sbend"></a>

# gdsfactory.components.mmis.mmi1x2\_with\_sbend

<a id="gdsfactory.components.mmis.mmi1x2_with_sbend.mmi1x2_with_sbend"></a>

#### mmi1x2\_with\_sbend

```python
@gf.cell_with_module_name
def mmi1x2_with_sbend(with_sbend: bool = True,
                      s_bend: ComponentFactory = bend_s,
                      cross_section: CrossSectionSpec = "strip") -> Component
```

Returns 1x2 splitter for Cband.

https://opg.optica.org/oe/fulltext.cfm?uri=oe-21-1-1310&id=248418

**Arguments**:

- `with_sbend` - add sbend.
- `s_bend` - S-bend spec.
- `cross_section` - spec.

<a id="gdsfactory.components.mmis"></a>

# gdsfactory.components.mmis

<a id="gdsfactory.components.mmis.mmi2x2_with_sbend"></a>

# gdsfactory.components.mmis.mmi2x2\_with\_sbend

<a id="gdsfactory.components.mmis.mmi2x2_with_sbend.mmi2x2_with_sbend"></a>

#### mmi2x2\_with\_sbend

```python
@gf.cell_with_module_name
def mmi2x2_with_sbend(with_sbend: bool = True,
                      s_bend: ComponentFactory = bend_s,
                      cross_section: CrossSectionSpec = "strip") -> Component
```

Returns mmi2x2 for Cband.

C_band 2x2MMI in 220nm thick silicon
https://opg.optica.org/oe/fulltext.cfm?uri=oe-25-23-28957&id=376719

**Arguments**:

- `with_sbend` - add sbend.
- `s_bend` - S-bend function.
- `cross_section` - spec.

<a id="gdsfactory.components.mmis.mmi2x2"></a>

# gdsfactory.components.mmis.mmi2x2

<a id="gdsfactory.components.mmis.mmi2x2.mmi2x2"></a>

#### mmi2x2

```python
@gf.cell_with_module_name
def mmi2x2(width: float | None = None,
           width_taper: float = 1.0,
           length_taper: float = 10.0,
           length_mmi: float = 5.5,
           width_mmi: float = 2.5,
           gap_mmi: float = 0.25,
           taper: ComponentSpec = taper_function,
           straight: ComponentSpec = straight_function,
           cross_section: CrossSectionSpec = "strip") -> Component
```

Mmi 2x2.

**Arguments**:

- `width` - input and output straight width.
- `width_taper` - interface between input straights and mmi region.
- `length_taper` - into the mmi region.
- `length_mmi` - in x direction.
- `width_mmi` - in y direction.
- `gap_mmi` - (width_taper + gap between tapered wg)/2.
- `taper` - taper function.
- `straight` - straight function.
- `cross_section` - spec.
  
  
  .. code::
  
  length_mmi
  <------>
  ________
  |        |
  __/          \__
  o2  __            __  o3
  \          /_ _ _ _
  |         | _ _ _ _| gap_mmi
  __/          \__
  o1  __            __  o4
  \          /
  |________|
  
  <->
  length_taper

<a id="gdsfactory.samples.snap_issue"></a>

# gdsfactory.samples.snap\_issue

snap issue.

<a id="gdsfactory.samples.41_verification_routing"></a>

# gdsfactory.samples.41\_verification\_routing

<a id="gdsfactory.samples.07_flattening_device"></a>

# gdsfactory.samples.07\_flattening\_device

__Flattening a Component.__


Sometimes you want to remove cell structure from a Component while keeping all
of the shapes/polygons intact and in place.

The Component.flatten() method flattens current Component by copying all polygons from the underlying references.

<a id="gdsfactory.samples.02_component_autoname"></a>

# gdsfactory.samples.02\_component\_autoname

When you create components you have to make sure they have unique names.

the cell decorator gives unique names to components that depend on their parameters.

<a id="gdsfactory.samples.24_doe_3"></a>

# gdsfactory.samples.24\_doe\_3

Design of Experiment (DOE) with custom add_fiber_array function.

In this case add_fiber_array does not add labels.

You can use gf.add_labels.add_labels_to_ports.

<a id="gdsfactory.samples.06_remapping_layers"></a>

# gdsfactory.samples.06\_remapping\_layers

You can remap layers.

<a id="gdsfactory.samples.30_lidar_pcell"></a>

# gdsfactory.samples.30\_lidar\_pcell

LiDAR demo.

Exercise1. increase the number of elements of the phase array.

Exercise2. Make a PCell.

<a id="gdsfactory.samples.30_lidar_pcell.lidar"></a>

#### lidar

```python
@gf.cell
def lidar(
    noutputs: int = 2**2,
    antenna_pitch: float = 2.0,
    splitter_tree_spacing: Spacing = (50.0, 70.0)
) -> gf.Component
```

LiDAR demo.

**Arguments**:

- `noutputs` - number of outputs.
- `antenna_pitch` - pitch of the antennas.
- `splitter_tree_spacing` - spacing of the splitter tree.

<a id="gdsfactory.samples.21_add_fiber_array"></a>

# gdsfactory.samples.21\_add\_fiber\_array

You can route all component optical ports to a fiber array.

<a id="gdsfactory.samples.sample_reticle_with_labels"></a>

# gdsfactory.samples.sample\_reticle\_with\_labels

<a id="gdsfactory.samples.sample_reticle_with_labels.label_farthest_right_port"></a>

#### label\_farthest\_right\_port

```python
def label_farthest_right_port(component: gf.Component, ports: Ports,
                              layer: LayerSpec, text: str) -> gf.Component
```

Adds a label to the right of the farthest right port in a given component.

**Arguments**:

- `component` - The component to which the label is added.
- `ports` - A list of ports to evaluate for positioning the label.
- `layer` - The layer on which the label will be added.
- `text` - The text to display in the label.

<a id="gdsfactory.samples.sample_reticle_with_labels.spiral_gc"></a>

#### spiral\_gc

```python
def spiral_gc(length: float = 0, **kwargs: Any) -> gf.Component
```

Returns a spiral double with Grating Couplers.

**Arguments**:

- `length` - length of the spiral straight section.
- `kwargs` - additional settings.
  

**Arguments**:

- `bend` - bend component.
- `straight` - straight component.
- `cross_section` - cross_section component.
- `spacing` - spacing between the spiral loops.
- `n_loops` - number of loops.

<a id="gdsfactory.samples.sample_reticle_with_labels.mzi_gc"></a>

#### mzi\_gc

```python
def mzi_gc(length_x: float = 10, **kwargs: Any) -> gf.Component
```

Returns a MZI with Grating Couplers.

**Arguments**:

- `length_x` - length of the MZI.
- `kwargs` - additional settings.

<a id="gdsfactory.samples.sample_reticle_with_labels.sample_reticle_with_labels"></a>

#### sample\_reticle\_with\_labels

```python
def sample_reticle_with_labels(grid: bool = False) -> gf.Component
```

Returns MZI with TE grating couplers.

<a id="gdsfactory.samples.01_component_pcell_with_ports"></a>

# gdsfactory.samples.01\_component\_pcell\_with\_ports

You can add ports to connect components .

<a id="gdsfactory.samples.01_component_pcell_with_ports.straight_narrow"></a>

#### straight\_narrow

```python
@gf.cell
def straight_narrow(length: float = 5.0,
                    width: float = 0.3,
                    layer: LayerSpec = (1, 0)) -> gf.Component
```

Returns straight Component.

**Arguments**:

- `length` - of the straight.
- `width` - in um.
- `layer` - layer spec.

<a id="gdsfactory.samples.19_references"></a>

# gdsfactory.samples.19\_references

<a id="gdsfactory.samples.34_route_edge_coupler_bend_s"></a>

# gdsfactory.samples.34\_route\_edge\_coupler\_bend\_s

Sample reticle with MZIs and edge couplers.

<a id="gdsfactory.samples.34_route_edge_coupler_bend_s.sample_reticle"></a>

#### sample\_reticle

```python
@gf.cell
def sample_reticle(
    size: Size = (1500, 2000),
    ec: str = "edge_coupler_silicon",
    bend_s: ComponentFactory | None = partial(gf.c.bend_s, size=(100, 100))
) -> gf.Component
```

Returns MZI with edge couplers.

**Arguments**:

- `size` - size of the reticle.
- `ec` - edge coupler component name.
- `bend_s` - bend_s component.

<a id="gdsfactory.samples.17_ports"></a>

# gdsfactory.samples.17\_ports

Ports define where each port has the follow properties.

- name
- center: (x, y)
- width:
- orientation: (deg) 0, 90, 180, 270.
    where 0 faces east, 90 (north), 180 (west), 270 (south)

<a id="gdsfactory.samples.17_ports.component_with_port"></a>

#### component\_with\_port

```python
@gf.cell
def component_with_port(length: float = 5.0,
                        width: float = 0.5,
                        layer: LayerSpec = "WG") -> Component
```

Returns a component with one port on the west side.

**Arguments**:

- `length` - in um.
- `width` - waveguide width in um.
- `layer` - layer.

<a id="gdsfactory.samples.30_lidar_with_pads"></a>

# gdsfactory.samples.30\_lidar\_with\_pads

LiDAR demo with pads.

Exercise1. increase the number of elements of the phase array.

Exercise2. Make a PCell.

<a id="gdsfactory.samples.34_route_edge_coupler"></a>

# gdsfactory.samples.34\_route\_edge\_coupler

Sample reticle with MZIs and edge couplers.

<a id="gdsfactory.samples.34_route_edge_coupler.sample_reticle"></a>

#### sample\_reticle

```python
@gf.cell
def sample_reticle(size: Size = (1000, 1000),
                   ec: str = "edge_coupler_silicon") -> gf.Component
```

Returns MZI with edge couplers.

**Arguments**:

- `size` - size of the reticle.
- `ec` - edge coupler component name.

<a id="gdsfactory.samples.coh_tx_dual_pol"></a>

# gdsfactory.samples.coh\_tx\_dual\_pol

<a id="gdsfactory.samples.coh_tx_dual_pol.coh_tx_dual_pol"></a>

#### coh\_tx\_dual\_pol

```python
@gf.cell
def coh_tx_dual_pol(splitter: ComponentSpec = "mmi1x2",
                    combiner: ComponentSpec | None = None,
                    spol_coh_tx: ComponentSpec = coh_tx_single_pol,
                    yspacing: float = 10.0,
                    xspacing: float = 40.0,
                    input_coupler: ComponentSpec | None = None,
                    output_coupler: ComponentSpec | None = None,
                    cross_section: CrossSectionSpec = "strip") -> Component
```

Dual polarization coherent transmitter.

**Arguments**:

- `splitter` - splitter function.
- `combiner` - combiner function.
- `spol_coh_tx` - function generating a coherent tx for a single polarization.
- `yspacing` - vertical spacing between each single polarization coherent tx.
- `xspacing` - horizontal spacing between splitter and combiner.
- `input_coupler` - Optional coupler to add before the splitter.
- `output_coupler` - Optional coupler to add after the combiner.
- `cross_section` - for routing (splitter to mzms and mzms to combiners).
  
  .. code::
  
  ___ single_pol_tx__
  |                  |
  |                  |
  |                  |
  (in_coupler)---splitter==|                  |==combiner---(out_coupler)
  |                  |
  |                  |
  |___ single_pol_tx_|

<a id="gdsfactory.samples.05_remove_layers"></a>

# gdsfactory.samples.05\_remove\_layers

You can remove a list of layers from a component.

<a id="gdsfactory.samples.coh_rx_single_pol"></a>

# gdsfactory.samples.coh\_rx\_single\_pol

<a id="gdsfactory.samples.coh_rx_single_pol.coh_rx_single_pol"></a>

#### coh\_rx\_single\_pol

```python
@gf.cell
def coh_rx_single_pol(
        bend: ComponentSpec = "bend_euler",
        cross_section: CrossSectionSpec = "strip",
        hybrid_90deg: ComponentSpec = gf.c.mmi_90degree_hybrid,
        detector: ComponentSpec = gf.c.ge_detector_straight_si_contacts,
        det_spacing: Spacing = (60.0, 50.0),
        in_wg_length: float = 20.0,
        lo_input_coupler: ComponentSpec | None = None,
        signal_input_coupler: ComponentSpec | None = None,
        cross_section_metal_top: CrossSectionSpec = "metal3",
        cross_section_metal: CrossSectionSpec = "metal2") -> Component
```

Single polarization coherent receiver.

**Arguments**:

- `bend` - 90 degrees bend library.
- `cross_section` - for routing.
- `hybrid_90deg` - generates the 90 degree hybrid.
- `detector` - generates the detector.
- `det_spacing` - spacing between 90 degree hybrid and detector and
  vertical spacing between detectors.
- `in_wg_length` - length of the straight waveguides at the input of the 90 deg hybrid.
- `lo_input_coupler` - Optional coupler for the LO.
- `signal_input_coupler` - Optional coupler for the signal.
- `cross_section_metal_top` - cross_section for the top metal layer.
- `cross_section_metal` - cross_section for the metal layer.
- `cross_section` - cross_section for the waveguides.
  
  .. code::
  
  _________
  (lo_in_coupler)---|          |--- detI1 \\ __ i signal
  |  90 deg  |--- detI2 //
  (signal_in_coupler)---|  hybrid  |--- detQ1 \\ __ q signal
  |__________|--- detQ2 //

<a id="gdsfactory.samples.03_move"></a>

# gdsfactory.samples.03\_move

based on phidl tutorial.

__Manipulating geometry 1 - Basic movement and rotation__


There are several actions we can take to move and rotate the geometry.
These actions include movement, rotation, and reflection.

<a id="gdsfactory.samples.18_port_pins"></a>

# gdsfactory.samples.18\_port\_pins

You can define a function to add pins.

<a id="gdsfactory.samples.24_doe"></a>

# gdsfactory.samples.24\_doe

Lets pack a doe and export it with metadata.

<a id="gdsfactory.samples"></a>

# gdsfactory.samples

<a id="gdsfactory.samples.01_component_pcell_with_parameters"></a>

# gdsfactory.samples.01\_component\_pcell\_with\_parameters

<a id="gdsfactory.samples.08_grid"></a>

# gdsfactory.samples.08\_grid

Group components in a cell using grid.

<a id="gdsfactory.samples.13_component_netlist"></a>

# gdsfactory.samples.13\_component\_netlist

<a id="gdsfactory.samples.13_component_netlist.netlist_yaml"></a>

#### netlist\_yaml

```python
@gf.cell
def netlist_yaml() -> Component
```

Test netlist yaml.

.. code::

    arm_top
     _____
    |     |
CP1=       =CP2=
    |_____|

     arm_bot

<a id="gdsfactory.samples.snap_bends_fixed"></a>

# gdsfactory.samples.snap\_bends\_fixed

Snap bends together.

<a id="gdsfactory.samples.fixme.route_bundle_bbox"></a>

# gdsfactory.samples.fixme.route\_bundle\_bbox

<a id="gdsfactory.samples.22_add_pads"></a>

# gdsfactory.samples.22\_add\_pads

You can also use the fiber array routing functions for connecting to pads.

<a id="gdsfactory.samples.sample_mzis"></a>

# gdsfactory.samples.sample\_mzis

<a id="gdsfactory.samples.demo.layers_xsection"></a>

# gdsfactory.samples.demo.layers\_xsection

<a id="gdsfactory.samples.demo.drc_errors"></a>

# gdsfactory.samples.demo.drc\_errors

Write GDS with sample errors.

<a id="gdsfactory.samples.demo.drc_errors.enclosing"></a>

#### enclosing

```python
@gf.cell
def enclosing(
    enclosing: float = 0.1,
    layer1: Layer = (40, 0),
    layer2: Layer = (41, 0)
) -> Component
```

Layer1 must be enclosed by layer2 by value.

checks if layer1 encloses (is bigger than) layer2 by value

<a id="gdsfactory.samples.demo.lvs"></a>

# gdsfactory.samples.demo.lvs

LVS demo.

<a id="gdsfactory.samples.demo.lvs.pads_correct"></a>

#### pads\_correct

```python
@gf.cell
def pads_correct(pad: ComponentFactory = gf.components.pad,
                 cross_section: str = "metal3") -> gf.Component
```

Returns 2 pads connected with metal wires.

<a id="gdsfactory.samples.demo.lvs.pads_shorted"></a>

#### pads\_shorted

```python
@gf.cell
def pads_shorted(pad: ComponentFactory = gf.components.pad,
                 cross_section: str = "metal3") -> gf.Component
```

Returns 2 pads connected with metal wires.

<a id="gdsfactory.samples.demo"></a>

# gdsfactory.samples.demo

<a id="gdsfactory.samples.demo.layers_sky130"></a>

# gdsfactory.samples.demo.layers\_sky130

<a id="gdsfactory.samples.demo.pcell"></a>

# gdsfactory.samples.demo.pcell

PCell demo.

<a id="gdsfactory.samples.demo.pcell.mzi_with_bend"></a>

#### mzi\_with\_bend

```python
@gf.cell
def mzi_with_bend(radius: float = 10) -> gf.Component
```

Returns MZI interferometer with bend.

<a id="gdsfactory.samples.09_pack"></a>

# gdsfactory.samples.09\_pack

Group components in a cell using pack.

<a id="gdsfactory.samples.30_lidar"></a>

# gdsfactory.samples.30\_lidar

LiDAR demo.

Exercise1. increase the number of elements of the phase array.

Exercise2. Make a PCell.

<a id="gdsfactory.samples.25_slot_cross_section"></a>

# gdsfactory.samples.25\_slot\_cross\_section

Small demonstration of the slot cross_section utilizing add_center_section=False.

<a id="gdsfactory.samples.40_verification"></a>

# gdsfactory.samples.40\_verification

<a id="gdsfactory.samples.30_route_bundle_lidar"></a>

# gdsfactory.samples.30\_route\_bundle\_lidar

LiDAR demo.

Exercise1. increase the number of noutputs of the phase array.

Exercise2. Make a PCell.

<a id="gdsfactory.samples.16_component_sequence2"></a>

# gdsfactory.samples.16\_component\_sequence2

<a id="gdsfactory.samples.16_component_sequence2.cutback_phase"></a>

#### cutback\_phase

```python
@gf.cell
def cutback_phase(straight_length: float = 100.0,
                  bend_radius: float = 12.0,
                  n: int = 2) -> Component
```

Modulator sections connected by bends.

**Arguments**:

- `straight_length` - length of the straight waveguides.
- `bend_radius` - radius of the bends.
- `n` - number of modulator sections.

<a id="gdsfactory.samples.00_hello_world"></a>

# gdsfactory.samples.00\_hello\_world

<a id="gdsfactory.samples.12_component_refs"></a>

# gdsfactory.samples.12\_component\_refs

Lets create a crossing component with two references to other components (crossing_arm).

- add references to a component (one of the arm references rotated)
- add ports from the child references into the parent cell
- use Component.auto_rename_ports() to rename ports according to their location

<a id="gdsfactory.samples.12_component_refs.crossing_arm"></a>

#### crossing\_arm

```python
@gf.cell
def crossing_arm(
    wg_width: float = 0.5,
    r1: float = 3.0,
    r2: float = 1.1,
    taper_width: float = 1.2,
    taper_length: float = 3.4,
    layer_wg: Layer = (1, 0),
    layer_slab: Layer = (2, 0)
) -> Component
```

Crossing arm.

**Arguments**:

- `wg_width` - waveguide width.
- `r1` - radius of the ellipse.
- `r2` - radius of the ellipse.
- `taper_width` - width of the taper.
- `taper_length` - length of the taper.
- `layer_wg` - waveguide layer.
- `layer_slab` - slab layer.

<a id="gdsfactory.samples.12_component_refs.crossing"></a>

#### crossing

```python
@gf.cell
def crossing(arm: ComponentFactory = crossing_arm,
             cross_section: str = "strip") -> Component
```

Waveguide crossing.

**Arguments**:

- `arm` - arm spec.
- `cross_section` - spec.

<a id="gdsfactory.samples.11_component_layout"></a>

# gdsfactory.samples.11\_component\_layout

Lets create a new component.

We create a function which returns a gf.Component.

Lets build straight crossing out of a vertical and horizontal arm

- Create a component using a function with the cell decorator to define the name automatically and uniquely.
- Define the polygons in the component
- Add ports to the component so you can connect it with other components

<a id="gdsfactory.samples.11_component_layout.crossing_arm"></a>

#### crossing\_arm

```python
@gf.cell
def crossing_arm(wg_width: float = 0.5,
                 r1: float = 3.0,
                 r2: float = 1.1,
                 taper_width: float = 1.2,
                 taper_length: float = 3.4) -> Component
```

Returns a crossing arm.

**Arguments**:

- `wg_width` - waveguide width.
- `r1` - radius of the ellipse.
- `r2` - radius of the ellipse.
- `taper_width` - width of the taper.
- `taper_length` - length of the taper.

<a id="gdsfactory.samples.15_component_sequence1"></a>

# gdsfactory.samples.15\_component\_sequence1

You can use component_sequence as a convenient function for cascading components, where you need to keep track of multiple tapers, doped sections, heaters etc...

The idea is to associate one symbol per type of section.
A section is uniquely defined by the component, input port name and output port name.

The mapping between symbols and components is supplied by a dictionary.
The actual chain of components is supplied by a string or a list

<a id="gdsfactory.samples.snap_bends"></a>

# gdsfactory.samples.snap\_bends

Snap bends together.

<a id="gdsfactory.samples.12_component_instance_arrays"></a>

# gdsfactory.samples.12\_component\_instance\_arrays

Lets access the ports for an array of instances.

<a id="gdsfactory.samples.sample_reticle"></a>

# gdsfactory.samples.sample\_reticle

<a id="gdsfactory.samples.sample_reticle.spiral_gc"></a>

#### spiral\_gc

```python
@gf.cell
def spiral_gc(**kwargs: Any) -> gf.Component
```

Returns a spiral double with Grating Couplers.

**Arguments**:

- `kwargs` - additional settings.
  

**Arguments**:

- `length` - length of the spiral straight section.
- `bend` - bend component.
- `straight` - straight component.
- `cross_section` - cross_section component.
- `spacing` - spacing between the spiral loops.
- `n_loops` - number of loops.

<a id="gdsfactory.samples.sample_reticle.mzi_gc"></a>

#### mzi\_gc

```python
@gf.cell
def mzi_gc(length_x: float = 10, **kwargs: Any) -> gf.Component
```

Returns a MZI with Grating Couplers.

**Arguments**:

- `length_x` - length of the MZI.
- `kwargs` - additional settings.

<a id="gdsfactory.samples.sample_reticle.sample_reticle"></a>

#### sample\_reticle

```python
@gf.cell
def sample_reticle(grid: bool = False) -> gf.Component
```

Returns MZI with TE grating couplers.

<a id="gdsfactory.samples.big_device_electrical"></a>

# gdsfactory.samples.big\_device\_electrical

<a id="gdsfactory.samples.big_device_electrical.big_device"></a>

#### big\_device

```python
@gf.cell
def big_device(size: Size = (400.0, 400.0),
               nports: int = 16,
               spacing: float = 15.0,
               port_type: str = "electrical",
               cross_section: CrossSectionSpec = "metal_routing") -> Component
```

Big component with N ports on each side.

**Arguments**:

- `size` - x, y.
- `nports` - number of ports.
- `spacing` - in um.
- `port_type` - optical, electrical, rf, etc.
- `cross_section` - spec.

<a id="gdsfactory.samples.20_components"></a>

# gdsfactory.samples.20\_components

__Components. You can adapt some component functions from the `gdsfactory.components` module. Each function there returns a Component object. Here are two equivalent functions.__


<a id="gdsfactory.samples.big_device"></a>

# gdsfactory.samples.big\_device

<a id="gdsfactory.samples.big_device.big_device"></a>

#### big\_device

```python
@gf.cell
def big_device(size: Size = (400.0, 400.0),
               nports: int = 16,
               spacing: float = 15.0,
               port_type: str = "optical",
               cross_section: CrossSectionSpec = "strip") -> Component
```

Big component with N ports on each side.

**Arguments**:

- `size` - x, y.
- `nports` - number of ports.
- `spacing` - in um.
- `port_type` - optical, electrical, rf, etc.
- `cross_section` - spec.

<a id="gdsfactory.samples.sample_reticle_electrical_with_labels"></a>

# gdsfactory.samples.sample\_reticle\_electrical\_with\_labels

<a id="gdsfactory.samples.sample_reticle_electrical_with_labels.label_farthest_right_port"></a>

#### label\_farthest\_right\_port

```python
def label_farthest_right_port(component: gf.Component, ports: Ports,
                              layer: LayerSpec, text: str) -> gf.Component
```

Adds a label to the right of the farthest right port in a given component.

**Arguments**:

- `component` - The component to which the label is added.
- `ports` - A list of ports to evaluate for positioning the label.
- `layer` - The layer on which the label will be added.
- `text` - The text to display in the label.

<a id="gdsfactory.samples.sample_reticle_electrical_with_labels.resistance"></a>

#### resistance

```python
@gf.cell
def resistance(width: float = 5, **kwargs: Any) -> gf.Component
```

Returns a resistance sheet.

**Arguments**:

- `width` - width of the resistance sheet.
- `kwargs` - additional settings.

<a id="gdsfactory.samples.sample_reticle_electrical_with_labels.via_chain"></a>

#### via\_chain

```python
def via_chain(num_vias: int = 100,
              component_name: str = "via_chain",
              **kwargs: Any) -> gf.Component
```

Returns a chain of vias.

**Arguments**:

- `num_vias` - number of vias in the chain.
- `component_name` - name of the component.
- `kwargs` - additional settings.

<a id="gdsfactory.samples.sample_reticle_electrical_with_labels.sample_reticle_with_labels"></a>

#### sample\_reticle\_with\_labels

```python
def sample_reticle_with_labels(grid: bool = False) -> gf.Component
```

Returns electrical test structures.

<a id="gdsfactory.samples.33_route_bundle_nxn"></a>

# gdsfactory.samples.33\_route\_bundle\_nxn

Routing bundle requires end ports to be on the same orientation but input can be any orientation.

<a id="gdsfactory.samples.04_connect"></a>

# gdsfactory.samples.04\_connect

based on phidl tutorial.

__Connecting devices with connect()__


The connect command allows you to connect ComponentReference ports together like Lego blocks.

<a id="gdsfactory.samples.14_component_connectivity"></a>

# gdsfactory.samples.14\_component\_connectivity

<a id="gdsfactory.samples.14_component_connectivity.ring_single_sample"></a>

#### ring\_single\_sample

```python
@gf.cell
def ring_single_sample(gap: float = 0.2,
                       radius: float = 10.0,
                       length_x: float = 4.0,
                       length_y: float = 0.010,
                       coupler_ring: ComponentSpec = "coupler_ring",
                       straight: ComponentSpec = "straight",
                       bend: ComponentSpec = "bend_euler",
                       cross_section: CrossSectionSpec = "strip") -> Component
```

Single bus ring made of a ring coupler.

(cb: bottom) connected with two vertical straights (wl: left, wr: right)
two bends (bl, br) and horizontal straight (wg: top).

**Arguments**:

- `gap` - gap between for coupler.
- `radius` - for the bend and coupler.
- `length_x` - ring coupler length.
- `length_y` - vertical straight length.
- `coupler_ring` - ring coupler function.
- `straight` - straight function.
- `bend` - 90 degrees bend function.
- `cross_section` - spec.
  
  
  .. code::
  
  bl-wt-br
  |      |
  wl     wr length_y
  |      |
  --==cb==-- gap
  
  length_x

<a id="gdsfactory.samples.coh_tx_single_pol"></a>

# gdsfactory.samples.coh\_tx\_single\_pol

<a id="gdsfactory.samples.coh_tx_single_pol.coh_tx_single_pol"></a>

#### coh\_tx\_single\_pol

```python
@gf.cell
def coh_tx_single_pol(balanced_phase_shifters: bool = False,
                      mzm_y_spacing: float = 50.0,
                      phase_shifter: ComponentSpec = "straight_pin",
                      phase_shifter_length: float = 100.0,
                      mzm_ps_spacing: float = 40.0,
                      splitter: ComponentSpec = "mmi1x2",
                      combiner: ComponentSpec | None = None,
                      mzm: ComponentSpec = "mzi_pin",
                      mzm_length: float = 200.0,
                      xspacing: float = 40.0,
                      input_coupler: ComponentSpec | None = None,
                      output_coupler: ComponentSpec | None = None,
                      pad_array: ComponentSpec = "pad_array",
                      cross_section: CrossSectionSpec = "strip") -> Component
```

MZM-based single polarization coherent transmitter.

**Arguments**:

- `balanced_phase_shifters` - True adds phase sifters after the MZM at both the I and Q arms.
  False, only adds Q arm has a phase shifter.
- `mzm_y_spacing` - vertical spacing between the bottom of the I MZM and the top of the Q MZM.
- `phase_shifter` - phase_shifter spec.
- `phase_shifter_length` - length of the phase shifter.
- `mzm_ps_spacing` - spacing between the end of the mzm and the phase shifter.
- `splitter` - splitter spec.
- `combiner` - combiner spec.
- `mzm` - Mach-Zehnder modulator spec.
- `mzm_length` - length of the MZMs.
- `xspacing` - horizontal spacing between the splitter and combiner and the mzm.
- `input_coupler` - Optional coupler to add before the splitter.
- `output_coupler` - Optional coupler to add after the combiner.
- `pad_array` - array of pads spec.
- `cross_section` - for routing (splitter to mzms and mzms to combiners).
  
  .. code::
  
  ___ mzm_i __ ps_i__
  |                  |
  |                  |
  |                  |
  (in_coupler)---splitter==|                  |==combiner---(out_coupler)
  |                  |
  |                  |
  |___ mzm_q __ ps_q_|

<a id="gdsfactory.samples.01_component_pcell"></a>

# gdsfactory.samples.01\_component\_pcell

Based on phidl tutorial.

We'll start by assuming we have a function straight() which already
exists and makes us a simple straight waveguide. Many functions like
this exist in the gdsfactory.components library and are ready-for-use.
We write this one out fully just so it's explicitly clear what's
happening

<a id="gdsfactory.samples.01_component_pcell.straight_wide"></a>

#### straight\_wide

```python
@gf.cell
def straight_wide(length: float = 5.0,
                  width: float = 1.0,
                  layer: LayerSpec = (1, 0)) -> gf.Component
```

Returns straight Component.

**Arguments**:

- `length` - of the straight.
- `width` - in um.
- `layer` - layer spec

<a id="gdsfactory.samples.pdk.fab_c"></a>

# gdsfactory.samples.pdk.fab\_c

FabC example.

<a id="gdsfactory.samples.pdk.fab_c.get_layer_stack_fab_c"></a>

#### get\_layer\_stack\_fab\_c

```python
def get_layer_stack_fab_c(thickness: float = 350.0) -> LayerStack
```

Returns generic LayerStack.

<a id="gdsfactory.samples.pdk.fab_c.strip"></a>

#### strip

type: ignore[assignment]

<a id="gdsfactory.samples.pdk.fab_d.phase_shifters"></a>

# gdsfactory.samples.pdk.fab\_d.phase\_shifters

<a id="gdsfactory.samples.pdk.fab_d"></a>

# gdsfactory.samples.pdk.fab\_d

<a id="gdsfactory.samples.pdk"></a>

# gdsfactory.samples.pdk

<a id="gdsfactory.samples.route_bundle_bbox2"></a>

# gdsfactory.samples.route\_bundle\_bbox2

<a id="gdsfactory.technology.layer_map"></a>

# gdsfactory.technology.layer\_map

<a id="gdsfactory.technology.layer_map.LayerMap"></a>

## LayerMap Objects

```python
class LayerMap(gf.LayerEnum)
```

You will need to create a new LayerMap with your specific foundry layers.

<a id="gdsfactory.technology.layer_map.lyp_to_dataclass"></a>

#### lyp\_to\_dataclass

```python
def lyp_to_dataclass(lyp_filepath: str | pathlib.Path,
                     overwrite: bool = True) -> str
```

Returns python LayerMap script from a klayout layer properties file lyp.

<a id="gdsfactory.technology.xml_utils"></a>

# gdsfactory.technology.xml\_utils

<a id="gdsfactory.technology.xml_utils.strip_xml"></a>

#### strip\_xml

```python
def strip_xml(node: Node) -> None
```

Strip XML of excess whitespace.

Source: https://stackoverflow.com/a/16919069

<a id="gdsfactory.technology.xml_utils.make_pretty_xml"></a>

#### make\_pretty\_xml

```python
def make_pretty_xml(root: ET.Element) -> bytes
```

Make XML pretty.

<a id="gdsfactory.technology"></a>

# gdsfactory.technology

<a id="gdsfactory.technology.processes"></a>

# gdsfactory.technology.processes

<a id="gdsfactory.technology.processes.ProcessStep"></a>

## ProcessStep Objects

```python
@dataclass(kw_only=True)
class ProcessStep()
```

Generic process step.

<a id="gdsfactory.technology.processes.Lithography"></a>

## Lithography Objects

```python
@dataclass(kw_only=True)
class Lithography(ProcessStep)
```

Simulates lithography by generating a logical on-wafer mask from one or many layers to be used in processing operations.

(1) First, a mask is created from the layer arguments:

if layer=None, behaviour should be:

mask opening
<---------------->
----->
|________________|                    |________________|

0       1        2         3          0       1        2         3


if argument_layers is provided to layers_or, for those layers:

layer                                 mask opening
<---------------->                   <--------------------------->
----->
|________________|                    |_______|________|_________|
|__________________|
0       1        2         3          0       1        2         3
<------------------>
layers_or


if argument_layers is provided to layers_and, for those layers:

layer                                 mask opening
<---------------->                            <--------->
----->
|________________|                    |       |_________|        |
|__________________|
0       1        2         3          0       1        2         3
<------------------>
layers_and

if argument_layers is provided to layers_diff, for those layers:

layer                                 mask opening
<---------------->                    <------->
----->
|________________|                    |________|        |        |
|__________________|
0       1        2         3          0       1        2         3
<------------------>
layers_and

if argument_layers is provided to layers_xor, for those layers:

layer                                  mask opening
<---------------->                   <-------->        <--------->
----->
|________________|                    |_______|        |_________|
|__________________|
0       1        2         3          0       1        2         3
<------------------>
layers_xor


(2) Convert the logical mask into a wafer mask, opening up parts of the wafer for processing:

if positive_tone:

mask opening             wafer mask opened
<------>                   <------>
_____      _____
|   |      |   |
----->     |   |      |   | mask_thickness
________________           |___|______|___|


else (negative tone):

mask opening            wafer mask NOT opened
<------>                   <------>
________
|      |
----->         |      | mask_thickness
________________           ____|______|____


(3) (Optional) Planarize the resist


**Arguments**:

- `layer` - main layer to use as a mask for this lithography step
- `layers_union` _List[Layers]_ - other layers to use to form the mask (see diagram)
- `layers_diff` _List[Layers]_ - other layers to use to form a mask (see diagram)
- `layers_intersect` _List[Layers]_ - other layers to use to form a mask (see diagram)
- `positive_tone` _bool_ - whether to invert the resulting mask (False) or not (True)
- `resist_thickness` _float_ - resist mask thickness, used in some simulators
- `planarization_height` _float_ - height at which to "clip" the resist above the wafer

<a id="gdsfactory.technology.processes.Grow"></a>

## Grow Objects

```python
@dataclass(kw_only=True)
class Grow(Lithography)
```

Simulates masking + addition of material + liftoff.

wafer mask opened           wafer mask opened
<------>                   <------>
________
|      |
----->       | mat  | thickness
________________           ____|______|____

**Arguments**:

- `material` _str_ - material tag of material to add
- `thickness` _float_ - thickness to add [nm]
- `type` _str_ - of growth/deposition (isotropic, anisotropic, etc.)
- `rate` _float_ - of growth [nm/s]

<a id="gdsfactory.technology.processes.Etch"></a>

## Etch Objects

```python
@dataclass(kw_only=True)
class Etch(Lithography)
```

Simulates masking + removal of material + strip.

wafer mask opened          wafer mask opened
<------>                   <----->
________________           _____      _____
|              |               |      |
|     mat      |    -----> mat | etch | mat  depth
|______________|           ____|______|____


**Arguments**:

- `material` _str_ - material tag to etch into
- `thickness` _float_ - thickness to remove [nm]
- `type` _str_ - of etch (isotropic, anisotropic, etc.)
- `rate` _float_ - of removal [nm/s]

<a id="gdsfactory.technology.processes.ImplantPhysical"></a>

## ImplantPhysical Objects

```python
@dataclass(kw_only=True)
class ImplantPhysical(Lithography)
```

Simulates masking + physical ion implantation + strip.

wafer mask opened          wafer mask opened
<------>                   <----->
________________          __________________
|              |          |                |
|              |  ----->  |    ------- <---- range (depends on energy)
|______________|          |________________|

**Arguments**:

- `ion` _str_ - ion tag
- `energy` _float_ - of the ions
- `dose` _float_ - in /cm^2
- `tilt` _float_ - ion angle from out-of-plane axis. in degrees. If None, uses simulator default
- `twist` _float_ - ion angle from wafer "x-axis", in degrees. If None, uses simulator default
- `rotation` _float_ - if twist is None, toggle to split the dose 4-ways between 4 cardinal twist angles (simulates substrate rotation during implantation)

<a id="gdsfactory.technology.processes.ImplantGaussian"></a>

## ImplantGaussian Objects

```python
@dataclass(kw_only=True)
class ImplantGaussian(Lithography)
```

Simulates masking + physical ion implantation + strip.

wafer mask opened          wafer mask opened
<------>                   <----->
________________          __________________
|              |          |                |
|              |  ----->  |    ------- <---- range (depends on energy)
|______________|          |________________|

**Arguments**:

- `ion` _str_ - ion tag
- `peak_conc` _float_ - peak concentration
- `range` _float_ - of the ions (center of distribution)
- `vertical_straggle` _float_ - of the ions (spread of distribution), normal to the plane
- `lateral_straggle` _float_ - of the ions (spread of distribution), parallel to the plane
- `into_materials` _List[str]_ - list of material tothis step can implant into

<a id="gdsfactory.technology.processes.DopingConstant"></a>

## DopingConstant Objects

```python
@dataclass(kw_only=True)
class DopingConstant(Lithography)
```

Constant doping for simplified processes.

wafer mask opened          wafer mask opened
<------>                   <----->
________________          __________________
|              |          |                |
|              |  ----->  |    ------- <---- range (depends on energy)
|______________|          |________________|

**Arguments**:

- `ion` _str_ - ion tag
- `peak_conc` _float_ - peak concentration (constant)
- `zmin` _float_ - lower bound of the doping box
- `zmax` _float_ - upper bound of the doping box. By default
- `into_materials` _List[str]_ - list of material tothis step can implant into

<a id="gdsfactory.technology.processes.Anneal"></a>

## Anneal Objects

```python
@dataclass(kw_only=True)
class Anneal(ProcessStep)
```

Simulates thermal diffusion of impurities and healing of defects.

**Arguments**:

  time (float)
- `temperature` _float_ - temperature
  
- `TODO` _long term_ - heating/cooling time profiles

<a id="gdsfactory.technology.processes.Planarize"></a>

## Planarize Objects

```python
@dataclass(kw_only=True)
class Planarize(ProcessStep)
```

Simulates chip planarization, "clipping" the structure above some height. Does not use masking.

__
_|  |___
__|        |____
|              |  ___                     _________________
|              |   |  height    ----->    |               |
|______________|  _|_  z=0                |_______________|


**Arguments**:

- `depth` _float_ - how much to remove

<a id="gdsfactory.technology.processes.ArbitraryStep"></a>

## ArbitraryStep Objects

```python
@dataclass(kw_only=True)
class ArbitraryStep(ProcessStep)
```

Arbitrary process step, used to handle all other cases.

<a id="gdsfactory.technology.yaml_utils"></a>

# gdsfactory.technology.yaml\_utils

<a id="gdsfactory.technology.yaml_utils.add_color_yaml_representer"></a>

#### add\_color\_yaml\_representer

```python
def add_color_yaml_representer(prefer_named_color: bool = True) -> None
```

Add a custom YAML presenter for Color objects.

<a id="gdsfactory.technology.yaml_utils.add_tuple_yaml_representer"></a>

#### add\_tuple\_yaml\_representer

```python
def add_tuple_yaml_representer() -> None
```

Add a custom YAML presenter for tuple objects.

<a id="gdsfactory.technology.yaml_utils.add_multiline_str_yaml_representer"></a>

#### add\_multiline\_str\_yaml\_representer

```python
def add_multiline_str_yaml_representer() -> None
```

Add a custom YAML presenter for multiline strings.

<a id="gdsfactory.technology.klayout_tech"></a>

# gdsfactory.technology.klayout\_tech

Classes and utils for working with KLayout technology files (.lyp, .lyt).

This module enables conversion between gdsfactory settings and KLayout technology.

<a id="gdsfactory.technology.klayout_tech.KLayoutTechnology"></a>

## KLayoutTechnology Objects

```python
class KLayoutTechnology(BaseModel)
```

A container for working with KLayout technologies (requires KLayout Python package).

Useful to import/export Layer Properties (.lyp) and Technology (.lyt) files.

Properties:
    name: technology name.
    layer_map: Maps names to GDS layer numbers.
    layer_views: Defines all the layer display properties needed for a .lyp file from LayerView objects.
    technology: KLayout Technology object from the KLayout API. Set name, dbu, etc.
    connectivity: List of layer names connectivity for netlist tracing.

<a id="gdsfactory.technology.klayout_tech.KLayoutTechnology.write_tech"></a>

#### write\_tech

```python
def write_tech(tech_dir: PathType,
               lyp_filename: str = "layers.lyp",
               lyt_filename: str = "tech.lyt",
               d25_filename: str | None = None,
               mebes_config: dict[str, Any] | None = None) -> None
```

Write technology files into 'tech_dir'.

**Arguments**:

- `tech_dir` - Where to write the technology files to.
- `lyp_filename` - Name of the layer properties file.
- `lyt_filename` - Name of the layer technology file.
- `d25_filename` - Name of the 2.5D stack file (only works on KLayout >= 0.28). Defaults to self.name.
- `mebes_config` - A dictionary specifying the KLayout mebes reader config.

<a id="gdsfactory.technology.layer_views"></a>

# gdsfactory.technology.layer\_views

A GDS layer is a tuple of two integers.

You can maintain LayerViews in YAML (.yaml) or Klayout XML file (.lyp)

<a id="gdsfactory.technology.layer_views.HatchPattern"></a>

## HatchPattern Objects

```python
class HatchPattern(BaseModel)
```

Custom dither pattern. See KLayout documentation for more info.

**Attributes**:

- `name` - Name of the pattern.
- `order` - Order of pattern.
- `custom_pattern` - Pattern defining custom shape.

<a id="gdsfactory.technology.layer_views.LineStyle"></a>

## LineStyle Objects

```python
class LineStyle(BaseModel)
```

Custom line style. See KLayout documentation for more info.

**Attributes**:

- `name` - Name of the line style.
- `order` - Order of line style.
- `custom_style` - Line style to use.

<a id="gdsfactory.technology.layer_views.LayerView"></a>

## LayerView Objects

```python
class LayerView(BaseModel)
```

KLayout layer properties.

Docstrings adapted from KLayout documentation:
https://www.klayout.de/lyp_format.html

**Attributes**:

- `name` - Layer name.
- `info` - Extra info to include in the LayerView.
- `layer` - GDSII layer.
- `layer_in_name` - Whether to display the name as 'name layer/datatype' rather than just the layer.
- `width` - This is the line width of the frame in pixels (or empty for the default which is 1).
- `line_style` - This is the number of the line style used to draw the shape boundaries.
  An empty string is "solid line". The values are "Ix" for one of the built-in styles
  where "I0" is "solid", "I1" is "dotted" etc.
- `hatch_pattern` - This is the number of the dither pattern used to fill the shapes.
  The values are "Ix" for one of the built-in pattern where "I0" is "solid" and "I1" is "clear".
- `fill_color` - Display color of the layer fill.
- `frame_color` - Display color of the layer frame.
  Accepts Pydantic Color types. See: https://docs.pydantic.dev/usage/types/`color`-type for more info.
- `fill_brightness` - Brightness of the fill.
- `frame_brightness` - Brightness of the frame.
- `animation` - This is a value indicating the animation mode.
  0 is "none", 1 is "scrolling", 2 is "blinking" and 3 is "inverse blinking".
  (Only applies to KLayout layer properties)
- `xfill` - Whether boxes are drawn with a diagonal cross. (Only applies to KLayout layer properties)
- `marked` - Whether the entry is marked (drawn with small crosses). (Only applies to KLayout layer properties)
- `transparent` - Whether the entry is transparent.
- `visible` - Whether the entry is visible.
- `valid` - Whether the entry is valid. Invalid layers are drawn but you can't select shapes on those layers.
  (Only applies to KLayout layer properties)
- `group_members` - Add a list of group members to the LayerView.

<a id="gdsfactory.technology.layer_views.LayerView.__init__"></a>

#### \_\_init\_\_

```python
def __init__(gds_layer: int | None = None,
             gds_datatype: int | None = None,
             color: ColorType | None = None,
             brightness: int | None = None,
             **data: Any) -> None
```

Initialize LayerView object.

<a id="gdsfactory.technology.layer_views.LayerView.dict"></a>

#### dict

```python
def dict(*,
         include: IncEx | None = None,
         exclude: IncEx | None = None,
         by_alias: bool = False,
         exclude_unset: bool = False,
         exclude_defaults: bool = False,
         exclude_none: bool = False,
         simplify: bool = True) -> dict[str, Any]
```

Generate a dictionary representation of the model, optionally specifying which fields to include or exclude.

Specify "simplify" to consolidate fill and frame color/brightness if they are the same.

**Arguments**:

- `mode` - The mode in which `to_python` should run.
  If mode is 'json', the dictionary will only contain JSON serializable types.
  If mode is 'python', the dictionary may contain any Python objects.
- `include` - A list of fields to include in the output.
- `exclude` - A list of fields to exclude from the output.
- `by_alias` - Whether to use the field's alias in the dictionary key if defined.
- `exclude_unset` - Whether to exclude fields that are unset or None from the output.
- `exclude_defaults` - Whether to exclude fields that are set to their default value from the output.
- `exclude_none` - Whether to exclude fields that have a value of `None` from the output.
- `simplify` - Whether to consolidate fill and frame color/brightness if they are the same.
  

**Returns**:

  A dictionary representation of the model.

<a id="gdsfactory.technology.layer_views.LayerView.__str__"></a>

#### \_\_str\_\_

```python
def __str__() -> str
```

Returns a formatted view of properties and their values.

<a id="gdsfactory.technology.layer_views.LayerView.__repr__"></a>

#### \_\_repr\_\_

```python
def __repr__() -> str
```

Returns a formatted view of properties and their values.

<a id="gdsfactory.technology.layer_views.LayerView.to_klayout_xml"></a>

#### to\_klayout\_xml

```python
def to_klayout_xml(
        custom_hatch_patterns: builtins.dict[str, HatchPattern],
        custom_line_styles: builtins.dict[str, LineStyle]) -> ET.Element
```

Return an XML representation of the LayerView.

<a id="gdsfactory.technology.layer_views.LayerView.from_xml_element"></a>

#### from\_xml\_element

```python
@classmethod
def from_xml_element(cls, element: ET.Element,
                     layer_pattern: str | re.Pattern[str]) -> LayerView | None
```

Read properties from .lyp XML and generate LayerViews from them.

**Arguments**:

- `element` - XML Element to iterate over.
- `layer_pattern` - Regex pattern to match layers with.

<a id="gdsfactory.technology.layer_views.LayerViews"></a>

## LayerViews Objects

```python
class LayerViews(BaseModel)
```

A container for layer properties for KLayout layer property (.lyp) files.

**Attributes**:

- `layer_views` - Dictionary of LayerViews describing how to display gds layers.
- `custom_dither_patterns` - Custom dither patterns.
- `custom_line_styles` - Custom line styles.
- `layers` - Specify a layer_map to get the layer tuple based on the name of the LayerView, rather than the 'layer' argument.

<a id="gdsfactory.technology.layer_views.LayerViews.__init__"></a>

#### \_\_init\_\_

```python
def __init__(filepath: PathLike | None = None,
             layers: type[LayerEnum] | None = None,
             **data: Any) -> None
```

Initialize LayerViews object.

**Arguments**:

- `filepath` - can be YAML or LYP.
- `layers` - Optional layermap.
- `data` - Additional data to add to the LayerViews object.

<a id="gdsfactory.technology.layer_views.LayerViews.add_layer_view"></a>

#### add\_layer\_view

```python
def add_layer_view(name: str,
                   layer_view: LayerView | None = None,
                   **kwargs: Any) -> None
```

Adds a layer to LayerViews.

**Arguments**:

- `name` - Name of the LayerView.
- `layer_view` - LayerView to add.
- `kwargs` - Additional arguments to pass to LayerView.

<a id="gdsfactory.technology.layer_views.LayerViews.get_layer_views"></a>

#### get\_layer\_views

```python
def get_layer_views(exclude_groups: bool = False) -> dict[str, LayerView]
```

Return all LayerViews.

**Arguments**:

- `exclude_groups` - Whether to exclude LayerViews that contain other LayerViews.

<a id="gdsfactory.technology.layer_views.LayerViews.get_layer_view_groups"></a>

#### get\_layer\_view\_groups

```python
def get_layer_view_groups() -> dict[str, LayerView]
```

Return the LayerViews that contain other LayerViews.

<a id="gdsfactory.technology.layer_views.LayerViews.__str__"></a>

#### \_\_str\_\_

```python
def __str__() -> str
```

Prints the number of LayerView objects in the LayerViews object.

<a id="gdsfactory.technology.layer_views.LayerViews.get"></a>

#### get

```python
def get(name: str) -> LayerView
```

Returns Layer from name.

**Arguments**:

- `name` - Name of layer.

<a id="gdsfactory.technology.layer_views.LayerViews.__getitem__"></a>

#### \_\_getitem\_\_

```python
def __getitem__(val: str) -> LayerView
```

Allows accessing to the layer names like ls['gold2'].

**Arguments**:

- `val` - Layer name to access within the LayerViews.
  

**Returns**:

- `self.layers[val]` - LayerView in the LayerViews.

<a id="gdsfactory.technology.layer_views.LayerViews.get_from_tuple"></a>

#### get\_from\_tuple

```python
def get_from_tuple(layer_tuple: tuple[int, int]) -> LayerView
```

Returns LayerView from layer tuple.

**Arguments**:

- `layer_tuple` - Tuple of (gds_layer, gds_datatype).
  

**Returns**:

  LayerView.

<a id="gdsfactory.technology.layer_views.LayerViews.get_layer_tuples"></a>

#### get\_layer\_tuples

```python
def get_layer_tuples() -> set[Layer]
```

Returns a tuple for each layer.

<a id="gdsfactory.technology.layer_views.LayerViews.clear"></a>

#### clear

```python
def clear() -> None
```

Deletes all layers in the LayerViews.

<a id="gdsfactory.technology.layer_views.LayerViews.preview_layerset"></a>

#### preview\_layerset

```python
def preview_layerset(size: float = 100.0, spacing: float = 100.0) -> Component
```

Generates a Component with all the layers.

**Arguments**:

- `size` - square size in um.
- `spacing` - spacing between each square in um.

<a id="gdsfactory.technology.layer_views.LayerViews.to_lyp"></a>

#### to\_lyp

```python
def to_lyp(filepath: str | pathlib.Path,
           overwrite: bool = True) -> pathlib.Path
```

Write all layer properties to a KLayout .lyp file.

**Arguments**:

- `filepath` - to write the .lyp file to (appends .lyp extension if not present).
- `overwrite` - Whether to overwrite an existing file located at the filepath.

<a id="gdsfactory.technology.layer_views.LayerViews.from_lyp"></a>

#### from\_lyp

```python
@staticmethod
def from_lyp(filepath: str | pathlib.Path,
             layer_pattern: str | re.Pattern[str] | None = None) -> LayerViews
```

Write all layer properties to a KLayout .lyp file.

**Arguments**:

- `filepath` - to write the .lyp file to (appends .lyp extension if not present).
- `layer_pattern` - Regex pattern to match layers with. Defaults to r'(\d+|\*)/(\d+|\*)'.

<a id="gdsfactory.technology.layer_views.LayerViews.to_yaml"></a>

#### to\_yaml

```python
def to_yaml(layer_file: str | pathlib.Path) -> None
```

Export layer properties to a YAML file.

**Arguments**:

- `layer_file` - Name of the file to write LayerViews to.

<a id="gdsfactory.technology.layer_views.LayerViews.from_yaml"></a>

#### from\_yaml

```python
@staticmethod
def from_yaml(layer_file: str | pathlib.Path) -> LayerViews
```

Import layer properties from two yaml files.

**Arguments**:

- `layer_file` - Name of the file to read LayerViews, CustomDitherPatterns, and CustomLineStyles from.

<a id="gdsfactory.technology.layer_views.test_load_lyp"></a>

#### test\_load\_lyp

```python
def test_load_lyp() -> None
```

Test loading a KLayout layer properties.

<a id="gdsfactory.technology.color_utils"></a>

# gdsfactory.technology.color\_utils

<a id="gdsfactory.technology.layer_stack"></a>

# gdsfactory.technology.layer\_stack

<a id="gdsfactory.technology.layer_stack.AbstractLayer"></a>

## AbstractLayer Objects

```python
class AbstractLayer(BaseModel)
```

Generic design layer.

**Attributes**:

- `sizings_xoffsets` - sequence of xoffset sizings to apply to this Logical or Derived layer.
- `sizings_yoffsets` - sequence of yoffset sizings to apply to this Logical or Derived layer.
- `sizings_modes` - sequence of sizing modes to apply to this Logical or Derived layer.

<a id="gdsfactory.technology.layer_stack.AbstractLayer.__and__"></a>

#### \_\_and\_\_

```python
def __and__(other: AbstractLayer) -> DerivedLayer
```

Represents boolean AND (&) operation between two layers.

**Arguments**:

- `other` _AbstractLayer_ - Another Layer object to perform AND operation.
  

**Returns**:

  A new DerivedLayer with the AND operation logged.

<a id="gdsfactory.technology.layer_stack.AbstractLayer.__or__"></a>

#### \_\_or\_\_

```python
def __or__(other: AbstractLayer) -> DerivedLayer
```

Represents boolean OR (|) operation between two layers.

**Arguments**:

- `other` _AbstractLayer_ - Another Layer object to perform OR operation.
  

**Returns**:

  A new DerivedLayer with the OR operation logged.

<a id="gdsfactory.technology.layer_stack.AbstractLayer.__add__"></a>

#### \_\_add\_\_

```python
def __add__(other: AbstractLayer) -> DerivedLayer
```

Represents boolean OR (+) operation between two derived layers.

**Arguments**:

- `other` _AbstractLayer_ - Another Layer object to perform OR operation.
  

**Returns**:

  A new DerivedLayer with the AND operation logged.

<a id="gdsfactory.technology.layer_stack.AbstractLayer.__xor__"></a>

#### \_\_xor\_\_

```python
def __xor__(other: AbstractLayer) -> DerivedLayer
```

Represents boolean XOR (^) operation between two derived layers.

**Arguments**:

- `other` _AbstractLayer_ - Another Layer object to perform XOR operation.
  

**Returns**:

  A new DerivedLayer with the XOR operation logged.

<a id="gdsfactory.technology.layer_stack.AbstractLayer.__sub__"></a>

#### \_\_sub\_\_

```python
def __sub__(other: AbstractLayer) -> DerivedLayer
```

Represents boolean NOT (-) operation on a derived layer.

**Arguments**:

- `other` _AbstractLayer_ - Another Layer object to perform NOT operation.
  

**Returns**:

  A new DerivedLayer with the NOT operation logged.

<a id="gdsfactory.technology.layer_stack.AbstractLayer.sized"></a>

#### sized

```python
def sized(xoffset: int | tuple[int, ...],
          yoffset: int | tuple[int, ...] | None = None,
          mode: int | tuple[int, ...] | None = None) -> T
```

Accumulates a list of sizing operations for the layer by the provided offset (in dbu).

**Arguments**:

- `xoffset` _int | tuple_ - number of dbu units to buffer by. Can be a tuple for sequential sizing operations.
- `yoffset` _int | tuple_ - number of dbu units to buffer by in the y-direction. If not specified, uses xfactor. Can be a tuple for sequential sizing operations.
- `mode` _int | tuple_ - mode of the sizing operation(s). Can be a tuple for sequential sizing operations.

<a id="gdsfactory.technology.layer_stack.LogicalLayer"></a>

## LogicalLayer Objects

```python
class LogicalLayer(AbstractLayer)
```

GDS design layer.

<a id="gdsfactory.technology.layer_stack.LogicalLayer.__eq__"></a>

#### \_\_eq\_\_

```python
def __eq__(other: object) -> bool
```

Check if two LogicalLayer instances are equal.

This method compares the 'layer' attribute of the two LogicalLayer instances.

**Arguments**:

- `other` _LogicalLayer_ - The other LogicalLayer instance to compare with.
  

**Returns**:

- `bool` - True if the 'layer' attributes are equal, False otherwise.
  

**Raises**:

- `NotImplementedError` - If 'other' is not an instance of LogicalLayer.

<a id="gdsfactory.technology.layer_stack.LogicalLayer.__hash__"></a>

#### \_\_hash\_\_

```python
def __hash__() -> int
```

Generates a hash value for a LogicalLayer instance.

This method allows LogicalLayer instances to be used in hash-based data structures such as sets and dictionaries.

**Returns**:

- `int` - The hash value of the layer attribute.

<a id="gdsfactory.technology.layer_stack.LogicalLayer.get_shapes"></a>

#### get\_shapes

```python
def get_shapes(component: "Component") -> kf.kdb.Region
```

Return the shapes of the component argument corresponding to this layer.

**Arguments**:

- `component` - Component from which to extract shapes on this layer.
  

**Returns**:

- `kf.kdb.Region` - A region of polygons on this layer.

<a id="gdsfactory.technology.layer_stack.LogicalLayer.__repr__"></a>

#### \_\_repr\_\_

```python
def __repr__() -> str
```

Print text representation.

<a id="gdsfactory.technology.layer_stack.DerivedLayer"></a>

## DerivedLayer Objects

```python
class DerivedLayer(AbstractLayer)
```

Physical "derived layer", resulting from a combination of GDS design layers. Can be used by renderers and simulators.

Overloads operators for simpler expressions.

**Attributes**:

- `input_layer1` - primary layer comprising the derived layer. Can be a GDS design layer (kf.kcell.LayerEnum , tuple[int, int]), or another derived layer.
- `input_layer2` - secondary layer comprising the derived layer. Can be a GDS design layer (kf.kcell.LayerEnum , tuple[int, int]), or another derived layer.
- `operation` - operation to perform between layer1 and layer2. One of "and", "or", "xor", or "not" or associated symbols.

<a id="gdsfactory.technology.layer_stack.DerivedLayer.__hash__"></a>

#### \_\_hash\_\_

```python
def __hash__() -> int
```

Generates a hash value for a LogicalLayer instance.

This method allows LogicalLayer instances to be used in hash-based data structures such as sets and dictionaries.

**Returns**:

- `int` - The hash value of the layer attribute.

<a id="gdsfactory.technology.layer_stack.DerivedLayer.get_shapes"></a>

#### get\_shapes

```python
def get_shapes(component: "Component") -> kf.kdb.Region
```

Return the shapes of the component argument corresponding to this layer.

**Arguments**:

- `component` - Component from which to extract shapes on this layer.
  

**Returns**:

- `kf.kdb.Region` - A region of polygons on this layer.

<a id="gdsfactory.technology.layer_stack.DerivedLayer.__repr__"></a>

#### \_\_repr\_\_

```python
def __repr__() -> str
```

Print text representation.

<a id="gdsfactory.technology.layer_stack.LayerLevel"></a>

## LayerLevel Objects

```python
class LayerLevel(BaseModel)
```

Level for 3D LayerStack.

**Arguments**:

- `name` - str
- `layer` - LogicalLayer or DerivedLayer. DerivedLayers can be composed of operations consisting of multiple other GDSLayers or other DerivedLayers.
- `derived_layer` - if the layer is derived, LogicalLayer to assign to the derived layer.
- `thickness` - layer thickness in um.
- `thickness_tolerance` - layer thickness tolerance in um.
- `width_tolerance` - layer width tolerance in um.
- `zmin` - height position where material starts in um.
- `zmin_tolerance` - layer height tolerance in um.
- `sidewall_angle` - in degrees with respect to normal.
- `sidewall_angle_tolerance` - in degrees.
- `width_to_z` - if sidewall_angle, reference z-position (0 --> zmin, 1 --> zmin + thickness, 0.5 in the middle).
- `bias` - shrink/grow of the level compared to the mask
- `z_to_bias` - most generic way to specify an extrusion.            Two tuples of the same length specifying the shrink/grow (float) to apply between zmin (0) and zmin + thickness (1)            I.e. [[z1, z2, ..., zN], [bias1, bias2, ..., biasN]]                    Defaults no buffering [[0, 1], [0, 0]].
- `NOTE` - A dict might be more expressive.
- `mesh_order` - lower mesh order (e.g. 1) will have priority over higher mesh order (e.g. 2) in the regions where materials overlap.
- `material` - used in the klayout script
- `info` - all other rendering and simulation metadata should go here.

<a id="gdsfactory.technology.layer_stack.LayerLevel.bounds"></a>

#### bounds

```python
@property
def bounds() -> tuple[float, float]
```

Calculates and returns the bounds of the layer level in the z-direction.

**Returns**:

- `tuple` - A tuple containing the minimum and maximum z-values of the layer level.

<a id="gdsfactory.technology.layer_stack.LayerStack"></a>

## LayerStack Objects

```python
class LayerStack(BaseModel)
```

For simulation and 3D rendering. Captures design intent of the chip layers after fabrication.

**Arguments**:

- `layers` - dict of layer_levels.

<a id="gdsfactory.technology.layer_stack.LayerStack.model_copy"></a>

#### model\_copy

```python
def model_copy(*,
               update: Mapping[str, Any] | None = None,
               deep: bool = False) -> LayerStack
```

Returns a copy of the LayerStack.

<a id="gdsfactory.technology.layer_stack.LayerStack.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**data: Any) -> None
```

Add LayerLevels automatically for subclassed LayerStacks.

<a id="gdsfactory.technology.layer_stack.LayerStack.get_layer_to_thickness"></a>

#### get\_layer\_to\_thickness

```python
def get_layer_to_thickness() -> dict[BroadLayer, float]
```

Returns layer tuple to thickness (um).

<a id="gdsfactory.technology.layer_stack.LayerStack.get_component_with_derived_layers"></a>

#### get\_component\_with\_derived\_layers

```python
def get_component_with_derived_layers(component: "Component",
                                      **kwargs: Any) -> "Component"
```

Returns component with derived layers.

<a id="gdsfactory.technology.layer_stack.LayerStack.get_layer_to_zmin"></a>

#### get\_layer\_to\_zmin

```python
def get_layer_to_zmin() -> dict[BroadLayer, float]
```

Returns layer tuple to z min position (um).

<a id="gdsfactory.technology.layer_stack.LayerStack.get_layer_to_material"></a>

#### get\_layer\_to\_material

```python
def get_layer_to_material() -> dict[BroadLayer, str | None]
```

Returns layer tuple to material name.

<a id="gdsfactory.technology.layer_stack.LayerStack.get_layer_to_sidewall_angle"></a>

#### get\_layer\_to\_sidewall\_angle

```python
def get_layer_to_sidewall_angle() -> dict[BroadLayer, float]
```

Returns layer tuple to material name.

<a id="gdsfactory.technology.layer_stack.LayerStack.get_layer_to_info"></a>

#### get\_layer\_to\_info

```python
def get_layer_to_info() -> dict[BroadLayer, dict[str, Any]]
```

Returns layer tuple to info dict.

<a id="gdsfactory.technology.layer_stack.LayerStack.get_layer_to_layername"></a>

#### get\_layer\_to\_layername

```python
def get_layer_to_layername() -> dict[BroadLayer, list[str]]
```

Returns layer tuple to layername.

<a id="gdsfactory.technology.layer_stack.LayerStack.__getitem__"></a>

#### \_\_getitem\_\_

```python
def __getitem__(key: str) -> LayerLevel
```

Access layer stack elements.

<a id="gdsfactory.technology.layer_stack.LayerStack.get_klayout_3d_script"></a>

#### get\_klayout\_3d\_script

```python
def get_klayout_3d_script(layer_views: LayerViews | None = None,
                          dbu: float | None = 0.001) -> str
```

Returns script for 2.5D view in KLayout.

You can include this information in your tech.lyt

**Arguments**:

- `layer_views` - optional layer_views.
- `dbu` - Optional database unit. Defaults to 1nm.

<a id="gdsfactory.technology.layer_stack.LayerStack.filtered"></a>

#### filtered

```python
def filtered(layers: list[str]) -> LayerStack
```

Returns filtered layerstack, given layer specs.

<a id="gdsfactory.technology.layer_stack.LayerStack.z_offset"></a>

#### z\_offset

```python
def z_offset(dz: float) -> LayerStack
```

Translates the z-coordinates of the layerstack.

<a id="gdsfactory.technology.layer_stack.LayerStack.invert_zaxis"></a>

#### invert\_zaxis

```python
def invert_zaxis() -> LayerStack
```

Flips the zmin values about the origin.

<a id="gdsfactory.technology.layer_stack.get_component_with_derived_layers"></a>

#### get\_component\_with\_derived\_layers

```python
def get_component_with_derived_layers(component: "Component",
                                      layer_stack: LayerStack) -> "Component"
```

Returns a component with derived layers.

**Arguments**:

- `component` - Component to get derived layers for.
- `layer_stack` - Layer stack to get derived layers from.

<a id="gdsfactory.path"></a>

# gdsfactory.path

You can define a path with a list of points combined with a cross-section.

A path can be extruded using any CrossSection returning a Component
The CrossSection defines the layer numbers, widths and offsets

Adapted from PHIDL https://github.com/amccaugh/phidl/ by Adam McCaughan

<a id="gdsfactory.path.reflect_points"></a>

#### reflect\_points

```python
def reflect_points(
    points: npt.NDArray[np.floating[Any]],
    p1: tuple[float, float] = (0, 0),
    p2: tuple[float, float] = (1, 0)
) -> npt.NDArray[np.float64]
```

Reflects points across the line formed by p1 and p2.

from https://github.com/amccaugh/phidl/pull/181

``points`` may be input as either single points [1,2] or array-like[N][2],
and will return in kind.

**Arguments**:

- `points` - array-like[N][2]
- `p1` - Coordinates of the start of the reflecting line.
- `p2` - Coordinates of the end of the reflecting line.
  

**Returns**:

  A new set of points that are reflected across ``p1`` and ``p2``.

<a id="gdsfactory.path.Path"></a>

## Path Objects

```python
class Path(UMGeometricObject)
```

You can extrude a Path with a CrossSection to create a Component.

**Arguments**:

- `path` - array-like[N][2], Path, or list of Paths.

<a id="gdsfactory.path.Path.__init__"></a>

#### \_\_init\_\_

```python
def __init__(path: npt.NDArray[np.floating[Any]] | Path | None = None) -> None
```

Creates an empty path.

<a id="gdsfactory.path.Path.__repr__"></a>

#### \_\_repr\_\_

```python
def __repr__() -> str
```

Returns path points.

<a id="gdsfactory.path.Path.__len__"></a>

#### \_\_len\_\_

```python
def __len__() -> int
```

Returns path points.

<a id="gdsfactory.path.Path.__iadd__"></a>

#### \_\_iadd\_\_

```python
def __iadd__(path_or_points: npt.NDArray[np.floating[Any]] | Path) -> Path
```

Adds points to current path.

<a id="gdsfactory.path.Path.__add__"></a>

#### \_\_add\_\_

```python
def __add__(path: npt.NDArray[np.floating[Any]] | Path) -> Path
```

Returns new path concatenating current and new path.

<a id="gdsfactory.path.Path.bbox_np"></a>

#### bbox\_np

```python
def bbox_np() -> npt.NDArray[np.float64]
```

Returns the bounding box of the Path as a numpy array.

<a id="gdsfactory.path.Path.append"></a>

#### append

```python
def append(path: npt.NDArray[np.floating[Any]] | Path | list[Path]) -> Path
```

Attach Path to the end of this Path.

The input path automatically rotates and translates such that it continues
smoothly from the previous segment.

**Arguments**:

- `path` - Path, array-like[N][2], or list of Paths. The input path that will be appended.

<a id="gdsfactory.path.Path.offset"></a>

#### offset

```python
def offset(offset: float | Callable[[float], float] = 0) -> Path
```

Offsets Path so that it follows the Path centerline plus an offset.

The offset can either be a fixed value, or a function
of the form my_offset(t) where t goes from 0->1

**Arguments**:

- `offset` - int or float, callable. Magnitude of the offset

<a id="gdsfactory.path.Path.centerpoint_offset_curve"></a>

#### centerpoint\_offset\_curve

```python
def centerpoint_offset_curve(
        points: npt.NDArray[np.floating[Any]],
        offset_distance: float | Sequence[float]
    | npt.NDArray[np.floating[Any]],
        start_angle: float | None = None,
        end_angle: float | None = None) -> npt.NDArray[np.floating[Any]]
```

Creates a offset curve computing the centerpoint offset of x and y points.

**Arguments**:

- `points` - array-like[N][2] The points to be offset.
- `offset_distance` - array-like[N] The distance to offset the points.
- `start_angle` - float or None The angle at the start of the path.
- `end_angle` - float or None The angle at the end of the path.

<a id="gdsfactory.path.Path.length"></a>

#### length

```python
def length() -> float
```

Return cumulative length.

<a id="gdsfactory.path.Path.curvature"></a>

#### curvature

```python
def curvature(
) -> tuple[npt.NDArray[np.floating[Any]], npt.NDArray[np.floating[Any]]]
```

Calculates Path curvature.

The curvature is numerically computed so areas where the curvature
jumps instantaneously (such as between an arc and a straight segment)
will be slightly interpolated, and sudden changes in point density
along the curve can cause discontinuities.

**Returns**:

- `s` - array-like[N] The arc-length of the Path
- `K` - array-like[N] The curvature of the Path

<a id="gdsfactory.path.Path.__hash__"></a>

#### \_\_hash\_\_

```python
def __hash__() -> int
```

Computes a hash of the Path.

<a id="gdsfactory.path.Path.hash_geometry"></a>

#### hash\_geometry

```python
def hash_geometry(precision: float = 1e-4) -> int
```

Computes an SHA1 hash of the points in the Path and the start_angle and end_angle.

**Arguments**:

- `precision` - Rounding precision for the the objects in the Component. For instance,                     a precision of 1e-2 will round a point at (0.124, 1.748) to (0.12, 1.75)
  

**Returns**:

  str Hash result in the form of an SHA1 hex digest string.
  
  .. code::
  
  hash(
  hash(First layer information: [layer1, datatype1]),
  hash(Polygon 1 on layer 1 points: [(x1,y1),(x2,y2),(x3,y3)] ),
  hash(Polygon 2 on layer 1 points: [(x1,y1),(x2,y2),(x3,y3),(x4,y4)] ),
  hash(Polygon 3 on layer 1 points: [(x1,y1),(x2,y2),(x3,y3)] ),
  hash(Second layer information: [layer2, datatype2]),
  hash(Polygon 1 on layer 2 points: [(x1,y1),(x2,y2),(x3,y3),(x4,y4)] ),
  hash(Polygon 2 on layer 2 points: [(x1,y1),(x2,y2),(x3,y3)] ),
  )

<a id="gdsfactory.path.Path.plot"></a>

#### plot

```python
def plot() -> None
```

Plot path in matplotlib.

.. plot::
    :include-source:

    import gdsfactory as gf

    p = gf.path.euler(radius=10)
    p.plot()

<a id="gdsfactory.path.Path.extrude"></a>

#### extrude

```python
def extrude(cross_section: CrossSectionSpec | None = None,
            layer: LayerSpec | None = None,
            width: float | None = None,
            simplify: float | None = None,
            all_angle: bool = False) -> AnyComponent
```

Returns Component by extruding a Path with a CrossSection.

A path can be extruded using any CrossSection returning a Component
The CrossSection defines the layer numbers, widths and offsets.

**Arguments**:

- `cross_section` - to extrude.
- `layer` - optional layer.
- `width` - optional width in um.
- `simplify` - Tolerance value for the simplification algorithm.                     All points that can be removed without changing the resulting polygon                    by more than the value listed here will be removed.
  
- `all_angle` - if True, the bend is drawn with a single euler curve.
  
  .. plot::
  :include-source:
  
  import gdsfactory as gf
  
  p = gf.path.euler(radius=10)
  c = p.extrude(layer=(1, 0), width=0.5)
  c.plot()

<a id="gdsfactory.path.Path.copy"></a>

#### copy

```python
def copy() -> Path
```

Returns a copy of the Path.

<a id="gdsfactory.path.Path.mirror"></a>

#### mirror

```python
def mirror(p1: tuple[float, float] = (0, 1),
           p2: tuple[float, float] = (0, 0)) -> Path
```

Mirrors the Path across the line formed between the two specified points.

``points`` may be input as either single points [1,2]
or array-like[N][2], and will return in kind.

**Arguments**:

- `p1` - First point of the line.
- `p2` - Second point of the line.

<a id="gdsfactory.path.transition_exponential"></a>

#### transition\_exponential

```python
def transition_exponential(
    y1: float,
    y2: float,
    exp: float = 0.5
) -> Callable[[npt.NDArray[np.floating[Any]]], npt.NDArray[np.floating[Any]]]
```

Returns the function for an exponential transition.

**Arguments**:

- `y1` - start width in um.
- `y2` - end width in um.
- `exp` - exponent.

<a id="gdsfactory.path.transition_adiabatic"></a>

#### transition\_adiabatic

```python
def transition_adiabatic(
    w1: float,
    w2: float,
    neff_w: Callable[[float], float],
    wavelength: float = 1.55,
    alpha: float = 1,
    max_length: float = 200,
    num_points_ODE: int = 2000
) -> tuple[npt.NDArray[np.floating[Any]], npt.NDArray[np.floating[Any]]]
```

Returns the points for an optimal adiabatic transition for well-guided modes.

**Arguments**:

- `w1` - start width in um.
- `w2` - end width in um.
- `neff_w` - a callable that returns the effective index as a function of width.                 By default, use a compact model of neff(y) for fundamental 1550 nm TE                 mode of 220nm-thick core with 3.45 index, fully clad with 1.44 index.                Many coefficients are needed to capture the behaviour.
- `wavelength` - wavelength, in same units as widths.
- `alpha` - parameter that scales the rate of width change
  - closer to 0 means longer and more adiabatic;
  - 1 is the intuitive limit beyond which higher order modes are excited;
  - [2] reports good performance up to 1.4 for fundamental TE in SOI (for multiple core thicknesses)
- `max_length` - maximum length in um.
- `num_points_ODE` - number of samplings points for the ODE solve.
  

**References**:

  [1] Burns, W. K., et al. "Optical waveguide parabolic coupling horns."
  Appl. Phys. Lett., vol. 30, no. 1, 1 Jan. 1977, pp. 28-30, doi:10.1063/1.89199.
  [2] Fu, Yunfei, et al. "Efficient adiabatic silicon-on-insulator waveguide taper."
  Photonics Res., vol. 2, no. 3, 1 June 2014, pp. A41-A44, doi:10.1364/PRJ.2.000A41.

<a id="gdsfactory.path.transition"></a>

#### transition

```python
def transition(
    cross_section1: CrossSectionSpec,
    cross_section2: CrossSectionSpec,
    width_type: WidthTypes | Callable[[float, float, float], float] = "sine",
    offset_type: WidthTypes | Callable[[float, float, float], float] = "sine"
) -> Transition
```

Returns a smoothly-transitioning between two CrossSections.

Only cross-sectional elements that have the `name` (as in X.add(..., name = 'wg') )
parameter specified in both input CrosSections will be created.
Port names will be cloned from the input CrossSections in reverse.

**Arguments**:

- `cross_section1` - First CrossSection.
- `cross_section2` - Second CrossSection.
- `width_type` - 'sine', 'parabolic', 'linear' or Callable. type of width transition used                 if any widths are different between the two input CrossSections.
- `offset_type` - 'sine', 'parabolic', 'linear' or Callable. type of width transition used                 if any widths are different between the two input CrossSections.

<a id="gdsfactory.path.along_path"></a>

#### along\_path

```python
def along_path(p: Path, component: ComponentSpec, spacing: float,
               padding: float) -> Component
```

Returns Component containing many copies of `component` along `p`.

Places as many copies of `component` along each segment of `p` as possible
under the given constraints. `spacing` is always followed precisely, but
actual `padding` may exceed the provided value to place components evenly.

**Arguments**:

- `p` - Path to place components along.
- `component` - Component to repeat along the path. The unrotated version of                 this object should be oriented for placement on a horizontal line.
- `spacing` - distance between component placements.
- `padding` - minimum distance from the path start to the first component.

<a id="gdsfactory.path.extrude"></a>

#### extrude

```python
def extrude(p: Path,
            cross_section: CrossSectionSpec | None = None,
            layer: LayerSpec | None = None,
            width: float | None = None,
            simplify: float | None = None,
            all_angle: bool = False) -> AnyComponent
```

Returns Component extruding a Path with a cross_section.

A path can be extruded using any CrossSection returning a Component
The CrossSection defines the layer numbers, widths and offsets

**Arguments**:

- `p` - a path is a list of points (arc, straight, euler).
- `cross_section` - to extrude.
- `layer` - optional layer to extrude.
- `width` - optional width to extrude.
- `simplify` - Tolerance value for the simplification algorithm.                 All points that can be removed without changing the resulting polygon                 by more than the value listed here will be removed.
- `all_angle` - if True, the bend is drawn with a single euler curve.

<a id="gdsfactory.path.extrude_transition"></a>

#### extrude\_transition

```python
def extrude_transition(p: Path, transition: Transition) -> Component
```

Extrudes a path along a transition.

**Arguments**:

- `p` - path to extrude.
- `transition` - transition to extrude along.

<a id="gdsfactory.path.arc"></a>

#### arc

```python
def arc(radius: float | None = 10.0,
        angle: float = 90,
        npoints: int | None = None,
        start_angle: float = -90) -> Path
```

Returns a radial arc.

**Arguments**:

- `radius` - minimum radius of curvature.
- `angle` - total angle of the curve.
- `npoints` - Number of points used per 360 degrees. Defaults to pdk.bend_points_distance.
- `start_angle` - initial angle of the curve for drawing, default -90 degrees.
  
  .. plot::
  :include-source:
  
  import gdsfactory as gf
  
  p = gf.path.arc(radius=10, angle=45)
  p.plot()

<a id="gdsfactory.path.euler"></a>

#### euler

```python
def euler(radius: float = 10,
          angle: float = 90,
          p: float = 0.5,
          use_eff: bool = False,
          npoints: int | None = None) -> Path
```

Returns an euler bend that adiabatically transitions from straight to curved.

`radius` is the minimum radius of curvature of the bend.
However, if `use_eff` is set to True, `radius` corresponds to the effective
radius of curvature (making the curve a drop-in replacement for an arc).
If p < 1.0, will create a "partial euler" curve as described in Vogelbacher et. al.
https://dx.doi.org/10.1364/oe.27.031394

**Arguments**:

- `radius` - minimum radius of curvature.
- `angle` - total angle of the curve.
- `p` - Proportion of the curve that is an Euler curve.
- `use_eff` - If False: `radius` is the minimum radius of curvature of the bend.                 If True: The curve will be scaled such that the endpoints match an                 arc with parameters `radius` and `angle`.
- `npoints` - Number of points used per 360 degrees.
  
  .. plot::
  :include-source:
  
  import gdsfactory as gf
  
  p = gf.path.euler(radius=10, angle=45, p=1, use_eff=True, npoints=720)
  p.plot()

<a id="gdsfactory.path.straight"></a>

#### straight

```python
def straight(length: float = 10.0, npoints: int = 2) -> Path
```

Returns a straight path.

For transitions you should increase have at least 100 points

**Arguments**:

- `length` - of straight.
- `npoints` - number of points.

<a id="gdsfactory.path.spiral_archimedean"></a>

#### spiral\_archimedean

```python
def spiral_archimedean(min_bend_radius: float, separation: float,
                       number_of_loops: float, npoints: int) -> Path
```

Returns an Archimedean spiral.

**Arguments**:

- `min_bend_radius` - Inner radius of the spiral.
- `separation` - Separation between the loops in um.
- `number_of_loops` - number of loops.
- `npoints` - number of Points.
  
  .. plot::
  :include-source:
  
  import gdsfactory as gf
  
  p = gf.path.spiral_archimedean(min_bend_radius=5, separation=2, number_of_loops=3, npoints=200)
  p.plot()

<a id="gdsfactory.path.smooth"></a>

#### smooth

```python
def smooth(points: npt.NDArray[np.floating[Any]] | Path,
           radius: float = 4.0,
           bend: PathFactory = euler,
           **kwargs: Any) -> Path
```

Returns a smooth Path from a series of waypoints.

**Arguments**:

- `points` - array-like[N][2] List of waypoints for the path to follow.
- `radius` - radius of curvature, passed to `bend`.
- `bend` - bend function that returns a path that round corners.
- `kwargs` - Extra keyword arguments that will be passed to `bend`.
  
  .. plot::
  :include-source:
  
  import gdsfactory as gf
  
  p = gf.path.smooth(([0, 0], [0, 10], [10, 10]))
  p.plot()

<a id="gdsfactory.write_cells"></a>

# gdsfactory.write\_cells

Generate the code from a GDS file based PDK.

<a id="gdsfactory.write_cells.get_script"></a>

#### get\_script

```python
def get_script(gdspath: PathType, module: str | None = None) -> str
```

Returns script for importing a fixed cell.

**Arguments**:

- `gdspath` - fixed cell gdspath.
- `module` - if any includes plot directive.

<a id="gdsfactory.write_cells.get_import_gds_script"></a>

#### get\_import\_gds\_script

```python
def get_import_gds_script(dirpath: PathType, module: str | None = None) -> str
```

Returns import_gds script from a directory with all the GDS files.

**Arguments**:

- `dirpath` - fixed cell directory path.
- `module` - Optional plot directive to plot imported component.

<a id="gdsfactory.write_cells.write_cells_recursively"></a>

#### write\_cells\_recursively

```python
def write_cells_recursively(gdspath: PathType,
                            dirpath: PathType | None = None
                            ) -> dict[str, Path]
```

Write gdstk cells recursively.

**Arguments**:

- `gdspath` - gds file to write cells from.
- `dirpath` - directory for the GDS file to write to.
  

**Returns**:

- `gdspaths` - dict of cell name to gdspath.

<a id="gdsfactory.write_cells.write_cells"></a>

#### write\_cells

```python
def write_cells(gdspath: PathType,
                dirpath: PathType | None = None) -> dict[str, Path]
```

Writes cells into separate GDS files.

**Arguments**:

- `gdspath` - GDS file to write cells.
- `dirpath` - directory path to write GDS files to.
  Defaults to current working directory.
  

**Returns**:

- `gdspaths` - dict of cell name to gdspath.

<a id="gdsfactory.add_ports"></a>

# gdsfactory.add\_ports

Add ports from pin markers or labels.

<a id="gdsfactory.add_ports.add_ports_from_markers_square"></a>

#### add\_ports\_from\_markers\_square

```python
def add_ports_from_markers_square(component: Component,
                                  pin_layer: LayerSpec = "DEVREC",
                                  port_layer: LayerSpec | None = None,
                                  orientation: AngleInDegrees = 90,
                                  min_pin_area_um2: float = 0,
                                  max_pin_area_um2: float | None = 150 * 150,
                                  pin_extra_width: float = 0.0,
                                  port_names: Sequence[str] | None = None,
                                  port_name_prefix: str | None = None,
                                  port_type: str = "optical") -> Component
```

Add ports from square markers at the port center in port_layer.

**Arguments**:

- `component` - to read polygons from and to write ports to.
- `pin_layer` - for port markers.
- `port_layer` - for the new created port.
- `orientation` - in degrees 90 north, 0 east, 180 west, 270 south.
- `min_pin_area_um2` - ignores pins with area smaller than min_pin_area_um2.
- `max_pin_area_um2` - ignore pins for area above certain size.
- `pin_extra_width` - 2*offset from pin to straight.
- `port_names` - names of the ports (defaults to {i}).
- `port_name_prefix` - defaults to 'o' for optical and 'e' for electrical.
- `port_type` - optical, electrical.

<a id="gdsfactory.add_ports.add_ports_from_markers_center"></a>

#### add\_ports\_from\_markers\_center

```python
def add_ports_from_markers_center(component: Component,
                                  pin_layer: LayerSpec,
                                  port_layer: LayerSpec | None = None,
                                  inside: bool = False,
                                  tol: float = 0.1,
                                  pin_extra_width: float = 0.0,
                                  min_pin_area_um2: float | None = None,
                                  max_pin_area_um2: float | None = None,
                                  skip_square_ports: bool = False,
                                  xcenter: float | None = None,
                                  ycenter: float | None = None,
                                  port_name_prefix: str | None = None,
                                  port_type: str = "optical",
                                  ports_on_short_side: bool = False,
                                  auto_rename_ports: bool = True,
                                  debug: bool = False) -> Component
```

Add ports from pins guessing port orientation from component boundary.

**Arguments**:

- `component` - to read polygons from and to write ports to.
- `pin_layer` - layer for pin maker.
- `port_layer` - for the new created port. Defaults to pin_layer.
- `inside` - True-> markers  inside. False-> markers at center.
- `tol` - tolerance area to search ports at component boundaries dxmin, dymin, dxmax, dxmax.
- `pin_extra_width` - 2*offset from pin to straight.
- `min_pin_area_um2` - ignores pins with area smaller than min_pin_area_um2.
- `max_pin_area_um2` - ignore pins for area above certain size.
- `skip_square_ports` - skips square ports (hard to guess orientation).
- `xcenter` - for guessing orientation of rectangular ports.
- `ycenter` - for guessing orientation of rectangular ports.
- `port_name_prefix` - defaults to 'o' for optical and 'e' for electrical ports.
- `port_type` - type of port (optical, electrical ...).
- `ports_on_short_side` - if the port is on the short side rather than the long side.
- `auto_rename_ports` - if True auto rename ports to avoid duplicates.
- `debug` - if True prints ports that are skipped.
  
  For inside=False the port location is at the middle of the PIN
  
  .. code::
  _______________
  |               |
  |               |
  |||             |||____  | pin_extra_width/2 > 0
  |||             |||
  |||             |||____
  |||             |||
  |      __       |
  |_____|__|______|
  |__|
  
  For inside=True all the pin is inside the port
  
  .. code::
  _______________
  |               |
  |               |
  |_              |
  | |             |
  |_|             |
  |               |
  |      __       |
  |_____|__|______|
  
  dx < dy: port is east or west
  dx > xc: east
  dx < xc: west
  
  dx > dy: port is north or south
  dy > yc: north
  dy < yc: south
  
  dx = dy
  dx > xc: east
  dx < xc: west

<a id="gdsfactory.add_ports.add_ports_from_boxes"></a>

#### add\_ports\_from\_boxes

```python
def add_ports_from_boxes(component: Component,
                         pin_layer: LayerSpec,
                         port_layer: LayerSpec | None = None,
                         inside: bool = False,
                         tol: float = 0.1,
                         pin_extra_width: float = 0.0,
                         min_pin_area_um2: float | None = None,
                         max_pin_area_um2: float | None = 150.0 * 150.0,
                         skip_square_ports: bool = False,
                         xcenter: float | None = None,
                         ycenter: float | None = None,
                         port_name_prefix: str | None = None,
                         port_type: str = "optical",
                         ports_on_short_side: bool = False,
                         auto_rename_ports: bool = True,
                         debug: bool = False) -> Component
```

Add ports from pins guessing port orientation from component boundary.

**Arguments**:

- `component` - to read polygons from and to write ports to.
- `pin_layer` - layer for pin maker.
- `port_layer` - for the new created port. Defaults to pin_layer.
- `inside` - True-> markers  inside. False-> markers at center.
- `tol` - tolerance area to search ports at component boundaries dxmin, dymin, dxmax, dxmax.
- `pin_extra_width` - 2*offset from pin to straight.
- `min_pin_area_um2` - ignores pins with area smaller than min_pin_area_um2.
- `max_pin_area_um2` - ignore pins for area above certain size.
- `skip_square_ports` - skips square ports (hard to guess orientation).
- `xcenter` - for guessing orientation of rectangular ports.
- `ycenter` - for guessing orientation of rectangular ports.
- `port_name_prefix` - defaults to 'o' for optical and 'e' for electrical ports.
- `port_type` - type of port (optical, electrical ...).
- `ports_on_short_side` - if the port is on the short side rather than the long side.
- `auto_rename_ports` - if True auto rename ports to avoid duplicates.
- `debug` - if True prints ports that are skipped.
  
  For inside=False the port location is at the middle of the PIN
  
  .. code::
  _______________
  |               |
  |               |
  |||             |||____  | pin_extra_width/2 > 0
  |||             |||
  |||             |||____
  |||             |||
  |      __       |
  |_____|__|______|
  |__|
  
  For inside=True all the pin is inside the port
  
  .. code::
  _______________
  |               |
  |               |
  |_              |
  | |             |
  |_|             |
  |               |
  |      __       |
  |_____|__|______|
  
  dx < dy: port is east or west
  dx > xc: east
  dx < xc: west
  
  dx > dy: port is north or south
  dy > yc: north
  dy < yc: south
  
  dx = dy
  dx > xc: east
  dx < xc: west

<a id="gdsfactory.add_ports.add_ports_from_labels"></a>

#### add\_ports\_from\_labels

```python
def add_ports_from_labels(component: Component,
                          port_width: float,
                          port_layer: LayerSpec,
                          xcenter: float | None = None,
                          port_name_prefix: str | None = None,
                          port_type: str = "optical",
                          get_name_from_label: bool = False,
                          layer_label: LayerSpec | None = None,
                          fail_on_duplicates: bool = False,
                          port_orientation: AngleInDegrees = 0,
                          guess_port_orientation: bool = True,
                          port_filter_prefix: str | None = None) -> Component
```

Add ports from labels.

Assumes that all ports have a label at the port center.
because labels do not have width, you have to manually specify the ports width

**Arguments**:

- `component` - to read polygons from and to write ports to.
- `port_width` - for ports.
- `port_layer` - for the new created port.
- `xcenter` - center of the component, for guessing port orientation.
- `port_name_prefix` - defaults to 'o' for optical and 'e' for electrical.
- `port_type` - optical, electrical.
- `get_name_from_label` - uses the label text as port name.
- `layer_label` - layer for the label.
- `fail_on_duplicates` - raises ValueError for duplicated port names.
  if False adds incremental suffix (1, 2 ...) to port name.
- `port_orientation` - None for electrical ports.
- `guess_port_orientation` - assumes right: 0, left: 180, top: 90, bot: 270.
- `port_filter_prefix` - prefix for the port name.

<a id="gdsfactory.add_ports.add_ports_from_siepic_pins"></a>

#### add\_ports\_from\_siepic\_pins

```python
def add_ports_from_siepic_pins(component: Component,
                               pin_layer: LayerSpec = "PORT",
                               port_layer: LayerSpec | None = None,
                               port_type: str = "optical") -> Component
```

Add ports from SiEPIC-type cells, where the pins are defined as paths.

Looks for label, path pairs.

**Arguments**:

- `component` - component.
- `pin_layer` - layer for optical pins.
- `port_layer` - layer for optical ports.
- `port_type` - optical, electrical.

<a id="gdsfactory.read.import_gds"></a>

# gdsfactory.read.import\_gds

<a id="gdsfactory.read.import_gds.import_gds"></a>

#### import\_gds

```python
def import_gds(gdspath: str | Path,
               cellname: str | None = None,
               post_process: PostProcesses | None = None,
               rename_duplicated_cells: bool = False) -> Component
```

Reads a GDS file and returns a Component.

**Arguments**:

- `gdspath` - path to GDS file.
- `cellname` - name of the cell to return. Defaults to top cell.
- `post_process` - function to run after reading the GDS file.
- `rename_duplicated_cells` - if True, rename duplicated cells.

<a id="gdsfactory.read.import_gds.import_gds_with_conflicts"></a>

#### import\_gds\_with\_conflicts

```python
def import_gds_with_conflicts(gdspath: str | Path,
                              cellname: str | None = None) -> Component
```

Reads a GDS file and returns a Component.

**Arguments**:

- `gdspath` - path to GDS file.
- `cellname` - name of the cell to return. Defaults to top cell.
  
  Modes:
- `AddToCell` - Add content to existing cell. Content of new cells is simply added to existing cells with the same name.
- `OverwriteCell` - The old cell is overwritten entirely (including child cells which are not used otherwise)
- `RenameCell` - The new cell will be renamed to become unique
- `SkipNewCell` - The new cell is skipped entirely (including child cells which are not used otherwise)

<a id="gdsfactory.read.from_np"></a>

# gdsfactory.read.from\_np

Read component from a numpy.ndarray.

<a id="gdsfactory.read.from_np.compute_area_signed"></a>

#### compute\_area\_signed

```python
def compute_area_signed(pr: npt.NDArray[np.floating[Any]]) -> float
```

Return the signed area enclosed by a ring using the linear time.

algorithm at http://www.cgafaq.info/wiki/Polygon_Area. A value >= 0
indicates a counter-clockwise oriented ring.

<a id="gdsfactory.read.from_np.from_np"></a>

#### from\_np

```python
def from_np(ndarray: npt.NDArray[np.floating[Any]],
            nm_per_pixel: int = 20,
            layer: tuple[int, int] = (1, 0),
            threshold: float = 0.99,
            invert: bool = True) -> Component
```

Returns Component from a np.ndarray.

Extracts contours skimage.measure.find_contours using `threshold`.

**Arguments**:

- `ndarray` - 2D ndarray representing the device layout.
- `nm_per_pixel` - scale_factor.
- `layer` - layer tuple to output gds.
- `threshold` - value along which to find contours in the array.
- `invert` - invert the mask.

<a id="gdsfactory.read.from_np.from_image"></a>

#### from\_image

```python
@gf.cell
def from_image(image_path: PathType, **kwargs: Any) -> Component
```

Returns Component from a png image.

**Arguments**:

- `image_path` - png file path.
- `kwargs` - for from_np.
  

**Arguments**:

- `nm_per_pixel` - scale_factor.
- `layer` - layer tuple to output gds.
- `threshold` - value along which to find contours in the array.

<a id="gdsfactory.read.from_yaml"></a>

# gdsfactory.read.from\_yaml

Returns Component from YAML syntax.

name: myComponent
settings:
    length: 3

info:
    description: just a demo
    polarization: TE
    ...

instances:
    mzi:
        component: mzi_phase_shifter
        settings:
            delta_length: ${settings.length}
            length_x: 50

    pads:
        component: pad_array
        settings:
            n: 2
            port_names:
                - e4

placements:
    mzi:
        x: 0
    pads:
        y: 200
        x: mzi,cc
ports:
    o1: mzi,o1
    o2: mzi,o2


routes:
    electrical:
        links:
            mzi,etop_e1: pads,e4_0
            mzi,etop_e2: pads,e4_1

        settings:
            layer: [31, 0]
            width: 10
            radius: 10

<a id="gdsfactory.read.from_yaml.place"></a>

#### place

```python
def place(placements_conf: dict[str, dict[str, int | float | str]],
          connections_by_transformed_inst: dict[str, dict[str, str]],
          instances: dict[str, ComponentReference],
          encountered_insts: list[str],
          instance_name: str | None = None,
          all_remaining_insts: list[str] | None = None) -> None
```

Place instance_name based on placements_conf config.

**Arguments**:

- `placements_conf` - Dict of instance_name to placement (x, y, rotation ...).
- `connections_by_transformed_inst` - Dict of connection attributes.
  keyed by the name of the instance which should be transformed.
- `instances` - Dict of references.
- `encountered_insts` - list of encountered_instances.
- `instance_name` - instance_name to place.
- `all_remaining_insts` - list of all the remaining instances to place
  instances pop from this instance as they are placed.

<a id="gdsfactory.read.from_yaml.transform_connections_dict"></a>

#### transform\_connections\_dict

```python
def transform_connections_dict(
    connections_conf: dict[str,
                           str]) -> dict[str, dict[str, str | int | None]]
```

Returns Dict with source_instance_name key and connection properties.

<a id="gdsfactory.read.from_yaml.make_connection"></a>

#### make\_connection

```python
def make_connection(instance_src_name: str,
                    port_src_name: str,
                    instance_dst_name: str,
                    port_dst_name: str,
                    instances: dict[str, ComponentReference],
                    src_ia: int | None = None,
                    src_ib: int | None = None,
                    dst_ia: int | None = None,
                    dst_ib: int | None = None) -> None
```

Connect instance_src_name,port to instance_dst_name,port.

**Arguments**:

- `instance_src_name` - source instance name.
- `port_src_name` - from instance_src_name.
- `instance_dst_name` - destination instance name.
- `port_dst_name` - from instance_dst_name.
- `instances` - dict of instances.
- `src_ia` - the a-index of the source instance, if it is an arrayed instance
- `src_ib` - the b-index of the source instance, if it is an arrayed instance
- `dst_ia` - the a-index of the destination instance, if it is an arrayed instance
- `dst_ib` - the b-index of the destination instance, if it is an arrayed instance

<a id="gdsfactory.read.from_yaml.cell_from_yaml"></a>

#### cell\_from\_yaml

```python
def cell_from_yaml(
        yaml_str: str | pathlib.Path | IO[Any] | dict[str, Any],
        routing_strategies: RoutingStrategies | None = None,
        label_instance_function: LabelInstanceFunction = add_instance_label,
        name: str | None = None) -> Callable[[], Component]
```

Returns Component factory from YAML string or file.

YAML includes instances, placements, routes, ports and connections.

**Arguments**:

- `yaml_str` - YAML string or file.
- `routing_strategies` - for each route.
- `label_instance_function` - to label each instance.
- `name` - Optional name.
- `kwargs` - function settings for creating YAML PCells.
  
  .. code::
  
  valid variables:
  
- `name` - Optional Component name
- `settings` - Optional variables
- `pdk` - overrides
- `info` - Optional component info
- `description` - just a demo
- `polarization` - TE
  ...
  instances:
  name:
- `component` - (ComponentSpec)
  settings (Optional)
- `length` - 10
  ...
  placements:
- `x` - float, str | None  str can be instanceName,portName
- `y` - float, str | None
- `rotation` - float | None
- `mirror` - bool, float | None float is x mirror axis
- `port` - str | None port anchor
- `connections` _Optional_ - between instances
- `ports` _Optional_ - ports to expose
- `routes` _Optional_ - bundles of routes
  routeName:
- `library` - optical
  links:
- `instance1,port1` - instance2,port2
  
  
  .. code::
  
  settings:
- `length_mmi` - 5
  
  instances:
  mmi_bot:
- `component` - mmi1x2
  settings:
- `width_mmi` - 4.5
- `length_mmi` - 10
  mmi_top:
- `component` - mmi1x2
  settings:
- `width_mmi` - 4.5
- `length_mmi` - ${settings.length_mmi}
  
  placements:
  mmi_top:
- `port` - o1
- `x` - 0
- `y` - 0
  mmi_bot:
- `port` - o1
- `x` - mmi_top,o2
- `y` - mmi_top,o2
- `dx` - 30
- `dy` - -30
  routes:
  optical:
- `library` - optical
  links:
- `mmi_top,o3` - mmi_bot,o1

<a id="gdsfactory.read.from_yaml.from_yaml"></a>

#### from\_yaml

```python
def from_yaml(
        yaml_str: str | pathlib.Path | IO[Any] | dict[str, Any],
        routing_strategies: RoutingStrategies | None = None,
        label_instance_function: LabelInstanceFunction = add_instance_label,
        name: str | None = None) -> Component
```

Returns Component from YAML string or file.

YAML includes instances, placements, routes, ports and connections.

**Arguments**:

- `yaml_str` - YAML string or file.
- `routing_strategies` - for each route.
- `label_instance_function` - to label each instance.
- `name` - Optional name.
  
  .. code::
  
  valid variables:
  
- `name` - Optional Component name
- `settings` - Optional variables
- `pdk` - overrides
- `info` - Optional component info
- `description` - just a demo
- `polarization` - TE
  ...
  instances:
  name:
- `component` - (ComponentSpec)
  settings (Optional)
- `length` - 10
  ...
  placements:
- `x` - float, str | None  str can be instanceName,portName
- `y` - float, str | None
- `rotation` - float | None
- `mirror` - bool, float | None float is x mirror axis
- `port` - str | None port anchor
- `connections` _Optional_ - between instances
- `ports` _Optional_ - ports to expose
- `routes` _Optional_ - bundles of routes
  routeName:
- `library` - optical
  links:
- `instance1,port1` - instance2,port2
  
  
  .. code::
  
  settings:
- `length_mmi` - 5
  
  instances:
  mmi_bot:
- `component` - mmi1x2
  settings:
- `width_mmi` - 4.5
- `length_mmi` - 10
  mmi_top:
- `component` - mmi1x2
  settings:
- `width_mmi` - 4.5
- `length_mmi` - ${settings.length_mmi}
  
  placements:
  mmi_top:
- `port` - o1
- `x` - 0
- `y` - 0
  mmi_bot:
- `port` - o1
- `x` - mmi_top,o2
- `y` - mmi_top,o2
- `dx` - 30
- `dy` - -30
  routes:
  optical:
- `library` - optical
  links:
- `mmi_top,o3` - mmi_bot,o1

<a id="gdsfactory.read"></a>

# gdsfactory.read

<a id="gdsfactory.read.from_yaml_template"></a>

# gdsfactory.read.from\_yaml\_template

<a id="gdsfactory.read.from_yaml_template.split_default_settings_from_yaml"></a>

#### split\_default\_settings\_from\_yaml

```python
def split_default_settings_from_yaml(yaml_lines: list[str]) -> tuple[str, str]
```

Separates out the 'default_settings' block from the rest of the file body.

Note: 'default settings' MUST be at the TOP of the file.

**Arguments**:

- `yaml_lines` - the lines of text in the yaml file.
  

**Returns**:

  a tuple of (main file contents), (setting block), both as multi-line strings.

<a id="gdsfactory.read.from_yaml_template.cell_from_yaml_template"></a>

#### cell\_from\_yaml\_template

```python
def cell_from_yaml_template(
        filename: _YamlDefinition,
        name: str,
        routing_strategies: RoutingStrategies | None = None
) -> "ComponentFactory"
```

Gets a PIC factory function from a yaml definition, which can optionally be a jinja template.

**Arguments**:

- `filename` - the filepath of the pic yaml template.
- `name` - the name of the component to create.
- `routing_strategies` - a dictionary of routing functions.
  

**Returns**:

  a factory function for the component.

<a id="gdsfactory.read.from_yaml_template.yaml_cell"></a>

#### yaml\_cell

```python
def yaml_cell(
        yaml_definition: _YamlDefinition,
        name: str,
        routing_strategies: RoutingStrategies | None = None
) -> "ComponentFactory"
```

The "cell" decorator equivalent for yaml files. Generates a proper cell function for yaml-defined circuits.

**Arguments**:

- `yaml_definition` - the filename to the pic yaml definition.
- `name` - the name of the pic to create.
- `routing_strategies` - a dictionary of routing strategies to use for pic generation.
  

**Returns**:

  a dynamically-generated function for the yaml file.

<a id="gdsfactory.read.from_updk"></a>

# gdsfactory.read.from\_updk

Read uPDK YAML definition and returns a gdsfactory script.

https://openepda.org/index.html

<a id="gdsfactory.read.from_updk.from_updk"></a>

#### from\_updk

```python
def from_updk(filepath: "PathType",
              filepath_out: "PathType | None" = None,
              layer_bbox: tuple[int, int] = (68, 0),
              layer_bbmetal: tuple[int, int] | None = None,
              layer_label: tuple[int, int] | None = None,
              layer_pin_label: tuple[int, int] | None = None,
              layer_pin: tuple[int, int] | None = None,
              layer_pin_optical: tuple[int, int] | None = None,
              layer_pin_electrical: tuple[int, int] | None = None,
              optical_xsections: Sequence[str] | None = None,
              electrical_xsections: Sequence[str] | None = None,
              layer_text: "LayerSpec | None" = None,
              text_size: float = 2.0,
              activate_pdk: bool = False,
              read_xsections: bool = True,
              use_port_layer: bool = False,
              prefix: str = "",
              suffix: str = "",
              add_plot_to_docstring: bool = True,
              pdk_name: str = "pdk") -> str
```

Read uPDK YAML file and returns a gdsfactory script.

**Arguments**:

- `filepath` - uPDK filepath.
- `filepath_out` - optional filepath to save script. if None only returns script and does not save it.
- `layer_bbox` - layer to draw bounding boxes.
- `layer_bbmetal` - layer to draw bounding boxes for metal.
- `layer_label` - layer to draw labels.
- `layer_pin_label` - layer to draw pin labels.
- `layer_pin` - layer to draw pins.
- `layer_pin_optical` - layer to draw optical pins.
- `layer_pin_electrical` - layer to draw electrical pins.
- `optical_xsections` - Optional list of names of xsections that will add optical ports.
- `electrical_xsections` - Optional list of names of xsections that will add electrical ports.
- `layer_text` - Optional list of layers to add text labels.
- `text_size` - text size for labels.
- `activate_pdk` - if True, activate the pdk after writing the script.
- `read_xsections` - if True, read xsections from uPDK.
- `use_port_layer` - if True, use the xsection layer for the port.
- `prefix` - optional prefix to add to the script.
- `suffix` - optional suffix to add to the script.
- `add_plot_to_docstring` - if True, add a plot to the docstring.
- `pdk_name` - name of the pdk.

<a id="gdsfactory.read.from_gdspaths"></a>

# gdsfactory.read.from\_gdspaths

<a id="gdsfactory.read.from_gdspaths.from_gdspaths"></a>

#### from\_gdspaths

```python
def from_gdspaths(cells: "Sequence[ComponentOrPath]") -> Component
```

Combine all GDS files or gf.components into a gf.component.

**Arguments**:

- `cells` - List of gdspaths or Components.

<a id="gdsfactory.read.from_gdspaths.from_gdsdir"></a>

#### from\_gdsdir

```python
def from_gdsdir(dirpath: "PathType") -> Component
```

Merges GDS cells from a directory into a single Component.

<a id="gdsfactory.boolean"></a>

# gdsfactory.boolean

<a id="gdsfactory.boolean.boolean"></a>

#### boolean

```python
def boolean(A: ComponentOrReference,
            B: ComponentOrReference,
            operation: str,
            layer: LayerSpec,
            layer1: LayerSpec | None = None,
            layer2: LayerSpec | None = None) -> Component
```

Performs boolean operations between 2 Component or Instance objects.

The `operation` parameter specifies the type of boolean operation to perform.
Supported operations include {'not', 'and', 'or', 'xor', '-', '&', '|', '^'}:
- `'|'` is equivalent to `'or'`
- `'-'` is equivalent to `'not'`
- `'&'` is equivalent to `'and'`
- `'^'` is equivalent to `'xor'`

**Arguments**:

- `A` - Component(/Reference) or list of Component(/References).
- `B` - Component(/Reference) or list of Component(/References).
- `operation` - {'not', 'and', 'or', 'xor', '-', '&', '|', '^'}.
- `layer` - Specific layer to put polygon geometry on.
- `layer1` - Specific layer to get polygons.
- `layer2` - Specific layer to get polygons.
  
- `Returns` - Component with polygon(s) of the boolean operations between
  the 2 input Components performed.
  
  .. plot::
  :include-source:
  
  import gdsfactory as gf
  
  c = gf.Component()
  c1 = c << gf.components.circle(radius=10)
  c2 = c << gf.components.circle(radius=9)
  c2.movex(5)
  
  c = gf.boolean(c1, c2, operation="xor")
  c.plot()

<a id="gdsfactory.routing.factories"></a>

# gdsfactory.routing.factories

<a id="gdsfactory.routing.route_quad"></a>

# gdsfactory.routing.route\_quad

Route for electrical based on phidl.routing.route_quad.

<a id="gdsfactory.routing.route_quad.route_quad"></a>

#### route\_quad

```python
def route_quad(component: gf.Component,
               port1: Port,
               port2: Port,
               width1: float | None = None,
               width2: float | None = None,
               layer: gf.typings.LayerSpec = "M1",
               manhattan_target_step: float | None = None) -> None
```

Routes a basic quadrilateral polygon directly between two ports.

**Arguments**:

- `component` - Component to add the route to.
- `port1` - Port to start route.
  port2 : Port objects to end route.
- `width1` - Width of quadrilateral at ports. If None, uses port widths.
- `width2` - Width of quadrilateral at ports. If None, uses port widths.
- `layer` - Layer to put the route on.
- `manhattan_target_step` - if not none, min step to manhattanize the polygon
  
  .. plot::
  :include-source:
  
  import gdsfactory as gf
  
  c = gf.Component()
  pad1 = c << gf.components.pad(size=(50, 50))
  pad2 = c << gf.components.pad(size=(10, 10))
  pad2.movex(100)
  pad2.movey(50)
  gf.routing.route_quad(
  c,
  pad1.ports["e2"],
  pad2.ports["e4"],
  width1=None,
  width2=None,
  )
  c.plot()

<a id="gdsfactory.routing.route_south"></a>

# gdsfactory.routing.route\_south

<a id="gdsfactory.routing.route_south.route_south"></a>

#### route\_south

```python
def route_south(component: Component,
                component_to_route: Component | ComponentReference,
                optical_routing_type: int = 1,
                excluded_ports: Sequence[str] | None = None,
                straight_separation: float = 4.0,
                io_gratings_lines: list[list[ComponentReference]]
                | None = None,
                gc_port_name: str = "o1",
                bend: ComponentSpec = "bend_euler",
                straight: ComponentSpec = "straight",
                select_ports: SelectPorts = select_ports_optical,
                port_names: Strs | None = None,
                cross_section: CrossSectionSpec = "strip",
                start_straight_length: float = 0.5,
                port_type: str | None = None,
                allow_width_mismatch: bool = False,
                auto_taper: bool = True) -> list[ManhattanRoute]
```

Places routes to route a component ports to the south.

**Arguments**:

- `component` - top level component to add the routes.
- `component_to_route` - component or reference to route ports to south.
- `optical_routing_type` - routing heuristic `1` or `2`             1: uses the component size info to estimate the box size.            2: only looks at the optical port positions to estimate the size.
- `excluded_ports` - list of port names to NOT route.
- `straight_separation` - in um.
- `io_gratings_lines` - list of ports to which the ports produced by this function will be connected.                 Supplying this information helps avoiding straight collisions.
- `gc_port_name` - grating coupler port name. Used only if io_gratings_lines is supplied.
- `bend` - spec.
- `straight` - spec.
- `select_ports` - function to select_ports.
- `port_names` - optional port names. Overrides select_ports.
- `cross_section` - cross_section spec.
- `start_straight_length` - in um.
- `port_type` - optical or electrical.
- `allow_width_mismatch` - allow width mismatch.
- `auto_taper` - auto taper.
  
  Works well if the component looks roughly like a rectangular box with:
  north ports on the north of the box.
  south ports on the south of the box.
  east ports on the east of the box.
  west ports on the west of the box.
  
  .. plot::
  :include-source:
  
  import gdsfactory as gf
  
  c = gf.Component()
  ref = c << gf.components.ring_double()
  r = gf.routing.route_south(c, ref)
  c.plot()

<a id="gdsfactory.routing.route_ports_to_side"></a>

# gdsfactory.routing.route\_ports\_to\_side

<a id="gdsfactory.routing.route_ports_to_side.route_ports_to_side"></a>

#### route\_ports\_to\_side

```python
def route_ports_to_side(
        component: Component,
        cross_section: CrossSectionSpec,
        ports: Ports | None = None,
        side: Literal["north", "east", "south", "west"] = "north",
        x: float | None | Literal["east", "west"] = None,
        y: float | None | Literal["north", "south"] = None,
        **kwargs: Any) -> tuple[list[ManhattanRoute], list[kf.DPort]]
```

Routes ports to a given side.

**Arguments**:

- `component` - component to route.
- `cross_section` - cross_section to use for routing.
- `ports` - ports to route to a side.
- `side` - 'north', 'south', 'east' or 'west'.
- `x` - position to route ports for east/west. None, uses most east/west value.
- `y` - position to route ports for south/north. None, uses most north/south value.
- `kwargs` - additional arguments to pass to the routing function.
  

**Arguments**:

- `radius` - in um.
- `separation` - in um.
  extend_bottom/extend_top for east/west routing.
  extend_left, extend_right for south/north routing.
  

**Returns**:

  List of routes: with routing elements.
  List of ports: of the new ports.
  
  .. plot::
  :include-source:
  
  import gdsfactory as gf
  
  c = gf.Component()
  dummy = gf.components.nxn(north=2, south=2, west=2, east=2)
  sides = ["north", "south", "east", "west"]
  d = 100
  positions = [(0, 0), (d, 0), (d, d), (0, d)]
  
  for pos, side in zip(positions, sides):
  dummy_ref = c << dummy
  dummy_ref.move(pos)
  routes, ports = gf.routing.route_ports_to_side(
  component=c, side=side, ports=dummy_ref.ports, cross_section="strip"
  )
  
  for i, p in enumerate(ports):
  c.add_port(name=f"{side[0]}{i}", port=p)
  
  c.plot()

<a id="gdsfactory.routing.route_ports_to_side.route_ports_to_x"></a>

#### route\_ports\_to\_x

```python
def route_ports_to_x(
    component: Component,
    ports: Ports,
    cross_section: CrossSectionSpec,
    x: float | Literal["east", "west"] = "east",
    separation: float = 10.0,
    radius: float = 10.0,
    extend_bottom: float = 0.0,
    extend_top: float = 0.0,
    extension_length: float = 0.0,
    y0_bottom: float | None = None,
    y0_top: float | None = None,
    backward_port_side_split_index: int = 0,
    start_straight_length: float = 0.01,
    dx_start: float | None = None,
    dy_start: float | None = None,
    side: Literal["east", "west"] = "east",
    **routing_func_args: Any
) -> tuple[list[ManhattanRoute], list[typings.Port]]
```

Returns route to x.

**Arguments**:

- `component` - component to route.
- `ports` - reasonably well behaved list of ports.
  ports facing north ports are norther than any other ports
  ports facing south ports are souther ...
  ports facing west ports are the wester ...
  ports facing east ports are the easter ...
- `cross_section` - cross_section to use for routing.
- `x` - float or string.
  if float: x coordinate to which the ports will be routed
  if string: "east" -> route to east
  if string: "west" -> route to west
- `separation` - in um.
- `radius` - in um.
- `extend_bottom` - in um.
- `extend_top` - in um.
- `extension_length` - in um.
- `y0_bottom` - in um.
- `y0_top` - in um.
- `backward_port_side_split_index` - integer represents and index in the list of backwards ports (bottom to top)
  all ports with an index strictly lower or equal are routed bottom
  all ports with an index larger or equal are routed top.
- `start_straight_length` - in um.
- `dx_start` - override minimum starting x distance.
- `dy_start` - override minimum starting y distance.
- `side` - "east" or "west".
- `routing_func_args` - additional arguments to pass to the routing function.
  

**Returns**:

- `routes` - list of routes
- `ports` - list of the new optical ports
  
  1. routes the bottom-half of the ports facing opposite side of x
  2. routes the south ports
  3. front ports
  4. north ports

<a id="gdsfactory.routing.route_ports_to_side.route_ports_to_y"></a>

#### route\_ports\_to\_y

```python
def route_ports_to_y(
    component: Component,
    ports: Ports,
    cross_section: CrossSectionSpec,
    y: float | Literal["north", "south"] = "north",
    separation: float = 10.0,
    radius: float = 10.0,
    x0_left: float | None = None,
    x0_right: float | None = None,
    extension_length: float = 0.0,
    extend_left: float = 0.0,
    extend_right: float = 0.0,
    backward_port_side_split_index: int = 0,
    start_straight_length: float = 0.01,
    dx_start: float | None = None,
    dy_start: float | None = None,
    side: Literal["north", "south"] = "north",
    **routing_func_args: Any
) -> tuple[list[ManhattanRoute], list[typings.Port]]
```

Route ports to y.

**Arguments**:

- `component` - component to route.
- `ports` - reasonably well behaved list of ports.
  ports facing north ports are norther than any other ports
  ports facing south ports are souther ...
  ports facing west ports are the wester ...
  ports facing east ports are the easter ...
- `cross_section` - cross_section to use for routing.
- `y` - float or string.
  if float: y coordinate to which the ports will be routed
  if string: "north" -> route to north
  if string: "south" -> route to south
- `separation` - in um.
- `radius` - in um.
- `x0_left` - in um.
- `x0_right` - in um.
- `extension_length` - in um.
- `extend_left` - in um.
- `extend_right` - in um.
- `backward_port_side_split_index` - integer
  this integer represents and index in the list of backwards ports
  (sorted from left to right)
  all ports with an index strictly larger are routed right
  all ports with an index lower or equal are routed left
- `start_straight_length` - in um.
- `dx_start` - override minimum starting x distance.
- `dy_start` - override minimum starting y distance.
- `side` - "north" or "south".
- `routing_func_args` - additional arguments to pass to the routing function.
  
  

**Returns**:

  - a list of Routes
  - a list of the new optical ports
  
  First route the bottom-half of the back ports (back ports are the one facing opposite side of x)
  Then route the south ports
  then the front ports
  then the north ports

<a id="gdsfactory.routing.route_bundle_sbend"></a>

# gdsfactory.routing.route\_bundle\_sbend

<a id="gdsfactory.routing.route_bundle_sbend.route_bundle_sbend"></a>

#### route\_bundle\_sbend

```python
def route_bundle_sbend(component: Component,
                       ports1: Ports,
                       ports2: Ports,
                       bend_s: ComponentSpec = "bend_s",
                       sort_ports: bool = True,
                       enforce_port_ordering: bool = True,
                       **kwargs: Any) -> list[ManhattanRoute]
```

Places sbend routes from ports1 to ports2.

**Arguments**:

- `component` - to place the sbend routes.
- `ports1` - start ports.
- `ports2` - end ports.
- `bend_s` - Sbend component.
- `sort_ports` - sort ports.
- `enforce_port_ordering` - enforces port ordering.
- `kwargs` - cross_section settings.

<a id="gdsfactory.routing.validation"></a>

# gdsfactory.routing.validation

<a id="gdsfactory.routing.validation.make_error_traces"></a>

#### make\_error\_traces

```python
def make_error_traces(component: gf.Component, ports1: list[Port],
                      ports2: list[Port], message: str) -> None
```

Creates a set of error traces showing the intended connectivity between ports1 and ports2.

The specified message will be included in the RouteWarning that is raised.

**Arguments**:

- `component` - the Component to add the error traces to.
- `ports1` - the list of starting ports.
- `ports2` - the list of ending ports.
- `message` - a message to include in the RouteWarning that is raised.
  

**Returns**:

  A list of Routes (the error traces).

<a id="gdsfactory.routing.validation.is_invalid_bundle_topology"></a>

#### is\_invalid\_bundle\_topology

```python
def is_invalid_bundle_topology(ports1: list[Port], ports2: list[Port]) -> bool
```

Returns True if the bundle is topologically unroutable without introducing crossings.

**Arguments**:

- `ports1` - the starting ports of the bundle.
- `ports2` - the ending ports of the bundle.
  

**Returns**:

  True if the bundle is unroutable. False otherwise.

<a id="gdsfactory.routing.add_pads"></a>

# gdsfactory.routing.add\_pads

<a id="gdsfactory.routing.add_pads.add_pads_bot"></a>

#### add\_pads\_bot

```python
def add_pads_bot(component: ComponentSpec = "straight_heater_metal",
                 select_ports: SelectPorts = select_ports_electrical,
                 port_names: Strs | None = None,
                 cross_section: CrossSectionSpec = "metal_routing",
                 pad_port_name: str = "e1",
                 pad: ComponentSpec = "pad_rectangular",
                 bend: ComponentSpec = "wire_corner",
                 straight_separation: float = 15.0,
                 pad_pitch: float = 100.0,
                 port_type: str = "electrical",
                 allow_width_mismatch: bool = True,
                 fanout_length: float | None = 0,
                 route_width: float | None = None,
                 bboxes: BoundingBoxes | None = None,
                 avoid_component_bbox: bool = False,
                 auto_taper: bool = True,
                 **kwargs: Any) -> Component
```

Returns new component with ports connected bottom pads.

**Arguments**:

- `component` - component spec to connect to.
- `select_ports` - function to select_ports.
- `port_names` - optional port names. Overrides select_ports.
- `cross_section` - cross_section spec.
- `get_input_labels_function` - function to get input labels. None skips labels.
- `layer_label` - optional layer for grating coupler label.
- `pad_port_name` - pad input port name.
- `pad_port_labels` - pad list of labels.
- `pad` - spec for route terminations.
- `bend` - bend spec.
- `straight_separation` - from wire edge to edge. Defaults to xs.width+xs.gap
- `pad_pitch` - in um. Defaults to pad_pitch constant from the PDK.
- `port_type` - port type.
- `allow_width_mismatch` - True
- `fanout_length` - if None, automatic calculation of fanout length.
- `route_width` - width of the route. If None, defaults to cross_section.width.
- `bboxes` - list bounding boxes to avoid for routing.
- `avoid_component_bbox` - avoid component bbox for routing.
- `auto_taper` - adds tapers to the routing.
- `kwargs` - additional arguments.
  

**Arguments**:

- `straight` - straight spec.
- `get_input_label_text_loopback_function` - function to get input label test.
- `get_input_label_text_function` - for labels.
- `max_y0_optical` - in um.
- `with_loopback` - True, adds loopback structures.
- `list_port_labels` - None, adds TM labels to port indices in this list.
- `connected_port_list_ids` - names of ports only for type 0 optical routing.
- `nb_optical_ports_lines` - number of grating coupler lines.
- `force_manhattan` - False
- `excluded_ports` - list of port names to exclude when adding gratings.
- `grating_indices` - list of grating coupler indices.
- `routing_straight` - function to route.
- `routing_method` - route_single.
- `gc_rotation` - fiber coupler rotation in degrees. Defaults to -90.
- `input_port_indexes` - to connect.
- `allow_width_mismatch` - True
  
  .. plot::
  :include-source:
  
  import gdsfactory as gf
  c = gf.c.nxn(
  xsize=600,
  ysize=200,
  north=2,
  south=3,
  wg_width=10,
  layer="M3",
  port_type="electrical",
  )
  cc = gf.routing.add_pads_bot(component=c, port_names=("e1", "e4"), fanout_length=50)
  cc.plot()

<a id="gdsfactory.routing.add_pads.add_pads_top"></a>

#### add\_pads\_top

```python
def add_pads_top(component: ComponentSpec = "straight_heater_metal",
                 select_ports: SelectPorts = select_ports_electrical,
                 port_names: Strs | None = None,
                 cross_section: CrossSectionSpec = "metal_routing",
                 pad_port_name: str = "e1",
                 pad: ComponentSpec = "pad_rectangular",
                 bend: ComponentSpec = "wire_corner",
                 straight_separation: float = 15.0,
                 pad_pitch: float = 100.0,
                 port_type: str = "electrical",
                 allow_width_mismatch: bool = True,
                 fanout_length: float | None = 0,
                 route_width: float | None = 0,
                 bboxes: BoundingBoxes | None = None,
                 avoid_component_bbox: bool = False,
                 auto_taper: bool = True,
                 **kwargs: Any) -> Component
```

Returns new component with ports connected top pads.

**Arguments**:

- `component` - component spec to connect to.
- `select_ports` - function to select_ports.
- `port_names` - optional port names. Overrides select_ports.
- `cross_section` - cross_section spec.
- `get_input_labels_function` - function to get input labels. None skips labels.
- `layer_label` - optional layer for grating coupler label.
- `pad_port_name` - pad input port name.
- `pad_port_labels` - pad list of labels.
- `pad` - spec for route terminations.
- `bend` - bend spec.
- `straight_separation` - from wire edge to edge. Defaults to xs.width+xs.gap
- `pad_pitch` - in um. Defaults to pad_pitch constant from the PDK.
- `port_type` - port type.
- `allow_width_mismatch` - True
- `fanout_length` - if None, automatic calculation of fanout length.
- `route_width` - width of the route. If None, defaults to cross_section.width.
- `bboxes` - list of bounding boxes to avoid.
- `avoid_component_bbox` - True
- `auto_taper` - adds tapers to the routing.
- `kwargs` - additional arguments.
  

**Arguments**:

- `straight` - straight spec.
- `get_input_label_text_loopback_function` - function to get input label test.
- `get_input_label_text_function` - for labels.
- `max_y0_optical` - in um.
- `with_loopback` - True, adds loopback structures.
- `list_port_labels` - None, adds TM labels to port indices in this list.
- `connected_port_list_ids` - names of ports only for type 0 optical routing.
- `nb_optical_ports_lines` - number of grating coupler lines.
- `force_manhattan` - False
- `excluded_ports` - list of port names to exclude when adding gratings.
- `grating_indices` - list of grating coupler indices.
- `routing_straight` - function to route.
- `routing_method` - route_single.
- `gc_rotation` - fiber coupler rotation in degrees. Defaults to -90.
- `input_port_indexes` - to connect.
- `allow_width_mismatch` - True
  
  .. plot::
  :include-source:
  
  import gdsfactory as gf
  c = gf.c.nxn(
  xsize=600,
  ysize=200,
  north=2,
  south=3,
  wg_width=10,
  layer="M3",
  port_type="electrical",
  )
  cc = gf.routing.add_pads_top(component=c, port_names=("e1", "e4"), fanout_length=50)
  cc.plot()

<a id="gdsfactory.routing.route_fiber_array"></a>

# gdsfactory.routing.route\_fiber\_array

<a id="gdsfactory.routing.route_fiber_array.route_fiber_array"></a>

#### route\_fiber\_array

```python
def route_fiber_array(
        component: Component,
        component_to_route: Component | ComponentReference,
        pitch: float = 127.0,
        grating_coupler: ComponentSpecOrList = "grating_coupler_te",
        bend: ComponentSpec = "bend_euler",
        straight: ComponentSpec = "straight",
        fanout_length: float | None = None,
        max_y0_optical: None = None,
        with_loopback: bool = True,
        with_loopback_inside: bool = True,
        straight_separation: float = 6.0,
        straight_to_grating_spacing: float = 5.0,
        nb_optical_ports_lines: int = 1,
        force_manhattan: bool = False,
        excluded_ports: list[str] | None = None,
        grating_indices: list[int] | None = None,
        gc_port_name: str = "o1",
        gc_port_name_fiber: str = "o2",
        gc_rotation: int = -90,
        component_name: str | None = None,
        x_grating_offset: float = 0,
        port_names: Strs | None = None,
        select_ports: PortsFactory = select_ports_optical,
        radius: float | None = None,
        radius_loopback: float | None = None,
        cross_section: CrossSectionSpec = "strip",
        allow_width_mismatch: bool = False,
        port_type: str = "optical",
        route_width: float | None = None,
        start_straight_length: float = 0,
        end_straight_length: float = 0,
        auto_taper: bool = True,
        waypoints: Coordinates | None = None,
        steps: Sequence[Mapping[str, int | float]] | None = None,
        bboxes: BoundingBoxes | None = None,
        avoid_component_bbox: bool = True,
        **kwargs: Any) -> Component
```

Returns new component with fiber array.

**Arguments**:

- `component` - top level component.
- `component_to_route` - component to route.
- `pitch` - pitch between the array.
- `grating_coupler` - grating coupler instance, function or list of functions.
- `bend` - for bends.
- `straight` - straight.
- `fanout_length` - target distance between gratings and the southmost component port.
  If None, automatically calculated.
- `max_y0_optical` - Maximum y coordinate at which the intermediate optical ports can be set.
  Usually fine to leave at None.
- `with_loopback` - If True, add compact loopback alignment ports.
- `with_loopback_inside` - If True, the loopback is inside the component.
- `straight_separation` - min separation between routing straights.
- `straight_to_grating_spacing` - from align ports.
- `nb_optical_ports_lines` - number of lines with I/O grating couplers. One line by default.
- `WARNING` - Only works properly if:
  - nb_optical_ports_lines divides the total number of ports.
  - the components have an equal number of inputs and outputs.
- `force_manhattan` - sometimes port linker defaults to an S-bend due to lack of space to do manhattan.
  Force manhattan offsets all the ports to replace the s-bend by a straight link.
  This fails if multiple ports have the same issue.
- `excluded_ports` - ports excluded from routing.
- `grating_indices` - allows to fine skip some grating slots.
  e.g [0,1,4,5] will put two gratings separated by the pitch.
  Then there will be two empty grating slots, and after that an additional two gratings.
- `gc_port_name` - grating_coupler port name, where to route straights.
- `gc_port_name_fiber` - grating_coupler port name, where to route fibers.
- `gc_rotation` - grating_coupler rotation (deg).
- `layer_label` - for measurement labels.
- `component_name` - name of component.
- `x_grating_offset` - x offset.
- `port_names` - port names to route_to_fiber_array.
- `select_ports` - function to select ports for which to add grating couplers.
- `radius` - optional radius of the bend. Defaults to the cross_section.
- `radius_loopback` - optional radius of the loopback bend. Defaults to the cross_section.
- `cross_section` - cross_section.
- `allow_width_mismatch` - allow width mismatch.
- `port_type` - port type.
- `route_width` - width of the route. If None, defaults to cross_section.width.
- `start_straight_length` - length of the start straight.
- `end_straight_length` - length of the end straight.
- `auto_taper` - taper length for the IO.
- `waypoints` - waypoints for the route.
- `steps` - steps for the route.
- `bboxes` - list bounding boxes to avoid for routing.
- `avoid_component_bbox` - avoid component bbox for routing.
- `kwargs` - route_bundle settings.

<a id="gdsfactory.routing.route_sharp"></a>

# gdsfactory.routing.route\_sharp

based on phidl.routing.

<a id="gdsfactory.routing.route_sharp.path_straight"></a>

#### path\_straight

```python
def path_straight(port1: typings.Port, port2: typings.Port) -> Path
```

Return waypoint path between port1 and port2 in a straight line.

Useful when ports point directly at each other.

**Arguments**:

- `port1` - start port.
- `port2` - end port.

<a id="gdsfactory.routing.route_sharp.path_L"></a>

#### path\_L

```python
def path_L(port1: typings.Port, port2: typings.Port) -> Path
```

Return waypoint path between port1 and port2 in an L shape.

Useful when orthogonal ports can be directly connected with one turn.

**Arguments**:

- `port1` - start port.
- `port2` - end port.

<a id="gdsfactory.routing.route_sharp.path_U"></a>

#### path\_U

```python
def path_U(port1: typings.Port,
           port2: typings.Port,
           length1: float = 200) -> Path
```

Return waypoint path between port1 and port2 in a U shape.

Useful when ports face the same direction or toward each other.

**Arguments**:

- `port1` - start port.
- `port2` - end port.
- `length1` - Length of segment exiting port1. Should be larger than bend radius.

<a id="gdsfactory.routing.route_sharp.path_J"></a>

#### path\_J

```python
def path_J(port1: typings.Port,
           port2: typings.Port,
           length1: float = 200,
           length2: float = 200) -> Path
```

Return waypoint path between port1 and port2 in a J shape.

Useful when  orthogonal ports cannot be connected directly with an L shape.

**Arguments**:

- `port1` - start port.
- `port2` - end port.
- `length1` - Length of segment exiting port1. Should be larger than bend radius.
- `length2` - Length of segment exiting port2. Should be larger than bend radius.

<a id="gdsfactory.routing.route_sharp.path_C"></a>

#### path\_C

```python
def path_C(port1: typings.Port,
           port2: typings.Port,
           length1: float = 100,
           left1: float = 100,
           length2: float = 100) -> Path
```

Return waypoint path between port1 and port2 in a C shape. Useful when ports are parallel and face away from each other.

**Arguments**:

- `port1` - start port.
- `port2` - end port.
- `length1` - Length of route segment coming out of port1. Should be larger than bend radius.
- `left1` - Length of route segment that turns left (or right if negative) from port1. Should be larger than twice the bend radius.
- `length2` - Length of route segment coming out of port2. Should be larger than bend radius.

<a id="gdsfactory.routing.route_sharp.path_manhattan"></a>

#### path\_manhattan

```python
def path_manhattan(port1: typings.Port, port2: typings.Port,
                   radius: float) -> Path
```

Return waypoint path between port1 and port2 using manhattan routing.

Routing uses straight, L, U, J, or C waypoint path as needed.
Ports must face orthogonal or parallel directions.

**Arguments**:

- `port1` - start port.
- `port2` - end port.
- `radius` - Bend radius for 90 degree bend.

<a id="gdsfactory.routing.route_sharp.path_Z"></a>

#### path\_Z

```python
def path_Z(port1: typings.Port,
           port2: typings.Port,
           length1: float = 100,
           length2: float = 100) -> Path
```

Return waypoint path between port1 and port2 in a Z shape.

Ports can have any relative orientation.

**Arguments**:

- `port1` - start port.
- `port2` - end port.
- `length1` - Length of route segment coming out of port1.
- `length2` - Length of route segment coming out of port2.

<a id="gdsfactory.routing.route_sharp.path_V"></a>

#### path\_V

```python
def path_V(port1: typings.Port, port2: typings.Port) -> Path
```

Return waypoint path between port1 and port2 in a V shape.

Useful when ports point to a single connecting point.

**Arguments**:

- `port1` - Start port.
- `port2` - End port.

<a id="gdsfactory.routing.route_sharp.route_sharp"></a>

#### route\_sharp

```python
def route_sharp(component: Component,
                port1: typings.Port,
                port2: typings.Port,
                width: float | None = None,
                path_type: str = "manhattan",
                manual_path: Path | None = None,
                layer: LayerSpec | None = None,
                cross_section: CrossSectionSpec | None = None,
                port_names: tuple[str, str] = ("o1", "o2"),
                **kwargs: Any) -> None
```

Returns Component route between ports.

**Arguments**:

- `component` - Component to add the route to.
- `port1` - start port.
- `port2` - end port.
- `width` - None, int, float, array-like[2], or CrossSection.                 If None, the route linearly tapers between the widths the ports                 If set to a single number (e.g. `width=1.7`): makes a fixed-width route                 If set to a 2-element array (e.g. `width=[1.8,2.5]`): makes a route                 whose width varies linearly from width[0] to width[1]                 If set to a CrossSection: uses the CrossSection parameters for the route.
  path_type : {'manhattan', 'L', 'U', 'J', 'C', 'V', 'Z', 'straight', 'manual'}.
- `manual_path` - array-like[N][2] or Path Waypoint for  manual route.
- `layer` - Layer to put route on.
- `cross_section` - CrossSection to use for the route.
- `port_names` - Tuple of port names for the start and end of the route.
- `kwargs` - Keyword arguments passed to the waypoint path function.
  
  Method of waypoint path creation. Should be one of:
  
  - manhattan: automatic manhattan routing (see path_manhattan() ).
  - L: L-shaped path for orthogonal ports that can be directly connected.
  - U: U-shaped path for parallel or facing ports.
  - J: J-shaped path for orthogonal ports that cannot be directly connected.
  - C: C-shaped path for ports that face away from each other.
  - Z: Z-shaped path with three segments for ports at any angles.
  - V: V-shaped path with two segments for ports at any angles.
  - straight: straight path for ports that face each other.
  - manual: use an explicit waypoint path provided in manual_path.
  
  .. plot::
  :include-source:
  
  import gdsfactory as gf
  
  c = gf.Component()
  c1 = c << gf.components.pad(port_orientation=None)
  c2 = c << gf.components.pad(port_orientation=None)
  
  c2.movex(400)
  c2.movey(-200)
  
  gf.routing.route_sharp(c, c1.ports["e4"], c2.ports["e1"], path_type="L")
  c.plot()

<a id="gdsfactory.routing.add_electrical_pads_top"></a>

# gdsfactory.routing.add\_electrical\_pads\_top

<a id="gdsfactory.routing.add_electrical_pads_top.add_electrical_pads_top"></a>

#### add\_electrical\_pads\_top

```python
def add_electrical_pads_top(
        component: ComponentSpec,
        direction: Literal["top", "right"] = "top",
        spacing: Float2 = (0.0, 100.0),
        pad_array: ComponentSpec = "pad_array",
        select_ports: SelectPorts = select_ports_electrical,
        port_names: Strs | None = None,
        layer: LayerSpec = "MTOP",
        **kwargs: Any) -> Component
```

Returns new component with electrical ports connected to top pad array.

**Arguments**:

- `component` - to route.
- `direction` - sets direction of the array (top or right).
- `spacing` - component to pad spacing.
- `pad_array` - function for pad_array.
- `select_ports` - function to select electrical ports.
- `port_names` - optional port names. Overrides select_ports.
- `layer` - for the routes.
- `kwargs` - additional arguments.
  

**Arguments**:

- `ports` - Dict[str, Port] a port dict {port name: port}.
- `prefix` - select ports with port name prefix.
- `suffix` - select ports with port name suffix.
- `orientation` - select ports with orientation in degrees.
- `width` - select ports with port width.
- `layers_excluded` - List of layers to exclude.
- `port_type` - select ports with port type (optical, electrical, vertical_te).
- `clockwise` - if True, sort ports clockwise, False: counter-clockwise.
  
  
  .. plot::
  :include-source:
  
  import gdsfactory as gf
  
  c = gf.components.wire_straight(length=200.)
  cc = gf.routing.add_electrical_pads_top(component=c, spacing=(-150, 30))
  cc.plot()

<a id="gdsfactory.routing.fanout2x2"></a>

# gdsfactory.routing.fanout2x2

<a id="gdsfactory.routing.fanout2x2.fanout2x2"></a>

#### fanout2x2

```python
def fanout2x2(component: ComponentSpec = "straight",
              port_spacing: float = 20.0,
              bend_length: float | None = None,
              npoints: int = 101,
              select_ports: PortsFactory = select_ports_optical,
              cross_section: CrossSectionSpec = "strip",
              **kwargs: Any) -> Component
```

Returns component with Sbend fanout routes.

**Arguments**:

- `component` - to fanout.
- `port_spacing` - for the returned component.
- `bend_length` - length of the bend (defaults to port_spacing).
- `npoints` - for sbend.
- `select_ports` - function to select  optical_ports ports.
- `cross_section` - cross_section spec.
- `kwargs` - cross_section settings.
  
  .. plot::
  :include-source:
  
  import gdsfactory as gf
  c = gf.components.nxn(west=2, east=2)
  
  cc = gf.routing.fanout2x2(component=c, port_spacing=20)
  cc.plot()

<a id="gdsfactory.routing.add_electrical_pads_top_dc"></a>

# gdsfactory.routing.add\_electrical\_pads\_top\_dc

<a id="gdsfactory.routing.add_electrical_pads_top_dc.add_electrical_pads_top_dc"></a>

#### add\_electrical\_pads\_top\_dc

```python
def add_electrical_pads_top_dc(
        component: ComponentSpec,
        spacing: Float2 = (0.0, 100.0),
        pad_array: ComponentSpec = "pad_array270",
        select_ports: SelectPorts = select_ports_electrical,
        port_names: Strs | None = None,
        cross_section: CrossSectionSpec = "metal_routing",
        **kwargs: Any) -> Component
```

Returns new component with electrical ports connected to top pad array.

**Arguments**:

- `component` - component spec to connect to.
- `spacing` - component to pad spacing.
- `pad_array` - component factor for pad_array
- `select_ports` - function to select_ports.
- `route_bundle_function` - function to route bundle of ports.
- `port_names` - optional port names. Overrides select_ports.
- `cross_section` - cross_section for the route.
- `kwargs` - route settings.
  
  .. plot::
  :include-source:
  
  import gdsfactory as gf
  c = gf.components.wire_straight(length=200.)
  c = gf.routing.add_electrical_pads_top_dc(c, width=10)
  c.plot()

<a id="gdsfactory.routing"></a>

# gdsfactory.routing

Functions to create routes between components.

<a id="gdsfactory.routing.route_astar"></a>

# gdsfactory.routing.route\_astar

<a id="gdsfactory.routing.route_astar.Node"></a>

## Node Objects

```python
class Node()
```

<a id="gdsfactory.routing.route_astar.Node.__init__"></a>

#### \_\_init\_\_

```python
def __init__(parent: Node | None = None,
             position: tuple[int, int] = (0, 0)) -> None
```

Initializes a node. A node is a point on the grid.

<a id="gdsfactory.routing.route_astar.simplify_path"></a>

#### simplify\_path

```python
def simplify_path(waypoints: Coordinates,
                  tolerance: float) -> list[Coordinate]
```

Simplifies a list of waypoints using the Douglas-Peucker algorithm.

**Arguments**:

- `waypoints` - List of waypoints as coordinate pairs (x, y).
- `tolerance` - Simplification tolerance.
  

**Returns**:

  List of simplified waypoints.

<a id="gdsfactory.routing.route_astar.route_astar"></a>

#### route\_astar

```python
def route_astar(component: Component,
                port1: Port,
                port2: Port,
                resolution: float = 1,
                avoid_layers: Sequence[LayerSpec] | None = None,
                distance: float = 8,
                cross_section: CrossSectionSpec = "strip",
                bend: ComponentSpec = "wire_corner",
                **kwargs: Any) -> Route
```

Bidirectional routing function using NetworkX. Finds a route between two ports avoiding obstacles.

**Arguments**:

- `component` - Component the route and ports belong to.
- `port1` - Input port.
- `port2` - Output port.
- `resolution` - Discretization resolution in um.
- `avoid_layers` - List of layers to avoid.
- `distance` - Distance from obstacles in um.
- `cross_section` - Cross-section specification.
- `bend` - Component to use for bends. Use wire_corner for Manhattan routing or bend_euler for Euler routing.
- `kwargs` - cross-section settings.

<a id="gdsfactory.routing.add_fiber_array"></a>

# gdsfactory.routing.add\_fiber\_array

<a id="gdsfactory.routing.add_fiber_array.add_fiber_array"></a>

#### add\_fiber\_array

```python
def add_fiber_array(
        component: ComponentSpec = "straight",
        grating_coupler: ComponentSpecOrList = "grating_coupler_te",
        gc_port_name: str = "o1",
        select_ports: PortsFactory = select_ports_optical,
        cross_section: CrossSectionSpec = "strip",
        start_straight_length: float = 0,
        end_straight_length: float = 0,
        **kwargs: Any) -> Component
```

Returns component with south routes and grating_couplers.

You can also use pads or other terminations instead of grating couplers.

**Arguments**:

- `component` - component spec to connect to grating couplers.
- `grating_coupler` - spec for route terminations.
- `gc_port_name` - grating coupler input port name.
- `select_ports` - function to select ports.
- `cross_section` - cross_section function.
- `kwargs` - additional arguments.
  

**Arguments**:

- `bend` - bend spec.
- `straight` - straight spec.
- `fanout_length` - if None, automatic calculation of fanout length.
- `max_y0_optical` - in um.
- `with_loopback` - True, adds loopback structures.
- `with_loopback_inside` - True, adds loopback structures inside the component.
- `straight_separation` - from edge to edge.
- `list_port_labels` - None, adds TM labels to port indices in this list.
- `nb_optical_ports_lines` - number of grating coupler lines.
- `force_manhattan` - False
- `excluded_ports` - list of port names to exclude when adding gratings.
- `grating_indices` - list of grating coupler indices.
- `routing_straight` - function to route.
- `routing_method` - route_single.
- `gc_rotation` - fiber coupler rotation in degrees. Defaults to -90.
- `input_port_indexes` - to connect.
- `pitch` - in um.
- `radius` - optional radius of the bend. Defaults to the cross_section.
- `radius_loopback` - optional radius of the loopback bend. Defaults to the cross_section.
- `start_straight_length` - length of the start straight.
- `end_straight_length` - length of the end straight.
  
  .. plot::
  :include-source:
  
  import gdsfactory as gf
  
  c = gf.components.crossing()
  cc = gf.routing.add_fiber_array(
  component=c,
  grating_coupler=gf.components.grating_coupler_elliptical_te,
  with_loopback=False
  )
  cc.plot()

<a id="gdsfactory.routing.auto_taper"></a>

# gdsfactory.routing.auto\_taper

This module contains functions to automatically add tapers to a component's ports, and to create tapers between different cross sections.

<a id="gdsfactory.routing.auto_taper.add_auto_tapers"></a>

#### add\_auto\_tapers

```python
def add_auto_tapers(component: Component, ports: Ports,
                    cross_section: CrossSectionSpec) -> list[Port]
```

Adds tapers to the ports of a component (to be used for routing) and returns the new lists of ports.

**Arguments**:

- `component` - the component to add tapers to
- `ports` - the list of ports
- `cross_section` - the cross section to route to
  

**Returns**:

  The new list of ports, on the opposite end of the tapers

<a id="gdsfactory.routing.auto_taper.auto_taper_to_cross_section"></a>

#### auto\_taper\_to\_cross\_section

```python
def auto_taper_to_cross_section(
        component: gf.Component,
        port: Port,
        cross_section: CrossSectionSpec,
        layer_transitions: LayerTransitions | None = None) -> Port
```

Creates a taper from a port to a given cross section and places it in the component. The opposite port of the taper will be returned.

**Arguments**:

- `component` - the component to place into
- `port` - a port to connect to, usually from a ComponentReference
- `cross_section` - a cross section to transition to
- `layer_transitions` - the layer transitions dictionary to use (use the pdk default if None)
  

**Returns**:

  The port at the opposite (unconnected end) of the taper.

<a id="gdsfactory.routing.add_electrical_pads_shortest"></a>

# gdsfactory.routing.add\_electrical\_pads\_shortest

<a id="gdsfactory.routing.add_electrical_pads_shortest.add_electrical_pads_shortest"></a>

#### add\_electrical\_pads\_shortest

```python
def add_electrical_pads_shortest(
        component: ComponentSpec = "wire_straight",
        pad: ComponentSpec = "pad",
        pad_port_spacing: float = 50.0,
        pad_size: Size | None = None,
        select_ports: PortsFactory = select_ports_electrical,
        port_names: Strs | None = None,
        port_orientation: AngleInDegrees = 90,
        layer: LayerSpec = "M3") -> Component
```

Returns new Component with a pad by each electrical port.

**Arguments**:

- `component` - to route.
- `pad` - pad element or function.
- `pad_port_spacing` - spacing between pad and port.
- `pad_size` - pad size.
- `select_ports` - function to select ports.
- `port_names` - optional port names. Overrides select_ports.
- `port_orientation` - in degrees.
- `layer` - for the routing.
  
  .. plot::
  :include-source:
  
  import gdsfactory as gf
  c = gf.components.cross(length=100, layer=(49, 0), port_type="electrical")
  c = gf.routing.add_electrical_pads_shortest(c, pad_port_spacing=200)
  c.plot()

<a id="gdsfactory.routing.route_single_sbend"></a>

# gdsfactory.routing.route\_single\_sbend

<a id="gdsfactory.routing.route_single_sbend.route_single_sbend"></a>

#### route\_single\_sbend

```python
def route_single_sbend(
        component: Component,
        port1: Port,
        port2: Port,
        bend_s: ComponentSpec = "bend_s",
        cross_section: CrossSectionSpec = "strip",
        allow_layer_mismatch: bool = False,
        allow_width_mismatch: bool = False) -> ComponentReference
```

Returns an Sbend to connect two ports.

**Arguments**:

- `component` - to add the route to.
- `port1` - start port.
- `port2` - end port.
- `bend_s` - Sbend component.
- `cross_section` - cross_section.
- `allow_layer_mismatch` - allow layer mismatch.
- `allow_width_mismatch` - allow width mismatch.
  
  .. plot::
  :include-source:
  
  import gdsfactory as gf
  
  c = gf.Component()
  mmi1 = c << gf.components.mmi1x2()
  mmi2 = c << gf.components.mmi1x2()
  mmi2.movex(50)
  mmi2.movey(5)
  route = gf.routing.route_single_sbend(c, mmi1.ports['o2'], mmi2.ports['o1'])
  c.plot()

<a id="gdsfactory.routing.add_fiber_single"></a>

# gdsfactory.routing.add\_fiber\_single

<a id="gdsfactory.routing.add_fiber_single.add_fiber_single"></a>

#### add\_fiber\_single

```python
def add_fiber_single(
        component: ComponentSpec = "straight",
        grating_coupler: ComponentSpecOrList = "grating_coupler_te",
        gc_port_name: str = "o1",
        gc_port_name_fiber: str = "o2",
        select_ports: SelectPorts = select_ports_optical,
        cross_section: CrossSectionSpec = "strip",
        input_port_names: Sequence[str] | None = None,
        pitch: float = 70,
        with_loopback: bool = True,
        loopback_spacing: float = 100.0,
        straight: ComponentSpec = "straight",
        **kwargs: Any) -> Component
```

Returns component with south routes and grating_couplers.

You can also use pads or other terminations instead of grating couplers.

**Arguments**:

- `component` - component spec to connect to grating couplers.
- `grating_coupler` - spec for route terminations.
- `gc_port_name` - grating coupler input port name.
- `gc_port_name_fiber` - grating coupler output port name.
- `select_ports` - function to select ports.
- `cross_section` - cross_section function.
- `input_port_names` - list of input port names to connect to grating couplers.
- `pitch` - spacing between fibers.
- `with_loopback` - adds loopback structures.
- `loopback_spacing` - spacing between loopback and test structure.
- `straight` - straight spec.
- `kwargs` - additional arguments.
  

**Arguments**:

- `bend` - bend spec.
- `straight` - straight spec.
- `fanout_length` - if None, automatic calculation of fanout length.
- `max_y0_optical` - in um.
- `with_loopback` - True, adds loopback structures.
- `straight_separation` - from edge to edge.
- `list_port_labels` - None, adds TM labels to port indices in this list.
- `connected_port_list_ids` - names of ports only for type 0 optical routing.
- `nb_optical_ports_lines` - number of grating coupler lines.
- `force_manhattan` - False
- `excluded_ports` - list of port names to exclude when adding gratings.
- `grating_indices` - list of grating coupler indices.
- `routing_straight` - function to route.
- `routing_method` - route_single.
- `gc_rotation` - fiber coupler rotation in degrees. Defaults to -90.
- `input_port_indexes` - to connect.
  
  .. plot::
  :include-source:
  
  import gdsfactory as gf
  
  c = gf.components.crossing()
  cc = gf.routing.add_fiber_array(
  component=c,
  grating_coupler=gf.components.grating_coupler_elliptical_te,
  with_loopback=False
  )
  cc.plot()

<a id="gdsfactory.routing.utils"></a>

# gdsfactory.routing.utils

<a id="gdsfactory.routing.utils.direction_ports_from_list_ports"></a>

#### direction\_ports\_from\_list\_ports

```python
def direction_ports_from_list_ports(
        optical_ports: Sequence[Port]) -> dict[str, list[Port]]
```

Returns a dict of WENS ports.

<a id="gdsfactory.routing.utils.check_ports_have_equal_spacing"></a>

#### check\_ports\_have\_equal\_spacing

```python
def check_ports_have_equal_spacing(list_ports: Sequence[Port]) -> float
```

Returns port separation.

Raises error if not constant.

<a id="gdsfactory.routing.utils.get_list_ports_angle"></a>

#### get\_list\_ports\_angle

```python
def get_list_ports_angle(list_ports: Sequence[Port]) -> float | None
```

Returns the orientation/angle (in degrees) of a list of ports.

<a id="gdsfactory.routing.route_bundle_all_angle"></a>

# gdsfactory.routing.route\_bundle\_all\_angle

<a id="gdsfactory.routing.route_bundle_all_angle.route_bundle_all_angle"></a>

#### route\_bundle\_all\_angle

```python
def route_bundle_all_angle(
    component: ComponentSpec,
    ports1: list[Port],
    ports2: list[Port],
    backbone: Coordinates | None = None,
    separation: list[float] | float = 3.0,
    straight: ComponentAllAngleFactory = straight_all_angle,
    bend: ComponentAllAngleFactory = partial(bend_euler_all_angle, radius=5),
    bend_ports: tuple[str, str] = ("o1", "o2"),
    straight_ports: tuple[str, str] = ("o1", "o2"),
    cross_section: CrossSectionSpec | None = None
) -> list[OpticalAllAngleRoute]
```

Route a bundle of ports to another bundle of ports with all angles.

**Arguments**:

- `component` - to add the routing.
- `ports1` - list of start ports to connect.
- `ports2` - list of end ports to connect.
- `backbone` - list of points to connect the ports.
- `separation` - list of spacings.
- `straight` - function to create straights.
- `bend` - function to create bends.
- `bend_ports` - tuple of ports to connect the bends.
- `straight_ports` - tuple of ports to connect the straights.
- `cross_section` - cross_section to use. Overrides the  cross_section.

<a id="gdsfactory.routing.route_bundle"></a>

# gdsfactory.routing.route\_bundle

Routes bundles of ports (river routing).

get bundle is the generic river routing function
route_bundle calls different function depending on the port orientation.

 - route_bundle_same_axis: ports facing each other with arbitrary pitch on each side
 - route_bundle_corner: 90Deg / 270Deg between ports with arbitrary pitch
 - route_bundle_udirect: ports with direct U-turns
 - route_bundle_uindirect: ports with indirect U-turns

<a id="gdsfactory.routing.route_bundle.get_min_spacing"></a>

#### get\_min\_spacing

```python
def get_min_spacing(ports1: Ports,
                    ports2: Ports,
                    separation: float = 5.0,
                    radius: float = 5.0,
                    sort_ports: bool = True) -> float
```

Returns the minimum amount of spacing in um required to create a fanout.

**Arguments**:

- `ports1` - first list of ports.
- `ports2` - second list of ports.
- `separation` - minimum separation between two straights in um.
- `radius` - bend radius in um.
- `sort_ports` - sort the ports according to the axis.

<a id="gdsfactory.routing.route_bundle.route_bundle"></a>

#### route\_bundle

```python
def route_bundle(
    component: gf.Component,
    ports1: Ports,
    ports2: Ports,
    cross_section: CrossSectionSpec | None = None,
    layer: LayerSpec | None = None,
    separation: float = 3.0,
    bend: ComponentSpec = "bend_euler",
    sort_ports: bool = False,
    start_straight_length: float = 0,
    end_straight_length: float = 0,
    min_straight_taper: float = 100,
    taper: ComponentSpec | None = None,
    port_type: str | None = None,
    collision_check_layers: LayerSpecs | None = None,
    on_collision: Literal["error", "show_error"] | None = None,
    bboxes: Sequence[kf.kdb.DBox] | None = None,
    allow_width_mismatch: bool = False,
    radius: float | None = None,
    route_width: float | None = None,
    straight: ComponentSpec = "straight",
    auto_taper: bool = True,
    waypoints: Coordinates | None = None,
    steps: Sequence[Mapping[str, int | float]] | None = None,
    start_angles: float | list[float] | None = None,
    end_angles: float | list[float] | None = None,
    router: Literal["optical", "electrical"] | None = None
) -> list[ManhattanRoute]
```

Places a bundle of routes to connect two groups of ports.

Routes connect a bundle of ports with a river router.
Chooses the correct routing function depending on port angles.

**Arguments**:

- `component` - component to add the routes to.
- `ports1` - list of starting ports.
- `ports2` - list of end ports.
- `cross_section` - CrossSection or function that returns a cross_section.
- `layer` - layer to use for the route.
- `separation` - bundle separation (center to center). Defaults to cross_section.width + cross_section.gap
- `bend` - function for the bend. Defaults to euler.
- `sort_ports` - sort port coordinates.
- `start_straight_length` - straight length at the beginning of the route. If None, uses default value for the routing CrossSection.
- `end_straight_length` - end length at the beginning of the route. If None, uses default value for the routing CrossSection.
- `min_straight_taper` - minimum length for tapering the straight sections.
- `taper` - function for the taper. Defaults to None.
- `port_type` - type of port to place. Defaults to optical.
- `collision_check_layers` - list of layers to check for collisions.
- `on_collision` - action to take on collision. Defaults to None (ignore).
- `bboxes` - list of bounding boxes to avoid collisions.
- `allow_width_mismatch` - allow different port widths.
- `radius` - bend radius. If None, defaults to cross_section.radius.
- `route_width` - width of the route. If None, defaults to cross_section.width.
- `straight` - function for the straight. Defaults to straight.
- `auto_taper` - if True, auto-tapers ports to the cross-section of the route.
- `waypoints` - list of waypoints to add to the route.
- `steps` - list of steps to add to the route.
- `start_angles` - list of start angles for the routes. Only used for electrical ports.
- `end_angles` - list of end angles for the routes. Only used for electrical ports.
- `router` - Set the type of router to use, either the optical one or the electrical one.
  If None, the router is optical unless the port_type is "electrical".
  
  .. plot::
  :include-source:
  
  import gdsfactory as gf
  
  dy = 200.0
  xs1 = [-500, -300, -100, -90, -80, -55, -35, 200, 210, 240, 500, 650]
  
  pitch = 10.0
  N = len(xs1)
  xs2 = [-20 + i * pitch for i in range(N // 2)]
  xs2 += [400 + i * pitch for i in range(N // 2)]
  
  a1 = 90
  a2 = a1 + 180
  
  ports1 = [gf.Port(name=f"top_{i}", center=(xs1[i], +0), width=0.5, orientation=a1, layer=(1,0)) for i in range(N)]
  ports2 = [gf.Port(name=f"bot_{i}", center=(xs2[i], dy), width=0.5, orientation=a2, layer=(1,0)) for i in range(N)]
  
  c = gf.Component()
  gf.routing.route_bundle(component=c, ports1=ports1, ports2=ports2, cross_section='strip', separation=5)
  c.plot()

<a id="gdsfactory.routing.route_dubins"></a>

# gdsfactory.routing.route\_dubins

A minimal implementation of Dubins paths for waveguide routing adapted for gdsFactory by Quentin Wach.

https://quentinwach.com/blog/2024/02/15/dubins-paths-for-waveguide-routing.html

<a id="gdsfactory.routing.route_dubins.route_dubins"></a>

#### route\_dubins

```python
def route_dubins(component: Component, port1: Port, port2: Port,
                 cross_section: CrossSectionSpec) -> OpticalAllAngleRoute
```

Route between ports using Dubins paths with radius from cross-section.

**Arguments**:

- `component` - component to add the route to.
- `port1` - input port.
- `port2` - output port.
- `cross_section` - cross-section.

<a id="gdsfactory.routing.route_dubins.general_planner"></a>

#### general\_planner

```python
def general_planner(
        planner: str, alpha: float, beta: float,
        d: float) -> tuple[list[float | Literal[0]], list[str], float] | None
```

Finds the optimal path between two points using various planning methods.

<a id="gdsfactory.routing.route_dubins.dubins_path_length"></a>

#### dubins\_path\_length

```python
def dubins_path_length(start: tuple[float, float,
                                    float], end: tuple[float, float, float],
                       xs: CrossSectionSpec) -> float
```

Calculate the length of a Dubins path.

<a id="gdsfactory.routing.route_dubins.dubins_path"></a>

#### dubins\_path

```python
def dubins_path(
        start: tuple[float, float, float], end: tuple[float, float, float],
        cross_section: CrossSectionSpec) -> list[tuple[str, float, float]]
```

Finds the Dubins path between two points.

<a id="gdsfactory.routing.route_dubins.mod_to_pi"></a>

#### mod\_to\_pi

```python
def mod_to_pi(angle: float) -> float
```

Normalizes an angle to the range [0, 2*pi).

<a id="gdsfactory.routing.route_dubins.pi_to_pi"></a>

#### pi\_to\_pi

```python
def pi_to_pi(angle: float) -> float
```

Constrains an angle to the range [-pi, pi].

<a id="gdsfactory.routing.route_dubins.linear"></a>

#### linear

```python
def linear(start: tuple[float, float, float], end: tuple[float, float, float],
           steps: int) -> tuple[list[float], list[float]]
```

Creates a list of points on lines between a given start point and end point.

start/end: [x, y, angle], the start/end point with given jaw angle.

<a id="gdsfactory.routing.route_dubins.arrow_orientation"></a>

#### arrow\_orientation

```python
def arrow_orientation(angle: float) -> tuple[float, float]
```

Returns x, y setoffs for a given angle to orient the arrows marking the yaw of the start and end points.

<a id="gdsfactory.routing.route_dubins.place_dubins_path"></a>

#### place\_dubins\_path

```python
def place_dubins_path(
        component: Component, xs: CrossSectionSpec, port1: Port,
        solution: list[tuple[str, float, float]]) -> list[kf.VInstance]
```

Creates GDS component with Dubins path.

**Arguments**:

- `component` - component to add the route to.
- `xs` - cross-section.
- `port1` - input port.
- `solution` - Dubins path solution.

<a id="gdsfactory.routing.sort_ports"></a>

# gdsfactory.routing.sort\_ports

<a id="gdsfactory.routing.sort_ports.sort_ports"></a>

#### sort\_ports

```python
def sort_ports(ports1: Ports, ports2: Ports,
               enforce_port_ordering: bool) -> tuple[list[Port], list[Port]]
```

Returns two lists of sorted ports.

**Arguments**:

- `ports1` - the starting ports
- `ports2` - the ending ports
- `enforce_port_ordering` - if True, only ports2 will be sorted in accordance with ports1.
  If False, the two lists will be sorted independently.

<a id="gdsfactory.routing.route_single"></a>

# gdsfactory.routing.route\_single

`route_single` places a Manhattan route between two ports.

`route_single` only works for an individual routes. For routing groups of ports you need to use `route_bundle` instead

To make a route, you need to supply:

 - input port
 - output port
 - bend
 - straight
 - taper to taper to wider straights and reduce straight loss (Optional)

To generate a route:

 1. Generate the backbone of the route.
 This is a list of manhattan coordinates that the route would pass through
 if it used only sharp bends (right angles)

 2. Replace the corners by bend references
 (with rotation and position computed from the manhattan backbone)

 3. Add tapers if needed and if space permits

 4. generate straight portions in between tapers or bends

<a id="gdsfactory.routing.route_single.route_single"></a>

#### route\_single

```python
def route_single(component: Component,
                 port1: Port,
                 port2: Port,
                 cross_section: CrossSectionSpec | None = None,
                 layer: LayerSpec | None = None,
                 bend: ComponentSpec = "bend_euler",
                 straight: ComponentSpec = "straight",
                 start_straight_length: float = 0.0,
                 end_straight_length: float = 0.0,
                 waypoints: WayPoints | None = None,
                 steps: Sequence[Mapping[Literal["x", "y", "dx", "dy"],
                                         int | float]] | None = None,
                 port_type: str | None = None,
                 allow_width_mismatch: bool = False,
                 radius: float | None = None,
                 route_width: float | None = None,
                 auto_taper: bool = True) -> ManhattanRoute
```

Returns a Manhattan Route between 2 ports.

The references are straights, bends and tapers.

**Arguments**:

- `component` - to place the route into.
- `port1` - start port.
- `port2` - end port.
- `cross_section` - spec.
- `layer` - layer spec.
- `bend` - bend spec.
- `straight` - straight spec.
- `start_straight_length` - length of starting straight.
- `end_straight_length` - length of end straight.
- `waypoints` - optional list of points to pass through.
- `steps` - optional list of steps to pass through.
- `port_type` - port type to route.
- `allow_width_mismatch` - allow different port widths.
- `radius` - bend radius. If None, defaults to cross_section.radius.
- `route_width` - width of the route in um. If None, defaults to cross_section.width.
- `auto_taper` - add auto tapers.
  
  .. plot::
  :include-source:
  
  import gdsfactory as gf
  
  c = gf.Component()
  mmi1 = c << gf.components.mmi1x2()
  mmi2 = c << gf.components.mmi1x2()
  mmi2.move((40, 20))
  gf.routing.route_single(c, mmi1.ports["o2"], mmi2.ports["o1"], radius=5, cross_section="strip")
  c.plot()

<a id="gdsfactory.routing.route_single.route_single_electrical"></a>

#### route\_single\_electrical

```python
def route_single_electrical(
        component: Component,
        port1: Port,
        port2: Port,
        start_straight_length: float | None = None,
        end_straight_length: float | None = None,
        layer: LayerSpec | None = None,
        width: float | None = None,
        cross_section: CrossSectionSpec = "metal_routing") -> None
```

Places a route between two electrical ports.

**Arguments**:

- `component` - The cell to place the route in.
- `port1` - The first port.
- `port2` - The second port.
- `start_straight_length` - The length of the straight at the start of the route.
- `end_straight_length` - The length of the straight at the end of the route.
- `layer` - The layer of the route.
- `width` - The width of the route.
- `cross_section` - The cross section of the route.

<a id="gdsfactory.functions"></a>

# gdsfactory.functions

<a id="gdsfactory.functions.move_port_to_zero"></a>

#### move\_port\_to\_zero

```python
def move_port_to_zero(component: Component,
                      port_name: str = "o1",
                      mirror: bool = False) -> gf.Component
```

Return a container that contains a reference to the original component.

The new component has port_name in (0, 0).

**Arguments**:

- `component` - to move the port to (0, 0).
- `port_name` - to move to (0, 0).
- `mirror` - if True, mirrors the component.

<a id="gdsfactory.functions.get_layers"></a>

#### get\_layers

```python
def get_layers(component: Component) -> list[tuple[int, int]]
```

Returns the layers of a component.

**Arguments**:

- `component` - to get the layers from.

<a id="gdsfactory.functions.extract"></a>

#### extract

```python
def extract(component: Component,
            layers: LayerSpecs,
            recursive: bool = True) -> Component
```

Extracts a list of layers and adds them to a new Component.

**Arguments**:

- `component` - to extract the layers from.
- `layers` - list of layers to extract.
- `recursive` - if True, extracts the shapes recursively.

<a id="gdsfactory.functions.move_to_center"></a>

#### move\_to\_center

```python
def move_to_center(component: Component,
                   dx: float = 0,
                   dy: float = 0) -> gf.Component
```

Moves the component to the center of the bounding box.

<a id="gdsfactory.functions.move_port"></a>

#### move\_port

```python
def move_port(component: Component,
              port_name: str,
              dx: float = 0,
              dy: float = 0) -> gf.Component
```

Moves the component port to a specific location.

Warning: This function modifies the component in-place.

**Arguments**:

- `component` - to move the port.
- `port_name` - to move.
- `dx` - to move the port.
- `dy` - to move the port.

<a id="gdsfactory.functions.get_polygons"></a>

#### get\_polygons

```python
def get_polygons(component_or_instance: "Component | ComponentReference",
                 merge: bool = False,
                 by: Literal["index", "name", "tuple"] = "index",
                 layers: LayerSpecs | None = None,
                 smooth: float | None = None) -> GetPolygonsResult
```

Returns a dict of Polygons per layer.

**Arguments**:

- `component_or_instance` - to extract the polygons.
- `merge` - if True, merges the polygons.
- `by` - the format of the resulting keys in the dictionary ('index', 'name', 'tuple').
- `layers` - list of layer specs to extract the polygons from. If None, extracts all layers.
- `smooth` - if True, smooths the polygons.

<a id="gdsfactory.functions.get_polygons_points"></a>

#### get\_polygons\_points

```python
def get_polygons_points(
    component_or_instance: "Component | ComponentReference",
    merge: bool = False,
    scale: float | None = None,
    by: Literal["index", "name", "tuple"] = "index",
    layers: LayerSpecs | None = None
) -> dict[int | str | tuple[int, int], list[npt.NDArray[np.floating[Any]]]]
```

Returns a dict with list of points per layer.

**Arguments**:

- `component_or_instance` - to extract the polygons.
- `merge` - if True, merges the polygons.
- `scale` - if True, scales the points.
- `by` - the format of the resulting keys in the dictionary ('index', 'name', 'tuple').
- `layers` - list of layer specs to extract the polygons from. If None, extracts all layers.

<a id="gdsfactory.functions.get_point_inside"></a>

#### get\_point\_inside

```python
def get_point_inside(component_or_instance: "Component | ComponentReference",
                     layer: LayerSpec) -> npt.NDArray[np.floating[Any]]
```

Returns a point inside the component or instance.

**Arguments**:

- `component_or_instance` - to find a point inside.
- `layer` - to find a point inside.

<a id="gdsfactory.functions.area"></a>

#### area

```python
def area(pts: npt.NDArray[np.floating[Any]]) -> float
```

Returns the area.

<a id="gdsfactory.functions.curvature"></a>

#### curvature

```python
def curvature(
        points: npt.NDArray[np.floating[Any]],
        t: npt.NDArray[np.floating[Any]]) -> npt.NDArray[np.floating[Any]]
```

Args are the points and the tangents at each point.

points : numpy.array shape (n, 2)
t: numpy.array of size n

**Returns**:

  The curvature at each point.
  
  Computes the curvature at every point excluding the first and last point.
  
  For a planar curve parametrized as P(t) = (x(t), y(t)), the curvature is given
  by (x' y'' - x'' y' ) / (x' **2 + y' **2)**(3/2)

<a id="gdsfactory.functions.path_length"></a>

#### path\_length

```python
def path_length(points: npt.NDArray[np.floating[Any]]) -> float
```

Returns: The path length.

**Arguments**:

- `points` - With shape (N, 2) representing N points with coordinates x, y.

<a id="gdsfactory.functions.snap_angle"></a>

#### snap\_angle

```python
def snap_angle(a: float) -> float
```

Returns angle snapped along manhattan angle (0, 90, 180, 270).

a: angle in deg
Return angle snapped along manhattan angle

<a id="gdsfactory.functions.angles_rad"></a>

#### angles\_rad

```python
def angles_rad(
        pts: npt.NDArray[np.floating[Any]]) -> npt.NDArray[np.floating[Any]]
```

Returns the angles (radians) of the connection between each point and the next.

<a id="gdsfactory.functions.angles_deg"></a>

#### angles\_deg

```python
def angles_deg(
        pts: npt.NDArray[np.floating[Any]]) -> npt.NDArray[np.floating[Any]]
```

Returns the angles (degrees) of the connection between each point and the next.

<a id="gdsfactory.functions.extrude_path"></a>

#### extrude\_path

```python
def extrude_path(points: npt.NDArray[np.floating[Any]],
                 width: float,
                 with_manhattan_facing_angles: bool = True,
                 spike_length: float64 | int | float = 0,
                 start_angle: int | None = None,
                 end_angle: int | None = None,
                 grid: float | None = None) -> npt.NDArray[np.floating[Any]]
```

Extrude a path of `width` along a curve defined by `points`.

**Arguments**:

- `points` - numpy 2D array of shape (N, 2).
- `width` - of the path to extrude.
- `with_manhattan_facing_angles` - snaps to manhattan angles.
- `spike_length` - in um.
- `start_angle` - in degrees.
- `end_angle` - in degrees.
- `grid` - in um.
  

**Returns**:

  numpy 2D array of shape (2*N, 2).

<a id="gdsfactory.functions.trim"></a>

#### trim

```python
def trim(component: Component,
         domain: Sequence[tuple[float, float]],
         flatten: bool = False) -> gf.Component
```

Trim a component by another geometry, preserving the component's layers and ports.

Useful to get a smaller component from a larger one for simulation.

**Arguments**:

- `component` - Component(/Reference).
- `domain` - list of array-like[N][2] representing the boundary of the component to keep.
- `flatten` - if True, flattens the component.
  
- `Returns` - New component with layers (and possibly ports) of the component restricted to the domain.
  
  .. plot::
  :include-source:
  
  import gdsfactory as gf
  c = gf.components.straight_pin(length=10)
  trimmed_c = gf.functions.trim(component=c, domain=[[0, -5], [0, 5], [5, 5], [5, -5]])
  trimmed_c.plot()

<a id="gdsfactory.functions.rotate"></a>

#### rotate

```python
@gf.cell
def rotate(component: Component, angle: float) -> gf.Component
```

Rotate a component by an angle in degrees.

**Arguments**:

- `component` - to rotate.
- `angle` - in increments of 90°.
  
- `Returns` - Rotated component.

<a id="gdsfactory.functions.mirror"></a>

#### mirror

```python
@gf.cell
def mirror(component: Component, x_mirror: bool = True) -> gf.Component
```

Rotate a component by an angle in degrees.

**Arguments**:

- `component` - to rotate.
- `x_mirror` - if True, mirrors the component along the x-axis.
  
- `Returns` - Rotated component.

<a id="gdsfactory.install"></a>

# gdsfactory.install

Install Klayout and GIT plugins.

<a id="gdsfactory.install.install_gdsdiff"></a>

#### install\_gdsdiff

```python
def install_gdsdiff() -> None
```

Install gdsdiff tool for GIT.

<a id="gdsfactory.install.get_klayout_path"></a>

#### get\_klayout\_path

```python
def get_klayout_path() -> pathlib.Path
```

Returns KLayout path.

<a id="gdsfactory.install.copy"></a>

#### copy

```python
def copy(src: pathlib.Path, dest: pathlib.Path) -> None
```

Copy overwriting file or directory.

<a id="gdsfactory.install.install_klayout_package"></a>

#### install\_klayout\_package

```python
def install_klayout_package() -> None
```

Install gdsfactory KLayout package.

Equivalent to using KLayout package manager.

<a id="gdsfactory.install.install_klayout_technology"></a>

#### install\_klayout\_technology

```python
def install_klayout_technology(tech_dir: pathlib.Path,
                               tech_name: str | None = None) -> None
```

Install technology to KLayout.

<a id="gdsfactory.install.convert_py_to_ipynb"></a>

#### convert\_py\_to\_ipynb

```python
def convert_py_to_ipynb(
        files: list[pathlib.Path] = py_files,
        output_folder: pathlib.Path = PATH.cwd / "notebooks") -> None
```

Convert notebooks from markdown to ipynb.

<a id="gdsfactory.cli"></a>

# gdsfactory.cli

<a id="gdsfactory.cli.Migration"></a>

## Migration Objects

```python
class Migration(str, Enum)
```

Available Migrations.

<a id="gdsfactory.cli.layermap_to_dataclass"></a>

#### layermap\_to\_dataclass

```python
@app.command()
def layermap_to_dataclass(
    filepath: str,
    force: bool = typer.Option(False, "--force", "-f", help="Force deletion")
) -> None
```

Converts KLayout LYP to a dataclass.

<a id="gdsfactory.cli.write_cells"></a>

#### write\_cells

```python
@app.command()
def write_cells(gdspath: str,
                dirpath: str = "",
                recursively: bool = True) -> None
```

Write each all level cells into separate GDS files.

<a id="gdsfactory.cli.merge_gds"></a>

#### merge\_gds

```python
@app.command()
def merge_gds(dirpath: str = "", gdspath: str = "") -> None
```

Merges GDS cells from a directory into a single GDS.

<a id="gdsfactory.cli.watch"></a>

#### watch

```python
@app.command()
def watch(path: str = str(pathlib.Path.cwd()),
          pdk: str = typer.Option(None, "--pdk", "-pdk", help="PDK name"),
          run_main: bool = typer.Option(False,
                                        "--run-main",
                                        "-rm",
                                        help="Run main"),
          run_cells: bool = typer.Option(False,
                                         "--run-cells",
                                         "-rc",
                                         help="Run cells"),
          pre_run: bool = typer.Option(False,
                                       "--pre-run",
                                       "-p",
                                       help="Build all cells on startup"),
          overwrite: bool = typer.Option(
              True, help="Overwrite existing cells")) -> None
```

Filewatch a folder for changes in *.py or *.pic.yml files.

If a file changes, it will run the main function and show the cells.

**Arguments**:

- `path` - folder to watch.
- `pdk` - process design kit.
- `run_main` - run the main function.
- `run_cells` - run the cells.
- `pre_run` - build all cells on startup.
- `overwrite` - overwrite existing cells.

<a id="gdsfactory.cli.show"></a>

#### show

```python
@app.command()
def show(filename: str) -> None
```

Show a GDS file using klive.

<a id="gdsfactory.cli.gds_diff"></a>

#### gds\_diff

```python
@app.command()
def gds_diff(gdspath1: str, gdspath2: str, xor: bool = False) -> None
```

Show boolean difference between two GDS files.

<a id="gdsfactory.cli.install_klayout_genericpdk"></a>

#### install\_klayout\_genericpdk

```python
@app.command()
def install_klayout_genericpdk() -> None
```

Install Klayout generic PDK.

<a id="gdsfactory.cli.install_git_diff"></a>

#### install\_git\_diff

```python
@app.command()
def install_git_diff() -> None
```

Install git diff.

<a id="gdsfactory.cli.version"></a>

#### version

```python
@app.command()
def version() -> None
```

Show installed plugin versions.

<a id="gdsfactory.cli.from_updk_command"></a>

#### from\_updk\_command

```python
@app.command(name="from-updk")
def from_updk_command(filepath: str, filepath_out: str = "") -> None
```

Writes a PDK in python from uPDK YAML spec.

<a id="gdsfactory.difftest"></a>

# gdsfactory.difftest

GDS regression test. Inspired by lytest.

<a id="gdsfactory.difftest.xor"></a>

#### xor

```python
def xor(old: KCLayout,
        new: KCLayout,
        test_name: str = "",
        ignore_sliver_differences: bool | None = None,
        ignore_cell_name_differences: bool | None = None,
        ignore_label_differences: bool | None = None,
        stagger: bool = True) -> DKCell
```

Returns XOR of two layouts.

**Arguments**:

- `old` - reference layout.
- `new` - run layout.
- `test_name` - prefix for the new cell.
- `ignore_sliver_differences` - if True, ignores any sliver differences in the XOR result. If None (default), defers to the value set in CONF.difftest_ignore_sliver_differences
- `ignore_cell_name_differences` - if True, ignores any cell name differences. If None (default), defers to the value set in CONF.difftest_ignore_cell_name_differences
- `ignore_label_differences` - if True, ignores any label differences when run in XOR mode. If None (default) defers to the value set in CONF.difftest_ignore_label_differences
- `stagger` - if True, staggers the old/new/xor views. If False, all three are overlaid.

<a id="gdsfactory.difftest.diff"></a>

#### diff

```python
def diff(ref_file: PathType,
         run_file: PathType,
         xor: bool = True,
         test_name: str = "",
         ignore_sliver_differences: bool | None = None,
         ignore_cell_name_differences: bool | None = None,
         ignore_label_differences: bool | None = None,
         show: bool = False,
         stagger: bool = True) -> bool
```

Returns True if files are different, prints differences and shows them in klayout.

**Arguments**:

- `ref_file` - reference (old) file.
- `run_file` - run (new) file.
- `xor` - runs xor on every layer between old and run files.
- `test_name` - prefix for the new cell.
- `ignore_sliver_differences` - if True, ignores any sliver differences in the XOR result. If None (default), defers to the value set in CONF.difftest_ignore_sliver_differences
- `ignore_cell_name_differences` - if True, ignores any cell name differences. If None (default), defers to the value set in CONF.difftest_ignore_cell_name_differences
- `ignore_label_differences` - if True, ignores any label differences when run in XOR mode. If None (default) defers to the value set in CONF.difftest_ignore_label_differences
- `show` - shows diff in klayout.
- `stagger` - if True, staggers the old/new/xor views. If False, all three are overlaid.

<a id="gdsfactory.difftest.difftest"></a>

#### difftest

```python
def difftest(component: gf.Component,
             test_name: str | None = None,
             dirpath: pathlib.Path = PATH.gds_ref,
             xor: bool = True,
             dirpath_run: pathlib.Path = PATH.gds_run,
             ignore_sliver_differences: bool | None = None) -> None
```

Avoids GDS regressions tests on the GeometryDifference.

If files are the same it returns None. If files are different runs XOR
between new component and the GDS reference stored in dirpath and
raises GeometryDifference if there are differences and show differences in KLayout.

If it runs for the fist time it just stores the GDS reference.

**Arguments**:

- `component` - to test if it has changed.
- `test_name` - used to store the GDS file.
- `dirpath` - directory where reference files are stored.
- `xor` - runs XOR.
- `dirpath_run` - directory to store gds file generated by the test.
- `ignore_sliver_differences` - if True, ignores any sliver differences in the XOR result.
  If None (default), defers to the value set in CONF.difftest_ignore_sliver_differences

<a id="gdsfactory.get_netlist"></a>

# gdsfactory.get\_netlist

Extract netlist from component port connectivity.

Assumes two ports are connected when they have same width, x, y

.. code:: yaml

    connections:
        - coupler,N0:bendLeft,W0
        - coupler,N1:bendRight,N0
        - bednLeft,N0:straight,W0
        - bendRight,N0:straight,E0

    ports:
        - coupler,E0
        - coupler,W0

<a id="gdsfactory.get_netlist.get_instance_name_from_alias"></a>

#### get\_instance\_name\_from\_alias

```python
def get_instance_name_from_alias(reference: ComponentReference) -> str
```

Returns the instance name from the label.

If no label returns to instanceName_x_y.

**Arguments**:

- `reference` - reference that needs naming.

<a id="gdsfactory.get_netlist.get_instance_name_from_label"></a>

#### get\_instance\_name\_from\_label

```python
def get_instance_name_from_label(
        component: Component,
        reference: ComponentReference,
        layer_label: LayerSpec = "LABEL_INSTANCE") -> str
```

Returns the instance name from the label.

If no label returns to instanceName_x_y.

**Arguments**:

- `component` - with labels.
- `reference` - reference that needs naming.
- `layer_label` - ignores layer_label[1].

<a id="gdsfactory.get_netlist.get_netlist"></a>

#### get\_netlist

```python
def get_netlist(
    component: DKCell,
    exclude_port_types: Sequence[str] | None = ("placement", "pad", "bump"),
    get_instance_name: Callable[..., str] = get_instance_name_from_alias,
    allow_multiple: bool = True,
    connection_error_types: dict[str, list[str]] | None = None
) -> dict[str, Any]
```

From Component returns a dict with instances, connections and placements.

warnings collected during netlisting are reported back into the netlist.
These include warnings about mismatched port widths, orientations, shear angles, excessive offsets, etc.
You can also configure warning types which should throw an error when encountered
by modifying connection_error_types.
A key difference in this algorithm is that we group each port type independently.
This allows us to use different logic to determine i.e.
if an electrical port is properly connected vs an optical port.
In this function, the core logic is the same, but we employ extra validation for optical ports.

**Arguments**:

- `component` - to extract netlist.
- `exclude_port_types` - optional list of port types to exclude from netlisting.
- `get_instance_name` - function to get instance name.
- `allow_multiple` - False to raise an error if more than two ports share the same connection.                 if True, will return key: [value] pairs with [value] a list of all connected instances.
- `connection_error_types` - optional dictionary of port types and error types to raise an error for.
  

**Returns**:

- `instances` - Dict of instance name and settings.
- `nets` - List of connected port pairs/groups
- `placements` - Dict of instance names and placements (x, y, rotation).
- `port` - Dict portName: ComponentName,port.
- `name` - name of component.
- `warnings` - warning messages (disconnected pins).

<a id="gdsfactory.get_netlist.get_netlist_recursive"></a>

#### get\_netlist\_recursive

```python
def get_netlist_recursive(component: DKCell,
                          component_suffix: str = "",
                          get_netlist_func: GetNetlistFunc = get_netlist,
                          get_instance_name: Callable[
                              ..., str] = get_instance_name_from_alias,
                          **kwargs: Any) -> dict[str, Any]
```

Returns recursive netlist for a component and subcomponents.

**Arguments**:

- `component` - to extract netlist.
- `component_suffix` - suffix to append to each component name.
  useful if to save and reload a back-annotated netlist.
- `get_netlist_func` - function to extract individual netlists.
- `get_instance_name` - function to get instance name.
- `kwargs` - additional keyword arguments to pass to get_netlist_func.
  

**Arguments**:

- `tolerance` - tolerance in grid_factor to consider two ports connected.
- `exclude_port_types` - optional list of port types to exclude from netlisting.
- `get_instance_name` - function to get instance name.
  

**Returns**:

  Dictionary of netlists, keyed by the name of each component.

<a id="gdsfactory.get_factories"></a>

# gdsfactory.get\_factories

<a id="gdsfactory.get_factories.get_cells"></a>

#### get\_cells

```python
def get_cells(modules: Any,
              ignore_non_decorated: bool = False,
              ignore_underscored: bool = True,
              ignore_partials: bool = False) -> dict[str, ComponentFactory]
```

Returns PCells (component functions) from a module or list of modules.

**Arguments**:

- `modules` - A module or an iterable of modules.
- `ignore_non_decorated` - only include functions that are decorated with gf.cell
- `ignore_underscored` - only include functions that do not start with '_'
- `ignore_partials` - only include functions, not partials

<a id="gdsfactory.get_factories.get_cells_from_dict"></a>

#### get\_cells\_from\_dict

```python
def get_cells_from_dict(
    cells: dict[str, Callable[...,
                              Any]]) -> dict[str, Callable[..., Component]]
```

Returns PCells (component functions) from a dictionary.

**Arguments**:

- `cells` - A dictionary of cells.
  

**Returns**:

  A dictionary of valid component functions.

<a id="gdsfactory.generic_tech.layer_map"></a>

# gdsfactory.generic\_tech.layer\_map

<a id="gdsfactory.generic_tech.layer_map.LAYER"></a>

## LAYER Objects

```python
class LAYER(gf.LayerEnum)
```

Generic layermap based on book.

Lukas Chrostowski, Michael Hochberg, "Silicon Photonics Design",
Cambridge University Press 2015, page 353
You will need to create a new LayerMap with your specific foundry layers.

<a id="gdsfactory.generic_tech.get_klayout_pyxs"></a>

# gdsfactory.generic\_tech.get\_klayout\_pyxs

write xsection script for KLayout plugin.

https://gdsfactory.github.io/klayout_pyxs/DocGrow.html

<a id="gdsfactory.generic_tech.get_klayout_pyxs.get_klayout_pyxs"></a>

#### get\_klayout\_pyxs

```python
def get_klayout_pyxs(t_box: float = 1.0,
                     t_slab: float = 90 * nm,
                     t_si: float = 0.22,
                     t_ge: float = 0.4,
                     t_nitride: float = 0.4,
                     h_etch1: float = 0.07,
                     h_etch2: float = 0.06,
                     h_etch3: float = 0.09,
                     t_clad: float = 0.6,
                     t_m1: float = 0.5,
                     t_m2: float = 0.5,
                     t_m3: float = 2.0,
                     gap_m1_m2: float = 0.6,
                     gap_m2_m3: float = 0.3,
                     t_heater: float = 0.1,
                     gap_oxide_nitride: float = 0.82,
                     t_m1_oxide: float = 0.6,
                     t_m2_oxide: float = 2.0,
                     t_m3_oxide: float = 0.5,
                     layer_wg: tuple[int, int] = LAYER.WG,
                     layer_fc: tuple[int, int] = LAYER.SLAB150,
                     layer_rib: tuple[int, int] = LAYER.SLAB90,
                     layer_n: tuple[int, int] = LAYER.N,
                     layer_np: tuple[int, int] = LAYER.NP,
                     layer_npp: tuple[int, int] = LAYER.NPP,
                     layer_p: tuple[int, int] = LAYER.P,
                     layer_pp: tuple[int, int] = LAYER.PP,
                     layer_ppp: tuple[int, int] = LAYER.PPP,
                     layer_PDPP: tuple[int, int] = LAYER.GEP,
                     layer_nitride: tuple[int, int] = LAYER.WGN,
                     layer_Ge: tuple[int, int] = LAYER.GE,
                     layer_GePPp: tuple[int, int] = LAYER.GEP,
                     layer_GeNPP: tuple[int, int] = LAYER.GEN,
                     layer_viac: tuple[int, int] = LAYER.VIAC,
                     layer_viac_slot: tuple[int, int] = LAYER.VIAC,
                     layer_m1: tuple[int, int] = LAYER.M1,
                     layer_mh: tuple[int, int] = LAYER.HEATER,
                     layer_via1: tuple[int, int] = LAYER.VIA1,
                     layer_m2: tuple[int, int] = LAYER.M2,
                     layer_via2: tuple[int, int] = LAYER.VIA2,
                     layer_m3: tuple[int, int] = LAYER.M3,
                     layer_open: tuple[int, int] = LAYER.PADOPEN) -> str
```

Returns klayout_pyxs plugin script to show chip cross-section in klayout.

https://gdsfactory.github.io/klayout_pyxs/DocGrow.html

<a id="gdsfactory.generic_tech"></a>

# gdsfactory.generic\_tech

<a id="gdsfactory.generic_tech.klayout.python.kgdsfactory"></a>

# gdsfactory.generic\_tech.klayout.python.kgdsfactory

<a id="gdsfactory.generic_tech.klayout.python.kgdsfactory.shortcuts"></a>

# gdsfactory.generic\_tech.klayout.python.kgdsfactory.shortcuts

Keybindings inspired by SiEPIC tools.

<a id="gdsfactory.generic_tech.klayout.python"></a>

# gdsfactory.generic\_tech.klayout.python

<a id="gdsfactory.generic_tech.klayout.drc.errors"></a>

# gdsfactory.generic\_tech.klayout.drc.errors

<a id="gdsfactory.generic_tech.klayout.drc.errors.enclosing"></a>

#### enclosing

```python
@gf.cell
def enclosing(
    enclosing: float = 0.1,
    layer1: Layer = (40, 0),
    layer2: Layer = (41, 0)
) -> Component
```

Layer1 must be enclosed by layer2 by value.

checks if layer1 encloses (is bigger than) layer2 by value

<a id="gdsfactory.generic_tech.klayout.drc.errors.not_inside"></a>

#### not\_inside

```python
@gf.cell
def not_inside(layer: Layer = (40, 0),
               not_inside: Layer = (24, 0)) -> Component
```

Layer must be inside by layer.

<a id="gdsfactory.generic_tech.klayout.drc"></a>

# gdsfactory.generic\_tech.klayout.drc

<a id="gdsfactory.generic_tech.klayout.lvs.drc_malformed.run_drc"></a>

# gdsfactory.generic\_tech.klayout.lvs.drc\_malformed.run\_drc

Run GENERIC TECH DRC-malformed runset.

Usage:
    run_drc.py (--help| -h)
    run_drc.py (--path=<file_path>) [--verbose] [--mp=<num_cores>] [--run_dir=<run_dir_path>] [--topcell=<topcell_name>] [--thr=<thr>] [--run_mode=<run_mode>] [--offgrid]

Options:
    --help -h                           Print this help message.
    --path=<file_path>                  The input GDS file path.
    --topcell=<topcell_name>            Topcell name to use.
    --mp=<num_cores>                    Run the rule deck in parts in parallel to speed up the run. [default: 1]
    --run_dir=<run_dir_path>            Run directory to save all the results [default: pwd]
    --thr=<thr>                         The number of threads used in run.
    --run_mode=<run_mode>               Select klayout mode Allowed modes (flat , deep, tiling). [default: deep]
    --verbose                           Detailed rule execution log for debugging.

<a id="gdsfactory.generic_tech.klayout.lvs.drc_malformed.run_drc.get_rules_with_violations"></a>

#### get\_rules\_with\_violations

```python
def get_rules_with_violations(results_database: str) -> set[str]
```

This function will find all the rules that has violated in a database.

Parameters
----------
results_database : string or Path object
Path string to the results file

**Returns**:

  -------
  set
  A set that contains all rules in the database with violations

<a id="gdsfactory.generic_tech.klayout.lvs.drc_malformed.run_drc.check_drc_results"></a>

#### check\_drc\_results

```python
def check_drc_results(results_db_files: list[str]) -> None
```

check_drc_results Checks the results db generated from run and report at the end if the DRC run failed or passed.

This function will exit with 1 if there are violations.

**Arguments**:

- `results_db_files` - A list of strings that represent paths to results databases of all the DRC runs.

<a id="gdsfactory.generic_tech.klayout.lvs.drc_malformed.run_drc.get_top_cell_names"></a>

#### get\_top\_cell\_names

```python
def get_top_cell_names(gds_path: str) -> list[str]
```

get_top_cell_names get the top cell names from the GDS file.

Parameters
----------
gds_path : string
Path to the target GDS file.

**Returns**:

  -------
  List of string
  Names of the top cell in the layout.

<a id="gdsfactory.generic_tech.klayout.lvs.drc_malformed.run_drc.get_run_top_cell_name"></a>

#### get\_run\_top\_cell\_name

```python
def get_run_top_cell_name(arguments: dict[str, str], layout_path: str) -> str
```

get_run_top_cell_name Get the top cell name to use for running. If it's provided by the user, we use the user input.

If not, we get it from the GDS file.

**Arguments**:

- `arguments` - Dictionary that holds the user inputs for the script generated by docopt.
- `layout_path` - Path to the target layout.
  
- `Returns` - Name of the topcell to use in run.

<a id="gdsfactory.generic_tech.klayout.lvs.drc_malformed.run_drc.generate_klayout_switches"></a>

#### generate\_klayout\_switches

```python
def generate_klayout_switches(arguments: dict[str, str],
                              layout_path: str) -> dict[str, str]
```

parse_switches Function that parse all the args from input to prepare switches for DRC run.

<a id="gdsfactory.generic_tech.klayout.lvs.drc_malformed.run_drc.check_klayout_version"></a>

#### check\_klayout\_version

```python
def check_klayout_version() -> None
```

check_klayout_version checks klayout version and makes sure it would work with the DRC.

<a id="gdsfactory.generic_tech.klayout.lvs.drc_malformed.run_drc.check_layout_path"></a>

#### check\_layout\_path

```python
def check_layout_path(layout_path: str) -> str
```

check_layout_type checks if the layout provided is GDS or OAS. Otherwise, kill the process. We only support GDS or OAS now.

Parameters
----------
layout_path : string
string that represent the path of the layout.

**Returns**:

  -------
  string
  string that represent full absolute layout path.

<a id="gdsfactory.generic_tech.klayout.lvs.drc_malformed.run_drc.build_switches_string"></a>

#### build\_switches\_string

```python
def build_switches_string(sws: dict[str, str]) -> str
```

build_switches_string Build switches string from dictionary.

<a id="gdsfactory.generic_tech.klayout.lvs.drc_malformed.run_drc.run_check"></a>

#### run\_check

```python
def run_check(drc_file: str, drc_name: str, path: str, run_dir: str,
              sws: dict[str, str]) -> str
```

run_antenna_check run DRC check based on DRC file provided.

**Arguments**:

- `drc_file` - String that has the file full path to run.
- `drc_name` - String that holds the name of the DRC check.
- `path` - String that holds the full path of the layout.
- `run_dir` - String that holds the full path of the run location.
- `sws` - Dictionary that holds all switches that needs to be passed to the antenna checks.

<a id="gdsfactory.generic_tech.klayout.lvs.drc_malformed.run_drc.run_single_processor"></a>

#### run\_single\_processor

```python
def run_single_processor(arguments: dict[str, str], rule_deck_full_path: str,
                         layout_path: str, switches: dict[str, str],
                         drc_run_dir: str) -> None
```

run_single_processor run the drc checks as single run.

**Arguments**:

- `arguments` - Dictionary that holds the user inputs for the script generated by docopt.
- `rule_deck_full_path` - String that holds the full path of the rule deck.
- `layout_path` - String that holds the full path of the layout.
- `switches` - Dictionary that holds all the switches that needs to be passed to the DRC checks.
- `drc_run_dir` - String that holds the full path of the run location.

<a id="gdsfactory.generic_tech.klayout.lvs.drc_malformed.run_drc.main"></a>

#### main

```python
def main(drc_run_dir: str, now_str: str, arguments: dict[str, str]) -> None
```

Main function to run the DRC.

**Arguments**:

- `drc_run_dir` - String that holds the full path of the run location.
- `now_str` - String that holds the current time string.
- `arguments` - Dictionary that holds the user inputs for the script generated by docopt.

<a id="gdsfactory.generic_tech.klayout.lvs.testing.testcases.unit.heater_devices.layout.straight_heater_metal"></a>

# gdsfactory.generic\_tech.klayout.lvs.testing.testcases.unit.heater\_devices.layout.straight\_heater\_metal

<a id="gdsfactory.generic_tech.klayout.lvs.run_lvs"></a>

# gdsfactory.generic\_tech.klayout.lvs.run\_lvs

Run GENERIC TECHs LVS.

Usage:
    run_lvs.py (--help| -h)
    run_lvs.py (--layout=<layout_path>) (--netlist=<netlist_path>) [--thr=<thr>] [--run_dir=<run_dir_path>] [--topcell=<topcell_name>] [--run_mode=<run_mode>] [--verbose] [--lvs_sub=<sub_name>] [--no_net_names] [--spice_comments] [--scale]

Options:
    --help -h                           Print this help message.
    --layout=<layout_path>              The input GDS file path.
    --netlist=<netlist_path>            The input netlist file path.
    --thr=<thr>                         The number of threads used in run.
    --run_dir=<run_dir_path>            Run directory to save all the results [default: pwd]
    --topcell=<topcell_name>            Topcell name to use.
    --run_mode=<run_mode>               Select klayout mode Allowed modes (flat , deep, tiling). [default: deep ]
    --lvs_sub=<sub_name>                Substrate name used in your design.
    --verbose                           Detailed rule execution log for debugging.
    --no_net_names                      Discard net names in extracted netlist.
    --spice_comments                    Enable netlist comments in extracted netlist.
    --scale                             Enable scale of 1e6 in extracted netlist.

<a id="gdsfactory.generic_tech.klayout.lvs.run_lvs.check_klayout_version"></a>

#### check\_klayout\_version

```python
def check_klayout_version() -> None
```

check_klayout_version checks klayout version and makes sure it would work with the LVS.

<a id="gdsfactory.generic_tech.klayout.lvs.run_lvs.check_layout_type"></a>

#### check\_layout\_type

```python
def check_layout_type(layout_path: str) -> str
```

check_layout_type checks if the layout provided is GDS or OAS. Otherwise, kill the process. We only support GDS or OAS now.

<a id="gdsfactory.generic_tech.klayout.lvs.run_lvs.get_top_cell_names"></a>

#### get\_top\_cell\_names

```python
def get_top_cell_names(gds_path: str) -> list[str]
```

get_top_cell_names get the top cell names from the GDS file.

<a id="gdsfactory.generic_tech.klayout.lvs.run_lvs.get_run_top_cell_name"></a>

#### get\_run\_top\_cell\_name

```python
def get_run_top_cell_name(arguments: dict[str, str], layout_path: str) -> str
```

get_run_top_cell_name Get the top cell name to use for running.

<a id="gdsfactory.generic_tech.klayout.lvs.run_lvs.generate_klayout_switches"></a>

#### generate\_klayout\_switches

```python
def generate_klayout_switches(arguments: dict[str, str], layout_path: str,
                              netlist_path: str) -> dict[str, str]
```

parse_switches Function that parse all the args from input to prepare switches for LVS run.

**Arguments**:

- `arguments` _dict_ - Dictionary that holds the arguments used by user in the run command. This is generated by docopt library.
- `layout_path` _string_ - Path to the layout file that we will run LVS on.
- `netlist_path` _string_ - Path to the netlist file that we will run LVS on.

<a id="gdsfactory.generic_tech.klayout.lvs.run_lvs.build_switches_string"></a>

#### build\_switches\_string

```python
def build_switches_string(sws: dict[str, str]) -> str
```

build_switches_string Build switches string from dictionary.

**Arguments**:

- `sws` - Dictionary that holds the Antenna switches.

<a id="gdsfactory.generic_tech.klayout.lvs.run_lvs.check_lvs_results"></a>

#### check\_lvs\_results

```python
def check_lvs_results(results_db_files: Sequence[str]) -> None
```

check_lvs_results Checks the results db generated from run and report at the end if the LVS run failed or passed.

Parameters
----------
results_db_files : list
    A list of strings that represent paths to results databases of all the LVS runs.

<a id="gdsfactory.generic_tech.klayout.lvs.run_lvs.run_check"></a>

#### run\_check

```python
def run_check(lvs_file: str, path: str, run_dir: str, sws: dict[str,
                                                                str]) -> str
```

run_check run LVS check.

Parameters
----------
lvs_file : str
String that has the file full path to run.
path : str
String that holds the full path of the layout.
run_dir : str
String that holds the full path of the run location.
sws : dict
Dictionary that holds all switches that needs to be passed to the antenna checks.

**Returns**:

  -------
  string
  string that represent the path to the results output database for this run.

<a id="gdsfactory.generic_tech.klayout.lvs.run_lvs.main"></a>

#### main

```python
def main(lvs_run_dir: str, arguments: dict[str, str]) -> None
```

Main function to run the LVS.

Parameters
----------
lvs_run_dir : str
    String with absolute path of the full run dir.
arguments : dict
    Dictionary that holds the arguments used by user in the run command. This is generated by docopt library.

<a id="gdsfactory.generic_tech.simulation_settings"></a>

# gdsfactory.generic\_tech.simulation\_settings

<a id="gdsfactory.generic_tech.simulation_settings.SimulationSettingsLumericalFdtd"></a>

## SimulationSettingsLumericalFdtd Objects

```python
class SimulationSettingsLumericalFdtd(BaseModel)
```

Lumerical FDTD simulation_settings.

**Arguments**:

- `background_material` - for the background.
- `port_margin` - on both sides of the port width (um).
- `port_height` - port height (um).
- `port_extension` - port extension (um).
- `mesh_accuracy` - 2 (1: coarse, 2: fine, 3: superfine).
- `zmargin` - for the FDTD region (um).
- `ymargin` - for the FDTD region (um).
- `xmargin` - for the FDTD region (um).
- `wavelength_start` - 1.2 (um).
- `wavelength_stop` - 1.6 (um).
- `wavelength_points` - 500.
- `simulation_time` - (s) related to max path length
  3e8/2.4*10e-12*1e6 = 1.25mm.
- `simulation_temperature` - in kelvin (default = 300).
- `frequency_dependent_profile` - compute mode profiles for each wavelength.
- `field_profile_samples` - number of wavelengths to compute field profile.

<a id="gdsfactory.generic_tech.layer_stack"></a>

# gdsfactory.generic\_tech.layer\_stack

<a id="gdsfactory.generic_tech.layer_stack.LayerStackParameters"></a>

## LayerStackParameters Objects

```python
class LayerStackParameters()
```

values used by get_layer_stack and get_process.

<a id="gdsfactory.generic_tech.layer_stack.get_layer_stack"></a>

#### get\_layer\_stack

```python
def get_layer_stack(
    thickness_wg: float = LayerStackParameters.thickness_wg,
    thickness_slab_deep_etch: float = LayerStackParameters.
    thickness_slab_deep_etch,
    thickness_slab_shallow_etch: float = LayerStackParameters.
    thickness_slab_shallow_etch,
    sidewall_angle_wg: float = LayerStackParameters.sidewall_angle_wg,
    thickness_clad: float = LayerStackParameters.thickness_clad,
    thickness_nitride: float = LayerStackParameters.thickness_nitride,
    thickness_ge: float = LayerStackParameters.thickness_ge,
    gap_silicon_to_nitride: float = LayerStackParameters.
    gap_silicon_to_nitride,
    zmin_heater: float = LayerStackParameters.zmin_heater,
    zmin_metal1: float = LayerStackParameters.zmin_metal1,
    thickness_metal1: float = LayerStackParameters.thickness_metal1,
    zmin_metal2: float = LayerStackParameters.zmin_metal2,
    thickness_metal2: float = LayerStackParameters.thickness_metal2,
    zmin_metal3: float = LayerStackParameters.zmin_metal3,
    thickness_metal3: float = LayerStackParameters.thickness_metal3,
    substrate_thickness: float = LayerStackParameters.substrate_thickness,
    box_thickness: float = LayerStackParameters.box_thickness,
    undercut_thickness: float = LayerStackParameters.undercut_thickness,
    layer_wafer: LogicalLayer = LogicalLayer(layer=LAYER.WAFER),
    layer_core: LogicalLayer = LogicalLayer(layer=LAYER.WG),
    layer_shallow_etch: LogicalLayer = LogicalLayer(layer=LAYER.SHALLOW_ETCH),
    layer_deep_etch: LogicalLayer = LogicalLayer(layer=LAYER.DEEP_ETCH),
    layer_nitride: LogicalLayer = LogicalLayer(layer=LAYER.WGN),
    layer_slab_deep_etch: LogicalLayer = LogicalLayer(layer=LAYER.SLAB90),
    layer_slab_shallow_etch: LogicalLayer = LogicalLayer(layer=LAYER.SLAB150),
    layer_ge: LogicalLayer = LogicalLayer(layer=LAYER.GE),
    layer_undercut: LogicalLayer = LogicalLayer(layer=LAYER.UNDERCUT),
    layer_heater: LogicalLayer = LogicalLayer(layer=LAYER.HEATER),
    layer_metal1: LogicalLayer = LogicalLayer(layer=LAYER.M1),
    layer_metal2: LogicalLayer = LogicalLayer(layer=LAYER.M2),
    layer_metal3: LogicalLayer = LogicalLayer(layer=LAYER.M3),
    layer_viac: LogicalLayer = LogicalLayer(layer=LAYER.VIAC),
    layer_via1: LogicalLayer = LogicalLayer(layer=LAYER.VIA1),
    layer_via2: LogicalLayer = LogicalLayer(layer=LAYER.VIA2)
) -> LayerStack
```

Returns generic LayerStack.

based on paper https://www.degruyter.com/document/doi/10.1515/nanoph-2013-0034/html

**Arguments**:

- `thickness_wg` - waveguide thickness in um.
- `thickness_slab_deep_etch` - for deep etched slab.
- `thickness_slab_shallow_etch` - thickness for the etch in um.
- `sidewall_angle_wg` - waveguide side angle.
- `thickness_clad` - cladding thickness in um.
- `thickness_nitride` - nitride thickness in um.
- `thickness_ge` - germanium thickness.
- `gap_silicon_to_nitride` - distance from silicon to nitride in um.
- `zmin_heater` - TiN heater.
- `zmin_metal1` - metal1.
- `thickness_metal1` - metal1 thickness.
- `zmin_metal2` - metal2.
- `thickness_metal2` - metal2 thickness.
- `zmin_metal3` - metal3.
- `thickness_metal3` - metal3 thickness.
- `substrate_thickness` - substrate thickness in um.
- `box_thickness` - bottom oxide thickness in um.
- `undercut_thickness` - thickness of the silicon undercut.
- `layer_wafer` - wafer layer.
- `layer_core` - waveguide layer.
- `layer_shallow_etch` - shallow etch layer.
- `layer_deep_etch` - deep etch layer.
- `layer_nitride` - nitride layer.
- `layer_slab_deep_etch` - deep etch slab layer.
- `layer_slab_shallow_etch` - shallow etch slab layer.
- `layer_ge` - germanium layer.
- `layer_undercut` - undercut layer.
- `layer_heater` - heater layer.
- `layer_metal1` - metal1 layer.
- `layer_metal2` - metal2 layer.
- `layer_metal3` - metal3 layer.
- `layer_viac` - viac layer.
- `layer_via1` - via1 layer.
- `layer_via2` - via2 layer.

<a id="gdsfactory.generic_tech.layer_stack.get_process"></a>

#### get\_process

```python
def get_process() -> tuple[ProcessStep, ...]
```

Returns generic process to generate LayerStack.

Represents processing steps that will result in the GenericLayerStack, starting from the waferstack LayerStack.

based on paper https://www.degruyter.com/document/doi/10.1515/nanoph-2013-0034/html

<a id="gdsfactory.component"></a>

# gdsfactory.component

Component is a canvas for geometry.

<a id="gdsfactory.component.ComponentBase"></a>

## ComponentBase Objects

```python
class ComponentBase(ProtoKCell[float, BaseKCell], ABC)
```

Canvas where you add polygons, instances and ports.

- stores settings that you use to build the component
- stores info that you want to use
- can return ports by type (optical, electrical ...)
- can return netlist for circuit simulation
- can write to GDS, OASIS
- can show in KLayout, matplotlib or 3D

Properties:
    info: dictionary that includes derived properties, simulation_settings, settings (test_protocol, docs, ...)

<a id="gdsfactory.component.ComponentBase.bbox_np"></a>

#### bbox\_np

```python
def bbox_np() -> npt.NDArray[np.float64]
```

Returns the bounding box of the Component as a numpy array.

<a id="gdsfactory.component.ComponentBase.add_port"></a>

#### add\_port

```python
def add_port(name: str | None = None,
             *,
             port: ProtoPort[Any] | None = None,
             center: Position | kdb.DPoint | None = None,
             width: float | None = None,
             orientation: AngleInDegrees = 0,
             layer: LayerSpec | None = None,
             port_type: str = "optical",
             keep_mirror: bool = False,
             cross_section: "CrossSectionSpec | None" = None) -> DPort
```

Adds a Port to the Component.

**Arguments**:

- `name` - name of the port.
- `port` - port to add.
- `center` - center of the port.
- `width` - width of the port.
- `orientation` - orientation of the port.
- `layer` - layer spec to add port on.
- `port_type` - port type (optical, electrical, ...)
- `keep_mirror` - if True, keeps the mirror of the port.
- `cross_section` - cross_section of the port.

<a id="gdsfactory.component.ComponentBase.copy"></a>

#### copy

```python
def copy() -> Self
```

Copy the full cell.

<a id="gdsfactory.component.ComponentBase.add_label"></a>

#### add\_label

```python
def add_label(text: str = "hello",
              position: Position | kf.kdb.DPoint = (0.0, 0.0),
              layer: LayerSpec = "TEXT") -> None
```

Adds Label to the Component.

**Arguments**:

- `text` - Label text.
- `position` - x-, y-coordinates of the Label location.
- `layer` - Specific layer(s) to put Label on.

<a id="gdsfactory.component.ComponentBase.get_ports_list"></a>

#### get\_ports\_list

```python
def get_ports_list(**kwargs: Any) -> "list[Port]"
```

Returns list of ports.

**Arguments**:

- `kwargs` - Additional kwargs.
  

**Arguments**:

- `layer` - select ports with GDS layer.
- `prefix` - select ports with prefix in port name.
- `suffix` - select ports with port name suffix.
- `orientation` - select ports with orientation in degrees.
- `orientation` - select ports with orientation in degrees.
- `width` - select ports with port width.
- `layers_excluded` - List of layers to exclude.
- `port_type` - select ports with port_type (optical, electrical, vertical_te).
- `clockwise` - if True, sort ports clockwise, False: counter-clockwise.

<a id="gdsfactory.component.ComponentBase.add_route_info"></a>

#### add\_route\_info

```python
def add_route_info(cross_section: "CrossSection | str",
                   length: float,
                   length_eff: float | None = None,
                   taper: bool = False,
                   **kwargs: Any) -> None
```

Adds route information to a component.

**Arguments**:

- `cross_section` - CrossSection or name of the cross_section.
- `length` - length of the route.
- `length_eff` - effective length of the route.
- `taper` - if True adds taper information.
- `kwargs` - extra information to add to the component.

<a id="gdsfactory.component.ComponentBase.copy_child_info"></a>

#### copy\_child\_info

```python
def copy_child_info(component: Component) -> None
```

Copy and settings info from child component into parent.

Parent components can access child cells settings.

<a id="gdsfactory.component.ComponentBase.write_gds"></a>

#### write\_gds

```python
def write_gds(gdspath: "PathType | None" = None,
              gdsdir: "PathType | None" = None,
              save_options: "kdb.SaveLayoutOptions | None" = None,
              with_metadata: bool = True) -> pathlib.Path
```

Write component to GDS and returns gdspath.

**Arguments**:

- `gdspath` - GDS file path to write to.
- `gdsdir` - directory for the GDS file. Defaults to /tmp/randomFile/gdsfactory.
- `save_options` - klayout save options.
- `with_metadata` - if True, writes metadata (ports, settings) to the GDS file.

<a id="gdsfactory.component.ComponentBase.pprint_ports"></a>

#### pprint\_ports

```python
def pprint_ports(**kwargs: Any) -> None
```

Pretty prints ports.

**Arguments**:

- `kwargs` - keyword arguments to filter ports.
  

**Arguments**:

- `layer` - select ports with GDS layer.
- `prefix` - select ports with prefix in port name.
- `suffix` - select ports with port name suffix.
- `orientation` - select ports with orientation in degrees.
- `orientation` - select ports with orientation in degrees.
- `width` - select ports with port width.
- `layers_excluded` - List of layers to exclude.
- `port_type` - select ports with port_type (optical, electrical, vertical_te).
- `clockwise` - if True, sort ports clockwise, False: counter-clockwise.

<a id="gdsfactory.component.ComponentBase.write_netlist"></a>

#### write\_netlist

```python
def write_netlist(netlist: dict[str, Any],
                  filepath: str | pathlib.Path | None = None) -> str
```

Returns netlist as YAML string.

**Arguments**:

- `netlist` - netlist to write.
- `filepath` - Optional file path to write to.

<a id="gdsfactory.component.ComponentBase.to_dict"></a>

#### to\_dict

```python
def to_dict(with_ports: bool = False) -> dict[str, Any]
```

Returns a dictionary representation of the Component.

<a id="gdsfactory.component.Component"></a>

## Component Objects

```python
class Component(ComponentBase, kf.DKCell)
```

Canvas where you add polygons, instances and ports.

- stores settings that you use to build the component
- stores info that you want to use
- can return ports by type (optical, electrical ...)
- can return netlist for circuit simulation
- can write to GDS, OASIS
- can show in KLayout, matplotlib or 3D

Properties:
    info: dictionary that includes derived properties, simulation_settings, settings (test_protocol, docs, ...)

<a id="gdsfactory.component.Component.absorb"></a>

#### absorb

```python
def absorb(reference: ComponentReference) -> Self
```

Absorbs polygons from ComponentReference into Component.

Destroys the reference in the process but keeping the polygon geometry.

**Arguments**:

- `reference` - Instance to be absorbed into the Component.

<a id="gdsfactory.component.Component.trim"></a>

#### trim

```python
def trim(left: float,
         bottom: float,
         right: float,
         top: float,
         flatten: bool = False) -> None
```

Trims the Component to a bounding box.

**Arguments**:

- `left` - left coordinate of the bounding box.
- `bottom` - bottom coordinate of the bounding box.
- `right` - right coordinate of the bounding box.
- `top` - top coordinate of the bounding box.
- `flatten` - if True, flattens the Component.

<a id="gdsfactory.component.Component.add_ref"></a>

#### add\_ref

```python
def add_ref(component: Component,
            name: str | None = None,
            columns: int = 1,
            rows: int = 1,
            column_pitch: float = 0.0,
            row_pitch: float = 0.0) -> ComponentReference
```

Adds a component instance reference to a Component.

**Arguments**:

- `component` - The referenced component.
- `name` - Name of the reference.
- `columns` - Number of columns in the array.
- `rows` - Number of rows in the array.
- `column_pitch` - column pitch.
- `row_pitch` - row pitch.

<a id="gdsfactory.component.Component.get_paths"></a>

#### get\_paths

```python
def get_paths(layer: "LayerSpec",
              recursive: bool = True) -> list[kf.kdb.DPath]
```

Returns a list of paths.

**Arguments**:

- `layer` - layer to get paths from.
- `recursive` - if True, gets paths recursively.

<a id="gdsfactory.component.Component.get_boxes"></a>

#### get\_boxes

```python
def get_boxes(layer: "LayerSpec", recursive: bool = True) -> list[kf.kdb.DBox]
```

Returns a list of boxes.

**Arguments**:

- `layer` - layer to get boxes from.
- `recursive` - if True, gets boxes recursively.

<a id="gdsfactory.component.Component.get_labels"></a>

#### get\_labels

```python
def get_labels(layer: "LayerSpec",
               recursive: bool = True) -> list[kf.kdb.DText]
```

Returns a list of labels from the Component.

**Arguments**:

- `layer` - layer to get labels from.
- `recursive` - if True, gets labels recursively.

<a id="gdsfactory.component.Component.area"></a>

#### area

```python
def area(layer: "LayerSpec") -> float
```

Returns the area of the Component in um2.

<a id="gdsfactory.component.Component.get_polygons"></a>

#### get\_polygons

```python
def get_polygons(
    merge: bool = False,
    by: Literal["index", "name", "tuple"] = "index",
    layers: "LayerSpecs | None" = None,
    smooth: float | None = None
) -> dict[tuple[int, int] | str | int, list[kf.kdb.Polygon]]
```

Returns a dict of Polygons per layer.

**Arguments**:

- `merge` - if True, merges the polygons.
- `by` - the format of the resulting keys in the dictionary ('index', 'name', 'tuple')
- `layers` - list of layers to get polygons from. Defaults to all layers.
- `smooth` - if True, smooths the polygons.

<a id="gdsfactory.component.Component.get_region"></a>

#### get\_region

```python
def get_region(layer: "LayerSpec",
               merge: bool = False,
               smooth: float | None = None) -> kdb.Region
```

Returns a Region of the Component.

Note that all operations that you do with the Region will be done in the database units.

Where for most processes 1 dbu = 1 nm.

**Arguments**:

- `layer` - layer to get region from.
- `merge` - if True, merges the region.
- `smooth` - if True, smooths the region by the specified amount (in um).

<a id="gdsfactory.component.Component.get_polygons_points"></a>

#### get\_polygons\_points

```python
def get_polygons_points(
    merge: bool = False,
    scale: float | None = None,
    by: Literal["index", "name", "tuple"] = "index",
    layers: "LayerSpecs | None" = None
) -> dict[int | str | tuple[int, int], list[npt.NDArray[np.floating[Any]]]]
```

Returns a dict with list of points per layer.

**Arguments**:

- `merge` - if True, merges the polygons.
- `scale` - if True, scales the points.
- `by` - the format of the resulting keys in the dictionary ('index', 'name', 'tuple')
- `layers` - list of layers to get polygons from. Defaults to all layers.

<a id="gdsfactory.component.Component.extract"></a>

#### extract

```python
def extract(layers: "LayerSpecs", recursive: bool = True) -> Component
```

Extracts a list of layers and adds them to a new Component.

**Arguments**:

- `layers` - list of layers to extract.
- `recursive` - if True, extracts layers recursively and returns a flattened Component.

<a id="gdsfactory.component.Component.copy_layers"></a>

#### copy\_layers

```python
def copy_layers(layer_map: "dict[LayerSpec, LayerSpec]",
                recursive: bool = False) -> Self
```

Remaps a list of layers and returns the same Component.

**Arguments**:

- `layer_map` - dictionary of layers to copy.
- `recursive` - if True, remaps layers recursively.

<a id="gdsfactory.component.Component.remove_layers"></a>

#### remove\_layers

```python
def remove_layers(layers: "LayerSpecs", recursive: bool = True) -> Self
```

Removes a list of layers and returns the same Component.

**Arguments**:

- `layers` - list of layers to remove.
- `recursive` - if True, removes layers recursively.

<a id="gdsfactory.component.Component.remap_layers"></a>

#### remap\_layers

```python
def remap_layers(layer_map: "dict[LayerSpec, LayerSpec]",
                 recursive: bool = False) -> Self
```

Remaps a list of layers and returns the same Component.

**Arguments**:

- `layer_map` - dictionary of layers to remap.
- `recursive` - if True, remaps layers recursively.

<a id="gdsfactory.component.Component.to_3d"></a>

#### to\_3d

```python
def to_3d(layer_views: "LayerViews | None" = None,
          layer_stack: "LayerStack | None" = None,
          exclude_layers: "Sequence[Layer] | None " = None) -> Scene
```

Return Component 3D trimesh Scene.

**Arguments**:

- `component` - to extrude in 3D.
- `layer_views` - layer colors from Klayout Layer Properties file.
  Defaults to active PDK.layer_views.
- `layer_stack` - contains thickness and zmin for each layer.
  Defaults to active PDK.layer_stack.
- `exclude_layers` - layers to exclude.

<a id="gdsfactory.component.Component.over_under"></a>

#### over\_under

```python
def over_under(layer: "LayerSpec",
               distance: float = 0.001,
               remove_old_layer: bool = True) -> None
```

Returns a Component over-under on a layer in the Component.

For big components use tiled version.

**Arguments**:

- `layer` - layer to perform over-under on.
- `distance` - distance to perform over-under in um.
- `remove_old_layer` - if True, removes the old layer.

<a id="gdsfactory.component.Component.offset"></a>

#### offset

```python
def offset(layer: "LayerSpec", distance: float) -> None
```

Offsets a Component layer by a distance in um.

**Arguments**:

- `layer` - layer to offset the Component on.
- `distance` - distance to offset the Component in um.

<a id="gdsfactory.component.Component.add_polygon"></a>

#### add\_polygon

```python
def add_polygon(points: _PolygonPoints,
                layer: "LayerSpec") -> kdb.Shape | None
```

Adds a Polygon to the Component and returns a klayout Shape.

**Arguments**:

- `points` - Coordinates of the vertices of the Polygon.
- `layer` - layer spec to add polygon on.

<a id="gdsfactory.component.Component.plot"></a>

#### plot

```python
def plot(lyrdb: pathlib.Path | str | None = None,
         display_type: Literal["image", "widget"] | None = None,
         *,
         show_labels: bool = True,
         show_ruler: bool = True,
         return_fig: bool = False) -> Figure | None
```

Plots the Component using klayout.

**Arguments**:

- `lyrdb` - path to layer properties file.
- `display_type` - if "image", displays the image.
- `show_labels` - if True, shows labels.
- `show_ruler` - if True, shows ruler.
- `return_fig` - if True, returns the figure.

<a id="gdsfactory.component.Component.get_netlist"></a>

#### get\_netlist

```python
def get_netlist(recursive: bool = False, **kwargs: Any) -> dict[str, Any]
```

Returns a place-aware netlist for circuit simulation.

It includes not only the connectivity information (nodes and connections) but also the specific placement coordinates for each component or cell in the layout.

**Arguments**:

- `recursive` - if True, returns a recursive netlist.
- `kwargs` - keyword arguments to get_netlist.

<a id="gdsfactory.component.Component.plot_netlist"></a>

#### plot\_netlist

```python
def plot_netlist(recursive: bool = False,
                 with_labels: bool = True,
                 font_weight: str = "normal",
                 **kwargs: Any) -> nx.Graph
```

Plots a netlist graph with networkx.

**Arguments**:

- `recursive` - if True, returns a recursive netlist.
- `with_labels` - add label to each node.
- `font_weight` - normal, bold.
- `kwargs` - keyword arguments to get_netlist.
  

**Arguments**:

- `tolerance` - tolerance in grid_factor to consider two ports connected.
- `exclude_port_types` - optional list of port types to exclude from netlisting.
- `get_instance_name` - function to get instance name.
- `allow_multiple` - False to raise an error if more than two ports share the same connection.                     if True, will return key: [value] pairs with [value] a list of all connected instances.

<a id="gdsfactory.component.Component.plot_netlist_graphviz"></a>

#### plot\_netlist\_graphviz

```python
def plot_netlist_graphviz(recursive: bool = False,
                          interactive: bool = False,
                          splines: str = "ortho") -> None
```

Plots a netlist graph with graphviz.

**Arguments**:

- `recursive` - if True, returns a recursive netlist.
- `interactive` - if True, opens the graph in a browser.
- `splines` - ortho, spline, polyline, line, curved.

<a id="gdsfactory.component.Component.to_graphviz"></a>

#### to\_graphviz

```python
def to_graphviz(recursive: bool = False) -> Digraph
```

Returns a netlist graph with graphviz.

**Arguments**:

- `recursive` - if True, returns a recursive netlist.

<a id="gdsfactory.component.ComponentAllAngle"></a>

## ComponentAllAngle Objects

```python
class ComponentAllAngle(ComponentBase, kf.VKCell)
```

<a id="gdsfactory.component.ComponentAllAngle.plot"></a>

#### plot

```python
def plot(**kwargs: Any) -> None
```

Plots the Component using klayout.

<a id="gdsfactory.component.ComponentAllAngle.dup"></a>

#### dup

```python
def dup(new_name: str | None = None) -> Self
```

Copy the full cell.

<a id="gdsfactory.component.ComponentAllAngle.add_polygon"></a>

#### add\_polygon

```python
def add_polygon(points: _PolygonPoints, layer: "LayerSpec") -> None
```

Adds a Polygon to the Component and returns a klayout Shape.

**Arguments**:

- `points` - Coordinates of the vertices of the Polygon.
- `layer` - layer spec to add polygon on.

<a id="gdsfactory.component.ComponentAllAngle.get_polygons"></a>

#### get\_polygons

```python
def get_polygons(layer: "LayerSpec") -> list[kf.kdb.DPolygon]
```

Returns a list of polygons from the Component.

<a id="gdsfactory.component.container"></a>

#### container

```python
def container(component: ComponentSpec,
              function: Callable[..., Any] | None = None,
              **kwargs: Any) -> Component
```

Returns new component with a component reference.

**Arguments**:

- `component` - to add to container.
- `function` - function to apply to component.
- `kwargs` - keyword arguments to pass to function.

<a id="gdsfactory.component_layout"></a>

# gdsfactory.component\_layout

Helper functions for layout.

Adapted from PHIDL https://github.com/amccaugh/phidl/ by Adam McCaughan

<a id="gdsfactory.component_layout.pprint_ports"></a>

#### pprint\_ports

```python
def pprint_ports(ports: Sequence[gf.Port]) -> None
```

Prints ports in a rich table.

<a id="gdsfactory.component_layout.rotate_points"></a>

#### rotate\_points

```python
def rotate_points(
    points: npt.NDArray[np.floating[Any]],
    angle: float = 45,
    center: Coordinate = (0, 0)
) -> npt.NDArray[np.floating[Any]]
```

Rotates points around a centerpoint defined by ``center``.

``points`` may be input as either single points [1,2] or array-like[N][2],
and will return in kind.

**Arguments**:

  points : array-like[N][2]
  Coordinates of the element to be rotated.
  angle : int or float
  Angle to rotate the points.
  center : array-like[2]
  Centerpoint of rotation.
  

**Returns**:

  A new set of points that are rotated around ``center``.

<a id="gdsfactory.component_layout.reflect_points"></a>

#### reflect\_points

```python
def reflect_points(
    points: npt.NDArray[np.floating[Any]],
    p1: Coordinate = (0, 0),
    p2: Coordinate = (1, 0)
) -> npt.NDArray[np.floating[Any]]
```

Reflects points across the line formed by p1 and p2.

from https://github.com/amccaugh/phidl/pull/181

``points`` may be input as either single points [1,2] or array-like[N][2],
and will return in kind.

**Arguments**:

  points : array-like[N][2]
  Coordinates of the element to be reflected.
  p1 : array-like[2]
  Coordinates of the start of the reflecting line.
  p2 : array-like[2]
  Coordinates of the end of the reflecting line.
  

**Returns**:

  A new set of points that are reflected across ``p1`` and ``p2``.

<a id="gdsfactory.component_layout.parse_coordinate"></a>

#### parse\_coordinate

```python
def parse_coordinate(
        c: Coordinate | Port | npt.NDArray[np.floating[Any]]) -> Coordinate
```

Translates various inputs (lists, tuples, Ports) to an (x,y) coordinate.

**Arguments**:

- `c` - array-like[N] or Port
  Input to translate into a coordinate.
  

**Returns**:

  c : array-like[2]
  Parsed coordinate.

<a id="gdsfactory.component_layout.parse_move"></a>

#### parse\_move

```python
def parse_move(origin: Coordinate | npt.NDArray[np.floating[Any]],
               destination: Coordinate | npt.NDArray[np.floating[Any]] | None,
               axis: Axis | None = None) -> tuple[float, float]
```

Translates input coordinates to changes in position in the x and y directions.

**Arguments**:

  origin : array-like[2] of int or float, Port, or key
  Origin point of the move.
  destination : array-like[2] of int or float, Port, key, or None
  Destination point of the move.
  axis : {'x', 'y'} Direction of move.
  

**Returns**:

  dx : int or float
  Change in position in the x-direction.
  dy : int or float
  Change in position in the y-direction.

<a id="gdsfactory.containers"></a>

# gdsfactory.containers

Containers are components that contain other components.

<a id="gdsfactory.constants"></a>

# gdsfactory.constants

<a id="gdsfactory.symbols"></a>

# gdsfactory.symbols

<a id="gdsfactory.symbols.symbol_from_cell"></a>

#### symbol\_from\_cell

```python
def symbol_from_cell(func: _F, to_symbol: ToSymbol) -> _F
```

Creates a symbol function from a component function.

**Arguments**:

- `func` - the cell function
- `to_symbol` - the function that transforms the output of the cell function into a symbol
  

**Returns**:

  a symbol function

<a id="gdsfactory.symbols.floorplan_with_block_letters"></a>

#### floorplan\_with\_block\_letters

```python
@symbol
def floorplan_with_block_letters(
    component: Component,
    copy_layers: LayerSpecs = ("WG", ),
    text_layer: LayerSpec = (2, 0),
    bbox_layer: LayerSpec = (90, 0)
) -> Component
```

Returns symbol.

Keeps same floorplan as component layout, function name         and optionally shapes on layers copied from the original layout.

**Arguments**:

- `component` - the layout component.
- `copy_layers` - if specified, copies layers from the layout into the symbol.
- `text_layer` - the layer for the text.
- `bbox_layer` - the layer for the bounding box.
  

**Returns**:

  A component representing the symbol.

<a id="gdsfactory.schematic"></a>

# gdsfactory.schematic

<a id="gdsfactory.schematic.OrthogonalGridArray"></a>

## OrthogonalGridArray Objects

```python
class OrthogonalGridArray(BaseModel)
```

Orthogonal grid array config.

**Arguments**:

- `columns` - number of columns.
- `rows` - number of rows.
- `column_pitch` - column pitch.
- `row_pitch` - row pitch.

<a id="gdsfactory.schematic.GridArray"></a>

## GridArray Objects

```python
class GridArray(BaseModel)
```

Non-orthogonal grid array config.

**Arguments**:

- `num_a` - number of elements in the a-dimension.
- `num_b` - number of elements in the b-dimension.
- `pitch_a` - x-y pitch in the a-dimension.
- `pitch_b` - x-y pitch in the b-dimension.

<a id="gdsfactory.schematic.Instance"></a>

## Instance Objects

```python
class Instance(BaseModel)
```

Instance of a component.

**Arguments**:

- `component` - component name.
- `settings` - input variables.
- `info` - information (polarization, wavelength ...).
- `array` - array config to make create an array reference for this instance

<a id="gdsfactory.schematic.Instance.update_settings_and_info"></a>

#### update\_settings\_and\_info

```python
@model_validator(mode="before")
@classmethod
def update_settings_and_info(cls, values: dict[str, Any]) -> dict[str, Any]
```

Validator to update component, settings and info based on the component.

<a id="gdsfactory.schematic.Placement"></a>

## Placement Objects

```python
class Placement(BaseModel)
```

<a id="gdsfactory.schematic.Placement.__getitem__"></a>

#### \_\_getitem\_\_

```python
def __getitem__(key: str) -> Any
```

Allows to access the placement attributes as a dictionary.

<a id="gdsfactory.schematic.Net"></a>

## Net Objects

```python
class Net(BaseModel)
```

Net between two ports.

**Arguments**:

- `p1` - instance_name,port 1.
- `p2` - instance_name,port 2.
- `name` - route name.

<a id="gdsfactory.schematic.Net.__init__"></a>

#### \_\_init\_\_

```python
def __init__(**data: Any) -> None
```

Initialize the net.

<a id="gdsfactory.schematic.Netlist"></a>

## Netlist Objects

```python
class Netlist(BaseModel)
```

Netlist defined component.

**Arguments**:

- `instances` - dict of instances (name, settings, component).
- `placements` - dict of placements.
- `connections` - dict of connections.
- `routes` - dict of routes.
- `name` - component name.
- `info` - information (polarization, wavelength ...).
- `ports` - exposed component ports.
- `settings` - input variables.
- `nets` - list of nets.
- `warnings` - warnings.

<a id="gdsfactory.schematic.to_yaml_graph_networkx"></a>

#### to\_yaml\_graph\_networkx

```python
def to_yaml_graph_networkx(
    netlist: Netlist, nets: list[Net]
) -> tuple[nx.Graph, dict[str, str], dict[str, tuple[float, float]]]
```

Generates a netlist graph using NetworkX.

<a id="gdsfactory.schematic.to_graphviz"></a>

#### to\_graphviz

```python
def to_graphviz(instances: dict[str, Instance],
                placements: dict[str, Placement],
                nets: list[Net],
                show_ports: bool = True) -> Digraph
```

Generates a netlist graph using Graphviz.

<a id="gdsfactory.schematic.Link"></a>

## Link Objects

```python
class Link(BaseModel)
```

Link between instances.

**Arguments**:

- `instance1` - instance name 1.
- `instance2` - instance name 2.
- `port1` - port name 1.
- `port2` - port name 2.

<a id="gdsfactory.schematic.Schematic"></a>

## Schematic Objects

```python
class Schematic(BaseModel)
```

Schematic.

<a id="gdsfactory.schematic.Schematic.add_placement"></a>

#### add\_placement

```python
def add_placement(instance_name: str, placement: Placement) -> None
```

Add placement to the netlist.

**Arguments**:

- `instance_name` - instance name.
- `placement` - placement.

<a id="gdsfactory.schematic.Schematic.add_net"></a>

#### add\_net

```python
def add_net(net: Net) -> None
```

Add a net between two ports.

<a id="gdsfactory.schematic.Schematic.to_graphviz"></a>

#### to\_graphviz

```python
def to_graphviz(show_ports: bool = True) -> Digraph
```

Generates a netlist graph using Graphviz.

**Arguments**:

- `show_ports` - whether to show ports or not.

<a id="gdsfactory.schematic.Schematic.plot_graphviz"></a>

#### plot\_graphviz

```python
def plot_graphviz(interactive: bool = False, splines: str = "ortho") -> None
```

Plots the netlist graph (Automatic fallback to networkx).

**Arguments**:

- `interactive` - whether to plot the graph interactively or not.
- `splines` - type of splines to use for the graph.

<a id="gdsfactory.schematic.Schematic.write_netlist"></a>

#### write\_netlist

```python
def write_netlist(netlist: dict[str, Any],
                  filepath: str | pathlib.Path | None = None) -> str
```

Returns netlist as YAML string.

**Arguments**:

- `netlist` - netlist to write.
- `filepath` - Optional file path to write to.

<a id="gdsfactory.schematic.plot_graphviz"></a>

#### plot\_graphviz

```python
def plot_graphviz(graph: Digraph,
                  interactive: bool = False,
                  splines: str = "ortho") -> None
```

Plots the netlist graph (Automatic fallback to networkx).

<a id="gdsfactory.port"></a>

# gdsfactory.port

We use Ports to connect Components with other Components.

we follow start from the bottom left and name the ports counter-clock-wise

.. code::

         3   4
         |___|_
     2 -|      |- 5
        |      |
     1 -|______|- 6
         |   |
         8   7

You can also rename them with W,E,S,N prefix (west, east, south, north).

    .. code::

             N0  N1
             |___|_
        W1 -|      |- E1
            |      |
        W0 -|______|- E0
             |   |
            S0   S1

Adapted from PHIDL https://github.com/amccaugh/phidl/ by Adam McCaughan

<a id="gdsfactory.port.pprint_ports"></a>

#### pprint\_ports

```python
def pprint_ports(ports: Ports) -> None
```

Prints ports in a rich table.

<a id="gdsfactory.port.to_dict"></a>

#### to\_dict

```python
def to_dict(port: kf.port.ProtoPort[Any]) -> dict[str, Any]
```

Returns dict.

<a id="gdsfactory.port.port_array"></a>

#### port\_array

```python
def port_array(center: tuple[float, float] = (0.0, 0.0),
               width: float = 0.5,
               orientation: AngleInDegrees = 0,
               pitch: tuple[float, float] = (10.0, 0.0),
               n: int = 2,
               **kwargs: Unpack[PortKwargs]) -> list[Port]
```

Returns a list of ports placed in an array.

**Arguments**:

- `center` - center point of the port.
- `width` - port width.
- `orientation` - angle in degrees.
- `pitch` - period of the port array.
- `n` - number of ports in the array.
- `kwargs` - additional arguments.

<a id="gdsfactory.port.read_port_markers"></a>

#### read\_port\_markers

```python
def read_port_markers(
    component: Component, layers: LayerSpecs = ("PORT", )) -> Component
```

Returns extracted polygons from component layers.

**Arguments**:

- `component` - Component to extract markers.
- `layers` - GDS layer specs.

<a id="gdsfactory.port.csv2port"></a>

#### csv2port

```python
def csv2port(csvpath: PathType) -> dict[str, list[str]]
```

Reads ports from a CSV file and returns a Dict.

<a id="gdsfactory.port.sort_ports_clockwise"></a>

#### sort\_ports\_clockwise

```python
def sort_ports_clockwise(ports: Sequence[TPort]) -> list[TPort]
```

Sort and return ports in the clockwise direction.

.. code::

        3   4
        |___|_
    2 -|      |- 5
       |      |
    1 -|______|- 6
        |   |
        8   7

<a id="gdsfactory.port.sort_ports_counter_clockwise"></a>

#### sort\_ports\_counter\_clockwise

```python
def sort_ports_counter_clockwise(ports: Sequence[TPort]) -> list[TPort]
```

Sort and return ports in the counter-clockwise direction.

.. code::

        4   3
        |___|_
    5 -|      |- 2
       |      |
    6 -|______|- 1
        |   |
        7   8

<a id="gdsfactory.port.select_ports"></a>

#### select\_ports

```python
def select_ports(ports: Ports | ComponentReference,
                 layer: LayerSpec | None = None,
                 prefix: str | None = None,
                 suffix: str | None = None,
                 orientation: AngleInDegrees | None = None,
                 width: float | None = None,
                 layers_excluded: Sequence[tuple[int, int]] | None = None,
                 port_type: str | None = None,
                 names: Sequence[str] | None = None,
                 clockwise: bool = True,
                 sort_ports: bool = False) -> list[typings.Port]
```

Returns a list of ports from a list of ports.

**Arguments**:

- `ports` - port list.
- `layer` - select ports with port GDS layer.
- `prefix` - select ports with port name prefix.
- `suffix` - select ports with port name suffix.
- `orientation` - select ports with orientation in degrees.
- `width` - select ports with port width.
- `layers_excluded` - List of layers to exclude.
- `port_type` - select ports with port type (optical, electrical, vertical_te).
- `names` - select ports with port names.
- `clockwise` - if True, sort ports clockwise, False: counter-clockwise.
- `sort_ports` - if True, sort ports.
  

**Returns**:

  List containing the selected ports.

<a id="gdsfactory.port.rename_ports_by_orientation"></a>

#### rename\_ports\_by\_orientation

```python
def rename_ports_by_orientation(component: Component,
                                layers_excluded: LayerSpecs | None = None,
                                select_ports: SelectPorts = select_ports,
                                function: Callable[
                                    ..., None] = _rename_ports_facing_side,
                                prefix: str = "o",
                                **kwargs: Any) -> Component
```

Returns Component with port names based on port orientation (E, N, W, S).

**Arguments**:

- `component` - to rename ports.
- `layers_excluded` - to exclude.
- `select_ports` - function to select_ports.
- `function` - to rename ports.
- `prefix` - to add on each port name.
- `kwargs` - select_ports settings.
  
  .. code::
  
  N0  N1
  |___|_
  W1 -|      |- E1
  |      |
  W0 -|______|- E0
  |   |
  S0   S1

<a id="gdsfactory.port.auto_rename_ports"></a>

#### auto\_rename\_ports

```python
def auto_rename_ports(component: Component,
                      function: Callable[..., None] = _rename_ports_clockwise,
                      select_ports_optical: Callable[..., list[typings.Port]]
                      | None = select_ports_optical,
                      select_ports_electrical: Callable[...,
                                                        list[typings.Port]]
                      | None = select_ports_electrical,
                      select_ports_placement: Callable[..., list[typings.Port]]
                      | None = select_ports_placement,
                      prefix: str = "",
                      prefix_optical: str = "o",
                      prefix_electrical: str = "e",
                      prefix_placement: str = "p",
                      port_type: str | None = None,
                      **kwargs: Any) -> Component
```

Adds prefix for optical and electrical.

**Arguments**:

- `component` - to auto_rename_ports.
- `function` - to rename ports.
- `select_ports_optical` - to select optical ports.
- `select_ports_electrical` - to select electrical ports.
- `select_ports_placement` - to select placement ports.
- `prefix_optical` - prefix of optical ports.
- `prefix_electrical` - prefix of electrical ports.
- `prefix_placement` - prefix of electrical ports.
- `port_type` - select ports with port type (optical, electrical, vertical_te).
- `kwargs` - select_ports settings.
  

**Arguments**:

- `prefix` - select ports with port name prefix.
- `suffix` - select ports with port name suffix.
- `orientation` - select ports with orientation in degrees.
- `width` - select ports with port width.
- `layers_excluded` - List of layers to exclude.
- `clockwise` - if True, sort ports clockwise, False: counter-clockwise.

<a id="gdsfactory.port.map_ports_layer_to_orientation"></a>

#### map\_ports\_layer\_to\_orientation

```python
def map_ports_layer_to_orientation(ports: "PortDict",
                                   function: Callable[
                                       ..., None] = _rename_ports_facing_side,
                                   **kwargs: Any) -> dict[str, str]
```

Returns dict of port name to port name original.

**Arguments**:

- `ports` - dict of ports.
- `function` - to rename ports.
- `kwargs` - for the function to rename ports.
  
  .. code::
  
  N0  N1
  |___|_
  W1 -|      |- E1
  |      |
  W0 -|______|- E0
  |   |
  S0   S1

<a id="gdsfactory.port.map_ports_to_orientation_cw"></a>

#### map\_ports\_to\_orientation\_cw

```python
def map_ports_to_orientation_cw(ports: PortDict,
                                function: Callable[
                                    ..., None] = _rename_ports_facing_side,
                                **kwargs: Any) -> dict[str, str]
```

Returns component or reference port mapping clockwise.

**Arguments**:

- `ports` - dict of ports.
- `function` - to rename ports.
- `kwargs` - for the function to rename ports.
  
  
  .. code::
  
  N0  N1
  |___|_
  W1 -|      |- E1
  |      |
  W0 -|______|- E0
  |   |
  S0   S1

<a id="gdsfactory.port.auto_rename_ports_layer_orientation"></a>

#### auto\_rename\_ports\_layer\_orientation

```python
def auto_rename_ports_layer_orientation(
        component: Component,
        function: Callable[..., None] = _rename_ports_facing_side) -> None
```

Renames port names with layer_orientation  (1_0_W0).

port orientation (E, N, W, S) numbering is clockwise

.. code::

         N0  N1
         |___|_
    W1 -|      |- E1
        |      |
    W0 -|______|- E0
         |   |
        S0   S1

<a id="gdsfactory.labels.add_labels"></a>

# gdsfactory.labels.add\_labels

<a id="gdsfactory.labels.add_labels.add_port_labels"></a>

#### add\_port\_labels

```python
def add_port_labels(component: gf.Component,
                    ports: Ports,
                    layer: LayerSpec,
                    texts: Sequence[str] | None = None) -> gf.Component
```

Add port labels to a component.

**Arguments**:

- `component` - to add the labels.
- `ports` - list of ports to add the labels.
- `layer` - layer to add the labels.
- `texts` - text to add to the labels. Defaults to port names.

<a id="gdsfactory.labels"></a>

# gdsfactory.labels

<a id="gdsfactory.labels.ehva"></a>

# gdsfactory.labels.ehva

<a id="gdsfactory.labels.ehva.add_label_ehva"></a>

#### add\_label\_ehva

```python
def add_label_ehva(
        component: gf.Component,
        die: str = "demo",
        prefix_to_type: dict[str, str] = prefix_to_type_default,
        layer: Layer = (66, 0),
        metadata_ignore: list[str] | None = None,
        metadata_include_parent: list[str] | None = None,
        metadata_include_child: list[str] | None = None) -> gf.Component
```

Returns Component with measurement labels.

**Arguments**:

- `component` - to add labels to.
- `die` - string.
- `prefix_to_type` - dict of port prefix to port type.
- `layer` - text label layer.
- `metadata_ignore` - list of settings keys to ignore. Works with flatdict setting:subsetting.
- `metadata_include_parent` - includes parent metadata. Works with flatdict setting:subsetting.
- `metadata_include_child` - includes child metadata.

<a id="gdsfactory.labels.add_label_yaml"></a>

# gdsfactory.labels.add\_label\_yaml

Add label YAML.

<a id="gdsfactory.labels.add_label_yaml.add_label_yaml"></a>

#### add\_label\_yaml

```python
def add_label_yaml(component: gf.Component,
                   layer: LayerSpec = "TEXT",
                   measurement: str | None = None,
                   measurement_settings: dict[str, Any] | None = None,
                   analysis: str | None = None,
                   analysis_settings: dict[str, Any] | None = None,
                   doe: str | None = None,
                   with_yaml_format: bool = True,
                   anchor: str = "sw") -> gf.Component
```

Returns Component with measurement label.

**Arguments**:

- `component` - to add labels to.
- `layer` - text label layer.
- `measurement` - measurement config name. Defaults to component['info']['measurement'].
- `measurement_settings` - measurement settings. Defaults to component['info']['measurement_settings'].
- `analysis` - analysis name. Defaults to component['info']['analysis'].
- `analysis_settings` - Extra analysis settings. Defaults to component settings.
- `doe` - Design of Experiment name. Defaults to component['info']['doe'].
- `with_yaml_format` - whether to use yaml or json format.
- `anchor` - anchor point for the label. Defaults to south-west "sw".             Valid options are: "n", "s", "e", "w", "ne", "nw", "se", "sw", "c".

<a id="gdsfactory.labels.write_labels"></a>

# gdsfactory.labels.write\_labels

Find GDS labels and write them to a CSV file.

<a id="gdsfactory.labels.write_labels.find_labels"></a>

#### find\_labels

```python
def find_labels(
    gdspath: PathType,
    layer_label: LayerSpec = (66, 0),
    prefixes: Iterable[str] = ("opt-", "elec-")
) -> Iterator[tuple[str, float, float, float]]
```

Return text label and locations iterator from a GDS file.

Klayout does not support label rotations.

**Arguments**:

- `gdspath` - for the gds.
- `layer_label` - for the labels.
- `prefixes` - prefixes to extract labels.
  

**Returns**:

- `string` - for the label.
- `x` - x position (um).
- `y` - y position (um).
- `angle` - in degrees.

<a id="gdsfactory.labels.write_labels.write_labels"></a>

#### write\_labels

```python
def write_labels(
    gdspath: PathType,
    layer_label: LayerSpec = (66, 0),
    filepath: PathType | None = None,
    prefixes: Iterable[str] = ("opt-", "elec-")
) -> Path
```

Load GDS and extracts labels in KLayout text and coordinates.

Returns CSV filepath with each row:
- Text
- x
- y
- rotation (degrees)

**Arguments**:

- `gdspath` - for the mask.
- `layer_label` - for labels to write.
- `filepath` - for CSV file. Defaults to gdspath with CSV suffix.
- `prefixes` - prefixes to extract labels.

<a id="gdsfactory.labels.write_test_manifest"></a>

# gdsfactory.labels.write\_test\_manifest

Converts CSV of test site labels into a CSV test manifest.

<a id="gdsfactory.labels.write_test_manifest.write_test_manifest"></a>

#### write\_test\_manifest

```python
def write_test_manifest(component: gf.Component,
                        csvpath: str | pathlib.Path,
                        search_strings: Iterable[str] | None = None,
                        parameters: Sequence[str] = (
                            "doe",
                            "analysis",
                            "analysis_parameters",
                            "measurement",
                            "measurement_parameters",
                            "ports_optical",
                            "ports_electrical",
                        ),
                        warn_if_missing: bool = True) -> None
```

Converts CSV of test site labels into a CSV test manifest.

It only includes cells that have a "doe" key in their info dictionary.

**Arguments**:

- `component` - the component to write the test manifest for.
- `csvpath` - the path to the CSV file to write.
- `search_strings` - the search_strings of the cells to include in the test manifest.
  If None, all cells one level below top cell are included.
- `parameters` - the parameters to include in the test manifest as columns.
- `warn_if_missing` - if True, warn if a parameter is missing from a cell's info dictionary.

<a id="gdsfactory.utils"></a>

# gdsfactory.utils

<a id="gdsfactory.pack"></a>

# gdsfactory.pack

pack a list of components into as few components as possible.

Adapted from PHIDL https://github.com/amccaugh/phidl/ by Adam McCaughan

<a id="gdsfactory.pack.pack"></a>

#### pack

```python
def pack(component_list: Sequence[ComponentSpec],
         spacing: float = 10.0,
         aspect_ratio: Float2 = (1.0, 1.0),
         max_size: tuple[float | None, float | None] = (None, None),
         sort_by_area: bool = True,
         density: float = 1.1,
         precision: float = 1e-2,
         text: TextFunction | None = None,
         text_prefix: str = "",
         text_mirror: bool = False,
         text_rotation: int = 0,
         text_offsets: tuple[Float2, ...] = ((0, 0), ),
         text_anchors: tuple[Anchor, ...] = ("cc", ),
         name_prefix: str | None = None,
         rotation: int = 0,
         h_mirror: bool = False,
         v_mirror: bool = False,
         add_ports_prefix: bool = True,
         add_ports_suffix: bool = False) -> list[Component]
```

Pack a list of components into as few Components as possible.

**Arguments**:

- `component_list` - list or tuple.
- `spacing` - Minimum distance between adjacent shapes.
- `aspect_ratio` - (width, height) ratio of the rectangular bin.
- `max_size` - Limits the size into which the shapes will be packed.
- `sort_by_area` - Pre-sorts the shapes by area.
- `density` - Values closer to 1 pack tighter but require more computation.
- `precision` - Desired precision for rounding vertex coordinates.
- `text` - Optional function to add text labels.
- `text_prefix` - for labels. For example. 'A' will produce 'A1', 'A2', ...
- `text_mirror` - if True mirrors text.
- `text_rotation` - Optional text rotation.
- `text_offsets` - relative to component size info anchor. Defaults to center.
- `text_anchors` - relative to component (ce cw nc ne nw sc se sw center cc).
- `name_prefix` - for each packed component (avoids the Unnamed cells warning).                 Note that the suffix contains a uuid so the name will not be deterministic.
- `rotation` - optional component rotation in degrees.
- `h_mirror` - horizontal mirror in y axis (x, 1) (1, 0). This is the most common.
- `v_mirror` - vertical mirror using x axis (1, y) (0, y).
- `add_ports_prefix` - adds port names with prefix.
- `add_ports_suffix` - adds port names with suffix.
  
  .. plot::
  :include-source:
  
  import gdsfactory as gf
  from functools import partial
  
  components = [gf.components.triangle(x=i) for i in range(1, 10)]
  c = gf.pack(
  components,
  spacing=20.0,
  max_size=(100, 100),
  text=partial(gf.components.text, justify="center"),
  text_prefix="R",
  name_prefix="demo",
  text_anchors=["nc"],
  text_offsets=[(-10, 0)],
  v_mirror=True,
  )
  c[0].plot()

<a id="gdsfactory.watch"></a>

# gdsfactory.watch

FileWatcher based on watchdog. Looks for changes in files with .pic.yml extension.

<a id="gdsfactory.watch.FileWatcher"></a>

## FileWatcher Objects

```python
class FileWatcher(FileSystemEventHandler)
```

Captures *.py or *.pic.yml file change events.

<a id="gdsfactory.watch.FileWatcher.__init__"></a>

#### \_\_init\_\_

```python
def __init__(path: str,
             run_main: bool = False,
             run_cells: bool = True,
             logger: logging.Logger | None = None) -> None
```

Initialize the YAML event handler.

**Arguments**:

- `path` - the path to the directory to watch.
- `run_main` - if True, will execute the main function of the file.
- `run_cells` - if True, will execute the cells of the file.
- `logger` - the logger to use.

<a id="gdsfactory.watch.FileWatcher.update_cell"></a>

#### update\_cell

```python
def update_cell(src_path: PathType, update: bool = False) -> ComponentFactory
```

Parses a YAML file to a cell function and registers into active pdk.

**Arguments**:

- `src_path` - the path to the file
- `update` - if True, will update an existing cell function of the same name without raising an error

**Returns**:

  The cell function parsed from the yaml file.

<a id="gdsfactory.watch.FileWatcher.get_component_yaml"></a>

#### get\_component\_yaml

```python
def get_component_yaml(filepath: PathType, dirpath: PathType) -> Component
```

Parses a YAML file to a cell function and registers into active pdk.

<a id="gdsfactory.watch.watch"></a>

#### watch

```python
def watch(path: PathType | None = cwd,
          pdk: Pdk | str | None = None,
          run_main: bool = True,
          run_cells: bool = True,
          pre_run: bool = False,
          logger: logging.Logger | None = None,
          run_embed: bool = True) -> None
```

Starts the file watcher.

**Arguments**:

- `path` - the path to the directory to watch.
- `pdk` - the name of the PDK to use.
- `run_main` - if True, will execute the main function of the file.
- `run_cells` - if True, will execute the cells of the file.
- `pre_run` - build all cells on startup
- `logger` - the logger to use.
- `run_embed` - if True, will run the embed function.

<a id="gdsfactory.watch.show"></a>

#### show

```python
def show(component: ComponentSpec) -> None
```

Shows a component in klayout.

<a id="gdsfactory.snap"></a>

# gdsfactory.snap

snaps values and coordinates to the GDS grid in nm.

<a id="gdsfactory.snap.snap_to_grid"></a>

#### snap\_to\_grid

```python
def snap_to_grid(
        x: Value,
        nm: int | None = None,
        grid_factor: int = 1) -> npt.NDArray[np.floating[Any]] | float
```

Snap x to grid.

**Arguments**:

- `x` - value to snap.
- `nm` - Optional grid size in nm. If None, it will use the default grid size from PDK multiplied by grid_factor.
- `grid_factor` - snap to grid_factor * grid_size.

<a id="gdsfactory.export.to_gerber"></a>

# gdsfactory.export.to\_gerber

Based on Gerber file spec.

https://www.ucamco.com/files/downloads/file_en/456/gerber-layer-format-specification-revision-2022-02_en.pdf.

**See Also**:

  - https://github.com/opiopan/pcb-tools-extension
  - https://github.com/jamesbowman/cuflow/blob/master/gerber.py

<a id="gdsfactory.export.to_gerber.number"></a>

#### number

```python
def number(n: float) -> str
```

Formats a floating-point number by scaling it to an integer (multiplied by 10,000).

Rounding to the nearest integer, and zero-padding it to 7 characters.

**Arguments**:

- `n` _float_ - The input floating-point number.
  

**Returns**:

- `str` - The formatted string.

<a id="gdsfactory.export.to_gerber.to_gerber"></a>

#### to\_gerber

```python
def to_gerber(
    component: Component,
    dirpath: Path,
    layermap_to_gerber_layer: dict[tuple[int, int], GerberLayer],
    options: GerberOptions = Field(default_factory=GerberOptions)
) -> None
```

Writes each layer to a different Gerber file.

**Arguments**:

- `component` - to export.
- `dirpath` - directory path.
- `layermap_to_gerber_layer` - map of GDS layer to GerberLayer.
- `options` - to save.
- `header` - List[str] | None = None
- `mode` - Literal["mm", "in"] = "mm"
- `resolution` - float = 1e-6
- `int_size` - int = 4

<a id="gdsfactory.export.to_svg"></a>

# gdsfactory.export.to\_svg

<a id="gdsfactory.export.to_svg.to_svg"></a>

#### to\_svg

```python
def to_svg(component: Component,
           layer_views: LayerViews | None = None,
           layer_stack: LayerStack | None = None,
           exclude_layers: LayerSpecs | None = None,
           filename: str = "component.svg",
           scale: float = 1.0) -> None
```

Write a 2D SVG file from a component.

**Arguments**:

- `component` - The component to render.
- `layer_views` - Layer colors from Klayout Layer Properties file.
  Defaults to active `PDK.layer_views`.
- `layer_stack` - Contains thickness and zmin for each layer.
  Defaults to active `PDK.layer_stack`.
- `exclude_layers` - Layers to exclude from the SVG.
- `filename` - Output SVG filename.
- `scale` - Scaling factor for the SVG dimensions.

<a id="gdsfactory.export"></a>

# gdsfactory.export

<a id="gdsfactory.export.to_np"></a>

# gdsfactory.export.to\_np

<a id="gdsfactory.export.to_np.to_np"></a>

#### to\_np

```python
def to_np(component: Component,
          nm_per_pixel: int = 20,
          layers: Layers = ((1, 0), ),
          values: Floats | None = None,
          pad_width: int = 1) -> npt.NDArray[np.float64]
```

Returns a pixelated numpy array from Component polygons.

**Arguments**:

- `component` - Component.
- `nm_per_pixel` - you can go from 20 (coarse) to 4 (fine).
- `layers` - to convert. Order matters (latter overwrite former).
- `values` - associated to each layer (defaults to 1).
- `pad_width` - padding pixels around the image.

<a id="gdsfactory.export.to_3d"></a>

# gdsfactory.export.to\_3d

<a id="gdsfactory.export.to_3d.to_3d"></a>

#### to\_3d

```python
def to_3d(component: Component,
          layer_views: LayerViews | None = None,
          layer_stack: LayerStack | None = None,
          exclude_layers: LayerSpecs | None = None) -> Scene
```

Return Component 3D trimesh Scene.

**Arguments**:

- `component` - to extrude in 3D.
- `layer_views` - layer colors from Klayout Layer Properties file.
  Defaults to active PDK.layer_views.
- `layer_stack` - contains thickness and zmin for each layer.
  Defaults to active PDK.layer_stack.
- `exclude_layers` - list of layer index to exclude.

<a id="gdsfactory.export.to_stl"></a>

# gdsfactory.export.to\_stl

<a id="gdsfactory.export.to_stl.to_stl"></a>

#### to\_stl

```python
def to_stl(component: Component,
           filepath: PathType,
           layer_stack: LayerStack | None = None,
           exclude_layers: LayerSpecs | None = None,
           hull_invalid_polygons: bool = False,
           scale: float | None = None) -> None
```

Exports a Component into STL.

**Arguments**:

- `component` - to export.
- `filepath` - filepath prefix to write STL to.
  Each file will have each exported layer as suffix.
- `layer_stack` - contains thickness and zmin for each layer.
- `exclude_layers` - list of layer index to exclude.
- `hull_invalid_polygons` - If True, replaces invalid polygons (determined by shapely.Polygon.is_valid) with its convex hull.
- `scale` - Optional factor by which to scale meshes before writing.

<a id="gdsfactory.serialization"></a>

# gdsfactory.serialization

Serialize component settings into YAML or strings.

<a id="gdsfactory.serialization.DEFAULT_SERIALIZATION_MAX_DIGITS"></a>

#### DEFAULT\_SERIALIZATION\_MAX\_DIGITS

By default, the maximum number of digits retained when serializing float-like arrays

<a id="gdsfactory.serialization.clean_value_json"></a>

#### clean\_value\_json

```python
def clean_value_json(
    value: Any,
    include_module: bool = True,
    serialize_function_as_dict: bool = True
) -> str | int | float | dict[str, Any] | list[Any] | bool | Any | None
```

Return JSON serializable object.

**Arguments**:

- `value` - object to serialize.
- `include_module` - include module in serialization.
- `serialize_function_as_dict` - serialize function as dict. False serializes as string.

<a id="gdsfactory.serialization.clean_value_name"></a>

#### clean\_value\_name

```python
def clean_value_name(value: Any) -> str
```

Returns a valid Python variable name representation of an object.

<a id="gdsfactory.name"></a>

# gdsfactory.name

Define names, clean values for names.

<a id="gdsfactory.name.get_name_short"></a>

#### get\_name\_short

```python
def get_name_short(name: str,
                   max_cellname_length: int = CONF.max_cellname_length) -> str
```

Returns a short name.

<a id="gdsfactory.name.join_first_letters"></a>

#### join\_first\_letters

```python
def join_first_letters(name: str) -> str
```

Join the first letter of a name separated with underscores.

taper_length -> TL

<a id="gdsfactory.name.get_component_name"></a>

#### get\_component\_name

```python
def get_component_name(component_type: str, *args: Any, **kwargs: Any) -> str
```

Returns concatenated kwargs Key_Value.

<a id="gdsfactory.name.dict2name"></a>

#### dict2name

```python
def dict2name(prefix: str = "", **kwargs: Any) -> str
```

Returns name from a dict.

<a id="gdsfactory.name.assert_first_letters_are_different"></a>

#### assert\_first\_letters\_are\_different

```python
def assert_first_letters_are_different(**kwargs: Any) -> None
```

Assert that the first letters for each key are different.

Avoids different args that start with the same first letter getting
the same hash.

<a id="gdsfactory.name.print_first_letters_warning"></a>

#### print\_first\_letters\_warning

```python
def print_first_letters_warning(**kwargs: Any) -> None
```

Prints kwargs that have same cell.

<a id="gdsfactory.name.clean_name"></a>

#### clean\_name

```python
def clean_name(name: str,
               remove_dots: bool = False,
               allowed_characters: list[str] | None = None) -> str
```

Return a string with correct characters for a cell name.

By default, the characters [a-zA-Z0-9] are allowed.

**Arguments**:

- `name` _str_ - The name to clean.
- `remove_dots` _bool, optional_ - Whether to remove dots from the name. Defaults to False.
- `allowed_characters` _list[str], optional_ - List of additional allowed characters. Defaults to an empty list.
  

**Returns**:

- `str` - The cleaned name.

