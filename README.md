# Sales Data Pipeline

This project implements a comprehensive data pipeline for analyzing sales data, integrating customer and weather data, and providing visual insights.

# Project Structure
The project is structured in the sales-data-pipeline directory as follows:

sales-data-pipeline/
│
├── src/
│   ├── __init__.py              # Starting point of the application
│   ├── config.py                # Configuration settings for the app
│   ├── data_fetcher.py          # Handles data fetching from APIs
│   ├── data_processor.py        # Processes data for aggregations and insights
│   ├── database_manager.py      # Manages database connections and operations
│   ├── models.py                # SQLAlchemy models for the database schema
│   ├── orchestrator.py          # Orchestrates the data fetching, processing, and storage
│   └── visualizer.py            # Creates visualizations of the data insights
│
├── plots/                       # Directory to store generated plots
│
├── Dockerfile                   # Dockerfile for building the application container
├── docker-compose.yml           # Docker Compose file to manage app and database services
├── requirements.txt             # Python dependencies
└── README.md                    # Instructions on setting up and running the project

## Project Setup

### Without Docker

#### Prerequisites
- Python 3.9+
- PostgreSQL

#### Installation
1. Clone the repository:
   git clone https://github.com/abhinavsharma8207/sales-data-pipeline.git
   cd sales-data-pipeline

2. Install Python dependencies:
   pip install -r requirements.txt

3. Set up the PostgreSQL database:
- Ensure PostgreSQL is running.
- Create a database and user as specified in your `.env` file.

4. Configure your `.env` file:
- Copy the `.env.example` to `.env`.
- Update the environment variables in `.env` according to your setup.

5. Run the application:
   python src/init.py

### With Docker

#### Prerequisites
- Docker
- Docker Compose

#### Running the Application
1. Build and run the application using Docker Compose:
   docker-compose up --build
This command starts all necessary services, including the PostgreSQL database and the application server, in Docker containers.

## Data Transformation Steps
The data pipeline performs several key transformations:
- **Sales Data Fetching:**  Sales data is fetched from sales_data.csv file which include order_id, customer_id, price, lat and lon details 
- **User Data Fetching:** User data is fetched from the JSONPlaceholder API. Fields such as user ID, name, and username are extracted.
- **Weather Data Integration:** For each sale, weather data is fetched based on the order location using the OpenWeatherMap API. Relevant weather details are included in the sales data.
- **Sales Data Processing:** Sales data is merged with the user and weather data based on user ID and timestamps.

### Assumptions
- All external API data matches with our sales data based on user ID and dates.
- The weather API provides accurate and timely weather data for the given locations.

## Database Schema
The transformed data is stored in three main tables:
- `customers`: Stores user data including ID, name, email, and geolocation.
- `sales`: Stores sales transactions with fields for date, product ID, quantity, and price.
- `weather`: Stores weather conditions related to each sale, linked via sale ID.

## Data Aggregations and Manipulations
The pipeline performs several aggregations to derive business insights:
- **Total Sales per Customer:** Calculates the total sales amount per customer.
- **Average Order Quantity per Product:** Determines the average quantity ordered for each product.
- **Top-Selling Products:** Identifies which products have the highest sales volumes.
- **Sales Trends:** Analyzes how sales figures change over time, broken down by month or quarter.
- **Impact of Weather on Sales:** Examines how different weather conditions affect sales volumes and amounts.

## Visualization
Visualizations are generated to represent these insights, helping to identify trends and anomalies in the sales data. These visualizations are stored in the `plots` directory.

