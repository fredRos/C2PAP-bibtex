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

On ads with full-text search for `C2PAP` and possibly restricting the year, use this [URL](https://ui.adsabs.harvard.edu/#search/q=full%3A%22C2PAP%22%20year%3A2016&sort=date%20desc%2C%20bibcode%20desc).

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

Clean the data: remove empty rows, line breaks in cells, missing values etc.

In `julia`,

``` julia

    import CSV
    using DataFrames
    long_names = Dict("Fred"=>"F. Beaujean", "Alexey"=>"A. Krukau", "Jovan"=>"J. Mitrevski", "Mohammad"=>"M. Mirkazemi")
    frame = CSV.read("/home/beaujean/Documents/short.csv", weakrefstrings=false) # a DataFrame
    for (i, row) in enumerate(eachrow(frame))
        t = string(get(row[1]))
        p = string(get(row[2]))
        ra = string(get(row[3]))
        cpuh = get(row[4])*1000
        supp = long_names[string(get(row[5]))]
        println("Project $i/2017: &quot;<b>$t</b>&quot;<br />Proposers: $p<br />Research Area: $ra<br />CPU hours: $cpuh<br />C2PAP support: $supp")
    end
```

Some test data for 2017

    "Title","Proposers","Areas","CPUh","Contact"
    "Modeling the corona, winds and space weather conditions in moderately active Sun-like stars","Julian David Alvarado-Gomez, Gaitee Hussain, Jason Grunhut, Ofer Cohen, Jeremy Drake","E,F",660,"Alexey"
    "Triaxial modeling of elliptical and barred galaxies","Roberto Saglia, Fabrizio Finozzi, Jens Thomas","Prpo",3500,"Alexey"
    "A general study of MSSM WIMP dark matter including Sommerfeld enhancement","Martin Beneke, Stefan Recksiegel, Pedro Ruiz Femenía (TUM T31), Aoife Bharucha, Andrzej Hryczuk (external collaborators)","B, E",500,"Alexey"
    "Towards Bayesian analysis toolkit (BAT) 2.0","F.Beaujean (C2PAP), A. Caldwell (MPP), D. Greenwald (TUM E18), K.Kröninger (TU Dortmund), O. Schulz (MPP)","B, D",50,"Fred"
    "Applications of Numerical Information Field Theory via parallelized NIFTy","Torsten Enßlin (TE), Vanessa Böhm (VB), Jakob Knollmüller (JK), Daniel Pumpe (DP), Theo Steininger (TS)","B,E,F",2100,"Fred"
