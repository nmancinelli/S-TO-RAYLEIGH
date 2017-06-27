#!/bin/bash
#
for AMP in 5000; do
for WAVLEN in 15000 20000 25000 50000; do
for ANGLE_SOURCE in 23; do
DIRNAME=$ANGLE_SOURCE-$AMP-$WAVLEN
sbatch run.sh $DIRNAME $ANGLE_SOURCE $AMP $WAVLEN
done
done
done
#
