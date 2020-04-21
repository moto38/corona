Corona Simulator(like COVID-19)
====
This is a virus infection simulator using cellular automata.
This simulator is assuming a new coronavirus (COVID-19) as a simulation target.

But I'm not using reliable numbers for parameters.
Please modify it appropriately according to the target.


Infection occurs stochastically using random number.
The probability is based on the situation in Tokyo, but it does not represent the actual situation.

It is hoped that the user will adjust the parameters appropriately before use.


Each cell of this cellular automaton has the following states.

- Uninfected
- Infected (From infection to recovery)
- Recovered(Immunity acquisition)
- Death

## Description
Simple two-dimensional automaton with periodic boundary conditions.
Infection only occurs from neighboring cells.

### Cell's state

| Value of Cell | State                                 |
|----------------|---------------------------------------|
| 0              | Uninfected                            |
| 15             | Recovered(Immunity acquisition)       |
| 16-29          | Infected (From infection to recovery) |
| 150            | Death                                 |
|                |                                       |

The number of infected cells decreases by 1 for each step, and when it reaches 15, it will recover (immunity acquisition).
A cell is infected if the remainder of "Recovered" in the cell value is not 0.
"Recovered" is "viruslife" + 1. "viruslife" is default 14, so "Recovered" is default 15.

### Stop condition
The automaton stops when the number of infected people reaches 0.

### Other
Depending on the initial state, if there is a person who goes to the end without being infected, it is probably the person who has been protected by "herd immunity" or "prevention of epidemics".
Herd immunity rarely occurs.
Spot cells that differ from the initial state cell that remain during the "Recovered" cell are "Death".
When the size of the automaton is small, sometimes no one is infected. Please retry.


If you do not prevent the disease (preventrate = 1), the increase in the number of infected people cannot be stopped. 
You'll understand what the declaration of an emergency means.
The number of deaths will rise.

The default quarantine(preventation) start timing is t = 30.
- preventrate=0.1(Quarantine 90%) -> The number of infected people decreases rapidly.
- preventrate=0.6(Quarantine 40%) -> The number of infected people cannot stop increasing.



### Prameters
| Variable      | Content                                                                                                                                                                                                                                                     |
|---------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| msize         | The size of one side of a two-dimensional grid of cellular automata. Execute with msize x msize grid.                                                                                                                                                       |
| viruslife     | It is the period from infection to recovery. Default is 14. It is supposed to acquire immunity in 14 days. There is no incubation period, but if you are infectious during the incubation period, you can change the value including the incubation period. |
| Nreproduction | Basic reproduction number(R0). It is adapted to the number of new coronaviruses produced in Tokyo(1.7).                                                                                                                                                     |
| isolationRate | inverse of mean infectious period of tau. Change this value to control the infectivity. The bigger it is, the more easily it becomes infected. The smaller it is, the less likely it is to be infected.                                                    |
| preventtime   | Time to start quarantine(preventation of epidmics). When Time (elapsed) reaches this value, infectrate is multiplied by preventrate. It can be said that people started to refrain from self-control.                                                      |
| preventrate   | Effect of quarantine. Numerical value indicating the percentage of infectiousness that can be achieved by prevention of epidemics. When preventtime comes, infectrate is multiplied. Change infectrate. It is 1 when not quarantine.                        |
| initialrate   | Initial infected cell ratio.                                                                                                                                                                                                                                |
| rod           | rate of death.                                                                                                                                                                                                                                              |


### Other variables
| Variable   | Content                                                                                                        |
|------------|----------------------------------------------------------------------------------------------------------------|
| infectrate | Infectivity. Nreproduction * isolationrate. Numerical value actually used to determine whether to be infected. |
| recovered  | Value of the cell in recovery state. ( viruslife + 1 = recovered )                                             |
| level1     | Initial cell value of infection. ( recovered + viruslife = level1 )                                            |
| death      | Value of the cell in death.     ( recovered * 10 = death )                                                     |
|            |                                                                                                                |



## Demo
Example is preventrate=0.6(40%) and preventrate=0.1(90%)

![Figure_1_prevent_rate4]https://github.com/moto38/corona/raw/master/Figure_1_prevent_rate4.png
<video width="320" height="240" controls>
  <source src="prevent_rate4.mp4" type="video/mp4">
</video>

![Figure_1_prevent_rate9]https://github.com/moto38/corona/raw/master/Figure_1_prevent_rate9.png
<video width="320" height="240" controls>
  <source src="prevent_rate9.mp4" type="video/mp4">
</video>


## Requirement
- python3
  - numpy
  - scipy
  - matplotlib

## Usage

```
python corona.py
```

## Output 
- Elaplsed time
- Number of Uninfected
- Number of Infected
- Number of Recovered
- infectrate


## Install

Install requirement modules.

```
pip install numpy
pip install scipy
pip install matplotlib
```


## License

GPL


## Author

[moto38] http://github.com/moto38
