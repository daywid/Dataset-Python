import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def main():
    """
    This function reads a CSV file, handles missing values, and plots charts based on the data.
    """
    file_path = 'data.csv'
    data = pd.read_csv(file_path)

    print(data.isnull().sum())

    # Handle the missing values
    data['Year'] = data['Year'].fillna(data['Year'].mode()[0])

    # Impute missing values in categorical columns with mode
    data['Publisher'] = data['Publisher'].fillna(data['Publisher'].mode()[0])

    # Sum global sales by genre
    genre_sales = data.groupby('Genre')['Global_Sales'].sum().reset_index()
    plot_sales_by_genre(genre_sales)

    # sum global sales by year
    year_sales = data.groupby('Year')['Global_Sales'].sum().reset_index()
    plot_sales_by_year(year_sales)

    # Plot pie chart of global sales percentage by genre
    plot_sales_percentage_by_genre(genre_sales)


def plot_sales_by_genre(genre_sales):
    """
    Plot a bar chart of global sales by genre.
    """
    plt.figure(figsize=(10, 6))
    sns.barplot(x='Genre', y='Global_Sales', data=genre_sales)
    plt.title('Vendas Globais por Gênero')
    plt.xticks(rotation=45)
    plt.ylabel('Vendas Globais (milhões)')
    plt.xlabel('Gênero')
    plt.show()


def plot_sales_percentage_by_genre(genre_sales):
    """
    Plot a pie chart of global sales percentage by genre.
    """
    plt.figure(figsize=(10, 8))
    plt.pie(genre_sales['Global_Sales'], labels=genre_sales['Genre'], autopct='%1.1f%%', startangle=140, colors=sns
            .color_palette("husl", len(genre_sales)))
    plt.title('Distribuição Percentual das Vendas Globais por Gênero')
    plt.axis('equal')
    plt.show()


def plot_sales_by_year(year_sales):
    """
    Plot a line chart of global sales over time.
    """
    plt.figure(figsize=(12, 6))
    sns.lineplot(x='Year', y='Global_Sales', data=year_sales)
    plt.title('Vendas Globais ao Longo do Tempo')
    plt.ylabel('Vendas Globais (milhões)')
    plt.xlabel('Ano')
    plt.grid(True)
    plt.show()


if __name__ == '__main__':
    main()
