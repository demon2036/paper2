SHELL := /bin/bash
export TEXINPUTS := .:vendor/acl:
export BSTINPUTS := .:vendor/acl:
export BIBINPUTS := .

.PHONY: all clean

all:
	mkdir -p build
	pdflatex -interaction=nonstopmode -output-directory=build main.tex
	bibtex build/main
	pdflatex -interaction=nonstopmode -output-directory=build main.tex
	pdflatex -interaction=nonstopmode -output-directory=build main.tex
	# ACL review line positions can need another pass after bibliography reflow.
	pdflatex -interaction=nonstopmode -output-directory=build main.tex
	cp build/main.pdf paper.pdf

clean:
	rm -f build/*.aux build/*.bbl build/*.blg build/*.log build/*.out
