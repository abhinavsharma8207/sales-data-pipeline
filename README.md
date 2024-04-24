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