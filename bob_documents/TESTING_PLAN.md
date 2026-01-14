# Galaxium Travels Frontend - Testing Plan

This document provides a comprehensive list of manual tests to verify the frontend application works correctly. These tests can be executed by humans or automated by AI agents with browser capabilities.

## Prerequisites

Before testing:
1. Backend server running on `http://localhost:8000`
2. Frontend server running on `http://localhost:5173`
3. Database seeded with sample data
4. Browser with developer tools available

## Test Categories

### 1. Initial Load & Environment

**Test 1.1: Application Loads Successfully**
- Navigate to `http://localhost:5173`
- Expected: Home page loads without errors
- Expected: Starfield animation visible in background
- Expected: Navigation header displays "Galaxium Travels" logo

**Test 1.2: API Connection**
- Open browser DevTools Network tab
- Refresh the page
- Expected: No 404 or 500 errors in console
- Expected: API calls to localhost:8000 succeed

**Test 1.3: Responsive Design - Desktop**
- View on desktop resolution (1920x1080)
- Expected: Full navigation menu visible
- Expected: Content properly centered and spaced

**Test 1.4: Responsive Design - Mobile**
- Resize browser to mobile width (375px)
- Expected: Hamburger menu icon appears
- Expected: Content stacks vertically
- Expected: All text remains readable

### 2. Navigation

**Test 2.1: Home Navigation**
- Click "Galaxium Travels" logo
- Expected: Navigates to home page (/)
- Expected: URL changes to base URL

**Test 2.2: Flights Navigation**
- Click "Flights" in navigation menu
- Expected: Navigates to /flights
- Expected: Flight list loads and displays

**Test 2.3: My Bookings Navigation (Not Signed In)**
- Click "My Bookings" without signing in
- Expected: Redirects to home or shows sign-in prompt
- Expected: User-friendly message displayed

**Test 2.4: Mobile Menu**
- Resize to mobile width
- Click hamburger menu icon
- Expected: Menu slides open
- Expected: All navigation links visible
- Click a link
- Expected: Menu closes automatically

### 3. Home Page

**Test 3.1: Hero Section**
- View home page
- Expected: Hero title "Journey Beyond the Stars" visible
- Expected: Subtitle text visible
- Expected: "Explore Flights" CTA button visible

**Test 3.2: Features Section**
- Scroll down on home page
- Expected: Three feature cards visible
- Expected: Icons and descriptions for each feature
- Expected: Cards have hover effects

**Test 3.3: CTA Button**
- Click "Explore Flights" button
- Expected: Navigates to /flights page
- Expected: Smooth transition

### 4. Flights Page

**Test 4.1: Flight List Loads**
- Navigate to /flights
- Expected: Loading spinner appears briefly
- Expected: List of flights displays
- Expected: Each flight shows: flight number, origin, destination, date, time, price, available seats

**Test 4.2: Search Functionality**
- Enter "Earth" in search box
- Expected: Results filter to show only flights with "Earth" in origin or destination
- Clear search
- Expected: All flights display again

**Test 4.3: Origin Filter**
- Select "Mars" from origin dropdown
- Expected: Only flights from Mars display
- Select "All Origins"
- Expected: All flights display again

**Test 4.4: Destination Filter**
- Select "Europa" from destination dropdown
- Expected: Only flights to Europa display
- Select "All Destinations"
- Expected: All flights display again

**Test 4.5: Combined Filters**
- Select origin "Earth" and destination "Mars"
- Expected: Only Earth→Mars flights display
- Expected: Count updates correctly

**Test 4.6: No Results**
- Apply filters that match no flights
- Expected: "No flights found" message displays
- Expected: Suggestion to adjust filters shown

**Test 4.7: Flight Card Hover**
- Hover over a flight card
- Expected: Card elevates with shadow effect
- Expected: Smooth animation

### 5. User Authentication

**Test 5.1: Sign In - Existing User**
- Click "Book Now" on any flight
- Enter existing user email (e.g., "john.doe@example.com")
- Click "Continue"
- Expected: User identified successfully
- Expected: Welcome message with user name
- Expected: Booking modal opens

