start: setup.sh
	chmod a+x setup.sh
	./setup.sh
	
	
test: test_checker.py
	python test_checker.py
	
clean: *.pyc
	rm -r *.pyc
	rm -rf __pycache__/
