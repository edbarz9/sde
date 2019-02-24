# dwm-gaps - dynamic window manager
# See LICENSE file for copyright and license details.

include config.mk

SRC = drw.c dwm-gaps.c util.c
OBJ = ${SRC:.c=.o}

all: options dwm-gaps

options:
	@echo dwm-gaps build options:
	@echo "CFLAGS   = ${CFLAGS}"
	@echo "LDFLAGS  = ${LDFLAGS}"
	@echo "CC       = ${CC}"

.c.o:
	${CC} -c ${CFLAGS} $<

${OBJ}: config.h config.mk

config.h:
	cp config.def.h $@

dwm-gaps: ${OBJ}
	${CC} -o $@ ${OBJ} ${LDFLAGS}

clean:
	rm -f dwm-gaps ${OBJ} dwm-${VERSION}.tar.gz

dist: clean
	mkdir -p dwm-${VERSION}
	cp -R LICENSE Makefile README config.def.h config.mk\
		dwm.1 drw.h util.h ${SRC} dwm.png transient.c dwm-${VERSION}
	tar -cf dwm-${VERSION}.tar dwm-${VERSION}
	gzip dwm-${VERSION}.tar
	rm -rf dwm-${VERSION}

install: all
	mkdir -p ${DESTDIR}${PREFIX}/bin
	cp -f dwm-gaps ${DESTDIR}${PREFIX}/bin
	chmod 755 ${DESTDIR}${PREFIX}/bin/dwm-gaps
	mkdir -p ${DESTDIR}${MANPREFIX}/man1
	sed "s/VERSION/${VERSION}/g" < dwm-gaps.1 > ${DESTDIR}${MANPREFIX}/man1/dwm-gaps.1
	chmod 644 ${DESTDIR}${MANPREFIX}/man1/dwm-gaps.1

uninstall:
	rm -f ${DESTDIR}${PREFIX}/bin/dwm-gaps\
		${DESTDIR}${MANPREFIX}/man1/dwm-gaps.1

.PHONY: all options clean dist install uninstall
