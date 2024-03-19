# Kuro - Unofficial MyFigureCollection REST API

Kuro is a REST API built using Flask that interacts with data from [MyFigureCollection](https://myfigurecollection.net/). This API allows users to retrieve information about figures, entries, and collections available on the MyFigureCollection website. It leverages web scraping techniques through open-source libraries to gather data dynamically from the MyFigureCollection website, ensuring that users have access to the latest information.

## Features:
- **Item Data Retrieval:** Fetch detailed information about a specific figure using its ID.
- **Entry Data Retrieval:** Retrieve entries along with pagination support.
- **User-Owned Collection:** Access a user's owned figure collection with pagination.
- **User-Ordered Collection:** Fetch a user's ordered figure collection with pagination.
- **User-Wished Collection:** Retrieve a user's wished figure collection with pagination.
- **Latest Figures:** Get information about the latest figures added to the collection with pagination.

## Endpoints:
- `/v1/items/<item_id>`: Retrieve data for a specific figure.
- `/v1/entry/<entry_id>/<page_number>`: Retrieve entries for a given entry ID with pagination.
- `/v1/profile/<username>/collection/owned/<page_number>`: Retrieve owned figure collection for a user with pagination.
- `/v1/profile/<username>/collection/ordered/<page_number>`: Retrieve ordered figure collection for a user with pagination.
- `/v1/profile/<username>/collection/wished/<page_number>`: Retrieve wished figure collection for a user with pagination.
- `/v1/latest/<page_number>`: Retrieve the latest figures with pagination.
- `/v1/items/onfire`: Retrieve figures that are currently trending.
- `/v1/items/most_wished`: Retrieve figures that are most wished by users.
- `/v1/items/most_ordered`: Retrieve figures that are most ordered by users.
- `/v1/items/most_owned`: Retrieve figures that are most owned by users.
- `/v1/items/most_rated`: Retrieve figures that are most highly rated by users.
- `/v1/items/most_viewed`: Retrieve figures that are most viewed by users.
- `/v1/items/releases/<year>/<month>/<day>`: Retrieve figures released on a specific date.
- `/v1/profile/<username>`: Retrieve profile information for a user.

## Installation:
1. Clone the repository:
   ```
   bash git clone https://github.com/your-username/Kuro.git

2. Navigate to the project directory:
   ```
   cd Kuro
   
3. Install dependencies:
   ```
   pip install -r requirements.txt

4. Run the application:
   ```
   python main.py

4. The API will be available at http://127.0.0.1:9192/

## Usage:
- Use the provided endpoints to retrieve data about figures, entries, and collections from MyFigureCollection.
- Make HTTP GET requests to the respective endpoints with appropriate parameters to fetch the desired information.

## Contribution

Contributions to Kuro are welcomed and encouraged! If you'd like to contribute to the project, please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature/contribution`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature/contribution`).
6. Create a new Pull Request.

Please ensure that your contributions adhere to the project's coding standards and follow the guidelines in the [CONTRIBUTING.md](CONTRIBUTING.md) file.

If you have any questions or need assistance, feel free to open an issue or reach out to the project maintainers.

## Disclaimer:
This project is intended for facilitating access to data from MyFigureCollection. Please ensure compliance with MyFigureCollection's terms of service and policies when using this API. Use responsibly and ethically.

## License:
This project is licensed under the [MIT License](LICENSE).
