# Activity 11: Full-Stack React IPL Ticket Booking with Supabase PostgreSQL

**Course:** Web Application Development (WAD)  
**Author:** Akshay N (`R25EF021`)  
**Repository:** [Web-Application-Development](https://github.com/Yagami-akshay/Web-Application-Development)

---

## 📌 Objective
Connect the React IPL ticket booking application to a real cloud PostgreSQL database using **Supabase**, replacing hardcoded initial arrays with live database read/write operations and real-time synchronization.

---

## 🛠️ Tech Stack & Tools
- **Frontend:** React 19, Vite 8, Modern JavaScript (ES6+)
- **Backend / Database:** Supabase (Cloud PostgreSQL 15+)
- **Realtime:** Supabase Realtime Subscriptions (WebSocket `postgres_changes`)
- **Client Library:** `@supabase/supabase-js`

---

## 🗄️ Database Schema

### 1. `matches` Table
| Column | Type | Constraints | Description |
| :--- | :--- | :--- | :--- |
| `id` | SERIAL | PRIMARY KEY | Unique match identifier |
| `team1` | TEXT | NOT NULL | Home team name |
| `team2` | TEXT | NOT NULL | Away team name |
| `date` | TEXT | NOT NULL | Match fixture date |
| `venue` | TEXT | NOT NULL | Stadium & city |
| `price` | INT | NOT NULL | Ticket base price (₹) |
| `available_seats` | INT | NOT NULL | Seats remaining for booking |

### 2. `bookings` Table
| Column | Type | Constraints | Description |
| :--- | :--- | :--- | :--- |
| `id` | SERIAL | PRIMARY KEY | Auto-incrementing booking ID |
| `match_id` | INT | REFERENCES matches(id) | Associated match foreign key |
| `user_name` | TEXT | NOT NULL | Passenger / attendee name |
| `match_title` | TEXT | NOT NULL | Match title (e.g. `RCB vs KKR`) |
| `tickets` | INT | NOT NULL | Number of booked tickets |
| `total_price` | INT | NOT NULL | Computed total cost |
| `created_at` | TIMESTAMPTZ | DEFAULT now() | Booking timestamp |

---

## 🚀 Step-by-Step Implementation

### Step 1: Database Setup & Security Policies
Run SQL to configure permissions and Row Level Security (RLS) for public client operations:
```sql
GRANT USAGE ON SCHEMA public TO anon, authenticated;
GRANT ALL ON TABLE matches, bookings TO anon, authenticated;
GRANT ALL ON ALL SEQUENCES IN SCHEMA public TO anon, authenticated;

ALTER TABLE matches ENABLE ROW LEVEL SECURITY;
ALTER TABLE bookings ENABLE ROW LEVEL SECURITY;

CREATE POLICY "Allow public read on matches" ON matches FOR SELECT TO anon, authenticated USING (true);
CREATE POLICY "Allow public update on matches" ON matches FOR UPDATE TO anon, authenticated USING (true) WITH CHECK (true);
CREATE POLICY "Allow public read on bookings" ON bookings FOR SELECT TO anon, authenticated USING (true);
CREATE POLICY "Allow public insert on bookings" ON bookings FOR INSERT TO anon, authenticated WITH CHECK (true);

ALTER PUBLICATION supabase_realtime ADD TABLE matches;
ALTER PUBLICATION supabase_realtime ADD TABLE bookings;
```

### Step 2: Supabase Client Configuration (`src/supabase.js`)
Configured using Vite environment variables (`.env.local`):
```javascript
import { createClient } from '@supabase/supabase-js';

const supabaseUrl = import.meta.env.VITE_SUPABASE_URL;
const supabaseKey = import.meta.env.VITE_SUPABASE_ANON_KEY;

export const supabase = createClient(supabaseUrl, supabaseKey);
```

### Step 3: Fetching Matches with `useEffect`
Replaced static dummy data with dynamic Supabase query:
```javascript
const fetchMatches = async () => {
  const { data, error } = await supabase
    .from('matches')
    .select('*')
    .order('id', { ascending: true });

  if (data) setMatches(data);
};
```

### Step 4: Transactional Booking (`.insert()` and `.update().eq()`)
On ticket selection, the app:
1. Inserts the reservation into `bookings`.
2. Decrements `available_seats` in `matches` by `1`.
3. Updates navigation total booking counter.

```javascript
const handleSelectMatch = async (selectedMatch) => {
  // Insert booking record
  await supabase.from('bookings').insert([{
    match_id: selectedMatch.id,
    user_name: 'Akshay N',
    match_title: `${selectedMatch.team1} vs ${selectedMatch.team2}`,
    tickets: 1,
    total_price: selectedMatch.price
  }]);

  // Decrement remaining seats
  await supabase.from('matches')
    .update({ available_seats: selectedMatch.available_seats - 1 })
    .eq('id', selectedMatch.id);
};
```

### Step 5: Realtime Subscription
Using Supabase Realtime Channels, any seat reduction or new booking made on another tab/device instantly updates the UI without page refresh:
```javascript
useEffect(() => {
  const channel = supabase
    .channel('realtime-matches')
    .on('postgres_changes', { event: '*', schema: 'public', table: 'matches' }, (payload) => {
      if (payload.eventType === 'UPDATE') {
        setMatches((prev) => prev.map((m) => m.id === payload.new.id ? payload.new : m));
      } else {
        fetchMatches();
      }
    })
    .subscribe();

  return () => { supabase.removeChannel(channel); };
}, []);
```

---

## 🏃 Running the Project Locally

1. Clone or navigate to the directory:
   ```bash
   cd "activity 11"
   ```
2. Install dependencies:
   ```bash
   npm install
   ```
3. Create `.env.local` in the project root:
   ```env
   VITE_SUPABASE_URL=your_project_url
   VITE_SUPABASE_ANON_KEY=your_publishable_anon_key
   ```
4. Start the dev server:
   ```bash
   npm run dev
   ```
5. Open `http://localhost:5173` in your browser.
