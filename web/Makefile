env:
	sudo easy_install pip &&\
	pip install virtualenv &&\
	virtualenv venv &&\
	. venv/bin/activate &&\
	make deps

deps:
	pip install -r requirements.txt && \cp -f ../nnw.py ./venv/lib/python2.7/site-packages

install:
	\cp -f /opt/nnw/web/conf/nonowords.conf /etc/httpd/conf.d/ &&\
	service httpd restart

    
    
