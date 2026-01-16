# Galaxium Travels - Demo Backlog

This backlog contains features, issues, and fixes for demonstrating an AI-native IDE. Items are organized by complexity and stack (frontend/backend).

---

## Tiny Tasks (Tab Completion Demos)

Perfect for demonstrating tab completion. Each task is 1-5 lines of code.

### TINY-001: Add currency symbol constant
**Stack:** Frontend
**File:** `booking_system_frontend/src/utils/formatters.ts`
**Task:** Extract the hardcoded "$" in `formatCurrency` to a `CURRENCY_SYMBOL` constant.
**Lines:** 1

---

### TINY-002: Add default seat count constant
**Stack:** Backend
**File:** `booking_system_backend/seed_data.py`
**Task:** Extract the hardcoded `100` seats to a `DEFAULT_SEAT_COUNT` constant.
**Lines:** 1

---

### TINY-003: Add TypeScript type for seat class
**Stack:** Frontend
**File:** `booking_system_frontend/src/types/index.ts`
**Task:** Add `type SeatClass = 'economy' | 'business' | 'first'`
**Lines:** 1

---

### TINY-004: Add aria-label to logout button
**Stack:** Frontend
**File:** `booking_system_frontend/src/components/Header.tsx`
**Task:** Add `aria-label="Log out of your account"` to the logout button.
**Lines:** 1

---

### TINY-005: Add index on user email
**Stack:** Backend
**File:** `booking_system_backend/models.py`
**Task:** Add `index=True` to the email column in User model.
**Lines:** 1

---

### TINY-006: Add API timeout constant
**Stack:** Frontend
**File:** `booking_system_frontend/src/services/api.ts`
**Task:** Add `timeout: 10000` to the axios instance config.
**Lines:** 1

---

### TINY-007: Add booking status enum
**Stack:** Backend
**File:** `booking_system_backend/models.py`
**Task:** Add Python enum: `class BookingStatus(str, Enum): BOOKED = "booked"; CANCELLED = "cancelled"; COMPLETED = "completed"`
**Lines:** 3

---

### TINY-008: Add placeholder text to search input
**Stack:** Frontend
**File:** `booking_system_frontend/src/pages/Flights.tsx`
**Task:** Change placeholder from "Search flights..." to "Search by origin or destination..."
**Lines:** 1

---

### TINY-009: Add min price validation
**Stack:** Backend
**File:** `booking_system_backend/schemas.py`
**Task:** Add `ge=0` (greater than or equal to 0) to price field in Flight schema.
**Lines:** 1

---

### TINY-010: Add hover effect to flight cards
**Stack:** Frontend
**File:** `booking_system_frontend/src/components/FlightCard.tsx`
**Task:** Add `hover:scale-[1.02]` class to the card wrapper div.
**Lines:** 1

---

### TINY-011: Add email lowercase normalization
**Stack:** Backend
**File:** `booking_system_backend/services/user_service.py`
**Task:** Add `email = email.lower()` at the start of `register_user` function.
**Lines:** 1

---

### TINY-012: Add title attribute to truncated text
**Stack:** Frontend
**File:** `booking_system_frontend/src/components/FlightCard.tsx`
**Task:** Add `title={flight.origin}` to show full text on hover for origin/destination.
**Lines:** 1

---

### TINY-013: Add canceled American spelling alias
**Stack:** Backend
**File:** `booking_system_backend/models.py`
**Task:** Add `CANCELED = "cancelled"` alias in booking status for American English support.
**Lines:** 1

---

### TINY-014: Add cursor pointer to clickable cards
**Stack:** Frontend
**File:** `booking_system_frontend/src/components/FlightCard.tsx`
**Task:** Add `cursor-pointer` class to make it clear the card is interactive.
**Lines:** 1

---

### TINY-015: Add response model to health endpoint
**Stack:** Backend
**File:** `booking_system_backend/server.py`
**Task:** Add `response_model=dict` to the root health check endpoint decorator.
**Lines:** 1

