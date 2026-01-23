# Galaxium Travels Frontend

A modern, space-themed frontend for the Galaxium Travels interplanetary booking system. Built with React, TypeScript, Tailwind CSS, and Framer Motion.

## 🚀 Features

- **Modern UI/UX**: Beautiful space-themed interface with animated starfield background
- **Responsive Design**: Works seamlessly on mobile, tablet, and desktop
- **Three Seat Classes**: Economy, Business, and Galaxium with real-time availability
- **Dynamic Pricing Display**: Shows calculated prices per seat class
- **Real-time Updates**: Live seat availability per class and booking status
- **User Management**: Simple name/email authentication with React Context
- **Flight Booking**: Browse, filter, and book interplanetary flights
- **Booking Management**: View and cancel your bookings with instant updates
- **Toast Notifications**: User-friendly feedback for all actions
- **Smooth Animations**: Framer Motion powered transitions
- **Type-Safe API**: Union types for error handling without try/catch

## 🛠️ Tech Stack

- **React 18** - UI library
- **TypeScript** - Type safety
- **Vite** - Build tool and dev server
- **Tailwind CSS** - Utility-first styling
- **Framer Motion** - Animations
- **React Router v6** - Client-side routing
- **Axios** - HTTP client
- **React Hot Toast** - Toast notifications
- **Lucide React** - Icons
- **date-fns** - Date formatting

## 📋 Prerequisites

- Node.js 18+ and npm
- Backend server running on `http://localhost:8080` (or configure `VITE_API_URL`)

## 🚀 Quick Start

### 1. Install Dependencies

```bash
npm install
```

### 2. Configure Environment

Create a `.env` file (or use the existing one):

```env
VITE_API_URL=http://localhost:8080
```

### 3. Start Development Server

```bash
npm run dev
```

The app will be available at `http://localhost:5173`

### 4. Build for Production

```bash
npm run build
```

### 5. Preview Production Build

```bash
npm run preview
```

## 📁 Project Structure

```
src/
├── components/
│   ├── common/          # Reusable UI components
│   │   ├── Button.tsx
│   │   ├── Card.tsx
│   │   ├── Input.tsx
│   │   ├── Modal.tsx
│   │   ├── LoadingSpinner.tsx
│   │   └── Starfield.tsx
│   ├── layout/          # Layout components
│   │   ├── Header.tsx
│   │   ├── Footer.tsx
│   │   └── Layout.tsx
│   ├── flights/         # Flight-related components
│   │   └── FlightCard.tsx
│   ├── bookings/        # Booking-related components
│   │   ├── BookingCard.tsx
│   │   └── BookingModal.tsx
│   └── user/            # User-related components
│       └── UserIdentification.tsx
├── pages/               # Route pages
│   ├── Home.tsx
│   ├── Flights.tsx
│   └── MyBookings.tsx
├── services/            # API services
│   └── api.ts
├── types/               # TypeScript types
│   └── index.ts
├── hooks/               # Custom React hooks
│   └── useUser.tsx
├── utils/               # Utility functions
│   └── formatters.ts
├── App.tsx              # Main app component
├── main.tsx             # Entry point
└── index.css            # Global styles
```

## 🎨 Design System

### Colors

- **Primary**: Cosmic Purple (`#6366F1`)
- **Secondary**: Nebula Pink (`#EC4899`)
- **Success**: Alien Green (`#10B981`)
- **Warning**: Solar Orange (`#F59E0B`)
- **Background**: Space Dark (`#030712`)
- **Text**: Star White (`#F9FAFB`)

### Components

All components follow a consistent design pattern with:
- Glass morphism effects
- Smooth hover transitions
- Responsive layouts
- Accessible markup

## 🔌 API Integration

The frontend connects to the backend API with the following endpoints:

- `GET /api/flights` - List all flights with seat class availability
- `POST /api/register` - Register new user
- `GET /api/user?name=...&email=...` - Get user by credentials
- `POST /api/book` - Book a flight with seat class selection
- `GET /api/bookings/{user_id}` - Get user's bookings
- `POST /api/cancel/{booking_id}` - Cancel a booking

