#!/bin/bash
#PBS -N MSNB Test
#PBS -l select=5:ncpus=48:mpiprocs=1
#PBS -l walltime = 00:15:00
#PBS -k doe
#PBS -j oe
#PBS -P edu_res

#cat $PBS_NODEFILE

echo 'Enter the starting control drum angle in degrees'
read START
echo 'Enter the ending control drum angle in degrees'
read STOP
echo 'Enter the increment in degrees'
read INCREMENT

echo "Loading Cross-Section Data"
export SERPENT_DATA=/hpc-common/data/serpent/xsdata
echo "DATAPATH=$SERPENT_DATA"
echo "Loading Serpent v2"
module load use.exp_ctl
module load serpent/2.1.31-intel-19.0_ACE_KERMA_fix
export TMPDIR=/tmp

for ANGLE in $(seq $START $INCREMENT $STOP)
do
    echo "Writing MSNB at $ANGLE degrees:"
    FOLDER=` echo $ANGLE | python3 makedeck.py  `
    #mpirun sss2 -version
    mpirun -n 4 sss2 ${FOLDER}/MSNB -omp 48  | tee ${FOLDER}/MSNB.txt
    #mpirun -n 4 sss2 ${FOLDER}/MSNB -omp 48  -plot  | tee ${FOLDER}/MSNB.txt
done