---

---

# Frontend Backlog

## Quick Fixes (5-10 minutes)

### FE-QF-001: Add loading state to cancel booking button
**File:** `booking_system_frontend/src/components/BookingCard.tsx`
**Description:** The cancel button doesn't show a loading spinner while the cancellation request is in progress.
**Acceptance Criteria:**
- Add loading state to cancel button
- Disable button while request is pending
- Show spinner inside button

---

### FE-QF-002: Fix missing error handling for network failures
**File:** `booking_system_frontend/src/services/api.ts`
**Description:** When the backend is down, show a user-friendly "Server unavailable" message instead of generic error.
**Acceptance Criteria:**
- Detect network errors vs API errors
- Show specific toast for connection failures

---

### FE-QF-003: Add seat availability color coding
**File:** `booking_system_frontend/src/components/FlightCard.tsx`
**Description:** Color code seat count: green (>50%), yellow (10-50%), red (<10%).
**Acceptance Criteria:**
- Calculate percentage of seats available
- Apply color classes based on thresholds

---

### FE-QF-004: Validate email format before API call
**File:** `booking_system_frontend/src/components/UserIdentification.tsx`
**Description:** Add client-side email validation to fail fast before hitting the API.
**Acceptance Criteria:**
- Add email regex validation
- Show inline error message

---

### FE-QF-005: Add tooltip to disabled book button
**File:** `booking_system_frontend/src/components/FlightCard.tsx`
**Description:** When a flight has no seats, show tooltip explaining "No seats available".
**Acceptance Criteria:**
- Show tooltip on hover when disabled
- Accessible for screen readers

---

### FE-QF-006: Add confirmation before logout
**File:** `booking_system_frontend/src/components/Header.tsx`
**Description:** Show confirmation dialog before logging out to prevent accidents.
**Acceptance Criteria:**
- Show confirmation modal
- Use existing Modal component

---

### FE-QF-007: Improve empty state on bookings page
**File:** `booking_system_frontend/src/pages/Bookings.tsx`
**Description:** Add friendly empty state with "Browse Flights" call-to-action.
**Acceptance Criteria:**
- Add space-themed icon
- Include link to /flights

---

### FE-QF-008: Add copy booking ID to clipboard
**File:** `booking_system_frontend/src/components/BookingCard.tsx`
**Description:** Add button to copy booking reference to clipboard.
**Acceptance Criteria:**
- Add copy button
- Show toast confirmation

---

### FE-QF-009: Format sub-hour flight durations
**File:** `booking_system_frontend/src/utils/formatters.ts`
**Description:** Handle edge cases like "45m" (under an hour) in duration formatting.
**Acceptance Criteria:**
- Handle sub-hour durations
- Add unit tests

---

### FE-QF-010: Fix Starfield memory leak
**File:** `booking_system_frontend/src/components/common/Starfield.tsx`
**Description:** Canvas animation doesn't clean up on unmount, causing memory leaks.
**Acceptance Criteria:**
- Add cleanup in useEffect return
- Cancel animation frame on unmount

---

## Medium Features (30-60 minutes)

### FE-MF-001: Add flight sorting options
**File:** `booking_system_frontend/src/pages/Flights.tsx`
**Description:** Sort flights by price, departure time, or duration.
**Acceptance Criteria:**
- Add sort dropdown
- Support: Price, Departure time, Duration
- Client-side sorting

---

### FE-MF-002: Implement price range filter
**File:** `booking_system_frontend/src/pages/Flights.tsx`
**Description:** Add price range slider to filter flights within a budget.
**Acceptance Criteria:**
- Add dual-handle range slider
- Filter flights by min/max price

---

### FE-MF-003: Add booking history export to CSV
**File:** `booking_system_frontend/src/pages/Bookings.tsx`
**Description:** Export booking history as CSV file.
**Acceptance Criteria:**
- Add "Export" button
- Include all booking details
- Trigger browser download

