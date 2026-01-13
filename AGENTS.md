# AGENTS.md

This file provides guidance to agents when working with code in this repository.

## Testing Commands (booking_system_rest)

**Run single test file:**
```bash
cd booking_system_rest
python -m pytest tests/test_user_management.py -v
```

**Run specific test:**
```bash
python -m pytest tests/test_user_management.py::TestUserRegistration::test_register_user_success -v
```

**Test runner shortcuts:**
```bash
python run_tests.py user      # User tests only
python run_tests.py booking   # Booking tests only
python run_tests.py flight    # Flight tests only
python run_tests.py fast      # No coverage (faster)
```

## Critical Non-Obvious Patterns

### Database Double-Commit Pattern (MCP Server)
The MCP server uses **intentional double commits** in `book_flight()`:
```python
db.commit()
db.refresh(new_booking)
db.commit()  # Second commit is required for MCP context
```
This is NOT a bug - it's required for the MCP server to properly persist bookings. Do not remove.

### Error Response Pattern (REST API)
Business logic errors return **200 status codes** with error details in body:
```python
return JSONResponse(
    status_code=200,  # Always 200 for business errors
    content={"success": false, "error": "...", "error_code": "..."}
)
```
Only fatal errors (database failures) use 500 status codes. This is intentional for AI agent compatibility.

### Test Database Isolation
Tests use `StaticPool` for in-memory SQLite to prevent threading issues:
```python
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,  # Required for test isolation
)
```

### HR Database Format
HR database uses **markdown tables** parsed as CSV with specific column handling:
```python
df = pd.read_csv('data/employees.md', sep='|', skiprows=3)
df = df.iloc[:, 1:-1]  # Must remove first/last empty columns
```

### Port Assignments (Non-Standard)
- HR Database: 8081
- Booking REST: 8082
- Web App: 8083
- Booking MCP: 8084

### Docker Compose Environment
The `start-containers.sh` script sources `.env` files from **parent directories**:
```bash
source $(pwd)/../booking_system_rest/.env
source $(pwd)/../galaxium-booking-web-app/.env
```
Run from `local-container/` directory only.

### Pydantic Configuration
Models use `from_attributes = True` (not deprecated `orm_mode`):
```python
class Config:
    from_attributes = True  # Required for SQLAlchemy ORM
```

### MCP Server Startup
MCP server requires database seeding before starting:
```bash
python seed.py  # Must run first
python mcp_server.py  # Then start server
```

### Test Coverage Configuration
Coverage targets specific modules only (not all Python files):
```ini
--cov=app
--cov=models
--cov=db
```
Do not add coverage for test files or seed scripts.