SHELL != which bash

contents := $(wildcard content/*.rst)

content.py: items.py ABOUT.md
	printf "%b" 'from items import items as items\n\nABOUT = r"""\n' > $@
	cat ABOUT.md >> $@;
	printf "%s\n\n" '""";' >> $@;
	printf "%b" "contents = (\n" >> $@
	for f in $(contents); \
	    do printf "%s\n" 'r"""' >> $@; \
	    cat $${f} >> $@; \
	    printf "%s,\n" '"""' >> $@; \
	done; \
	echo ")" >> $@;

items.py: $(contents)
	echo "" > $@;
	items="items = (\n" ;\
	for f in $(contents); \
	    do items+="\"$$(head -n 3 $${f} | grep '[^=]\+')\",\n"; \
	done; \
	items+=");"; \
	printf "%b" "$${items}" > $@;