---

### FE-MF-004: Add user profile page
**Files:** New page + Header link
**Description:** View and edit profile information.
**Acceptance Criteria:**
- Create /profile route
- Display user info
- Allow editing name

---

### FE-MF-005: Add flight details modal
**File:** New component
**Description:** Click flight for detailed view before booking.
**Acceptance Criteria:**
- Create FlightDetailsModal
- Show full details
- Include "Book Now" button

---

### FE-MF-006: Add booking status timeline
**File:** `booking_system_frontend/src/components/BookingCard.tsx`
**Description:** Visual timeline: Booked → Confirmed → Completed.
**Acceptance Criteria:**
- Create Timeline component
- Visual indicators for each step

---

### FE-MF-007: Add dark mode toggle
**Files:** Theme + Header
**Description:** Toggle between dark and light themes.
**Acceptance Criteria:**
- Create light theme
- Add toggle in header
- Persist in localStorage

---

### FE-MF-008: Add flight comparison feature
**Files:** New component + Flights page
**Description:** Select 2-3 flights and compare side by side.
**Acceptance Criteria:**
- Add "Compare" checkbox to cards
- Create ComparisonModal
- Highlight differences

---

### FE-MF-009: Implement API request caching
**File:** `booking_system_frontend/src/services/api.ts`
**Description:** Cache flight data to reduce API calls.
**Acceptance Criteria:**
- Cache GET /flights response
- Set 5 minute TTL
- Add manual refresh button

---

### FE-MF-010: Add date picker for flight search
**File:** `booking_system_frontend/src/pages/Flights.tsx`
**Description:** Filter flights by departure date range.
**Acceptance Criteria:**
- Add date picker component
- Filter by date range

---

## Large Features (2+ hours)

### FE-LF-001: Implement frontend authentication flow
**Files:** Multiple components + context
**Description:** Full login/register flow with JWT storage.
**Acceptance Criteria:**
- Password input fields
- JWT storage and refresh
- Protected routes
- Auth context updates

---

### FE-LF-002: Add comprehensive component tests
**Files:** New test files
**Description:** Set up Vitest and test all components.
**Acceptance Criteria:**
- Set up Vitest
- Test all components
- Coverage reporting

---

### FE-LF-003: Implement lazy loading for routes
**File:** `booking_system_frontend/src/App.tsx`
**Description:** Code splitting with React.lazy.
**Acceptance Criteria:**
- Lazy load page components
- Add Suspense fallbacks

---

### FE-LF-004: Add real-time flight updates
**Files:** New WebSocket hook + components
**Description:** WebSocket for live seat availability.
**Acceptance Criteria:**
- WebSocket connection hook
- Update flight cards in real-time
- Handle reconnection

---

### FE-LF-005: Create component storybook
**Files:** Storybook configuration
**Description:** Set up Storybook for component documentation.
**Acceptance Criteria:**
- Install Storybook
- Add stories for all components
- Interactive controls

---

## Accessibility

### FE-A11Y-001: Add ARIA labels to interactive elements
**Files:** All interactive components
**Description:** Add proper ARIA labels for screen readers.

---

### FE-A11Y-002: Improve keyboard navigation
**Files:** Modal, forms, cards
**Description:** Ensure full keyboard accessibility and focus management.

---

### FE-A11Y-003: Add screen reader announcements
**Files:** Toast, loading states
**Description:** Announce dynamic content changes to screen readers.

---

### FE-A11Y-004: Improve color contrast
**Files:** Tailwind theme
**Description:** Ensure WCAG AA compliance (4.5:1 ratio).

---

## Technical Debt

### FE-TD-001: Enable TypeScript strict null checks
**File:** `tsconfig.app.json`
**Description:** Enable strictNullChecks and fix resulting errors.

