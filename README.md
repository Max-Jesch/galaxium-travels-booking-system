# 🚀 Galaxium Travels - Interplanetary Booking System

A complete full-stack application for booking interplanetary space travel, featuring a modern React frontend and a FastAPI backend with dual REST and MCP protocol support.

## 🌟 Features

- **Modern Space-Themed UI** - Beautiful, responsive interface with animated starfield
- **Full Booking System** - Browse flights, make bookings, manage reservations
- **Three Seat Classes** - Economy, Business, and Galaxium Class with independent availability tracking
- **Dynamic Pricing** - Class-based multipliers (1x, 2.5x, 5x) applied to base flight prices
- **Dual Protocol Backend** - REST API and MCP (Model Context Protocol) support
- **Type-Safe** - Full TypeScript frontend and Python type hints with strict validation
- **Real-Time Updates** - Live seat availability per class and booking status
- **User Management** - Simple name/email authentication
- **Comprehensive Testing** - Full test coverage for services and REST endpoints
- **Production Ready** - Optimized builds and comprehensive error handling

## 🏗️ Architecture

```
galaxium-travels-infrastructure/
├── booking_system_backend/     # FastAPI backend (Python)
│   ├── server.py              # Main server with REST & MCP
│   ├── services/              # Business logic layer
│   ├── models.py              # SQLAlchemy ORM models
│   └── tests/                 # Test suite
│
├── booking_system_frontend/    # React frontend (TypeScript)
│   ├── src/
│   │   ├── components/        # Reusable UI components
│   │   ├── pages/            # Route pages
│   │   ├── services/         # API integration
│   │   └── types/            # TypeScript definitions
│   └── dist/                 # Production build
│
├── bob_documents/             # Implementation plans & architecture docs
├── internal_monologue/        # Development session summaries
├── AGENTS.md                  # Critical patterns for AI agents
├── DEMO_BACKLOG.md           # 76 demo tasks organized by complexity
└── start.sh                   # Unix/Mac startup script
```

### Key Architecture Documents

- **[AGENTS.md](AGENTS.md)** - Critical non-obvious patterns, testing specifics, and architectural constraints
- **[DEMO_BACKLOG.md](DEMO_BACKLOG.md)** - 76 organized tasks (tiny to large) for demos and contributions
- **[bob_documents/](bob_documents/)** - Detailed implementation plans and architecture decisions

## 🚀 Quick Start

### Prerequisites

