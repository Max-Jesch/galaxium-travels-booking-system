# AGENTS.md

This file provides guidance to agents when working with code in this repository.

## Critical Architecture Patterns

**Dual Protocol Server**: Backend exposes BOTH REST and MCP from single FastAPI app. MCP server MUST be created before FastAPI app (line 16 in server.py) to properly combine lifespans. MCP mounted at `/mcp` endpoint (line 183).

**MCP Tool Pattern**: MCP tools manually manage SessionLocal() - they create, use, and close sessions in try/finally blocks. This differs from REST endpoints which use FastAPI's Depends(get_db) dependency injection.

**Service Layer Returns Union Types**: All service functions return `Result | ErrorResponse` (not exceptions). Check response type with `isinstance(result, ErrorResponse)` before using. MCP tools convert ErrorResponse to exceptions; REST endpoints return them directly.

**User Validation Requires Name Match**: `book_flight()` validates BOTH user_id AND name match (line 27 in services/booking.py). This is intentional - prevents booking with wrong user_id.

## Testing

**Test Database Isolation**: Tests use in-memory SQLite with StaticPool (conftest.py line 18-22). Each test gets fresh db via `db_session` fixture that creates/drops tables per test.

**Monkeypatch Pattern**: Test client patches BOTH `db.SessionLocal` AND `server.SessionLocal` (conftest.py line 49-50) because MCP tools import SessionLocal directly, not via dependency injection.

**Seed Disabled in Tests**: conftest.py line 53 patches `seed()` to no-op during tests to prevent test data pollution.

## Frontend State Management

**User Persistence**: useUser hook stores user in localStorage with key `'galaxium_user'` (line 7 in hooks/useUser.tsx). User state synced on every change via useEffect.

**API Error Handling**: axios interceptor (api.ts line 20-35) transforms backend ErrorResponse into rejected promises. Check errors with `isErrorResponse()` helper.

## Running Tests

```bash
cd booking_system_backend
pytest                    # Run all tests
pytest tests/test_services.py  # Service layer only
pytest tests/test_rest.py      # REST endpoints only
```

Tests must be run from `booking_system_backend` directory due to sys.path manipulation in conftest.py.