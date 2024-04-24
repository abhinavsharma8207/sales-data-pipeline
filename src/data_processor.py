import pandas as pd


class DataProcessor:
    @staticmethod
    def transform_and_merge(sales_data, user_data, weather_data):
        merged_data = sales_data.merge(user_data, left_on='customer_id', right_on='id', how='left')
        merged_data = merged_data.merge(weather_data, left_on='order_id', right_on='order_id', how='left')
        return merged_data

    @staticmethod
    def perform_aggregations(merged_data):
        # Ensure 'order_date' is in the correct datetime format
        merged_data['order_date'] = pd.to_datetime(merged_data['order_date'])

        # Aggregations
        # Total sales amount per customer
        total_sales_per_customer_df = merged_data.groupby(['customer_id', 'username'])['price'].sum().reset_index()
        total_sales_per_customer_df.columns = ['customer_id', 'username', 'total_sales']

        # Average order quantity per product
        average_order_quantity_df = merged_data.groupby('product_id')['quantity'].mean().reset_index()
        average_order_quantity_df.columns = ['product_id', 'average_quantity']

        # Top-selling products
        top_selling_products_df = merged_data.groupby('product_id')['price'].sum().nlargest(3).reset_index()
        top_selling_products_df.columns = ['product_id', 'total_revenue']

        # Top-selling customers
        top_selling_customers_df = merged_data.groupby(['customer_id', 'username'])['price'].sum().nlargest(3).reset_index()
        top_selling_customers_df.columns = ['customer_id', 'username', 'total_revenue']

        # Sales trends over time (monthly)
        merged_data.set_index('order_date', inplace=True)
        sales_trends_df = merged_data.resample('M')['price'].sum().reset_index()
        sales_trends_df.columns = ['month', 'total_sales']
        merged_data.reset_index(inplace=True)  # Reset index for other operations

        # Average sales amount per weather condition
        sales_per_weather_condition_df = merged_data.groupby('weather')['price'].mean().reset_index()
        sales_per_weather_condition_df.columns = ['weather_condition', 'average_sales']

        return {
            'total_sales_per_customer': total_sales_per_customer_df,
            'average_order_quantity': average_order_quantity_df,
            'top_selling_products': top_selling_products_df,
            'top_selling_customers': top_selling_customers_df,
            'sales_trends': sales_trends_df,
            'sales_per_weather_condition': sales_per_weather_condition_df
        }