**Test 5.2: Sign In - New User**
- Click "Book Now" on any flight
- Enter new email (e.g., "newuser@test.com")
- Enter name (e.g., "New User")
- Click "Register"
- Expected: New user created
- Expected: Welcome message displays
- Expected: Booking modal opens

**Test 5.3: Invalid Email**
- Try to sign in with invalid email format
- Expected: Validation error message
- Expected: Cannot proceed until valid email entered

**Test 5.4: Empty Fields**
- Try to submit with empty email
- Expected: Validation prevents submission
- Expected: Error message displays

**Test 5.5: User Persistence**
- Sign in as a user
- Refresh the page
- Expected: User remains signed in
- Expected: "My Bookings" link accessible

**Test 5.6: Sign Out**
- Click user name in header
- Click "Sign Out"
- Expected: User signed out
- Expected: Returns to guest state
- Expected: "My Bookings" link disabled/hidden

### 6. Booking Flow

**Test 6.1: Open Booking Modal**
- Sign in as user
- Click "Book Now" on a flight
- Expected: Booking confirmation modal opens
- Expected: Flight details displayed correctly
- Expected: Price shown
- Expected: "Confirm Booking" button visible

**Test 6.2: Confirm Booking**
- In booking modal, click "Confirm Booking"
- Expected: Loading state shows
- Expected: Success toast notification appears
- Expected: Modal closes
- Expected: Booking confirmation number shown in toast

**Test 6.3: Cancel Booking Modal**
- Open booking modal
- Click "Cancel" or X button
- Expected: Modal closes
- Expected: No booking created

**Test 6.4: Booking Fully Booked Flight**
- Find a flight with 0 available seats
- Try to book it
- Expected: "Book Now" button disabled or shows "Fully Booked"
- Expected: Cannot proceed with booking

**Test 6.5: Multiple Bookings**
- Book first flight successfully
- Book second different flight
- Expected: Both bookings succeed
- Expected: Each shows unique confirmation number

### 7. My Bookings Page

**Test 7.1: View Bookings**
- Sign in as user with existing bookings
- Navigate to "My Bookings"
- Expected: List of user's bookings displays
- Expected: Each booking shows: confirmation number, flight details, booking date, status

**Test 7.2: Empty Bookings**
- Sign in as new user with no bookings
- Navigate to "My Bookings"
- Expected: "No bookings yet" message displays
- Expected: Link to browse flights shown

**Test 7.3: Booking Status Display**
- View bookings list
- Expected: "Confirmed" status shown in green
- Expected: "Cancelled" status shown in red (if any)

**Test 7.4: Booking Details**
- View a booking card
- Expected: All flight information visible
- Expected: Passenger name matches signed-in user
- Expected: Booking date formatted correctly

### 8. Cancellation Flow

**Test 8.1: Cancel Booking**
- On My Bookings page, click "Cancel Booking"
- Expected: Confirmation dialog appears
- Expected: Warning message about cancellation

**Test 8.2: Confirm Cancellation**
- In cancellation dialog, click "Yes, Cancel"
- Expected: Loading state shows
- Expected: Success toast appears
- Expected: Booking status updates to "Cancelled"
- Expected: Booking card shows cancelled state

**Test 8.3: Abort Cancellation**
- Click "Cancel Booking"
- In dialog, click "No, Keep It"
- Expected: Dialog closes
- Expected: Booking remains confirmed
- Expected: No changes made

**Test 8.4: Cancel Already Cancelled Booking**
- Try to cancel an already cancelled booking
- Expected: Cancel button disabled or hidden
- Expected: Status shows "Cancelled"

### 9. Error Handling

**Test 9.1: Backend Offline**
- Stop backend server
- Try to load flights page
- Expected: Error message displays
- Expected: User-friendly error text
- Expected: Suggestion to check connection

**Test 9.2: Network Error During Booking**
- Simulate network interruption during booking
- Expected: Error toast notification
- Expected: Booking not created
- Expected: User can retry

**Test 9.3: Invalid API Response**
- (Requires backend modification or mock)
- Expected: Application handles gracefully
- Expected: Error message shown to user

**Test 9.4: 404 Route**
- Navigate to non-existent route (e.g., /invalid-page)
- Expected: 404 page or redirect to home
- Expected: User can navigate back

### 10. UI/UX Elements

