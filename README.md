# PokeScience

## PokeScience Proposal

We want to make a program that can calculate the relative power of a given Pokemon compared to all existing Pokemon. Pokemons have either one or two types (e.g. fire, grass, electric), and each type is either strong, netrual, or weak to other types (e.g. fire is strong versus grass). Apart from that Pokemons can learn different Moves that can either deal Physical damage or Special damage that are increased with the attacking Pokemon's stats and reduced by the defending Pokemon's stats.

### Data gathering

We have found an API that contains all the data we need: <https://pokeapi.co/>(Pokeapi)

### Data analysis

To begin with the plan is:

- To figure out whether a Pokemon should be used as a Physical or Special damage attack dealer, and find the strongest attack it can learn.
  - Scale the attack's damage with the Pokemon's attack stat and its STAB (Same Type Attack Bonus) modifier
  - Sum its defensive stats (HP, defense, special defense)
  - Determine how important the Speed stat is for the Pokemon

- Give the Pokemon a score compared to all other Pokemons

### Data visualization

Use a graphing tool, like Matplotlib, to show where the Pokemon is placed in power.

### Future nice-to-haves

- Figure out how strong a given Pokemon is compared to other strong Pokemons
