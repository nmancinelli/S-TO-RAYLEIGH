#!/bin/bash
#
SIMULATION_TIME=${1}
#
for AMP in 000; do
for WAVLEN in 000; do
for ANGLE_SOURCE in 23; do
DIRNAME=$ANGLE_SOURCE-$AMP-$WAVLEN
sbatch run.sh $DIRNAME $ANGLE_SOURCE $AMP $WAVLEN ${SIMULATION_TIME}
done
done
done
#
