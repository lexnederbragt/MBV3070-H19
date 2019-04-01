DO_FILES   := $(shell ls [0-9]*.do.txt 2>/dev/null)
TARGETS    := $(subst .do.txt,.ipynb, ${DO_FILES})

all: ${TARGETS}

test:
	@echo ${TARGETS}

%.ipynb: %.do.txt
	doconce format ipynb $< --markdown
