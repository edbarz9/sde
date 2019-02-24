# st - simple terminal
# See LICENSE file for copyright and license details.
.POSIX:

include config.mk

SRC = st-82.c x.c
OBJ = $(SRC:.c=.o)

all: options st-82

options:
	@echo st-82 build options:
	@echo "CFLAGS  = $(STCFLAGS)"
	@echo "LDFLAGS = $(STLDFLAGS)"
	@echo "CC      = $(CC)"

config.h:
	cp config.def.h config.h

.c.o:
	$(CC) $(STCFLAGS) -c $<

st-82.o: config.h st-82.h win.h
x.o: arg.h config.h st-82.h win.h

$(OBJ): config.h config.mk

st-82: $(OBJ)
	$(CC) -o $@ $(OBJ) $(STLDFLAGS)

clean:
	rm -f st-82 $(OBJ) st-$(VERSION).tar.gz

dist: clean
	mkdir -p st-$(VERSION)
	cp -R FAQ LEGACY TODO LICENSE Makefile README config.mk\
		config.def.h st.info st.1 arg.h st.h win.h $(SRC)\
		st-$(VERSION)
	tar -cf - st-$(VERSION) | gzip > st-$(VERSION).tar.gz
	rm -rf st-$(VERSION)

install: st-82
	mkdir -p $(DESTDIR)$(PREFIX)/bin
	cp -f st-82 $(DESTDIR)$(PREFIX)/bin
	chmod 755 $(DESTDIR)$(PREFIX)/bin/st-82
	mkdir -p $(DESTDIR)$(MANPREFIX)/man1
	sed "s/VERSION/$(VERSION)/g" < st-82.1 > $(DESTDIR)$(MANPREFIX)/man1/st-82.1
	chmod 644 $(DESTDIR)$(MANPREFIX)/man1/st-82.1
	tic -sx st-82.info
	@echo Please see the README file regarding the terminfo entry of st.

uninstall:
	rm -f $(DESTDIR)$(PREFIX)/bin/st-82
	rm -f $(DESTDIR)$(MANPREFIX)/man1/st-82.1

.PHONY: all options clean dist install uninstall
