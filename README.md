# Vehicle-Maintenance-API

##​# Setup instructions.
### Clone the repository
git clone https://github.com/faith-hopewachira/Vehicle-Maintenance-Test-API.git
cd Vehicle-Maintenance-Test-API

### Create and activate a virtual environment
python3 -m venv env
source env/bin/activate

### Set up the database
python3 manage.py migrate

### Run the development server
python3 manage.py runserver


## How to Run the API
http://127.0.0.1:8000/


## Example API requests and responses.
### Create a New Maintenance Task
#### POST /api/tasks/→ Create a new maintenance task.
**Request:**
```json
{
  "vehicle_reg_no": "KDR 708P",
  "maintenance_type": "Engine",
  "description": "troubleshoot issues within a vehicle's engine",
  "next_due_date": "2025-04-08",
  "technician": "Paul Clement",
  "status": "completed"
}


Response
{
    "maintence_id": 7,
    "vehicle_reg_no": "KDR 708P",
    "maintenance_type": "Engine",
    "description": "troubleshoot issues within a vehicle's engine",
    "maintenance_date": "2025-03-09T16:30:31.006466Z",
    "next_due_date": "2025-04-08T00:00:00Z",
    "technician": "Paul Clement",
    "status": "completed"
}
```


#### GET /api/tasks/ → Retrieve a list of all maintenance tasks.
**Response:**
```json
[
    {
        "maintence_id": 1,
        "vehicle_reg_no": "KBX 149Q",
        "maintenance_type": "Brake Inspection",
        "description": "Checked brake pads and replaced worn-out ones.",
        "maintenance_date": "2025-03-08T07:46:36.358311Z",
        "next_due_date": "2024-06-08T00:00:00Z",
        "technician": "Peter Kariuki",
        "status": "pending"
    },
    {
        "maintence_id": 4,
        "vehicle_reg_no": "KBC 507Q",
        "maintenance_type": "Oil changes",
        "description": "Changed the oil",
        "maintenance_date": "2025-03-08T12:49:05.410357Z",
        "next_due_date": "2025-04-08T00:00:00Z",
        "technician": "Paul Clement",
        "status": "pending"
    },
    {
        "maintence_id": 5,
        "vehicle_reg_no": "KBC 507Q",
        "maintenance_type": "Engine",
        "description": "troubleshoot issues within a vehicle's engine",
        "maintenance_date": "2025-03-08T12:56:00.582241Z",
        "next_due_date": "2025-04-08T00:00:00Z",
        "technician": "Paul Clement",
        "status": "completed"
    },
    {
        "maintence_id": 6,
        "vehicle_reg_no": "KDP 707P",
        "maintenance_type": "Engine",
        "description": "troubleshoot issues within a vehicle's engine",
        "maintenance_date": "2025-03-09T16:25:20.929242Z",
        "next_due_date": "2025-04-08T00:00:00Z",
        "technician": "Paul Clement",
        "status": "completed"
    },
    {
        "maintence_id": 7,
        "vehicle_reg_no": "KDR 708P",
        "maintenance_type": "Engine",
        "description": "troubleshoot issues within a vehicle's engine",
        "maintenance_date": "2025-03-09T16:30:31.006466Z",
        "next_due_date": "2025-04-08T00:00:00Z",
        "technician": "Paul Clement",
        "status": "completed"
    }
]
```

#### GET /api/tasks/{id}/ → Retrieve details of a specific maintenance task by ID.

**Response:**
```json
{
    "maintence_id": 1,
    "vehicle_reg_no": "KBX 149Q",
    "maintenance_type": "Brake Inspection",
    "description": "Checked brake pads and replaced worn-out ones.",
    "maintenance_date": "2025-03-08T07:46:36.358311Z",
    "next_due_date": "2024-06-08T00:00:00Z",
    "technician": "Peter Kariuki",
    "status": "pending"
}
```


#### PATCH /api/tasks/{id}/ → Update an existing maintenance task.
**Request:**
```json
{
  "technician": "Jake Clement",
}

Response
{
    "maintence_id": 6,
    "vehicle_reg_no": "KDR 708P",
    "maintenance_type": "Engine",
    "description": "troubleshoot issues within a vehicle's engine",
    "maintenance_date": "2025-03-09T16:25:20.929242Z",
    "next_due_date": "2025-04-08T00:00:00Z",
    "technician": "Jake Clement",
    "status": "completed"
}
```

#### DELETE /api/tasks/{id}/ → Remove a maintenance task if recorded incorrectly.

**Response:**
```json
{
    "detail": "Maintenance task with ID 5 has been successfully deleted."
}

```

#### Add a filter to the GET /tasks/ endpoint to filter tasks by vehicle registration number.
##### GET /api/tasks/?vehicle_reg_no={vehicle_reg_no}
**Response:**
```json
[
    {
        "maintence_id": 6,
        "vehicle_reg_no": "KDR 708P",
        "maintenance_type": "Engine",
        "description": "troubleshoot issues within a vehicle's engine",
        "maintenance_date": "2025-03-09T16:25:20.929242Z",
        "next_due_date": "2025-04-08T00:00:00Z",
        "technician": "Jake Clement",
        "status": "completed"
    },
    {
        "maintence_id": 7,
        "vehicle_reg_no": "KDR 708P",
        "maintenance_type": "Engine",
        "description": "troubleshoot issues within a vehicle's engine",
        "maintenance_date": "2025-03-09T16:30:31.006466Z",
        "next_due_date": "2025-04-08T00:00:00Z",
        "technician": "Paul Clement",
        "status": "completed"
    }
]

```