---

### FE-TD-002: Extract magic numbers to constants
**Files:** Various components
**Description:** Move animation durations, timeouts to constants file.

---

### FE-TD-003: Remove hardcoded API URLs
**Files:** Various
**Description:** Ensure all API calls use VITE_API_URL.

---

---

# Backend Backlog

## Quick Fixes (5-10 minutes)

### BE-QF-001: Add request logging middleware
**File:** `booking_system_backend/server.py`
**Description:** Log all API requests with method, path, status, duration.
**Acceptance Criteria:**
- Add logging middleware
- Log request details
- JSON format

---

### BE-QF-002: Fix inconsistent error response format
**Files:** Error handling throughout
**Description:** Standardize all errors to use ErrorResponse schema.
**Acceptance Criteria:**
- Audit all error responses
- Use consistent format

---

### BE-QF-003: Add database indexes
**File:** `booking_system_backend/models.py`
**Description:** Add indexes on user_id, email, departure_time.
**Acceptance Criteria:**
- Index bookings.user_id
- Index users.email
- Index flights.departure_time

---

### BE-QF-004: Normalize email to lowercase
**File:** `booking_system_backend/services/user_service.py`
**Description:** Convert emails to lowercase before storing.
**Acceptance Criteria:**
- Lowercase on registration
- Lowercase on lookup

---

### BE-QF-005: Add input length validation
**File:** `booking_system_backend/schemas.py`
**Description:** Add max_length to name and email fields.
**Acceptance Criteria:**
- Name: max 100 chars
- Email: max 255 chars

---

### BE-QF-006: Add flight capacity validation
**File:** `booking_system_backend/schemas.py`
**Description:** Validate seats_available is non-negative.
**Acceptance Criteria:**
- Add ge=0 constraint
- Add max seats constraint

---

### BE-QF-007: Improve error hints
**Files:** Service error responses
**Description:** Add helpful hints to error messages.
**Acceptance Criteria:**
- Add hint field
- Actionable suggestions

---

### BE-QF-008: Add health check details
**File:** `booking_system_backend/server.py`
**Description:** Return version, uptime, database status in health check.
**Acceptance Criteria:**
- Add version info
- Add db connectivity check

---

## Medium Features (30-60 minutes)

### BE-MF-001: Add flight search by date range
**File:** `booking_system_backend/services/flight_service.py`
**Description:** Add date range filtering to flight queries.
**Acceptance Criteria:**
- Add departure_after param
- Add departure_before param
- Update REST endpoint

---

### BE-MF-002: Implement pagination for flights
**File:** `booking_system_backend/server.py`
**Description:** Add limit/offset pagination.
**Acceptance Criteria:**
- Add limit, offset params
- Return total count
- Default limit of 20

---

### BE-MF-003: Add booking modification endpoint
**File:** `booking_system_backend/server.py`
**Description:** PUT endpoint to modify bookings.
**Acceptance Criteria:**
- PUT /bookings/{id}
- Allow name changes
- Validate modifications

---

### BE-MF-004: Add user update endpoint
**File:** `booking_system_backend/server.py`
**Description:** Allow users to update their name.
**Acceptance Criteria:**
- PUT /user/{id}
- Validate name
- Return updated user

---

### BE-MF-005: Add booking statistics endpoint
**File:** `booking_system_backend/server.py`
**Description:** Return user's booking statistics.
**Acceptance Criteria:**
- GET /user/{id}/stats
- Total bookings, cancellations
- Total spent

---

### BE-MF-006: Fix race condition in seat booking
**File:** `booking_system_backend/services/booking_service.py`
**Description:** Add row-level locking to prevent double-booking.
**Acceptance Criteria:**
- Add SELECT FOR UPDATE
- Write test for race condition

---

### BE-MF-007: Add rate limiting
**File:** `booking_system_backend/server.py`
**Description:** Rate limit API endpoints.
**Acceptance Criteria:**
- Limit per IP
- Return 429 when exceeded
- Configurable limits

