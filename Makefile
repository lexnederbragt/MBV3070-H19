DO_FILES   := $(shell ls lab/[0-9]*.do.txt 2>/dev/null)
TARGETS    := $(subst .do.txt,.ipynb, ${DO_FILES})
TARGETS    += exercises.html

EXDIR      := /Users/alexajo/github/cse-exercises/src

# variable to generate all sustitutions of variables in the doconce files
preprocess_include_subst := EXDIR=${EXDIR}

# general parameters
DOCONCE_PARAMS :=	--userdef_environment_file=${HOME}/github/bios1100-uke-for-uke/general/userdef_environments.py

all: ${TARGETS}

test:
	@echo ${TARGETS}

lab/%.ipynb: lab/%.do.txt lab/%.md
	doconce format ipynb $< --markdown

exercises.html : exercises.do.txt
	doconce format html $< \
	--pygments_html_style=autumn --keep_pygments_html_bg \
	SLIDE_TYPE=deck SLIDE_THEME=swiss \
	--preprocess_include_subst -i ${preprocess_include_subst} \
	--without_solutions --without_answers --without_hints \
	--skip_inline_comments ${DOCONCE_PARAMS} && \
	doconce slides_html exercises.html deck --html_slide_theme=swiss \
	${DOCONCE_PARAMS}	&& \
	mv exercises.html tmp_exercises.html
	awk '{if(NR==1&&$$0=="\\"){}else{print $0}}' tmp_exercises.html > exercises.html
