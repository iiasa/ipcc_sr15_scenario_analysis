# Scenario analysis notebooks <br />for the *IPCC Special Report on Global Warming of 1.5°C*

## License

Copyright 2018-2019 IIASA

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

## Overview

The notebooks included in this repository implement the categorisation of
scenarios by climate impact and generate figures, tables, summary statistics,
and assessment indicators used in the **IPCC Special Report on Global Warming
of 1.5°C** ([SR15](http://www.ipcc.ch/report/sr15/)).

See [assessment/README](assessment/README.md) for an overview of notebooks
and the cross-references to figures, tables and assessment in the SR15.

A rendered version of this repository and the notebooks are available at
[data.ene.iiasa.ac.at/sr15_scenario_analysis](https://data.ene.iiasa.ac.at/sr15_scenario_analysis).

## Data release notes

We are using this repository to track data issues identified in the scenario
ensemble. Please check the [related issues labeled 'iamc15 data issue'](https://github.com/iiasa/ipcc_sr15_scenario_analysis/issues?utf8=✓&q=label%3A%22iamc15+data+issue%22+)
and the [data release notes](DATA_RELEASE_NOTES.md) in this repository.

## Scenario ensemble download

The scenario ensemble used for this assessment is available for download
at [data.ene.iiasa.ac.at/iamc-1.5c-explorer](https://data.ene.iiasa.ac.at/iamc-1.5c-explorer).

The scenario data is released under a custom license.
If appropriate reference is made to the data source, it is permitted to use
the data for scientific research and science communication.
However, redistribution of substantial portions of the data is restricted.

Please read the guidelines and legal code
at [data.ene.iiasa.ac.at/iamc-1.5c-explorer/#/license](https://data.ene.iiasa.ac.at/iamc-1.5c-explorer/#/license)
before redistributing this data or adapted material.

When using the scenario data for any analysis, figures or tables,
please clearly state the release version of the scenario ensemble.

## Scientific references

For the **scientific assessment of the Special Report**, please cite:
> Joeri Rogelj, Drew Shindell, Kejun Jiang,
> Solomone Fifita, Piers Forster, Veronika Ginzburg, Collins Handa,
> Haroon Kheshgi, Shigeki Kobayashi, Elmar Kriegler, Luis Mundaca,
> Roland Séférian, and Maria Virginia Vilariño.  
> *Mitigation pathways compatible with 1.5°C
> in the context of sustainable development*,  
> in "Special Report on Global Warming of 1.5°C (SR15)".
> Intergovernmental Panel on Climate Change: Geneva, 2018.  
> url: [www.ipcc.ch/report/sr15/](https://www.ipcc.ch/report/sr15/)

For a **high-level description of the scenario ensemble**, please refer to:
> Daniel Huppmann, Joeri Rogelj, Elmar Kriegler, Volker Krey, and Keywan Riahi.  
> A new scenario resource for integrated 1.5 °C research.  
> *Nature Climate Change*, 2018.  
> doi: [10.1038/s41558-018-0317-4](https://doi.org/10.1038/s41558-018-0317-4)

When using the **scenario ensemble data** for own analysis, please cite:
> Daniel Huppmann, Elmar Kriegler, Volker Krey, Keywan Riahi, Joeri Rogelj,
> Katherine Calvin, Florian Humpenoeder, Alexander Popp,
> Steven K. Rose, John Weyant, et al.,  
> *IAMC 1.5°C Scenario Explorer and Data hosted by IIASA*.  
> Integrated Assessment Modeling Consortium & International Institute for Applied Systems Analysis, 2019.  
> doi: [10.5281/zenodo.33633459](https://doi.org/10.5281/zenodo.3363345) |
> url: [data.ene.iiasa.ac.at/iamc-1.5c-explorer](https://data.ene.iiasa.ac.at/iamc-1.5c-explorer)

For the **Jupyter notebooks containing figure plotting and analysis scripts**
included in this repository, please cite:
> Daniel Huppmann et al.,
> *Scenario analysis notebooks for the IPCC Special Report on Global Warming of 1.5°C*. 2018.  
> doi: [10.22022/SR15/08-2018.15428](https://doi.org/10.22022/SR15/08-2018.15428) |
> url: [github.com/iiasa/ipcc_sr15_scenario_analysis](https://github.com/iiasa/ipcc_sr15_scenario_analysis)

Please refer to the [AUTHORS](AUTHORS.md) document for the full list of authors
of the scenario ensemble and the notebooks in this repository.

You can download these citations and the references
for all studies that submitted scenarios to the ensemble
as [Endnote (enl)](bibliography/iamc_1.5c_scenario_data.enl),
[Reference Manager (ris)](bibliography/iamc_1.5c_scenario_data.ris),
and [BibTex (bib)](bibliography/iamc_1.5c_scenario_data.bib) format.

## Dependencies

The notebooks included in this repository depend on the *pyam* package,
an open-source Python package for IAM scenario analysis and visualization
developed by Matthew Gidden ([@gidden](https://github.com/gidden))
and Daniel Huppmann ([@danielhuppmann](https://github.com/danielhuppmann/)).

See [pyam-iamc.readthedocs.io](https://pyam-iamc.readthedocs.io)
for installation instructions and the full documentation of *pyam*.
The source code is available at [github.com/IAMconsortium/pyam](https://github.com/IAMconsortium/pyam).

