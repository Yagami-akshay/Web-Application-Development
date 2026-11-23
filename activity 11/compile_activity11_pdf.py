import os
import pymupdf

def build_pdf():
    a4_w, a4_h = 595.0, 842.0
    dest_dir = r"C:\Users\Akshay N\OneDrive\Desktop\Web Application Development\activity 11"
    shots_dir = os.path.join(dest_dir, "screenshots")
    pdf_path = os.path.join(dest_dir, "activity11_sub-wad.pdf")

    img1 = os.path.join(shots_dir, "01_website_booked.png")
    img2 = os.path.join(shots_dir, "02_supabase_bookings.png")
    img3 = os.path.join(shots_dir, "03_vscode_source.png")

    doc = pymupdf.open()

    # ==========================================
    # PAGE 1: Live Working UI & Supabase Proof
    # ==========================================
    p1 = doc.new_page(width=a4_w, height=a4_h)

    # Header
    p1.insert_text((36.0, 38.0), "Activity 11 – Web Application Development", fontsize=15, fontname="helv", color=(0.04, 0.12, 0.23))
    p1.insert_text((36.0, 54.0), "Full-Stack React IPL Ticket Booking with Supabase PostgreSQL & Realtime", fontsize=10.5, fontname="helv", color=(0.2, 0.2, 0.2))
    
    # Student & Links
    p1.insert_text((36.0, 70.0), "Student: Akshay N  |  Reg. No: R25EF021  |  Date: 23 November 2026", fontsize=9.5, fontname="helv", color=(0.3, 0.3, 0.3))
    p1.insert_text((36.0, 84.0), "GitHub Repo: https://github.com/Yagami-akshay/Web-Application-Development", fontsize=9.0, fontname="helv", color=(0.1, 0.35, 0.8))
    p1.insert_text((36.0, 97.0), "Activity Link: https://github.com/Yagami-akshay/Web-Application-Development/tree/main/activity%2011", fontsize=9.0, fontname="helv", color=(0.1, 0.35, 0.8))

    # Divider line
    p1.draw_line((36.0, 105.0), (559.0, 105.0), color=(0.8, 0.8, 0.8), width=0.8)

    # Image 1: Live Website
    rect_img1 = pymupdf.Rect(36.0, 115.0, 559.0, 397.0)
    p1.insert_image(rect_img1, filename=img1)
    p1.insert_text((36.0, 410.0), "Figure 1: React application UI showing live matches fetched from Supabase, total bookings count (3),", fontsize=8.5, fontname="helv", color=(0.3, 0.3, 0.3))
    p1.insert_text((36.0, 421.0), "and decremented available seats (RCB vs KKR updated live from 30 to 29 seats).", fontsize=8.5, fontname="helv", color=(0.3, 0.3, 0.3))

    # Image 2: Supabase Table Editor
    rect_img2 = pymupdf.Rect(36.0, 440.0, 559.0, 717.0)
    p1.insert_image(rect_img2, filename=img2)
    p1.insert_text((36.0, 730.0), "Figure 2: Supabase Table Editor (public.bookings) confirming real-time insertion with row ID 7", fontsize=8.5, fontname="helv", color=(0.3, 0.3, 0.3))
    p1.insert_text((36.0, 741.0), "(user_name: 'Akshay N', match_title: 'RCB vs KKR', tickets: 1, total_price: 1800).", fontsize=8.5, fontname="helv", color=(0.3, 0.3, 0.3))

    # Footer Page 1
    p1.draw_line((36.0, 810.0), (559.0, 810.0), color=(0.85, 0.85, 0.85), width=0.6)
    p1.insert_text((36.0, 824.0), "Web Application Development  •  Activity 11 Deliverable", fontsize=8.0, fontname="helv", color=(0.5, 0.5, 0.5))
    p1.insert_text((520.0, 824.0), "Page 1 of 2", fontsize=8.0, fontname="helv", color=(0.5, 0.5, 0.5))

    # ==========================================
    # PAGE 2: VS Code Source & Step Verification
    # ==========================================
    p2 = doc.new_page(width=a4_w, height=a4_h)

    p2.insert_text((36.0, 38.0), "Activity 11 – Component Architecture & Implementation", fontsize=15, fontname="helv", color=(0.04, 0.12, 0.23))
    p2.insert_text((36.0, 54.0), "VS Code Source Code: supabase.js Client, App.jsx State & Vite Server Execution", fontsize=10.0, fontname="helv", color=(0.2, 0.2, 0.2))
    p2.draw_line((36.0, 64.0), (559.0, 64.0), color=(0.8, 0.8, 0.8), width=0.8)

    # Image 3: VS Code Workspace
    rect_img3 = pymupdf.Rect(36.0, 74.0, 559.0, 369.0)
    p2.insert_image(rect_img3, filename=img3)
    p2.insert_text((36.0, 382.0), "Figure 3: Visual Studio Code split view showing App.jsx state management, supabase.js client configuration,", fontsize=8.5, fontname="helv", color=(0.3, 0.3, 0.3))
    p2.insert_text((36.0, 393.0), ".env.local credentials, and live Vite development server execution.", fontsize=8.5, fontname="helv", color=(0.3, 0.3, 0.3))

    # Step Verification Summary Box
    p2.draw_rect(pymupdf.Rect(36.0, 412.0, 559.0, 800.0), color=(0.82, 0.85, 0.9), fill=(0.97, 0.98, 1.0), width=0.8)
    p2.insert_text((48.0, 432.0), "Technical Implementation & Rubric Verification Checklist", fontsize=11.5, fontname="helv", color=(0.05, 0.15, 0.35))

    steps = [
        ("Step 1: Database Setup & Security Policies", "Created 'matches' and 'bookings' tables in PostgreSQL on Supabase. Configured Row Level Security (RLS) policies and granted table privileges to the anon role."),
        ("Step 2: Client Configuration (src/supabase.js)", "Configured Supabase client using createClient(supabaseUrl, supabaseKey) with Vite environment variables VITE_SUPABASE_URL and VITE_SUPABASE_ANON_KEY."),
        ("Step 3: Dynamic Data Fetching with useEffect", "Replaced hardcoded initialMatches array with supabase.from('matches').select('*').order('id') inside useEffect to hydrate the UI with live database records."),
        ("Step 4: Ticket Booking Transaction Handling", "Implemented handleSelectMatch() to insert new reservations into 'bookings' and decrement available_seats in 'matches' using .insert() and .update().eq()."),
        ("Step 5: Realtime WebSocket Subscription", "Established a live channel subscription with supabase.channel().on('postgres_changes') listening to 'matches' and 'bookings' so multi-tab clients auto-sync instantly."),
        ("Step 6: End-to-End Verification", "Successfully booked tickets via UI, verified seat decrement from 30 down to 29 for RCB vs KKR, and confirmed persistent row generation in Supabase Table Editor.")
    ]

    y_offset = 452.0
    for title, desc in steps:
        p2.insert_text((48.0, y_offset), f"[OK] {title}", fontsize=9.0, fontname="helv", color=(0.08, 0.45, 0.15))
        # Word wrap description
        p2.insert_textbox(pymupdf.Rect(48.0, y_offset + 3.0, 545.0, y_offset + 50.0), desc, fontsize=8.0, fontname="helv", color=(0.25, 0.25, 0.25))
        y_offset += 55.0

    # Footer Page 2
    p2.draw_line((36.0, 810.0), (559.0, 810.0), color=(0.85, 0.85, 0.85), width=0.6)
    p2.insert_text((36.0, 824.0), "Web Application Development  •  Activity 11 Deliverable", fontsize=8.0, fontname="helv", color=(0.5, 0.5, 0.5))
    p2.insert_text((520.0, 824.0), "Page 2 of 2", fontsize=8.0, fontname="helv", color=(0.5, 0.5, 0.5))

    # Save
    doc.save(pdf_path, garbage=4, deflate=True)
    doc.close()

    # Also copy to Downloads and desktop ipl-ticket-booking for convenience
    import shutil
    shutil.copy(pdf_path, r"C:\Users\Akshay N\Downloads\activity11_sub-wad.pdf")
    shutil.copy(pdf_path, r"C:\Users\Akshay N\OneDrive\Desktop\ipl-ticket-booking\activity11_sub-wad.pdf")

    print(f"Successfully generated deliverable PDF at: {pdf_path}")
    print(f"File size: {os.path.getsize(pdf_path):,} bytes")

if __name__ == "__main__":
    build_pdf()
