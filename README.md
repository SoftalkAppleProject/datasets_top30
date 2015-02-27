<img src="https://raw.githubusercontent.com/SoftalkAppleProject/datasets_top30/master/images/STAP_masthead_1200.png" width="600" align="center" hspace="10" vspace="0" border="0" /><br />
# Softalk Magazine: Top 30 List Dataset

<img src="https://raw.githubusercontent.com/SoftalkAppleProject/datasets_top30/master/images/what_softalk_means_to_us.png" width="260" align="right" hspace="10" vspace="0" border="0" /><br />
Original source: **Peter Caylor's Excel spreadsheet** <br />
Original author: **Peter Caylor** <br />
Version 2 with CSV and screenshots, etc: **Jim Salmons** <br />
Project: **The Softalk Apple Project** <br />
URL: **www.SoftalkApple.com**

<img src="https://raw.githubusercontent.com/SoftalkAppleProject/datasets_top30/master/Screenshots/v1n03_Nov80_top30.jpg" width="220" align="left" hspace="10" border="1" />
This repository contains the Softalk magazine (Apple edition) Top 30 List as a dataset with validating screenshots and other helpful files and information to encourage and support Citizen Science/History data exploration. 

An Excel spreadsheet is provided together with a set of exported CSV files. For data validation and to satisfy folks' basic curiosity, screenshots of the Top 30 lists, as they appeared in the magazine, are provided. The first issue, September 1980, did not have a Top 30 list, so there are 47 lists of between 30 and 32 listed items per month. Ties on the computed index for position 30 would occasionally result in 31 or 32 items on the list.

The primary Excel spreadsheet -- and its associated CSV export of the primary data worksheet -- contain two columns per month for the 47 months of record. For each pair of columns per month, the first contains the index computed for that title for that month and the second column contains the ordinal position assigned for that index value for that month. NOTE: Index values are NOT comparable across months. This value is only used for ordinal positioning within a given month's list.

Index ties result in ties for a given ordinal position, and thereby result in more than one item with the same position in a given month, as well as ordinal numbers being missing on a list with tied items.

A Python script is provided to parse the primary CSV file and generate a subdirectory of 47 month-by-month CSV data files for each of the Softalk Top 30 lists. Each file includes three fields; product name, ordinal position in the list, and computed indes.

## A Big Thank You to Project Volunteer Peter Caylor

<img src="https://raw.githubusercontent.com/SoftalkAppleProject/datasets_top30/master/images/LoRes_Peter_Caylor_handsoff_Softalk_megascans_to_Jim_Salmons.jpg" width="420" align="left" hspace="10" border="1" />Peter "Lo-res" Caylor is an inspiring volunteer helping to develop **The Softalk Apple Project**. He selflessly donated his personal scan of most of the issues of Softalk, then worked diligently with us to secure and scan the remaining issues. Peter's initial "Caylor Foundation Scans" are not archival quality, being two-up photocopies of available but often well-used issues. However, Peter's contribution did allow our project to get a quick start on our own research initiative and, perhaps more importantly, support some interesting doctoral and postdoc research collaborations. His scans, for example, are making it possible for us to pull this Top 30 dataset together.

In the photo, Peter -- on the left -- hands off his initial scans to STAP project co-founder, Jim Salmons, during an informal celebration at Bertha's Pub in Fells Point, Baltimore. The ceremonial transfer of the USB hard-drive was the culmination of Jim's attendance at the *Museums and the Web 2014* conference where he had an opportunity to demo our project's sofware platform work-in-process and discuss the research agenda of both The Softalk Apple Project and our associated applied research project, FactMiners.org.

## Peter's 49th Issue Prognostication!
<img src="https://raw.githubusercontent.com/SoftalkAppleProject/datasets_top30/master/images/Peters_issue49_forecast_top30.png" width="440" align="right" hspace="10" border="1" />
Needing a subject to exercise his growing skills and interest in Decision Support Systems, Peter had the great idea to OCR and transcribe the Softalk Apple Top 30 lists as a dataset to be used as part of a professional development course he is taking. His clever "homework" assignment was to create an Excel spreadsheet-based forecasting model to predict the Top 30 list for the unpublished "49th issue" of Softalk that would have appeared for September 1984.

Here's a screenshot of Peter's creative homework assignment in which he imagines what he would editorially write to introduce the publication of the imagined "unpublished" Top 30 list that would have appeared in September 1984. You can [find out more about Peter's "homework" assignment](http://goo.gl/L97G1Y) in our blog on The Softalk Apple Project.

**For his great work that continues to help move our grassroots project forward, Peter Caylor is the FIRST winner of a Softalk/FactMiners Data Digger achievement!** Peter will be receiving the inaugural custom Softalk/FactMiners Data Digger mug which will become the standard design for the soon-to-be-announced **Softalk/FactMiners Data Digger Challenge**. As soon as we design this next Achievment mug and have a run of them made, Peter's Data Digger mug will be in the mail to be added to the Volunteer award mug already in his possession! Actually, we're getting pretty good at the mug-making stuff, having done it to everyone's satisfaction on the Volunteeer of the Year and Researcher of the Year awards we announced recently. :-)

## Ahead, the Softalk/FactMiners Data Digger Challenge!

As soon as we have the rules worked out -- they will be pretty obvious having to do with adding data-driven insights into what we can "read into" this dataset -- we'll officially launch an on-going **Softalk/FactMiners Data Digger Challenge**. Our goal is to stimulate interest in folks having some "serious fun" doing exploratory analysis and insight discovery on this fascinating dataset.

In the meantime, you are welcome to peruse these files and begin to think about the kinds of questions that could be asked and insights gleaned from clever analyses of this dataset. As Challenge entries accumulate, it will become increasingly easy to imagine the full potential of creating a metamodel-based, structural and content model of all the information (the elementary "facts") of the full run of Softalk magazine captured in a FactMiners' Fact Cloud as envisioned in our [*Where Facts Live*](http://goo.gl/gS2FJk) presentation at #MCN2014, the annual conference of the Museum Computer Network.

More as it develops... :-)

On behalf of **The Softalk Apple Project** and **FactMiners**,<br />
-: Jim Salmons :-<br />

<a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/4.0/88x31.png" /></a><br /><span xmlns:dct="http://purl.org/dc/terms/" property="dct:title">Softalk Top 30 Dataset</span> by <a xmlns:cc="http://creativecommons.org/ns#" href="http://www.SoftalkApple.com" property="cc:attributionName" rel="cc:attributionURL">The Softalk Apple Project</a> is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">Creative Commons Attribution-ShareAlike 4.0 International License</a>.<br />Based on a work at <a xmlns:dct="http://purl.org/dc/terms/" href="http://www.SoftalkApple.com" rel="dct:source">http://www.SoftalkApple.com</a>.
