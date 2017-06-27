#!/bin/bash
#
#SBATCH --time=02:00:00
#SBATCH --mem=8GB
# Default resources are 1 core with 2.8GB of memory.
# Specify a job name:
#SBATCH -J ocean-continent
#SBATCH --mail-type=END,FAIL
#SBATCH --mail-user=nicholas_mancinelli@brown.edu
# Specify an output file
#SBATCH -o ocean-continent-%j.out
#SBATCH -e ocean-continent-%j.err
##
newdir=OUTPUT_FILES_$1
if [ -d "$newdir" ]; then
echo "$newdir already exists, exiting."
exit 0
fi
#
mkdir $newdir
cd $newdir
mkdir -p DATA
ln -s ../src
bash src/create_sem_synthetics.sh $2 $3 $4 $5
python src/estimate_S_arrival_time.py
python src/plot_seismos.py
cd ..
