all : solution.pdf

solution.pdf : solution.tex
	pdflatex -shell-escape solution.tex

clean :
	rm -rf solution.pdf solution.aux solution.log

.PHONY: all clean
