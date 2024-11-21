# Reproducibility Package for HSCC Submission: Safe Temperature Regulation: Formally Verified and Real-World Validated

The full contents of the package can be found [here](https://github.com/cisasam/SafeTemperatureReproducibilityHSCC2025).

This is the reproducibility package for Safe Temperature Regulation: Formally Verified and Real-World Validated submitted to HSCC 2025.
It contains the data from the experiments and a docker container to run the proofs.


## Content
Docker scripts for the proof:
- setup.sh: the setup script for creating the Docker container.
- Dockerfile: the Docker configuration file used by setup.sh.
- keymaerax.math.conf: the KeYmaera X configuration file used in setup.sh.
- check_all.sh: the run script to check all the proofs.

Data:
- Data used in the paper:
  - Clean data:
    - `params1-state.csv` contains the data from the first experiment after cleanup.
    - `params2-state.csv` contains the data from the second experiment after cleanup. 
    - `cbair-error-state.csv` contains the data from the third experiment after cleanup.
    - `gbox-error-state.csv` contains the data from the fourth experiment after cleanup.
    - `visualization.py` is a script that plots the data to obtain the image shown in the paper.
  - Original data 
    - `params1-state-original.csv`, `params2-state-original.csv`, `cbair-error-state-original.csv`, `gbox-error-state-original.csv` contain the data from before cleanup.
- Unused data:
  - Controller data 
    - `params1-cont.csv`, `params2-cont.csv`, `cbair-error-cont.csv`, `gbox-error-cont.csv` contain the controller data after cleanup, including decision bounds and estimated `T_h`.
    - `params1-cont-original.csv`, `params2-cont-original.csv`, `cbair-error-cont-original.csv`, `gbox-error-cont-original.csv` contain the controller data before cleanup.
  - Extra experiment
    - `35-40-state-original.csv`, `35-40-state.csv`, `35-40-cont-original.csv`, `35-40-cont.csv` contain data from an experiment with bigger safety bounds unused in the paper.

## Setup and Checking the Proofs

In order to run the scripts, Docker needs to be installed on your machine and working correctly, see [docs.docker.com/get-docker/](https://docs.docker.com/get-docker/). KeYmaera X requires Wolfram Engine for QE. The Wolfram Engine license can be obtained for free and you will be prompted during the setup to login with your account.

1. Run `./setup.sh`. This script creates a docker image with all necessary components to run KeYmaera X and check the proof.
2. Log in with a Wolfram ID with a Wolfram Engine license when prompted. It can be obtained [here](https://wolfram.com/engine/free-license) for free.
3. Once the setup is complete run `./check_proof.sh`. This script calls KeYmaera X with our proof in order to check it. It may take up to 20-30 minutes.
4. You should see the output:
```
PROVED Safe Temperature Regulation (HSSC'25 Submission 22): tactic=<undefined>,tacticsize=824,budget=0[s],duration=267731[ms],qe=155228[ms],rcf=0,steps=156215

*******************************************************************************
Finished checking proof in KeYmaera X.
*******************************************************************************
```

## Data and Experimental Validation
The experimental data was obtained from the real-world incubator. The code can be checked in the following [github](https://github.com/cisasam/incubator_kyx_safe). The controller is [here](https://github.com/cisasam/incubator_kyx_safe/blob/master/software/incubator/physical_twin/controller_from_kyx.py) and the parameters used in the different experiments can be seen [here](https://github.com/cisasam/incubator_kyx_safe/blob/master/software/startup.conf).

The state data is directly collected from the incubator low level driver and contains the readings from the sensors. It has 12 columns representing the time (in epoch), the temperatures of the three sensors (two inside the incubator one outside to measure room temperature) and its reading time, booleans signaling if the heater and the fan are on, the controller time step and the elapsed time from ordering the readings to the message being passed. 

The controller data is collected from the controller running in a separate computer. It has 9 columns showing the time (in epoch), the plant time (as of the last sensor data passed to the controller), the orders to the fan and heater (to be actuated by the low level driver), the safety bounds, the estimated heater temperature and the controller decision bounds.


## System Specs
The proof and the incubator controller were run on a MacBook Pro 2021 with 16GB of RAM and an Apple M1 Pro microprocessor, on which the proofs can be checked in a roughly 5 minutes. The incubator specs are describe in this arxiv [publication](https://arxiv.org/abs/2102.10390).
