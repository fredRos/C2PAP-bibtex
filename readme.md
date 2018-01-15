C2PAP bibtex
============

A python package to convert information about articles from bibtex into html format suitable for display with typo3.

This packages provides plugins for `pybtex`.

Installation
------------

Clone this repo, then

    pip3 install [--user] .

Workflow
--------

### Search for new articles

On ads with full-text search for `C2PAP` and possibly restricting the year, use got to https://ui.adsabs.harvard.edu 
and enter this query

     year:2017  AND (full:"C2PAP" OR aff:"C2PAP" OR author:"Beaujean, Frederik"OR author:"Petkova, Margarita" OR author:"Krukau, Alexey" OR author:"Hubber, David")
     
The full list of publications used for the brochure 

    (((full:"C2PAP" OR aff:"C2PAP" OR ack:"C2PAP") OR (author:"Beaujean, Frederik" OR author:"Petkova, Margarita" OR author:"Krukau, Alexey" OR (author:"Cadolle Bel, Marion" AND aff:"Excellence Cluster Universe") OR (author:"Hubber, David" AND year:2017) OR (author:"Mirkazemi, Mohammad" AND year:2016-2017))) AND (year:2014-2017) OR (arxiv:"arxiv:1702.06546" OR doi:"10.3390/galaxies5030049" OR doi:"10.3390/galaxies5030035" OR doi:"10.1017/S1743921315003506" OR doi:"doi:10.1017/S1743921314009491" OR doi:"10.1140/epjc/s10052-017-4700-5" OR doi:"10.1007/JHEP02(2017)117" OR doi:"10.1103/PhysRevD.94.052009" OR doi:"10.1016/j.physletb.2017.08.047" OR doi:"10.1016/j.physletb.2016.07.042" OR doi:"10.1103/PhysRevD.92.072004" OR doi:"10.1103/PhysRevD.93.052002" OR doi:"10.1140/epjc/s10052-016-4184-8" OR doi:"10.1007/JHEP10(2015)134" OR doi:"10.1140/epjc/s10052-015-3408-7" OR doi:"10.1140/epjc/s10052-015-3544-0" OR doi:"10.1016/j.physletb.2014.09.008" OR doi:"10.1140/epjc/s10052-015-3534-2" OR doi:"10.1007/JHEP04(2015)116" OR doi:"10.1140/epjc/s10052-015-3373-1" OR doi:"10.1007/JHEP01(2015)068" OR doi:"10.1103/PhysRevD.90.052004" OR doi:"10.1088/1742-6596/513/4/042049" OR doi:"10.1103/PhysRevD.92.072001"))

### Export to bibtex

Select papers among search results, then press `Export - selected papers - in BibTeX` button above search results, save to a local file `c2pap.bib`

### Format

    pybtex-format --style C2PAP -b typo3 c2pap.bib results.html

The result is a standalone unstyled web page that you can check in your favorite webbrowser.

### Update in typo3

Open the C2PAP webpage in `typo3`, disable the `Rich Text Editor`, paste everything in between `<body> </body>` from `results.html` into `typo3`. Make sure there is a newline only between entire entries. Then click the tiny `Save document and view page` button.

Done!


Projects
--------

Download spreadsheet from google docs as openoffice. Open and save the
five columns `Title, Proposers, Areas, CPUh, Contact` as a CSV file in
UTF8.

Clean the data: remove empty rows, line breaks in cells, fill in any missing values etc.

In `julia`,

``` julia
import CSV
using DataFrames
long_names = Dict("Fred"=>"F. Beaujean", "Alexey"=>"A. Krukau", "Jovan"=>"J. Mitrevski", "Mohammad"=>"M. Mirkazemi", "David"=>"D. Hubber", "Margarita"=>"M. Petkova")
filename = "/tmp/c2pap.csv"
frame = CSV.read(filename, weakrefstrings=false) # a DataFrame
for (i, row) in enumerate(eachrow(frame))
    t = string(get(row[1]))
    p = string(get(row[2]))
    ra = string(get(row[3]))
    cpuh = get(row[4])*1000
    supp = long_names[string(get(row[5]))]
    println("Project $i/2018: &quot;<b>$t</b>&quot;<br />Proposers: $p<br />Research Area: $ra<br />CPU hours: $cpuh<br />C2PAP support: $supp")
end

```

Some test data for 2017

    "Title","Proposers","Areas","CPUh","Contact"
    "Modeling the corona, winds and space weather conditions in moderately active Sun-like stars","Julian David Alvarado-Gomez, Gaitee Hussain, Jason Grunhut, Ofer Cohen, Jeremy Drake","E,F",660,"Alexey"
    "Triaxial modeling of elliptical and barred galaxies","Roberto Saglia, Fabrizio Finozzi, Jens Thomas","Prpo",3500,"Alexey"
    "A general study of MSSM WIMP dark matter including Sommerfeld enhancement","Martin Beneke, Stefan Recksiegel, Pedro Ruiz Femenía (TUM T31), Aoife Bharucha, Andrzej Hryczuk (external collaborators)","B, E",500,"Alexey"
    "Towards Bayesian analysis toolkit (BAT) 2.0","F.Beaujean (C2PAP), A. Caldwell (MPP), D. Greenwald (TUM E18), K.Kröninger (TU Dortmund), O. Schulz (MPP)","B, D",50,"Fred"
    "Applications of Numerical Information Field Theory via parallelized NIFTy","Torsten Enßlin (TE), Vanessa Böhm (VB), Jakob Knollmüller (JK), Daniel Pumpe (DP), Theo Steininger (TS)","B,E,F",2100,"Fred"
