from src.ApiToCsv import read_pokemon_data


def plot_types():
    # Plotting all pokemon type_1
    pokemons = read_pokemon_data("../../data/pokemon.csv")
    poke_types = pokemons["Type_1"].value_counts()
    plt = poke_types.plot(kind="pie", title="Pokemon types", autopct="%1.1f%%", legend=True, figsize=(9, 6))
    plt.legend(loc="center right", bbox_to_anchor=(1.3, 0.5))
    fig = plt.get_figure()
    fig.savefig("types.png")

    # plotting both types with NoType
    poke_types_both = pokemons[["Type_1", "Type_2"]].value_counts()
    plt_2 = poke_types_both.plot(kind="pie", title="Pokemon types both", autopct="%1.1f%%", legend=True, figsize=(9, 6))
    plt_2.legend(loc="center right", bbox_to_anchor=(1.3, 0.5))
    fig_2 = plt_2.get_figure()
    fig_2.savefig("types_both.png")

    # Dropping NoType
    poke_types_drop = pokemons[["Type_1", "Type_2"]]
    pbt = poke_types_drop

    pbt = poke_types_drop.drop(pbt[pbt["Type_2"] == "noType"].index)
    pbt = pbt.value_counts()
    plt_3 = pbt.plot(kind="pie", title="Pokemon types both \n (noType dropped))", autopct="%1.1f%%", legend=True, figsize=(9, 6))
    plt_3.legend(loc="center right", bbox_to_anchor=(1.3, 0.5))
    fig_3 = plt_3.get_figure()
    fig_3.savefig("types_both_dropped.png")


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
