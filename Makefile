DO_FILES   := $(shell ls lab/[0-9]*.do.txt 2>/dev/null)
TARGETS    := $(subst .do.txt,.ipynb, ${DO_FILES})
TARGETS    .= $(addprefix lab/, ${TARGETS})

all: ${TARGETS}

test:
	@echo ${TARGETS}

lab/%.ipynb: lab/%.do.txt lab/%.md
	doconce format ipynb $< --markdown
