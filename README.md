# Web Application Development (WAD)

Course repository for Web Application Development lab activities and assignments by **Akshay N** (`Yagami-akshay`).

---

## 📁 Repository Structure

| Directory | Title & Topic | Key Features & Deliverables |
| :--- | :--- | :--- |
| [`activity 1`](./activity%201) | **HTML5 Semantic Structure & Headings** | Semantic page layout, navigation, and structural tags |
| [`activity 2`](./activity%202) | **CSS Styling & Responsive Design** | CSS styling, color schemes, card grids, and typography |
| [`activity 3`](./activity%203) | **Form Elements & Validation** | HTML5 forms, regex patterns, input types, and constraints |
| [`activity 5`](./activity%205) | **JavaScript Basics & User Interaction** | DOM manipulation, reusable `showToast()`, and smooth scrolling |
| [`activity 7`](./activity%207) | **Selector Forms & Live Interaction** | Dropdown selectors (`<select>`), quantity input, real-time price calculation, live Booking Summary Card updates, and toast alerts without page reload |
| [`activity 8`](./activity%208) | **Responsive Layout Using CSS Grid & Flexbox** | Flexbox navbar with brand alignment, CSS Grid match schedule cards, 3-column guidelines section, JS team filter, grid/list view toggle, mobile hamburger drawer, and media query single-column reflow |
| [`activity 10`](./activity%2010) | **Introduction to React JS** | Rebuilding IPL Ticket Booking with React components, props, and state |

---

## ⚡ Activity 7: Selector Forms and Live Interaction Using JavaScript

### Objective
Use the booking form's dropdowns and selectors with JavaScript to read user choices and update the **Booking Summary Card** and total price live in real time without reloading the page.

### Tools Used
- **Visual Studio Code** (Live Server extension on `http://127.0.0.1:5500`)
- **Modern JavaScript (ES6+)**
- **HTML5 & CSS3**

### Step-by-Step Implementation
1. **Form Controls:** Utilized `<select id="match">` for match selection, `<select id="stand">` for stadium stand category, and `<input type="number" id="tickets">` for ticket quantity.
2. **DOM Selectors:** Selected all interactive controls and card targets using `document.getElementById()` and `document.querySelector()`.
3. **Event Listeners:** Attached `change` and `input` event listeners to monitor user adjustments instantly.
4. **Live Calculation & Summary Card:** Computed ticket unit prices, add-ons, and grand totals, dynamically rendering match details into the `#booking-summary-card`.
5. **Toast Confirmation:** Triggered `showToast()` to confirm price recalculation and provide immediate feedback to the user.

### Worked Example Evidence
When a user selects **Match 2: RCB vs CSK**, **Premium Stand** (₹4,000/ticket), and **Quantity: 2**, the **Booking Summary Card** instantly calculates:
$$\text{Total} = ₹4,000 \times 2 = ₹8,000$$
and displays the venue, date/time, and calculated total alongside a toast confirmation notification.

---

## 📱 Activity 8: Responsive Layout Using CSS Grid and Flexbox

### Objective
Build a responsive layout for the IPL website using **Flexbox**, **CSS Grid**, and **Media Queries**, and use **JavaScript** to make the layout interactive across devices.

### Tools Used
- **Visual Studio Code** (Live Server extension on `http://127.0.0.1:5500`)
- **CSS3 Flexbox & CSS Grid**
- **Media Queries** (`@media screen and (max-width: 1024px)`, `(max-width: 768px)`, and `(max-width: 480px)`)
- **Modern Vanilla JavaScript (ES6+)**

### Step-by-Step Technical Implementation
1. **Flexbox Navigation Bar:** 
   - Utilized `display: flex; justify-content: space-between; align-items: center;` in `.navbar` to align the logo on the left and navigation links on the right.
   - Built a brand group (`.nav-brand`) and navigation link list (`.nav-links`) utilizing flexbox spacing and alignment.
2. **CSS Grid Match Schedule & Guidelines:**
   - **Match Schedule Cards:** Implemented a multi-column CSS Grid (`grid-template-columns: repeat(3, 1fr)`) to render match schedule fixtures as structured cards.
   - **3-Column Guidelines Section:** Configured `.guidelines-grid` with `grid-template-columns: repeat(3, 1fr)` on desktop view for stadium protocols.
3. **JavaScript Team Filtering & Grid/List View Toggle:**
   - **Team Filter:** JavaScript dynamically filters `.match-card` elements by reading the `data-teams` attribute via dropdown select (`#team-filter`) or quick pills (`.pill-btn`).
   - **Grid vs List Toggle:** Toggling `#list-view-btn` adds the `.list-view` class to the grid container, transforming cards into full-width horizontal rows.
4. **Mobile Hamburger Menu (JS Class Toggle):**
   - Implemented a 3-bar hamburger button (`#hamburger-btn`) and collapsible navigation drawer.
   - JavaScript toggles the `.open` class and updates accessibility attributes (`aria-expanded`), auto-closing upon link selection, outside click, or `Escape` key press.
5. **Media Queries for Responsive Stacking:**
   - On tablets & mobile viewports ($\le 768\text{px}$), match cards reflow into a **single column** (`grid-template-columns: 1fr`).
   - The guidelines section reflows from 3 columns into a **single column**.
   - Navigation links collapse into the hamburger drawer while team filters and layout toggles remain fully functional.

### Worked Example Demonstration
When resizing the browser viewport below $768\text{px}$:
- The desktop navigation collapses into the animated hamburger menu.
- The 3-column match schedule cards reflow into a clean **single column**.
- The 3-column guidelines section stacks vertically into a **single column**.
- The team filter dropdown, quick pills, and grid/list view toggles continue to operate flawlessly across devices.
