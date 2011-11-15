all : solution.pdf

solution.pdf : solution.tex
	pdflatex -shell-escape solution.tex

clean :
	rm -rf solution.pdf solution.aux solution.log solution.out

.PHONY: all clean
