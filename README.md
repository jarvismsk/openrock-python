# OpenRock Python Project

## Overview

The OpenRock Python Project is part of the OpenRock initiative, which aims to provide open-source datasets and models for data science and machine learning enthusiasts. This Python project serves as a backend API for managing and retrieving data related to financial markets.

## Features

- **Save Data**: Save user input data to a text file.
- **Retrieve Historical Data**: Retrieve historical data from CSV files.
- **Paginated Data**: Retrieve paginated historical data.
- **Cross-Origin Support**: Allow specific origins to access API endpoints.

## Why OpenRock?

OpenRock is committed to democratizing access to financial data and machine learning resources. Our mission is to empower researchers, students, and developers by providing free and open access to high-quality datasets and models. By contributing to OpenRock, you're contributing to a community that believes in the power of open-source collaboration.

## Usage

- **Save Data**: Send a POST request to `/api/saveData` with JSON data.
- **Retrieve Historical Data**: Send a GET request to `/api/getAllHistoricalData` or `/api/getHistoricalData` with appropriate parameters.
- **Pagination**: Use the `page` parameter to paginate results.

## License

This project is licensed under the MIT License 
