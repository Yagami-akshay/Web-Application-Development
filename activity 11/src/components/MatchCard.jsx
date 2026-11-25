// =========================================================================
// 💡 REACT CHILD COMPONENT: MatchCard
// - Props received: 
//   1. 'match' (data object containing team1, team2, date, venue, price, seats)
//   2. 'onSelectMatch' (callback function sent from parent App.jsx)
//
// 💡 TEACHER MODIFICATION GUIDE:
// - If teacher asks: "Add a 'High Demand' badge when seats < 50":
//   Add: {seats < 50 && <span className="badge">Filling Fast!</span>}
// - If teacher asks: "Disable button when sold out":
//   Notice: 'disabled={isSoldOut}' is already implemented below!
// =========================================================================
export function MatchCard({ match, onSelectMatch }) {
  const seats = match.available_seats !== undefined ? match.available_seats : match.availableSeats;
  const isSoldOut = seats === 0;

  return (
    <article className="match-card">
      <h3>{match.team1} vs {match.team2}</h3>
      <p>{match.date} • {match.venue}</p>
      <p>₹{match.price} • {seats} seats left</p>
      <button disabled={isSoldOut} onClick={() => onSelectMatch(match)}>
        {isSoldOut ? 'Sold Out' : 'Book Tickets'}
      </button>
    </article>
  );
}