- **Python 3.8+** - [Download](https://www.python.org/downloads/)
- **Node.js 18+** - [Download](https://nodejs.org/)
- **npm** (comes with Node.js)

### Option 1: One-Command Start (Recommended)

#### On macOS/Linux:
```bash
./start.sh
```

#### On Windows:
```bash
start.bat
```

This will automatically:
- ✅ Install all dependencies
- ✅ Start the backend server on port 8080
- ✅ Start the frontend dev server on port 5173
- ✅ Open both in separate terminal windows

### Option 2: Manual Start

#### Start Backend:
```bash
cd booking_system_backend
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
python server.py
```

#### Start Frontend (in a new terminal):
```bash
cd booking_system_frontend
npm install
npm run dev
```

## 🌐 Access the Application

Once started, access:

- **Frontend**: http://localhost:5173
- **Backend API**: http://localhost:8080
- **API Documentation**: http://localhost:8080/docs
- **MCP Endpoint**: http://localhost:8080/mcp

## 📚 Documentation

### Backend
See [booking_system_backend/README.md](booking_system_backend/README.md) for:
- API endpoints documentation
- MCP tools reference
- Database schema
- Testing instructions

### Frontend
See [booking_system_frontend/README.md](booking_system_frontend/README.md) for:
- Component documentation
- Styling guide
- Build instructions
- Deployment options

## 🎯 User Guide

### Booking a Flight

1. **Browse Flights** - Navigate to the Flights page to see all available routes
2. **View Seat Classes** - Each flight displays three classes with real-time availability:
   - 🛫 **Economy** - Standard comfort (1x base price)
   - 👑 **Business** - Premium experience (2.5x base price)
   - 🚀 **Galaxium Class** - Ultimate luxury (5x base price)
3. **Check Availability** - Each class shows available seats independently
4. **Select Your Class** - Choose based on availability and budget
5. **Sign In/Register** - Click "Book Now" and enter your name and email
6. **Confirm Booking** - Review flight details, selected class, and final price
7. **Manage Bookings** - View and cancel bookings from "My Bookings" page

### Demo Data

The system comes pre-seeded with:
- **10 Users** - Alice, Bob, Charlie, Diana, Eve, Frank, Grace, Heidi, Ivan, Judy
- **10 Flights** - Routes between Earth, Mars, Moon, Venus, Jupiter, Europa, Pluto
- **Seat Distribution** - Each flight has Economy (60%), Business (30%), Galaxium (10%)
- **20 Sample Bookings** - Distributed across all three seat classes with realistic availability

## 💺 Seat Classes & Pricing

Galaxium Travels offers three distinct seat classes for every flight:

| Class | Icon | Multiplier | Features | Seat Allocation |
|-------|------|------------|----------|-----------------|
| **Economy** | 🛫 | 1.0x | Standard seating, Basic amenities | 60% of seats |
| **Business** | 👑 | 2.5x | Priority boarding, Extra legroom, Premium meals | 30% of seats |
| **Galaxium** | 🚀 | 5.0x | Private pods, Zero-G lounge, Gourmet dining, Concierge | 10% of seats |

### Pricing Example
For a flight with base price of $1,000,000:
- Economy: $1,000,000
- Business: $2,500,000
- Galaxium Class: $5,000,000

### Seat Availability
- **Independent Tracking** - Each class has separate available/booked counters
- **Real-Time Updates** - Availability updates immediately after booking/cancellation
- **Sold Out Handling** - Classes show "Sold Out" when no seats remain, other classes stay bookable
- **Database Integrity** - Seat counters stored in Flight model, updated via service layer

## 🛠️ Technology Stack

### Backend
- **FastAPI** - Modern Python web framework
- **SQLAlchemy** - ORM for database operations
- **Pydantic** - Data validation
- **FastMCP** - MCP protocol support
- **SQLite** - Lightweight database
- **Uvicorn** - ASGI server

### Frontend
- **React 18** - UI library
- **TypeScript** - Type safety
- **Vite** - Build tool
- **Tailwind CSS** - Styling
- **Framer Motion** - Animations
- **React Router** - Routing
- **Axios** - HTTP client
- **React Hot Toast** - Notifications

## 🧪 Testing

### Backend Tests
```bash
cd booking_system_backend
pytest                          # Run all tests
pytest -v                       # Verbose output
pytest tests/test_services.py   # Service layer tests
pytest tests/test_rest.py       # REST API tests
```

**Test Coverage:**
- Service layer functions (booking, flight, user operations)
- REST API endpoints
- Seat class validation and availability
- Error handling and edge cases

### Frontend Build Test
```bash
cd booking_system_frontend
npm run build                   # Production build
npm run lint                    # Code quality check
```

## 📦 Production Deployment

### Backend
```bash
cd booking_system_backend
pip install -r requirements.txt
uvicorn server:app --host 0.0.0.0 --port 8080
```

### Frontend
```bash
cd booking_system_frontend
npm run build
# Deploy the 'dist' folder to your hosting service
```

### Docker Support
Both backend and frontend include Dockerfiles for containerized deployment.

## 🎨 Customization

### Change API URL
Edit `booking_system_frontend/.env`:
```env
VITE_API_URL=https://your-api-url.com
```

### Modify Theme Colors
Edit `booking_system_frontend/tailwind.config.js`:
```js
colors: {
  'cosmic-purple': '#6366F1',
  'nebula-pink': '#EC4899',
  // Add your colors
}
```

## 🐛 Troubleshooting

### Backend won't start
- Ensure Python 3.8+ is installed: `python --version`
- Check if port 8080 is available
- Verify all dependencies are installed: `pip install -r requirements.txt`

### Frontend won't start
- Ensure Node.js 18+ is installed: `node --version`
- Check if port 5173 is available
- Delete `node_modules` and reinstall: `rm -rf node_modules && npm install`

### Connection Issues
- Verify backend is running on http://localhost:8080
- Check CORS settings in backend
- Ensure `.env` file exists in frontend with correct API URL

## 📄 License

This project is part of the Galaxium Travels booking system.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📧 Support

For issues or questions:
- Check the documentation in each component's README
- Review the troubleshooting section above
- Open an issue on GitHub

---

**Built with ❤️ for space travelers** 🚀✨

*Explore the cosmos, one booking at a time!*