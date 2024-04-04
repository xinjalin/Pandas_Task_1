import pandas as pd
import matplotlib.pyplot as plt


def read_and_transform_data():
    # Read dataset from csv
    gapminder_all_data = pd.read_csv("data/gapminder_all.csv")
    # Create dataframe from raw data
    gapminder_all_raw_df = pd.DataFrame(gapminder_all_data)
    # Melt the dataframe to transform it into long format
    gapminder_all_melted_df = pd.melt(gapminder_all_raw_df, id_vars=["continent", "country"], var_name="year")
    # Split the year column to get gdp_perCap, lifeExp, and pop separately
    gapminder_all_melted_df[["measure", "year"]] = gapminder_all_melted_df["year"].str.split("_", expand=True)
    # Pivot the dataframe
    gapminder_all_pivoted_df = gapminder_all_melted_df.pivot_table(index=["continent", "country", "year"],
                                                                   columns="measure", values="value").reset_index()

    return gapminder_all_pivoted_df


def filter_data_equal_to(df, column, value):
    # filters a dataframe where column equals value
    return df[(df[f"{column}"] == f"{value}")]


def scatter_plot(df, x_axis, y_axis):
    # creates a scatter plot based on the given dataframe
    df.plot.scatter(x=f"{x_axis}", y=f"{y_axis}", c="DarkBlue")
    # Add title and labels
    plt.title("Total GDP of Australia and New Zealand across time")
    plt.xlabel("Year")
    plt.ylabel("GDP per cap")
    # Show the plot
    plt.show()


if __name__ == "__main__":
    data = read_and_transform_data()
    oceania_df = filter_data_equal_to(data, "continent", "Oceania")
    scatter_plot(oceania_df, "year", "gdpPercap")
