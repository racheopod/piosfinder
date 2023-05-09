# Finding piospheres (livestock concentration areas) in NAIP imagery

*This project began in 2022 at Caltech's [Computer Vision for Ecology Summer Workshop](https://cv4ecology.caltech.edu/).*

<img src="figures/WY%20Salt%20block.jpg" alt="Cows" width="400" height="300" title="Cattle at a salt block on the western slope of the Big Horn Mountains, Wyoming, USA.">

## Background

Identifying patterns of livestock use and gradients of disturbance is a key component to understanding the dynamics of dryland plant communities and potential impacts of climate change on these ecosystems. Livestock can effect changes in plant communities through preferential use of certain plant types (e.g., cattle eat grass and avoid shrubs) [1]. The location of water sources dictates the distribution and concentration of animals, leading to heterogeneous use across the landscape. Gradients of grazing intensity and disturbance form around water sources, with the greatest (and most visible) impacts close to the source, termed the “piosphere” [2] (Fig. 1). This phenomenon is well documented and ranching practices draw upon a suite of attractants (such as salt-blocks and artificial water sources) to achieve more even use of forage and to ameliorate concentrated use of wetland and riparian areas [3].

<img src="figures/FourPiospheres.png" alt="piospheres" width="500" height="300" title="Piospheres in the western United States.">

Yet, even in relatively well-studied systems like the rangelands of the western U.S., data sources for these attractants are incomplete and inaccurate. The National Hydrography Dataset [4] includes over 80,000 well points across the West, but many of these points are not associated with piospheres and some piospheres are not associated with wells. Water is often piped or trucked to troughs and piospheres can also form around salt blocks and other attractants. Because piospheres are visually distinct and widespread, the task of finding these features is well suited to Computer Vision techniques. To improve the current data limitation for livestock concentration points across the western U.S., this project uses Convolutional Neural Networks to detect piospheres in aerial imagery in Wyoming.

<img src="figures/OR tank.jpg" alt="tank" width="400" height="300" title="Water is often trucked to tanks located far from wells.">

## Dataset

The National Agricultural Imagery Program ([NAIP](https://www.usgs.gov/centers/eros/science/usgs-eros-archive-aerial-photography-national-agriculture-imagery-program-naip?qt-science_center_objects=0#qt-science_center_objects)) collects aerial photographs with $\le$ 1 m resolution every 2 to 3 years across the United States [5]. The images collect red, blue, green, and near infra-red bands and are mosaiced into large tiles. These tiles are available on [Google Earth Engine](https://earthengine.google.com/).

<img src="figures/NAIPpiospheres2.png" alt="tank" width="550" height="110" title="Piospheres in false-color 2019 NAIP imagery from Wyoming.">

## References

[1] Augustine and McNaughton (1998). J. Wildlife Manage. [2] Lange (1969). J. Range Manag. [3] Rigge et al. (2013). Rangeland Ecol. Manage. [4] U.S. Geological Survey (2019). [5] U.S. Department of Agriculture (2017).