---

### BE-MF-008: Add API versioning
**File:** `booking_system_backend/server.py`
**Description:** Move endpoints under /api/v1/.
**Acceptance Criteria:**
- Prefix all routes
- Document versioning

---

## Large Features (2+ hours)

### BE-LF-001: Implement JWT authentication
**Files:** New auth module
**Description:** Full JWT auth with password hashing.
**Acceptance Criteria:**
- Password field in User model
- bcrypt hashing
- Login/register endpoints
- JWT middleware

---

### BE-LF-002: Add admin endpoints
**Files:** New admin module
**Description:** Admin CRUD for flights, users, bookings.
**Acceptance Criteria:**
- Admin role
- Flight management
- User management
- Booking management

---

### BE-LF-003: Implement email notifications
**Files:** New email service
**Description:** Send booking confirmations.
**Acceptance Criteria:**
- Email service setup
- Booking confirmation
- Cancellation email

---

### BE-LF-004: Add PostgreSQL support
**Files:** Database configuration
**Description:** Replace SQLite with PostgreSQL.
**Acceptance Criteria:**
- PostgreSQL driver
- Environment variable config
- Docker Compose setup

---

### BE-LF-005: Set up Alembic migrations
**Files:** New alembic configuration
**Description:** Proper database migration system.
**Acceptance Criteria:**
- Initialize Alembic
- Create initial migration
- Document workflow

---

### BE-LF-006: Add seat class support
**Files:** Models + services
**Description:** Economy/Business/First class with pricing.
**Acceptance Criteria:**
- Seat class in booking
- Price multipliers
- Update seed data

---

### BE-LF-007: Implement waitlist
**Files:** New waitlist model + service
**Description:** Waitlist for sold-out flights.
**Acceptance Criteria:**
- Waitlist model
- Join/leave endpoints
- Auto-notify on availability

---

## MCP (AI Agent) Features

### BE-MCP-001: Add flight search MCP tool
**File:** `booking_system_backend/mcp_tools.py`
**Description:** Search flights by criteria.
**Acceptance Criteria:**
- search_flights tool
- Filter by origin/destination/date

---

### BE-MCP-002: Add booking summary MCP tool
**File:** `booking_system_backend/mcp_tools.py`
**Description:** Return user's booking summary.
**Acceptance Criteria:**
- get_booking_summary tool
- Upcoming count, total spent

---

### BE-MCP-003: Add MCP integration tests
**File:** `booking_system_backend/tests/`
**Description:** Test MCP tool functionality.
**Acceptance Criteria:**
- Test each tool
- Test error handling

---

## Technical Debt

### BE-TD-001: Add structured logging
**Files:** Throughout
**Description:** Replace print statements with proper logging.

---

### BE-TD-002: Add request validation tests
**Files:** Test files
**Description:** Test all input validation edge cases.

---

### BE-TD-003: Add API response compression
**File:** Server middleware
**Description:** Enable gzip compression.

---

---

# Summary

| Category | Frontend | Backend | Total |
|----------|----------|---------|-------|
| Tiny Tasks | 9 | 6 | 15 |
| Quick Fixes | 10 | 8 | 18 |
| Medium Features | 10 | 8 | 18 |
| Large Features | 5 | 7 | 12 |
| Accessibility | 4 | - | 4 |
| MCP Features | - | 3 | 3 |
| Technical Debt | 3 | 3 | 6 |
| **Total** | **41** | **35** | **76** |

---

## Recommended Demo Order

### Tab Completion Demo (2 min)
Start with any TINY task - they're all 1-3 lines.

### Quick Win Demo (10 min)
- FE-QF-003: Seat availability colors
- BE-QF-004: Email normalization

### Feature Demo (30 min)
- FE-MF-001: Flight sorting
- BE-MF-002: Pagination
