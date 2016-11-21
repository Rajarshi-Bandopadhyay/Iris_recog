start: setup.sh
	chmod a+x setup.sh
	./setup.sh
	
	
test: test_checker.py
	python test_checker.py
	
clean: 
	cd codes && rm -rf __pycache__/
	cd codes && rm -r *.pyc