### API Response Handling

The frontend uses **Union types** for error handling:

```typescript
// Check for errors without try/catch
const response = await api.bookFlight(userId, name, flightId, seatClass);
if (response.success === false) {
  // Handle error
  toast.error(response.message);
} else {
  // Handle success
  toast.success('Booking confirmed!');
}
```

### Seat Class Type Safety

Seat classes are enforced via TypeScript Literal types:

```typescript
type SeatClass = 'economy' | 'business' | 'galaxium';
```

This ensures compile-time validation and prevents invalid seat class values.

## 🎯 User Flows

### Booking a Flight

1. Browse available flights on the Flights page
2. View seat class options with availability and pricing
3. Select desired seat class (Economy, Business, or Galaxium)
4. Click "Book Now" on desired flight and class
5. Sign in or register (if not already logged in)
6. Confirm booking details with final price
7. Receive confirmation and view in My Bookings

### Managing Bookings

1. Navigate to My Bookings (requires login)
2. View active bookings with seat class information
3. Cancel active bookings if needed (restores seat availability)
4. See real-time status updates

### Seat Class Selection

- Each flight card displays three seat class options
- Real-time availability shown for each class
- Sold out classes are clearly marked but other classes remain bookable
- Prices calculated dynamically based on base price and class multiplier

## 🎨 Customization

### Changing Colors

Edit `tailwind.config.js`:

```js
theme: {
  extend: {
    colors: {
      'space-dark': '#030712',
      'cosmic-purple': '#6366F1',
      // Add your colors here
    }
  }
}
```

### Modifying API URL

Update `.env`:

```env
VITE_API_URL=https://your-api-url.com
```

## 🧪 Development

### Available Scripts

- `npm run dev` - Start development server (port 5173)
- `npm run build` - Build for production
- `npm run preview` - Preview production build
- `npm run lint` - Run ESLint

### Code Style

- **TypeScript Strict Mode**: Enabled for maximum type safety
- **React 19**: Uses new JSX transform (no React imports needed)
- **Functional Components**: All components use hooks
- **Component Organization**: Small, focused, single-responsibility components
- **Tailwind Utilities**: Prefer utility classes over custom CSS
- **Type Safety**: All API responses typed as Union types

### State Management

- **No Global State Library**: Uses React Context for user state only
- **useUser Hook**: Provides user authentication state
- **Local Component State**: For UI-specific state
- **API State**: Managed via async/await with Union type responses

### Critical Frontend Patterns

For detailed non-obvious patterns and architectural constraints, see **[../AGENTS.md](../AGENTS.md)**, which documents:
- API error handling via Union types (no try/catch)
- Seat class type safety with Literal types
- State management patterns
- Type system conventions

### Contributing & Demo Tasks

See **[../DEMO_BACKLOG.md](../DEMO_BACKLOG.md)** for 41 organized frontend tasks ranging from:
- **Tiny Tasks** (1-5 lines) - Perfect for quick contributions
- **Quick Fixes** (5-10 min) - Loading states, validation, UI improvements
- **Medium Features** (30-60 min) - Sorting, filtering, export functionality
- **Large Features** (2+ hours) - Authentication, testing, real-time updates
- **Accessibility** - ARIA labels, keyboard navigation, screen reader support

## 🚀 Deployment

### Vercel

```bash
npm run build
# Deploy the 'dist' folder
```

### Netlify

```bash
npm run build
# Deploy the 'dist' folder
```

### Docker

```dockerfile
FROM node:18-alpine as build
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build

FROM nginx:alpine
COPY --from=build /app/dist /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
```

## 🐛 Troubleshooting

### Backend Connection Issues

- Ensure backend is running on the correct port
- Check `VITE_API_URL` in `.env`
- Verify CORS is enabled on backend

### Build Errors

- Clear node_modules: `rm -rf node_modules && npm install`
- Clear Vite cache: `rm -rf node_modules/.vite`

## 📝 License

This project is part of the Galaxium Travels booking system.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📧 Support

For issues or questions, please open an issue on GitHub.

---

**Built with ❤️ for space travelers** 🚀
