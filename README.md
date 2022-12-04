# PokeScience

![pika](https://user-images.githubusercontent.com/58971957/201761340-5ecabcbc-c7a0-4631-8761-2621b598c1f6.jpg)

---
## Exam hand-in information

### Description of Project

Poke Science uses the data of the original 151 Pokémon created in 1998 to predict whether a given Pokémon will win
against another given Pokémon. Two iterations of the program is made to make these predictions:
- The first iteration (v1)
uses the [stats](https://bulbapedia.bulbagarden.net/wiki/Stat#Permanent_stats) of the Pokémon to determine the winner.
- The second iteration (v2) uses both [stats](https://bulbapedia.bulbagarden.net/wiki/Stat#Permanent_stats) as well as
[types](https://bulbapedia.bulbagarden.net/wiki/Type) to determine the winner. To see how types have an affect, see this
[type chart](https://bulbapedia.bulbagarden.net/wiki/Type#Type_chart).

It is possible to use the machine learning models trained on the 151 Pokémon to predict whether newer Pokémon would win
or not.

### Technologies Used

- Python for the project
- Poetry for dependency management
- Requests to use an API to fetch Pokémon [data](https://pokeapi.co/)
- CSV for storing data
- Pandas and to some extent numpy for data analysis and manipulation
- Matplotlib and Pandas for data visualization
- scikit-learn for machine learning models

### Installation Guide

We decided to use Poetry instead of requirements.txt for dependency management.
- Follow these instructions if you use Pycharm <https://www.jetbrains.com/help/pycharm/poetry.html>
- For VSCode use the above instructions to install Poetry - then run `poetry shell` to start a virtual environment.
If the environment does not start `poetry install` or `poetry build` may be required to be run first.

### How to run the Program

The program is split up into v1 and v2 as explained earlier.

To run v1, go into src/v1/ML_models and choose a model to run. The interesting models to try are perceptron.py, neural_network.py,
and rfc.py.

To run v2, go into src/v2/ML_models and choose a model to run. The interesting models to try are perceptron.py, neural_network.py,
and rfc.py.

The program will return either a 1 or a 0. If it returns 1 the model predicts that the first Pokémon provided in the
get_two_pokemon() function won the battle, if it returns 0 it predicts a loss.

Find your own two Pokémon and try them out. We have data from Pokémon 001 to 493 <https://pokemondb.net/pokedex/all>

### Status of the Project



### List of Challenges



## PokeScience Proposal

We want to make a program that can calculate the relative power of a given Pokémon compared to all existing Pokémon. Pokémon have either one or two types (e.g. fire, grass, electric), and each type is either strong, netrual, or weak to other types (e.g. fire is strong versus grass). Apart from that Pokémon can learn different Moves that can either deal Physical damage or Special damage that are increased with the attacking Pokémon's stats and reduced by the defending Pokémon's stats.

### Data gathering

We have found an API that contains all the data we need: <https://pokeapi.co/>

### Data analysis

To begin with the plan is:

- To figure out whether a Pokémon should be used as a Physical or Special damage attack dealer, and find the strongest attack it can learn.
  - Scale the attack's damage with the Pokémon's attack stat and its STAB (Same Type Attack Bonus) modifier
  - Sum its defensive stats (HP, defense, special defense)
  - Determine how important the Speed stat is for the Pokémon

- Give the Pokémon a score compared to all other Pokémon

- Use a decision tree to determine whether a Pokémon and its types counter a different Pokémon and its types, and scale that damage with the score found above.

![counters](https://media.discordapp.net/attachments/1040234360500146186/1042012000387072010/image.png)

#### Ambitious machine learning

- Use an unsupervised learning algorithm like, autoencoder, that automagically calculates the "power levels" of Pokémon. 

### Data visualization

Use a graphing tool, like Matplotlib, to show where the Pokémon is placed in power.

### Future nice-to-haves

- Figure out how strong a given Pokémon is compared to other strong Pokémon.

- The probability of a team, consisting of 6 Pokémon, winning against an opponent team.

---

## Poetry

### Poetry commands

To add a new package to the project, e.g. pandas:

```python
poetry add pandas
```

To run your file:

```python
poetry run python src/main.py
```

OR you can make a virtual environment using:

```python
poetry shell
```

---
