# AGENTS.md

This file provides guidance to agents when working with code in this repository.

## Critical Non-Obvious Patterns

### Backend Architecture
- **MCP server MUST be created before FastAPI app** (server.py:14-16) - lifespan combination requires this order
- **Service layer returns Union types** - All service functions return `ModelOut | ErrorResponse`, not exceptions
- **Seat class validation happens in service layer** - booking.py validates against SEAT_CLASS_MULTIPLIERS dict, not Pydantic
- **Database sessions must be manually closed** - MCP tools use SessionLocal() directly and require try/finally blocks
- **Price calculation uses multipliers** - booking.py:8-12 defines SEAT_CLASS_MULTIPLIERS (economy: 1.0, business: 2.5, galaxium: 5.0)

### Testing
- **Tests run from backend directory** - `cd booking_system_backend && pytest`, not from project root
- **pytest.ini configures verbose output** - `-v --tb=short` is default, tests always show detailed output

### Frontend API Integration
- **API base URL from env variable** - api.ts:13 uses `import.meta.env.VITE_API_URL` with localhost:8080 fallback
- **Error responses have specific structure** - Check `response.success === false` to detect errors (api.ts:112)
- **All API endpoints are prefixed with /api/** - Except root health check at `/`

### Monorepo Structure
- **Backend and frontend are separate projects** - Each has own dependencies, must cd into directory before running commands
- **Start script handles both servers** - start.sh creates venv, installs deps, starts both servers with proper cleanup
- **Backend uses .venv in its directory** - Not at project root, start.sh uses `.venv/bin/python` explicitly

## Commands

### Backend (from booking_system_backend/)
```bash
# Run server (creates DB, seeds data, starts on port 8080)
python server.py

# Run all tests
pytest

# Run specific test file
pytest tests/test_services.py
pytest tests/test_rest.py
```

### Frontend (from booking_system_frontend/)
```bash
# Dev server (port 5173)
npm run dev

# Production build
npm run build

# Lint
npm run lint
```

### Full Stack (from project root)
```bash
# Start both servers (recommended)
./start.sh
```

## Code Style

### Backend (Python)
- Type hints required - All functions use return type annotations
- Pydantic models use `from_attributes = True` for ORM compatibility
- Service functions are pure - No FastAPI dependencies in services/
- Error responses use structured ErrorResponse model with error_code field

### Frontend (TypeScript)
- Strict mode enabled - tsconfig.app.json has strict: true
- No unused locals/parameters - Enforced by TypeScript config
- React 19 with new JSX transform - Uses react-jsx, not React imports
- API responses typed as Union types - `Model | ErrorResponse` pattern matches backend