# Activity 8: Responsive Layout Using CSS Grid and Flexbox

**Course:** Web Application Development (WAD)  
**Author:** Akshay N (SRN: `25020301587` | GitHub: `Yagami-akshay`)  
**Project:** IPL 2026 Ticket Booking Portal  

---

## 🎯 Objective
Build a responsive layout for the IPL website using **Flexbox**, **CSS Grid**, and **media queries**, and use **JavaScript** to make the layout interactive across devices.

---

## 🛠️ Step-by-Step Implementation Breakdown

### 1. Flexbox Navigation Bar
- Used `display: flex; justify-content: space-between; align-items: center;` on `.navbar` to align the IPL 2026 brand logo on the far left and the navigation menu links on the right.
- Applied Flexbox to `.nav-brand` and `.nav-links` for clean vertical centering and proportional gap distribution.

### 2. CSS Grid for Match Schedule Cards and Guidelines Section
- **Match Schedule Cards (`#matches-container`):** Displayed as a responsive card grid using `display: grid; grid-template-columns: repeat(3, 1fr); gap: 24px;` on desktop. Each fixture card displays match badges, team icons, clash codes, venue, date/time, stand ticket tiers, and a "Book Tickets" trigger button.
- **Stadium Guidelines Section (`.guidelines-grid`):** Built as an exact 3-column CSS Grid section (`grid-template-columns: repeat(3, 1fr)`) presenting Digital QR Verification, Government Photo ID, and Security Prohibitions.

### 3. JavaScript Interactivity: Team Filtering & Grid/List View Switcher
- **Dynamic Team Filtering:** Dropdown select (`#team-filter`) and franchise quick-pills (All, CSK, RCB, MI, KKR) dynamically filter match cards by checking the `data-teams` attribute in real time, updating fixture counter text and triggering toast feedback.
- **Grid vs List View Switcher:** Switching between `#grid-view-btn` and `#list-view-btn` toggles the `.list-view` class on `#matches-container`. In list view, cards transform into streamlined horizontal single-row entries.

### 4. Hamburger Menu (JS Class Toggle)
- Added `#hamburger-btn` with three animated bars.
- Implemented JavaScript click listeners that toggle the `.open` class on both the hamburger button and `.nav-links`, updating `aria-expanded`.
- Configured auto-close behavior upon clicking any navigation link, clicking outside the menu drawer, pressing the `Escape` key, or resizing above 768px.

### 5. Media Queries for Responsive Stacking
- **Desktop (> 1024px):** 3-column match schedule grid, 3-column guidelines grid, horizontal flexbox navigation, side-by-side 2-column booking layout with sticky summary card.
- **Tablet ($\le 1024px$ & $> 768px$):** Match cards reflow to 2 columns, guidelines reflow to 2 columns, booking layout stacks vertically.
- **Mobile ($\le 768px$ & $\le 480px$):**
  - Navigation links collapse into the hamburger mobile drawer.
  - Match schedule cards reflow into a **single column** (`grid-template-columns: 1fr`).
  - Guidelines section stacks into a **single column** (`grid-template-columns: 1fr`).
  - All interactive features (team filter, grid/list toggle, live price calculator) remain 100% interactive and functional.

---

## 📸 Screenshots Checklist for Submission

Place your captured screenshots inside this `screenshots/` directory:

1. **`01_desktop_navbar_flexbox.png`**  
   - Viewport: Desktop (1280px+).  
   - Content: Show top navigation bar demonstrating Flexbox alignment of the IPL logo on the left and menu links on the right.
2. **`02_desktop_match_cards_css_grid.png`**  
   - Viewport: Desktop (1280px+).  
   - Content: Show the Match Schedule section with cards arranged in a multi-column CSS Grid layout.
3. **`03_desktop_guidelines_3column_grid.png`**  
   - Viewport: Desktop (1280px+).  
   - Content: Show the Stadium Guidelines section displaying the exact 3-column CSS Grid.
4. **`04_desktop_team_filter_active.png`**  
   - Viewport: Desktop.  
   - Content: Select a team (e.g., "RCB" or "CSK") via dropdown or pills, showing only filtered match cards with the active counter and toast alert.
5. **`05_desktop_list_view_toggle.png`**  
   - Viewport: Desktop.  
   - Content: Click the "List" toggle button, showing match cards transformed into full-width horizontal rows.
6. **`06_mobile_hamburger_menu_open.png`**  
   - Viewport: Mobile (375px - 414px, e.g. iPhone / DevTools responsive mode).  
   - Content: Hamburger button clicked and active ('X' icon) with the mobile navigation drawer expanded.
7. **`07_mobile_match_cards_single_column.png`**  
   - Viewport: Mobile (375px - 414px).  
   - Content: Resized mobile view showing match cards reflowing into a clean single column.
8. **`08_mobile_guidelines_single_column.png`**  
   - Viewport: Mobile (375px - 414px).  
   - Content: Stadium Guidelines cards stacked vertically into a single column.
9. **`09_vscode_live_server_evidence.png`**  
   - Content: VS Code editor showing `index.html` / `styles.css` / `app.js` with Live Server running at `http://127.0.0.1:5500`.
