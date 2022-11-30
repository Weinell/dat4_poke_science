from src.ApiToCsv import read_pokemon_data


def plot_types():
    # Plotting all pokemon type_1
    pokemons = read_pokemon_data("../../data/pokemon.csv")
    poke_types = pokemons["Type_1"].value_counts()
    plt = poke_types.plot(kind="pie", title="Pokemon types 1", autopct="%1.1f%%", legend=True, figsize=(9, 6))
    plt.legend(loc="center right", bbox_to_anchor=(1.3, 0.5))
    fig = plt.get_figure()
    fig.savefig("types.png")


def plot_types_2():
    # Dropping NoType
    pokemons = read_pokemon_data("../../data/pokemon.csv")

    poke_types = pokemons.drop(pokemons[pokemons["Type_2"] == "noType"].index)
    poke_types = poke_types["Type_2"].value_counts()

    plt = poke_types.plot(kind="pie", title="Pokemon types 2", autopct="%1.1f%%", legend=True,
                          figsize=(9, 6))
    plt.legend(loc="center right", bbox_to_anchor=(1.3, 0.5))
    fig = plt.get_figure()
    fig.savefig("types_2.png")


def plot_legendaries():
    pokemons = read_pokemon_data("../../data/pokemon.csv")
    legendaries = pokemons["Is_Legendary"].value_counts()
    plt = legendaries.plot(kind="pie",
                           title="Percentage of legendaries in dataset \n (True represents a Legendary Pokemon)",
                           autopct="%1.1f%%")

    fig = plt.get_figure()
    fig.savefig("legendaries.png")


if __name__ == "__main__":
    plot_types()
    # plot_types_2()
