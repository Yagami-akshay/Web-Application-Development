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

    # --- Page 1: Live Website & Supabase Table ---
    p1 = doc.new_page(width=a4_w, height=a4_h)

    p1.insert_text((40.0, 42.0), "Activity 11 – Web Application Development", fontsize=15, fontname="helv", color=(0, 0, 0))
    p1.insert_text((40.0, 62.0), "GitHub Repository: https://github.com/Yagami-akshay/Web-Application-Development", fontsize=9.5, fontname="helv", color=(0.1, 0.3, 0.8))
    p1.insert_text((40.0, 77.0), "Activity 11 Link: https://github.com/Yagami-akshay/Web-Application-Development/tree/main/activity%2011", fontsize=9.5, fontname="helv", color=(0.1, 0.3, 0.8))

    # Image 1: Live Working Website
    rect_img1 = pymupdf.Rect(40.0, 95.0, 555.0, 425.0)
    p1.insert_image(rect_img1, filename=img1)

    # Image 2: Supabase Table Editor
    rect_img2 = pymupdf.Rect(40.0, 445.0, 555.0, 775.0)
    p1.insert_image(rect_img2, filename=img2)

    # --- Page 2: VS Code Source Code ---
    p2 = doc.new_page(width=a4_w, height=a4_h)

    p2.insert_text((40.0, 42.0), "Activity 11 – Web Application Development", fontsize=15, fontname="helv", color=(0, 0, 0))
    p2.insert_text((40.0, 62.0), "GitHub Repository: https://github.com/Yagami-akshay/Web-Application-Development", fontsize=9.5, fontname="helv", color=(0.1, 0.3, 0.8))
    p2.insert_text((40.0, 77.0), "Activity 11 Link: https://github.com/Yagami-akshay/Web-Application-Development/tree/main/activity%2011", fontsize=9.5, fontname="helv", color=(0.1, 0.3, 0.8))

    # Image 3: VS Code Source Code & Dev Server
    rect_img3 = pymupdf.Rect(40.0, 95.0, 555.0, 455.0)
    p2.insert_image(rect_img3, filename=img3)

    # Optimize and save
    doc.save(pdf_path, garbage=4, deflate=True)
    doc.close()

    # Copy to Downloads and desktop project
    import shutil
    shutil.copy(pdf_path, r"C:\Users\Akshay N\Downloads\activity11_sub-wad.pdf")
    shutil.copy(pdf_path, r"C:\Users\Akshay N\OneDrive\Desktop\ipl-ticket-booking\activity11_sub-wad.pdf")

    print(f"Successfully compiled simple PDF to: {pdf_path}")
    print(f"File size: {os.path.getsize(pdf_path):,} bytes")

if __name__ == "__main__":
    build_pdf()
