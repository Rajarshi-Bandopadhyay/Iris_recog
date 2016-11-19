start: main.py
	python main.py
	
test: test_checker.py
	python test_checker.py
	
clean: *.pyc
	rm -r *.pyc
