# Release notes for the *IAMC 1.5°C Scenario Explorer and Data hosted by IIASA*

This document keeps track of the data changes of the scenario ensemble
compiled in the *IAMC 1.5°C Scenario Explorer and Data hosted by IIASA*.


## Release 2.0

This release coincides with the approval and acceptance of the
[IPCC's Special Report on Climate Change and Land (SRCCL)](https://www.ipcc.ch/report/srccl/).
It data was extended by several timeseries on prices related to agriculture

To acknowledge the significant contribution by several authors of the SRCCL
regarding the additional analysis and extension of the scenario ensemble,
the list of authors was amended and a new DOI was issued for the extended data.

One data issue identified since Release 1.1 was also corrected in this release,
namely an incorrect aggregation of prices at the regional (R5) level.
To mitigate any confusion, all erroneous data was removed as part of this release.
This change does not have any impact on the assessment in the IPCC SR15.

### Detailed list of changes

 - Additional timeseries data on prices related to agriculture for the 
   implementations of the Shared Socioeconomic Pathways (SSP)
   included in the scenario ensemble.

 - Aggregation error for regional price timeseries (R5) computed from
   native model regions during submission. All affected data was removed
   from the interactive Scenario Explorer as part of this release.
   See [#19](https://github.com/iiasa/ipcc_sr15_scenario_analysis/issues/19)
   for details.


## Release 1.1

This release includes additional timeseries data to increase reproducibility
of the figures and tables in the IPCC SR15, and it corrects a number of
data issues identified since Release 1.0. None of the changes have
any impact on the assessment in the IPCC SR15.

### Detailed list of changes

 - Reporting error for primary energy from fossils (aggregate) submitted by
   the 'MESSAGE-GLOBIOM 1.0' scenarios as part of the 'EMF33' project.
   See [#1](https://github.com/iiasa/ipcc_sr15_scenario_analysis/issues/1)
   for details.

 - Typo in a variable name and incorrect values in two timeseries of 
   the reference data from 'IEA Statistics' included in the release.
   See [#2](https://github.com/iiasa/ipcc_sr15_scenario_analysis/issues/2)
   for details.

 - Missing subsectoral CO2 emissions for scenarios from the SSP, CD-LINKS
   and LED projects.
   See [#3](https://github.com/iiasa/ipcc_sr15_scenario_analysis/issues/3)
   and [#4](https://github.com/iiasa/ipcc_sr15_scenario_analysis/issues/4)
   for details.

 - Missing timeseries of harmonized emissions as used for climate impact
   assessment by the MAGICC and FAIR models.
   See [#5](https://github.com/iiasa/ipcc_sr15_scenario_analysis/issues/5)
   for details.

 - Error in index year for the variable 'Price|Agriculture|*' in scenarios
   submitted by the 'AIM' model.
   See [#7](https://github.com/iiasa/ipcc_sr15_scenario_analysis/issues/7)
   for details.

 - Missing value for cumulative BECCS in the metadata for
   the 'LowEnergyDemand' scenario submitted by the 'MESSAGEix-GLOBIOM' model.
   See [#9](https://github.com/iiasa/ipcc_sr15_scenario_analysis/issues/9)
   for details.

 - Incorrect regional data (other than 'World') for scenario submitted
   by the 'POLES' model as part of the 'EMF33' project.
   See [#12](https://github.com/iiasa/ipcc_sr15_scenario_analysis/issues/12)
   for details.


## Release 1.0

Scenario ensemble release for the soft launch of the IPCC SR15
following the approval plenary in Incheon, Republic of Korea.
