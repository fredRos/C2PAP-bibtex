C2PAP bibtex
============

A python package to convert information about articles from bibtex into html format suitable for display with typo3.

This packages provides plugins for `pybtex`.

Installation
------------

    pip3 install [--user] c2pap-bibtex

Workflow
--------

### Search for new articles

On ads with full-text search for `C2PAP` and possibly restricting the year.
https://ui.adsabs.harvard.edu/#search/q=full%3A%22C2PAP%22%20year%3A2016&sort=date%20desc%2C%20bibcode%20desc

### Export to bibtex

Select papers among search results, then press `Export - selected papers - in BibTeX` button above search results, save to a local file `c2pap.bib`

### Format

    pybtex-format --style C2PAP -b typo3 c2pap.bib results.html

The result is a standalone unstyled web page that you can check in your favorite webbrowser.

### Update in typo3

Open the C2PAP webpage in `typo3`, disable the `Rich Text Editor`, paste everything in between `<body> </body>` from `results.html` into `typo3`. Make sure there is a newline only between entire entries. Then click the tiny `Save document and view page` button.

Done!
