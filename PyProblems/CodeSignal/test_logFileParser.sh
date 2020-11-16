#!/bin/bash

touch server.log
echo -n -e '[01/Aug/1995:00:54:59 -0400] "GET /images/opf-logo.gif HTTP/1.0" 200 32511\n[01/Aug/1995:00:55:04 -0400] "GET /images/ksclogosmall.gif HTTP/1.0" 200 3635\n[01/Aug/1995:00:55:06 -0400] "GET /images/ksclogosmall.gif HTTP/1.0" 403 298\n[01/Aug/1995:00:55:09 -0400] "GET /images/ksclogosmall.gif HTTP/1.0" 200 3635\n[01/Aug/1995:00:55:18 -0400] "GET /images/opf-logo.gif HTTP/1.0" 200 32511\n[01/Aug/1995:00:56:52 -0400] "GET /images/ksclogosmall.gif HTTP/1.0" 200 3635\n' >> server.log
