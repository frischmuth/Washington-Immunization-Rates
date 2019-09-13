# Washington-Immunization-Rates

The Washington State Department of Health publishes annual vaccinate rate data for Kindergarteners and 6th graders. This data is publically available and can be viewed at the state level, nine Educational Service Districts, 285 School districts, and at the individual school level. Additionally, the Office of Supintendent of Public Instruction publishes annual enrollment report card which includes demographic data of Washington State students, also available at the school level. I combined these two datasets to investigate any correlation between student vaccination rates and school demographic data.

## Data Sources

The vaccine data is available by year in raw csv format from 2014-5 to 2016-7 on the data.wa.gov website. In 2017 they began providing access to this data in an [interactive dashboard](https://www.doh.wa.gov/DataandStatisticalReports/HealthDataVisualization/SchoolImmunization/SchoolBuildingImmunization) so that individuals could easily see information about a particular school compared to state averages. It seems plausible that most people seeking this data are parents looking for information about their own children's schools, so this is a very useful tool for the state to provide, however it created more work to collect data for all schools in the state. Ultimately I was able to export all of this data into a .txt file, but the format was completely different than of previous years and thus required time to prepare for comparison. This data include percentages fully vaccinated, counts of various exemptions, and vaccination rates separated by individual illnesses.

The [Report Card Enrollment from 2014-15 to Current Year](https://data.wa.gov/Education/Report-Card-Enrollment-from-2014-15-to-Current-Yea/rxjk-6ieq) contains student demographic data by school and grade level for public and private schools in the state. There is data about gender, race/ethnicity, income, housing status, and disibilities, all aggregated at the state level. 

I joined these two datasets on school district and school name, and including only schools that had reported vaccination data. Due to time constraints, I have not done extensive data cleaning to ensure complete matches, e.g. there were cases where one dataset would include XYZ Elementary School and the other would have XYZ K-8 school. 

## Findings

It is clear from the data that schools with the highest rates of exemptions all come from schools that are predominantly white. 

## Limitations

There is no public data available at the student level, so it is difficult to make correlations between vaccine rates and demographic information. Therefore, it is extremely difficult to view the 

## Further Exploration Topics

Further clean dataset to ensure all schools are included
Trends over time (K and 6th over six years would provide a 12 year set)
Public vs Private
Geographic data - info by City, urban vs. rural
Look at locations of recent measles outbreaks
Look at all school data to see if rates change as kids get older (whether or not people catch up on their vaccines)

