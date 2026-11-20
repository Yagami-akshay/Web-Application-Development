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
