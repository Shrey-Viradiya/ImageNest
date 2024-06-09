# ImageNest

ImageNest is a Python application built with FastAPI. It allows users to create and manage boards and pins.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python 3.9
- Docker
- PostgreSQL

### Installation

1. Clone the repository
```bash
git clone https://github.com/Shrey-Viradiya/ImageNest.git
```

2. Navigate to the project directory
```bash
cd ImageNest
```

3. Install the required Python packages
```bash
pip install -r requirements.txt
```

4. Start the PostgreSQL Docker container
```bash
docker run --name imagenest-postgres -e POSTGRES_PASSWORD=password -e POSTGRES_DB=imagenest -p 5432:5432 -d postgres
```

### Running the Application

To run the application, use the following command:

```bash
fastapi dev src/main.py
```
