import pandas as pd
import matplotlib.pyplot as plt


def read_csv():
    # Read dataset from csv
    gapminder_all_data = pd.read_csv("data/gapminder_all.csv")
    # Create dataframe from raw data
    gapminder_all_raw_df = pd.DataFrame(gapminder_all_data)
    return gapminder_all_raw_df


def pivot_data_wide_to_long(df):
    # Melt the dataframe to transform it into long format
    gapminder_all_melted_df = pd.melt(df, id_vars=["continent", "country"], var_name="year")
    # Split the year column to get gdp_perCap, lifeExp, and pop separately
    gapminder_all_melted_df[["measure", "year"]] = gapminder_all_melted_df["year"].str.split("_", expand=True)
    # Pivot the dataframe using the measures column
    gapminder_all_pivoted_df = gapminder_all_melted_df.pivot_table(index=["continent", "country", "year"],
                                                                   columns="measure", values="value").reset_index()
    return gapminder_all_pivoted_df


def filter_data_equal_to(df, column, value):
    # filters a dataframe where column equals value
    return df[(df[f"{column}"] == f"{value}")]


def scatter_plot(df1, df1_label, df2, df2_label, x_axis, y_axis):
    # sets the size of the window
    plt.figure(figsize=(10, 6))
    # creates a scatter plot based on the given dataframe
    plt.scatter(df1[x_axis], df1[y_axis], color="r", label=f"{df1_label}", alpha=0.5)
    plt.scatter(df2[x_axis], df2[y_axis], color="b", label=f"{df2_label}", alpha=0.5)
    # Add title and labels
    plt.title("Total GDP of Australia and New Zealand across time")
    plt.xlabel("Year")
    plt.ylabel("GDP per capita")
    plt.legend()
    # Show the plot
    plt.show()


if __name__ == "__main__":
    base_df = read_csv()
    transformed_df = pivot_data_wide_to_long(base_df)
    oceania_df = filter_data_equal_to(transformed_df, "continent", "Oceania")
    australia_df = filter_data_equal_to(oceania_df, "country", "Australia")
    new_zealand_df = filter_data_equal_to(oceania_df, "country", "New Zealand")
    scatter_plot(australia_df, "Australia", new_zealand_df, "New Zealand", "year",
                 "gdpPercap")
