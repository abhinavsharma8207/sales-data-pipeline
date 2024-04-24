import sched
import time
import pandas as pd

from src.config import Config
from src.data_fetcher import APIDataFetcher
from src.data_processor import DataProcessor
from src.database_manager import DatabaseManager
from src.visualizer import plot_total_sales_per_customer, plot_sales_trends, plot_weather_impact_on_sales


class PipelineOrchestrator:
    def __init__(self, scheduler):
        self.config = Config()
        self.scheduler = scheduler
        self.data_fetcher = APIDataFetcher(self.config)
        self.db_manager = DatabaseManager(self.config.postgresql_conn_string)
        self.db_manager.create_database()

    def run_pipeline(self):
        print("Pipeline is running...")
        sales_data = pd.read_csv(self.config.sales_data_csv)
        user_data = self.data_fetcher.fetch_user_data()
        self.db_manager.load_to_database(user_data, 'customer')
        self.db_manager.load_to_database(sales_data, 'sales')
        sales_lat_lon_list = sales_data[['order_id', 'lat', 'lon']].to_dict(orient='records')
        print(sales_lat_lon_list)
        weather_data = self.data_fetcher.fetch_weather_data(sales_lat_lon_list)
        self.db_manager.load_to_database(weather_data, 'sales_weather')
        processor = DataProcessor()
        merged_data = processor.transform_and_merge(sales_data, user_data, weather_data)
        aggregated_data = processor.perform_aggregations(merged_data)

        for key, df in aggregated_data.items():
            self.db_manager.load_to_database(df, key)
            if key == "total_sales_per_customer":
                plot_total_sales_per_customer(df)
            if key == "sales_trends":
                plot_sales_trends(df)
            if key == "sales_per_weather_condition":
                plot_weather_impact_on_sales(df)
        print("Pipeline executed successfully. Check aggregation tables in database and check the plots folder by "
              "right-clicking and opening it in Windows "
              "Explorer or "
              "Finder in Mac for visualizations as the app is still running")
        self.schedule_run(600)

    def schedule_run(self, interval):
        # Schedule the next pipeline run
        self.scheduler.enter(interval, 1, self.run_pipeline)

    def start(self):
        # Start the scheduler
        self.schedule_run(600)  # Schedule the first run in 600 seconds (10 minutes)
        self.scheduler.run()

    def start_immediately(self):
        # Execute immediately for the first time
        self.run_pipeline()
        # Then continue with normal scheduling
        self.scheduler.run()
