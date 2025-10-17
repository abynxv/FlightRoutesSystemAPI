# FlightRoutesSystemAPI

A simple Django REST Framework API to manage airport routes and perform queries like finding the Nth node, longest duration, and shortest path between airports.

### Installation

```bash
# Clone the repository
git clone git@github.com:abynxv/FlightRoutesSystemAPI.git
cd FlightRoutesSystemAPI

# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

### Run the Server
python manage.py runserver
```

The server will start at: **http://127.0.0.1:8000/**

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/route/add/` | POST | Add a new airport route with code, position, and duration |
| `/api/route/nth-node/` | GET | Find the Nth node from left or right |
| `/api/route/longest/` | GET | Get the airport with the longest duration |
| `/api/route/shortest/` | GET | Find shortest duration path between two airports |


## Tech Stack

- Django
- Django REST Framework
- SQLite (default database)

## Testing

Use Postman, cURL, or any API client to test the endpoints.
