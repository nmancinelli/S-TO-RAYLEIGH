all:
	bash run_all.sh 100

fast:
	bash run_all.sh 1

clean:
	rm -f err.* log.* *.out *.err
	rm -rf PROC*
	rm -rf RUN*
	rm -f run.log.*
	rm -rf OUTPUT_FILES*
	rm -f *.in *.dat
	rm -f *.eps
	rm -f xz2svp.py
	rm -f x*2D
	rm -f filelist*
	rm -f _*
	rm -f *.pyc
	rm -f *.xy	
