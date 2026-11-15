# IPL Ticket Booking - Activity 10: Introduction to React JS

## 🚀 How to Run the Project

1. Open your terminal in this directory:
   ```bash
   cd "C:\Users\Akshay N\.gemini\antigravity\scratch\ipl-ticket-booking"
   ```
2. Start the development server:
   ```bash
   npm run dev
   ```
3. Open the URL shown in your terminal (usually `http://localhost:5173`) in your browser.

---

## 📁 Component Structure

- **`src/components/Navbar.jsx`**: Top navigation displaying brand name, navigation links, and dynamic total booking count received as a prop.
- **`src/components/Hero.jsx`**: Catchy hero banner introducing the ticket booking platform.
- **`src/components/MatchCard.jsx`**: Reusable component rendering match details (`team1`, `team2`, `date`, `venue`, `price`, `availableSeats`). Handles disabled state when tickets are sold out.
- **`src/components/Footer.jsx`**: Simple footer component.
- **`src/App.jsx`**: Central state management (`matches` list and `totalBookings`). Maps over the matches array to dynamically render multiple `MatchCard` components.
