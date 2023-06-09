## Discrete Event

### Target Shooter System

Include the detection subsystem by extending the model structure and re-run simulation experiments.  Create a new delay node for the detection with a random detection time. Its delay will be included in the overall response time. Vary its random characteristics and observe the resulting response time behavior.

NumPy Distributions

You can use the following functions after `import numpy as np`:

`np.random.random()` The function does not take any arguments and returns a random value between 0 and 1.

`np.random.uniform(min, max)` The function takes two arguments, which are the minimum and maximum values of the distribution.

`np.random.triangle(min, mode, max)` The function takes three arguments, which are the minimum, mode, and maximum values of the distribution.

`np.random.exponential(rate)` The function takes one argument, which is the rate parameter of the distribution.

### Security Gate Operations
* Modify the target shooter system, electric car charging system, or create a new model for security gate operations.
* Vary the number of attendant guards as "capacity" and observe changes in the waiting times.
* First simulate cars coming at a constant interarrival rates and gate service times.
* Next simulate cars coming at a uniformly distributed interarrival rate.
* Calibrate the incoming rate to actual traffic levels.
* Include an additional entry gate and vary the incoming traffic patterns across both.

### Electric Car Charging Model

* Modify the incoming traffic arrival pattern.
* Add another source of incoming cars.
* First simulate cars coming at a constant interarrival rates and gate service times.
* Next simulate cars coming at a uniformly distributed interarrival rate.
* Calibrate the incoming rate to actual traffic levels.

## System Dynamics

* Modify some examples in the notebook [se-lib system dynamics examples](<https://colab.research.google.com/drive/1oE5TBdF-hpJTQbQgSmPgmPoofBgOTR0B?usp=sharing>)
  * Change parameters
  * Change model structure
  * Add more variable plots

### Workforce Model
Develop a workforce model with an incoming hiring rate, a stock for the current level of workforce level, and an attrition outflow.  Use a first order delay with an average delay time for the hiring rate.

### Law System Modeling

Create a simple predator-prey model of criminal behavior to help evaluate enforcement and sanction policies.
