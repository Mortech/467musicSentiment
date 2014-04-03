467musicSentiment
=================

Audio-visual assignment for cs467 at UIUC

To run the visualization:
	Run a web server (eg. "python -m SimpleHTTPServer") and navigate to
		index.html in a browser.

To parse a new dataset:
	Requires stanford-corenlp-full-2014-01-04 files to be located in that
		folder with sentanalyzer.py
	Run sentanalyzer.py.
	The format of the lyrics should be identical to that of ours (No empty
		lines, no sentence-ending punctuation, periods at the end of lines,
		song and album titles in titlecase with spaces), and
		should be in the lyrics directory in subfolders with album titles
