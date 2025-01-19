# OliveChainAPI

**Modernizing Tunisia's Olive Oil Industry**

## Project Overview

The **OliveChainAPI** is a RESTful API designed to streamline and modernize the olive oil production process in Tunisia. By addressing inefficiencies in traditional practices, the API introduces traceability, scalability, and enhanced quality assurance. The project integrates cutting-edge technologies like **OAuth 2.0 authentication**, **PostgreSQL** for data management, and **Swagger** for comprehensive API documentation.

---

## Features

- **Harvest Management**: Record and manage olive collection data.
- **Milling Management**: Track and update milling processes in real-time.
- **Quality Assurance**: Log and monitor quality control metrics.
- **Logistics Management**: Manage and trace transportation and delivery operations.
- **Authentication**: Secure access with OAuth 2.0 and role-based permissions.
- **Comprehensive Documentation**: Swagger UI for API visualization and testing.

---

## Technologies

- **Backend Framework**: Flask
- **Database**: PostgreSQL
- **Authentication**: OAuth 2.0 (Google)
- **Documentation**: Swagger (via Flask-RESTx)
- **Testing**: Insomnia

---

## System Architecture

The OliveChainAPI follows a modular architecture:

1. **User Interaction Layer**: API endpoints for data interaction and retrieval.
2. **Backend Layer**: RESTful services for CRUD operations.
3. **Database Layer**: Relational database schema with normalized tables.
4. **Security Layer**: OAuth 2.0, role-based access control, and token validation.

---

## Setup Instructions

### 1. Set up a Virtual Environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 2. Install Required Dependencies:

```bash
pip install -r requirements.txt
```

### 3. Configure Environment Variables:

- `GOOGLE_CLIENT_ID`
- `GOOGLE_CLIENT_SECRET`
- `SECRET_KEY`
- `DATABASE_URI` (e.g., `postgresql://username:password@localhost/olive_chain_db`)

### 4. Initialize the Database:

```bash
flask db upgrade
```

### 5. Start the Flask Application:

```bash
flask run --port=8000
```

---

## API Documentation

Interactive API documentation is accessible at:

```
http://127.0.0.1:8000/swagger-ui/
```

---

## Testing the API

Use Swagger UI or Insomnia to test the following endpoints:

### Harvest:
- `POST /harvest`
- `GET /harvest`
- `GET /harvest/{id}`
- `PUT /harvest/{id}`
- `DELETE /harvest/{id}`

### Milling:
- `POST /milling`
- `GET /milling`
- `GET /milling/{id}`
- `PUT /milling/{id}`
- `DELETE /milling/{id}`

### Quality Assurance:
- `POST /quality`
- `GET /quality`
- `GET /quality/{id}`
- `PUT /quality/{id}`
- `DELETE /quality/{id}`

### Logistics:
- `POST /logistics`
- `GET /logistics`
- `GET /logistics/{id}`
- `PUT /logistics/{id}`
- `DELETE /logistics/{id}`

### Authentication:
- `POST /auth/register`
- `POST /auth/login`

---

## Results and Insights

- Enhanced traceability and operational efficiency in olive oil production.
- Streamlined authentication using OAuth 2.0.
- Comprehensive API testing and documentation using Swagger.

---

## Future Work

- **Real-Time Notifications**: Email/SMS alerts for significant events.
- **IoT Integration**: Climate monitoring to optimize production cycles.
- **Predictive Analytics**: Insights into yield trends and quality metrics.
- **Mobile Application**: Simplified access for farmers and mill operators.

---

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---

## Contributing

We welcome contributions! Please open an issue or submit a pull request for any enhancements or bug fixes.

---

### Developed by:
Maram Abdallah  
**Date**: 19/01/2025





