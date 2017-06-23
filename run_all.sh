#!/bin/bash
#
for AMP in 10000; do
for WAVLEN in 50000; do
for ANGLE_SOURCE in 23; do
DIRNAME=$ANGLE_SOURCE-$AMP-$WAVLEN
sbatch run.sh $DIRNAME $ANGLE_SOURCE $AMP $WAVLEN
done
done
done
#
