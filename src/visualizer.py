import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import warnings

# Suppress specific FutureWarnings regarding Seaborn
warnings.filterwarnings("ignore", category=FutureWarning, message="Passing `palette` without assigning `hue`")


def plot_weather_impact_on_sales(data):
    # Visualize the impact of weather conditions on sales
    plt.figure(figsize=(10, 6))
    weather_sales = data.groupby('weather_condition')['average_sales'].sum().reset_index()
    sns.barplot(x='weather_condition', y='average_sales', data=weather_sales, palette='coolwarm', legend=False, hue='weather_condition')
    plt.title('Impact of Weather Conditions on Sales')
    plt.xlabel('Weather Condition')
    plt.ylabel('Total Sales')
    plt.xticks(rotation=45)
    plt.savefig('./plots/weather_impact_on_sales.png')
    plt.close()


def plot_total_sales_per_customer(data):
    # Generate plot for top 10 customers by total sales
    plt.figure(figsize=(10, 6))
    total_sales = data.groupby('username')['total_sales'].sum().reset_index()
    top_customers = total_sales.sort_values(by='total_sales', ascending=False).head(10)
    sns.barplot(x='username', y='total_sales', data=top_customers, palette='viridis', legend=False, hue='username')
    plt.title('Top 10 Customers by Total Sales')
    plt.xlabel('Customer')
    plt.ylabel('Total Sales Amount')
    plt.xticks(rotation=45)
    plt.savefig('./plots/total_sales_per_customer.png')
    plt.close()


def plot_sales_trends(data):
    # Plot monthly sales trends
    plt.figure(figsize=(12, 7))
    data['month'] = pd.to_datetime(data['month'])
    sales_trends = data.set_index('month')['total_sales']
    sales_trends.plot()
    plt.title('Monthly Sales Trends')
    plt.xlabel('Month')
    plt.ylabel('Total Sales')
    plt.grid(True)
    plt.savefig('./plots/sales_trends.png')
    plt.close()
