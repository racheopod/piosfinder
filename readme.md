# Finding piospheres in NAIP imagery

*This project began in 2022 at Caltech's [Computer Vision for Ecology Summer Workshop](https://cv4ecology.caltech.edu/).*

<p align="center">
<img src="figures/WY%20Salt%20block.jpg" alt="Cows" width="400" height="300" title="Cattle at a salt block on the western slope of the Big Horn Mountains, Wyoming, USA.">
</p>

*<p align="center">Figure 1: Cattle at a salt block on the western slope of the Big Horn Mountains, Wyoming, USA.</p>*


## Background

Identifying patterns of livestock use and gradients of disturbance is a key component to understanding the dynamics of dryland plant communities and potential impacts of climate change on these ecosystems. Livestock can effect changes in plant communities through preferential use of certain plant types (e.g., cattle eat grass and avoid shrubs) [1]. The location of water sources dictates the distribution and concentration of animals, leading to heterogeneous use across the landscape. Gradients of grazing intensity and disturbance form around water sources, with the greatest (and most visible) impacts close to the source, termed the “piosphere” [2]. This phenomenon is well documented and ranching practices draw upon a suite of attractants (such as salt-blocks and artificial water sources) to achieve more even use of forage and to ameliorate concentrated use of wetland and riparian areas [3].

<p align="center">
<img src="figures/FourPiospheres.png" alt="piospheres" width="500" height="300" title="Piospheres in the western United States.">
</p>

*<p align="center">Figure 2: Piospheres in Idaho (top left), Wyoming (bottom left), and Oregon (right).</p>*

Yet, even in relatively well-studied systems like the rangelands of the western U.S., data sources for these attractants are incomplete and inaccurate. The National Hydrography Dataset [4] includes over 80,000 well points across the West, but many of these points are not associated with piospheres and some piospheres are not associated with wells. Water is often piped or trucked to troughs and piospheres can also form around salt blocks and other attractants. Because piospheres are visually distinct and widespread, the task of finding these features is well suited to Computer Vision techniques. To improve the current data limitation for livestock concentration points across the western U.S., this project uses Convolutional Neural Networks to detect piospheres in aerial imagery in Wyoming.

<p align="center">
<img src="figures/OR tank.jpg" alt="tank" width="400" height="300" title="Water is often trucked to tanks located far from wells.">
</p>

*<p align="center">Figure 3: Water is often trucked to tanks located far from wells, like this tank in south-central Oregon.</p>*

## Dataset

The National Agricultural Imagery Program ([NAIP](https://www.usgs.gov/centers/eros/science/usgs-eros-archive-aerial-photography-national-agriculture-imagery-program-naip?qt-science_center_objects=0#qt-science_center_objects)) collects aerial photographs with $\le$ 1 m resolution every 2 to 3 years across the United States [5]. The images collect red, green, blue, and near infra-red bands and are mosaiced into large tiles. These tiles are available on [Google Earth Engine](https://earthengine.google.com/).

<p align="center">
<img src="figures/NAIPpiospheres2.png" alt="tank" width="550" height="110" title="Piospheres in false-color 2019 NAIP imagery from Wyoming.">
</p>

*<p align="center">Figure 4: Piospheres displayed in false-color (NIR, R, G) 2019 Wyoming NAIP imagery.</p>*

## References

[1] Augustine, D.J., McNaughton, S.J., 1998. Ungulate Effects on the Functional Species Composition of Plant Communities: Herbivore Selectivity and Plant Tolerance. *The Journal of Wildlife Management* 62, 1165–1183. https://doi.org/10.2307/3801981

[2] Lange, R.T., 1969. The Piosphere: Sheep Track and Dung Patterns. *Journal of Range Management* 22, 396–400.
 
[3] Rigge, M., Smart, A., Wylie, B., 2013. Optimal Placement of Off-Stream Water Sources for Ephemeral Stream Recovery. *Rangeland Ecology & Management* 66, 479–486. https://doi.org/10.2111/REM-D-12-00099.1

[4] U.S. Geological Survey, 2016. USGS National Hydrography Dataset (NHD) Downloadable Data Collection - National Geospatial Data Asset (NGDA) National Hydrography Dataset (NHD): USGS - National Geospatial Technical Operations Center (NGTOC): Rolla, MO and Denver, CO, http://nhd.usgs.gov, http://viewer.nationalmap.gov/.

[5] U.S. Department of Agriculture (2019). National Agriculture Imagery Program (NAIP). https://doi.org/10.5066/F7QN651G 