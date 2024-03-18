# Kuro - MyFigureCollection REST API

Kuro is a REST API built using Flask that interacts with data from [MyFigureCollection](https://myfigurecollection.net/). This API allows users to retrieve information about figures, entries, and collections available on the MyFigureCollection website.

## Features:
- **Item Data Retrieval:** Fetch detailed information about a specific figure using its ID.
- **Entry Data Retrieval:** Retrieve entries along with pagination support.
- **User-Owned Collection:** Access a user's owned figure collection with pagination.
- **User-Ordered Collection:** Fetch a user's ordered figure collection with pagination.
- **User-Wished Collection:** Retrieve a user's wished figure collection with pagination.
- **Latest Figures:** Get information about the latest figures added to the collection with pagination.

## Endpoints:
- `/items/<item_id>`: Retrieve data for a specific figure.
- `/entry/<entry_id>/<page_number>`: Retrieve entries for a given entry ID with pagination.
- `/profile/<username>/collection/owned/<page_number>`: Retrieve owned figure collection for a user with pagination.
- `/profile/<username>/collection/ordered/<page_number>`: Retrieve ordered figure collection for a user with pagination.
- `/profile/<username>/collection/wished/<page_number>`: Retrieve wished figure collection for a user with pagination.
- `/latest/<page_number>`: Retrieve the latest figures with pagination.

## Installation:
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/Kuro.git