**Test 10.1: Loading States**
- Observe loading spinners during data fetches
- Expected: Spinner visible during API calls
- Expected: Spinner disappears when data loads
- Expected: Smooth transition

**Test 10.2: Toast Notifications**
- Perform actions that trigger toasts (booking, cancellation)
- Expected: Toast appears in corner
- Expected: Auto-dismisses after few seconds
- Expected: Can be manually dismissed

**Test 10.3: Animations**
- Observe page transitions and element animations
- Expected: Smooth fade-in effects
- Expected: Hover animations on interactive elements
- Expected: No janky or broken animations

**Test 10.4: Starfield Background**
- View any page
- Expected: Animated stars moving in background
- Expected: Performance remains smooth
- Expected: Stars don't interfere with content readability

**Test 10.5: Button States**
- Hover over buttons
- Expected: Color change on hover
- Expected: Cursor changes to pointer
- Click button
- Expected: Visual feedback (press effect)

**Test 10.6: Form Validation**
- Try to submit forms with invalid data
- Expected: Validation messages appear
- Expected: Form doesn't submit until valid
- Expected: Error messages are clear

### 11. Accessibility

**Test 11.1: Keyboard Navigation**
- Use Tab key to navigate
- Expected: Focus visible on interactive elements
- Expected: Can navigate entire site with keyboard
- Expected: Enter key activates buttons

**Test 11.2: Screen Reader (Optional)**
- Use screen reader tool
- Expected: All content readable
- Expected: Images have alt text
- Expected: Form labels associated correctly

**Test 11.3: Color Contrast**
- Check text readability
- Expected: Sufficient contrast between text and background
- Expected: All text legible

### 12. Performance

**Test 12.1: Initial Load Time**
- Clear cache and reload
- Expected: Page loads within 3 seconds
- Expected: No blocking resources

**Test 12.2: Smooth Scrolling**
- Scroll through long lists
- Expected: Smooth 60fps scrolling
- Expected: No lag or stuttering

**Test 12.3: Memory Usage**
- Use browser DevTools Performance tab
- Navigate through all pages
- Expected: No memory leaks
- Expected: Reasonable memory consumption

## Test Execution Checklist

- [ ] All Initial Load tests passed
- [ ] All Navigation tests passed
- [ ] All Home Page tests passed
- [ ] All Flights Page tests passed
- [ ] All Authentication tests passed
- [ ] All Booking Flow tests passed
- [ ] All My Bookings tests passed
- [ ] All Cancellation tests passed
- [ ] All Error Handling tests passed
- [ ] All UI/UX tests passed
- [ ] All Accessibility tests passed
- [ ] All Performance tests passed

## Automation Notes for AI Agents

When automating these tests:
1. Use browser automation tools (Puppeteer, Playwright, Selenium)
2. Wait for elements to be visible before interacting
3. Capture screenshots at each step for verification
4. Log all console errors and network failures
5. Use explicit waits for API responses
6. Test in multiple viewport sizes
7. Clear localStorage between test suites
8. Verify toast notifications appear and contain correct text
9. Check for accessibility violations using automated tools
10. Measure and report performance metrics

## Test Data Requirements

- At least 5 sample flights with varying origins/destinations
- At least 2 sample users with existing bookings
- At least 1 flight with 0 available seats
- Mix of confirmed and cancelled bookings

## Bug Reporting Template

When issues are found:
```
**Test ID:** [e.g., Test 6.2]
**Description:** [What went wrong]
**Steps to Reproduce:**
1. [Step 1]
2. [Step 2]
3. [Step 3]
**Expected Result:** [What should happen]
**Actual Result:** [What actually happened]
**Screenshots:** [If applicable]
**Browser:** [Chrome/Firefox/Safari + version]
**Console Errors:** [Any errors from DevTools]
```

## Success Criteria

The frontend is considered fully functional when:
- ✅ All 60+ test cases pass
- ✅ No critical bugs found
- ✅ Performance metrics meet targets
- ✅ Responsive design works on all screen sizes
- ✅ Error handling is graceful and user-friendly
- ✅ User flows are intuitive and complete

---

**Document Version:** 1.0  
**Last Updated:** 2026-01-13  
**Total Test Cases:** 60+