#!/bin/bash
#
#SBATCH --time=02:00:00
#SBATCH --mem=8GB
# Default resources are 1 core with 2.8GB of memory.
# Specify a job name:
#SBATCH -J specfem2d
#SBATCH --mail-type=END,FAIL
#SBATCH --mail-user=nicholas_mancinelli@brown.edu
#SBATCH -J kernel_gen
# Specify an output file
#SBATCH -o kernel_gen-%j.out
#SBATCH -e kernel_gen-%j.err
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
