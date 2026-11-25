import { useState } from 'react';
import { Navbar } from './components/Navbar';
import { Hero } from './components/Hero';
import { MatchCard } from './components/MatchCard';
import { Footer } from './components/Footer';
import './App.css';

// =========================================================================
// 💡 ACTIVITY 10: REUSABLE COMPONENTS, PROPS & STATE (PURE REACT)
// - Objective: Rebuild booking UI using JSX, props, and state.
// - Matches are stored in this initial array and mapped dynamically.
// =========================================================================
const initialMatches = [
  {
    id: 1,
    team1: 'Chennai Super Kings',
    team2: 'Royal Challengers Bengaluru',
    date: '22 March 2026',
    venue: 'MA Chidambaram Stadium, Chennai',
    price: 1500,
    availableSeats: 5,
  },
  {
    id: 2,
    team1: 'Mumbai Indians',
    team2: 'Kolkata Knight Riders',
    date: '25 March 2026',
    venue: 'Wankhede Stadium, Mumbai',
    price: 2000,
    availableSeats: 0, // Sold out test
  },
  {
    id: 3,
    team1: 'Gujarat Titans',
    team2: 'Rajasthan Royals',
    date: '28 March 2026',
    venue: 'Narendra Modi Stadium, Ahmedabad',
    price: 1200,
    availableSeats: 12,
  },
  {
    id: 4,
    team1: 'Delhi Capitals',
    team2: 'Sunrisers Hyderabad',
    date: '31 March 2026',
    venue: 'Arun Jaitley Stadium, Delhi',
    price: 1800,
    availableSeats: 8,
  },
];

export default function App() {
  // State for matches (allows decrementing seats on booking)
  const [matches, setMatches] = useState(initialMatches);

  // State for total bookings count
  const [totalBookings, setTotalBookings] = useState(0);

  // Handler passed to MatchCard component as a prop
  const handleSelectMatch = (selectedMatch) => {
    if (selectedMatch.availableSeats <= 0) return;

    // Decrement available seats for selected match
    setMatches((prevMatches) =>
      prevMatches.map((match) =>
        match.id === selectedMatch.id
          ? { ...match, availableSeats: match.availableSeats - 1 }
          : match
      )
    );

    // Increase total booking count in state
    setTotalBookings((prevCount) => prevCount + 1);
  };

  return (
    <div className="app-container">
      {/* Passing totalBookings down to Navbar as a prop */}
      <Navbar totalBookings={totalBookings} />
      
      <main className="main-content">
        <Hero />

        <section className="matches-section">
          <h2>Upcoming Matches</h2>
          <div className="matches-grid">
            {/* Dynamic list rendering using .map() and passing props to MatchCard */}
            {matches.map((match) => (
              <MatchCard
                key={match.id}
                match={match}
                onSelectMatch={handleSelectMatch}
              />
            ))}
          </div>
        </section>
      </main>

      <Footer />
    </div>
  );
}
