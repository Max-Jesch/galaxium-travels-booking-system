# Galaxium Travels Infrastructure

A comprehensive space travel booking system infrastructure featuring REST APIs, MCP servers, web applications, and supporting services for the fictional Galaxium Travels company.

## 🚀 Overview

This repository contains the complete infrastructure for Galaxium Travels, a futuristic space tourism company operating in the year 2125. The system demonstrates modern agentic AI capabilities through a modular, microservices architecture with enhanced error handling designed specifically for AI agent integration.

**Main Repository:** https://github.com/Max-Jesch/galaxium-travels

## 📋 Table of Contents

- [Recent Improvements](#recent-improvements-)
- [Architecture](#architecture)
- [Components](#components)
- [Quick Start](#quick-start)
- [Development](#development)
- [Testing](#testing)
- [Deployment](#deployment)
- [Agent Guidelines](#agent-guidelines)
- [License](#license)

## Recent Improvements 🆕

### Enhanced Error Messages for AI Agents
We've significantly improved error messages across all systems to make them more actionable for AI agents:

- **Clear Problem Identification**: Error messages now explain exactly what went wrong
- **Actionable Next Steps**: Specific suggestions for resolution are provided
- **Alternative Approaches**: Other endpoints or tools are suggested when applicable
- **AI-Friendly Format**: Messages are structured to help AI agents make decisions

**Examples:**
- **Before**: `"User not found"`
- **After**: `"User with ID 999 is not registered. Please register first using /register endpoint"`

See the [Error Handling Guide](booking_system_rest/docs/error-handling-guide.md) for detailed examples and the [Error Handling Examples](booking_system_rest/docs/error-handling-examples.md) for before/after comparisons.

### Comprehensive Testing Framework
- **100% Code Coverage** achieved for booking system REST API
- **34 Test Cases** covering all critical functionality
- **pytest** with FastAPI TestClient for integration testing
- See [Testing Guide](booking_system_rest/docs/testing-guide.md) for details

## 🏗️ Architecture

The system uses a microservices architecture with the following components:

```
┌─────────────────────────────────────────────────────────────┐
│                     Galaxium Travels                         │
├─────────────────────────────────────────────────────────────┤
│                                                               │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐      │
│  │   Web App    │  │  REST API    │  │  MCP Server  │      │
│  │  (Flask)     │  │  (FastAPI)   │  │  (MCP)       │      │
│  │  Port 8083   │  │  Port 8082   │  │  Port 8084   │      │
│  └──────┬───────┘  └──────┬───────┘  └──────┬───────┘      │
│         │                  │                  │               │
│         └──────────────────┴──────────────────┘              │
│                            │                                  │
│                   ┌────────▼────────┐                        │
│                   │   SQLite DB     │                        │
│                   │  (Bookings)     │                        │
│                   └─────────────────┘                        │
│                                                               │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐      │
│  │ HR Database  │  │  Graph RAG   │  │   Docling    │      │
│  │  (FastAPI)   │  │  (Knowledge) │  │  (PDF Proc)  │      │
│  │  Port 8081   │  │              │  │              │      │
│  └──────────────┘  └──────────────┘  └──────────────┘      │
│                                                               │
└─────────────────────────────────────────────────────────────┘
```

## 📦 Components

### 1. Booking System REST API
**Path:** `booking_system_rest/`

A FastAPI-based REST service for booking interplanetary flights with comprehensive test coverage.

**Features:**
- User registration and management
- Flight browsing and booking
- Booking management (view, cancel)
- Flight seat availability tracking
- Auto-seeded demo data on startup
- 100% test coverage with 34 test cases

**Port:** 8082

**Quick Start:**
```bash
cd booking_system_rest
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python seed.py
python app.py
```

**Testing:**
```bash
python run_tests.py all      # Run all tests with coverage
python run_tests.py fast     # Run tests without coverage
python run_tests.py user     # User management tests only
python run_tests.py booking  # Booking system tests only
python run_tests.py flight   # Flight management tests only
```

**Documentation:** [booking_system_rest/README.md](booking_system_rest/README.md)

### 2. Booking System MCP Server
**Path:** `booking_system_mcp/`

Model Context Protocol (MCP) server version of the booking system, designed for direct AI agent integration.

**Features:**
- Same functionality as REST API but via MCP tools
- Optimized for AI agent workflows
- Enhanced error messages for better agent understanding
- Intentional double-commit pattern for MCP context persistence

**Port:** 8084

**Quick Start:**
```bash
cd booking_system_mcp
pip install -r requirements.txt
python seed.py
python mcp_server.py
```

**Local Testing:**
```bash
export DANGEROUSLY_OMIT_AUTH=true
npx @modelcontextprotocol/inspector
```

**Documentation:** [booking_system_mcp/README.md](booking_system_mcp/README.md)

### 3. Web Application
**Path:** `galaxium-booking-web-app/`

A Flask-based user interface for flight bookings with a modern, responsive design.

**Features:**
- User-friendly interface for flight booking
- View available flights
- Manage user bookings
- Responsive design
- Containerized with Docker

**Port:** 8083

**Quick Start:**
```bash
cd galaxium-booking-web-app
cp .env-template .env
# Edit .env to set BACKEND_URL
cd app
pip install -r requirements.txt
python app.py
```

**Documentation:** [galaxium-booking-web-app/README.md](galaxium-booking-web-app/README.md)

### 4. HR Database Service
**Path:** `HR_database/`

HR database application with markdown backend for employee management.

**Features:**
- Employee CRUD operations
- Markdown-based data storage (human-readable)
- RESTful API endpoints
- Enhanced error handling for AI agents

**Port:** 8081

**API Endpoints:**
- `GET /employees` - List all employees
- `GET /employees/{employee_id}` - Get specific employee
- `POST /employees` - Create new employee
- `PUT /employees/{employee_id}` - Update employee
- `DELETE /employees/{employee_id}` - Delete employee

**Quick Start:**
```bash
cd HR_database
python3.12 -m venv .venv
source ./.venv/bin/activate
pip install -r requirements.txt
python app.py
```

**Documentation:** [HR_database/README.md](HR_database/README.md)

### 5. Graph RAG System
**Path:** `graph_rag/`

Knowledge graph system for company documentation using RAG (Retrieval-Augmented Generation).

**Features:**
- Process company documentation
- Build knowledge graphs
- Support for AI-powered queries
- Organized documentation structure

**Documentation Structure:**
- Corporate information and sustainability
- Customer service manuals
- HR policies and training
- Marketing materials and spacecraft specs
- Legal documents
- Technical documentation
- Financial data
- IT system architecture

### 6. Document Processing
**Path:** `docling/`

PDF processing capabilities using Docling for document extraction and analysis.

**Features:**
- PDF text extraction
- Document structure analysis
- Integration with knowledge systems

### 7. Model Gateway
**Path:** `model_gateway/`

LLM deployment configurations for various model providers.

**Features:**
- GPT service deployment
- JetGPT integration
- Model gateway configuration

## 🚀 Quick Start

### Run All Services with Docker Compose

The easiest way to run all services together:

```bash
cd local-container
bash start-containers.sh
```

This will start:
- HR Database on http://localhost:8081
- Booking REST API on http://localhost:8082
- Web Application on http://localhost:8083

**Services:**
- Web App: http://localhost:8083
- Booking API: http://localhost:8082/docs (Swagger UI)
- HR Database: http://localhost:8081/employees

### Individual Service Setup

Each service can be run independently. Navigate to the service directory and follow its README.md instructions.

## 🛠️ Development

### Prerequisites
- Python 3.9+ (Python 3.12 recommended)
- pip
- Docker (for containerized deployment)
- (Optional) Fly.io CLI or IBM Code Engine CLI for cloud deployment

### Project Structure

```
galaxium-travels-infrastructure/
├── booking_system_rest/      # FastAPI REST API with SQLite
├── booking_system_mcp/       # MCP server version
├── galaxium-booking-web-app/ # Flask web interface
├── HR_database/              # HR database with markdown backend
├── graph_rag/                # Knowledge graph system
├── docling/                  # PDF processing
├── model_gateway/            # LLM deployment configs
├── local-container/          # Docker Compose setup
├── architecture/             # Architecture diagrams
├── images/                   # Documentation images
├── AGENTS.md                 # Agent development guidelines
└── README.md                 # This file
```

### Environment Configuration

Each service has an `.env-template` file. Copy it to `.env` and configure:

```bash
# Example for booking_system_rest
cd booking_system_rest
cp .env-template .env
# Edit .env with your configuration
```

## 🧪 Testing

### Booking System REST API

Comprehensive test suite with 100% coverage:

```bash
cd booking_system_rest

# Run all tests with coverage report
python run_tests.py all

# Run tests without coverage (faster)
python run_tests.py fast

# Run specific test categories
python run_tests.py user      # User management tests
python run_tests.py booking   # Booking system tests
python run_tests.py flight    # Flight management tests

# Run single test file
python -m pytest tests/test_user_management.py -v

# Run specific test
python -m pytest tests/test_user_management.py::TestUserRegistration::test_register_user_success -v
```

See [Testing Guide](booking_system_rest/TESTING.md) for detailed testing documentation.

## 🚢 Deployment

### Docker Compose (Local)

```bash
cd local-container
bash start-containers.sh
```

### IBM Code Engine

Each service includes deployment notebooks and configurations for IBM Code Engine:
- `booking_system_rest/deployment_rest_server.ipynb`
- `booking_system_mcp/deployment_mcp_server.ipynb`
- `galaxium-booking-web-app/deployment_web_application_server.ipynb`

### Fly.io

Each service can be deployed independently to Fly.io. See individual service READMEs for deployment instructions.

### Building Containers

```bash
cd local-container
bash build-containers.sh
```

## 🤖 Agent Guidelines

This project includes comprehensive guidelines for AI agents working with the codebase. See [AGENTS.md](AGENTS.md) for:

- Testing commands and patterns
- Critical non-obvious patterns (e.g., double-commit pattern in MCP server)
- Error response patterns
- Database configuration details
- Port assignments
- Docker Compose environment setup
- Pydantic configuration
- Test coverage configuration

**Key Points for Agents:**
- Business logic errors return 200 status codes with error details in body
- MCP server uses intentional double commits for proper persistence
- Tests use StaticPool for in-memory SQLite isolation
- HR database uses markdown tables parsed as CSV
- Non-standard port assignments (8081-8084)

## 📚 Documentation

- **[AGENTS.md](AGENTS.md)**: Guidelines for AI agents working with the codebase
- **[Error Handling Guide](booking_system_rest/docs/error-handling-guide.md)**: Comprehensive error message improvements
- **[Error Handling Examples](booking_system_rest/docs/error-handling-examples.md)**: Before/after examples with AI agent actions
- **[Testing Guide](booking_system_rest/docs/testing-guide.md)**: How to test the improved error handling
- **[TESTING.md](booking_system_rest/TESTING.md)**: Detailed testing documentation

## 🤝 Contributing

Feel free to fork, open issues, or submit pull requests for improvements or new demo applications!

## 📄 License

See [LICENSE](LICENSE) file for details.

---

**This repository is for demonstration and prototyping purposes only.**

Built to showcase agentic AI capabilities in a modular, microservices architecture with enhanced error handling and comprehensive testing.