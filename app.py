import streamlit as st
import html

st.set_page_config(page_title="HydroStar Signature Builder", page_icon="✉️", layout="centered")
st.title("HydroStar Email Signature Builder")

# PASTE YOUR BASE64 DATA URI HERE (between the triple quotes)
LOGO_DATA_URI = """data:image/png;base64,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"""

# ============================================
# EASY CUSTOMIZATION SETTINGS - CHANGE THESE!
# ============================================

# FONT SETTINGS
FONT_BUMP = 0  # Increase or decrease ALL font sizes by this amount (e.g., 2 = +2px everywhere)
FONT_FAMILY = "Arial, sans-serif"  # Options: "Georgia, serif" | "Verdana, sans-serif" | "Calibri, sans-serif" | "Tahoma, sans-serif"

# COLOR SETTINGS (use hex codes like #18a44a or color names like "blue")
COLOR_NAME = "#18a44a"  # Green color for the person's name
COLOR_LINKS = "#18a44a"  # Green color for clickable links (email, phone, web)
COLOR_TEXT = "#111111"  # Dark gray for regular text
COLOR_TITLE = "#111111"  # Color for job title
COLOR_LEGAL = "#555555"  # Color for the legal disclaimer text

# SIZE SETTINGS
LOGO_SIZE = 90  # Size of the logo in pixels (default: 90)
NAME_BOLD = True  # Make name bold? (True or False)
TITLE_BOLD = True  # Make title bold? (True or False)
COMPANY_BOLD = True  # Make company name bold? (True or False)

# SPACING SETTINGS (in pixels)
SPACE_AFTER_NAME = 2  # Space between name and title
SPACE_AFTER_TITLE = 12  # Space between title and logo
SPACE_AFTER_LOGO = 12  # Space between logo and company name
SPACE_AFTER_COMPANY = 10  # Space between company and contact details
SPACE_BETWEEN_CONTACTS = 3  # Space between each contact line (M, E, W)
SPACE_BEFORE_ADDRESS = 12  # Space before the address lines
SPACE_BEFORE_LEGAL = 8  # Space before legal disclaimer

# FONT SIZE SETTINGS (these get bumped by FONT_BUMP automatically)
BASE_SIZE_NAME = 16  # Base size for name
BASE_SIZE_TITLE = 13  # Base size for job title
BASE_SIZE_COMPANY = 13  # Base size for company name
BASE_SIZE_CONTACTS = 13  # Base size for contact details
BASE_SIZE_ADDRESS = 13  # Base size for address
BASE_SIZE_LEGAL = 11  # Base size for legal text

# ============================================
# END OF CUSTOMIZATION SETTINGS
# ============================================

def build_signature_html(name, title, mobile, email, web):
    """Build email signature HTML with maximum compatibility"""
    
    # Clean inputs
    name = html.escape(name)
    title = html.escape(title)
    email_escaped = html.escape(email)
    
    # Format phone for tel: link
    tel_clean = "+" + "".join(c for c in mobile if c.isdigit() or c == "+")
    
    # Clean website URL
    web_display = html.escape(web.replace("https://", "").replace("http://", "").replace("/", ""))
    web_link = web if web.startswith("http") else f"https://{web}"
    
    # Apply font bump to all sizes
    size_name = BASE_SIZE_NAME + FONT_BUMP
    size_title = BASE_SIZE_TITLE + FONT_BUMP
    size_company = BASE_SIZE_COMPANY + FONT_BUMP
    size_contacts = BASE_SIZE_CONTACTS + FONT_BUMP
    size_address = BASE_SIZE_ADDRESS + FONT_BUMP
    size_legal = BASE_SIZE_LEGAL + FONT_BUMP
    
    # Apply bold settings
    name_weight = "bold" if NAME_BOLD else "normal"
    title_weight = "bold" if TITLE_BOLD else "normal"
    company_weight = "bold" if COMPANY_BOLD else "normal"
    
    # Table-based HTML for maximum email client compatibility
    return f"""<table cellpadding="0" cellspacing="0" border="0" style="font-family: {FONT_FAMILY}; color: {COLOR_TEXT};">
  <tbody>
    <tr>
      <td>
        <table cellpadding="0" cellspacing="0" border="0">
          <tbody>
            <tr>
              <td style="font-size: {size_name}px; font-weight: {name_weight}; color: {COLOR_NAME}; padding-bottom: {SPACE_AFTER_NAME}px;">{name}</td>
            </tr>
            <tr>
              <td style="font-size: {size_title}px; font-weight: {title_weight}; color: {COLOR_TITLE}; padding-bottom: {SPACE_AFTER_TITLE}px;">{title}</td>
            </tr>
            <tr>
              <td style="padding-bottom: {SPACE_AFTER_LOGO}px;">
                <img src="{LOGO_DATA_URI}" alt="HydroStar" width="{LOGO_SIZE}" height="{LOGO_SIZE}" style="display: block; border: 0;">
              </td>
            </tr>
            <tr>
              <td style="font-size: {size_company}px; color: {COLOR_TEXT}; padding-bottom: {SPACE_AFTER_COMPANY}px;">
                <{'strong' if COMPANY_BOLD else 'span'}>HydroStar Europe Ltd</{'strong' if COMPANY_BOLD else 'span'}>
              </td>
            </tr>
            <tr>
              <td>
                <table cellpadding="0" cellspacing="0" border="0">
                  <tbody>
                    <tr>
                      <td style="font-size: {size_contacts}px; color: {COLOR_TEXT}; padding-right: 8px; vertical-align: top;">M</td>
                      <td style="font-size: {size_contacts}px; padding-bottom: {SPACE_BETWEEN_CONTACTS}px;">
                        <a href="tel:{tel_clean}" style="color: {COLOR_LINKS}; text-decoration: none;">{mobile}</a>
                      </td>
                    </tr>
                    <tr>
                      <td style="font-size: {size_contacts}px; color: {COLOR_TEXT}; padding-right: 8px; vertical-align: top;">E</td>
                      <td style="font-size: {size_contacts}px; padding-bottom: {SPACE_BETWEEN_CONTACTS}px;">
                        <a href="mailto:{email_escaped}" style="color: {COLOR_LINKS}; text-decoration: none;">{email_escaped}</a>
                      </td>
                    </tr>
                    <tr>
                      <td style="font-size: {size_contacts}px; color: {COLOR_TEXT}; padding-right: 8px; vertical-align: top;">W</td>
                      <td style="font-size: {size_contacts}px; padding-bottom: {SPACE_BEFORE_ADDRESS}px;">
                        <a href="{web_link}" style="color: {COLOR_LINKS}; text-decoration: none;">{web_display}</a>
                      </td>
                    </tr>
                  </tbody>
                </table>
              </td>
            </tr>
            <tr>
              <td style="font-size: {size_address}px; color: {COLOR_TEXT}; padding-bottom: 3px;">
                Registered Office: Quantum House, 18A Old Vicarage Road, Exeter, EX2 9BJ
              </td>
            </tr>
            <tr>
              <td style="font-size: {size_address}px; color: {COLOR_TEXT}; padding-bottom: 12px;">
                Registered in England and Wales No. <a href="https://find-and-update.company-information.service.gov.uk/company/12557059" style="color: {COLOR_LINKS}; text-decoration: none;">12557059</a>
              </td>
            </tr>
            <tr>
              <td style="font-size: {size_legal}px; color: {COLOR_LEGAL}; line-height: {size_legal + 3}px; padding-top: {SPACE_BEFORE_LEGAL}px;">
                The information contained in this email, including any attachments, is confidential and may contain proprietary or legally privileged information. If you are not the intended recipient, you must not use, print, distribute, or copy this email. If you have received this email in error, please notify the sender immediately and delete this email. You should only re-transmit, disclose, or distribute this email (or any part of it) if you are authorised to do so. Thank you for understanding. HydroStar Europe Ltd.
              </td>
            </tr>
          </tbody>
        </table>
      </td>
    </tr>
  </tbody>
</table>"""

# Form for user details
with st.form("signature_form"):
    col1, col2 = st.columns(2)
    
    with col1:
        name = st.text_input("Full Name", placeholder="e.g. Ahmed Abdalla")
        title = st.text_input("Job Title", placeholder="e.g. Research Associate")
        mobile = st.text_input("Mobile", placeholder="e.g. +44(0) 7377457742")
    
    with col2:
        email = st.text_input("Email", placeholder="e.g. ahmed@hydrostar-uk.com")
        website = st.text_input("Website", value="www.hydrostar-eu.com")
    
    submitted = st.form_submit_button("Generate Signature", type="primary", use_container_width=True)

if submitted:
    if not LOGO_DATA_URI.startswith("data:image"):
        st.error("⚠️ Please paste your base64 data URI into LOGO_DATA_URI variable in the code.")
    elif not name or not title or not mobile or not email:
        st.error("⚠️ Please fill in all fields before generating the signature.")
    else:
        signature_html = build_signature_html(name, title, mobile, email, website)
        
        st.success("✅ Signature ready! Copy it below and paste into Outlook.")
        st.markdown("---")
        
        # Simple copyable signature
        signature_copy_widget = f"""
        <style>
        #signature-container:hover {{
            border-color: #18a44a !important;
            box-shadow: 0 0 5px rgba(24, 164, 74, 0.3);
        }}
        </style>
        
        <div id="signature-container" style="background-color: white; padding: 20px; border: 2px solid #ddd; border-radius: 5px; cursor: pointer; transition: all 0.3s;" onclick="selectSignature()" title="Click to select signature">
            <div id="signature">
                {signature_html}
            </div>
        </div>
        
        <button onclick="copySignature(event)" style="
            background-color: #18a44a;
            color: white;
            border: none;
            padding: 14px 28px;
            font-size: 18px;
            font-weight: bold;
            border-radius: 5px;
            cursor: pointer;
            margin-top: 15px;
            width: 100%;
        ">COPY SIGNATURE</button>
        
        <div id="copy-status" style="margin-top: 15px; text-align: center; padding: 10px; border-radius: 5px; font-size: 16px; font-weight: bold; min-height: 40px;"></div>
        
        <script>
        function selectSignature() {{
            const range = document.createRange();
            range.selectNodeContents(document.getElementById('signature'));
            const selection = window.getSelection();
            selection.removeAllRanges();
            selection.addRange(range);
        }}
        
        function copySignature(event) {{
            const sig = document.getElementById('signature');
            const statusDiv = document.getElementById('copy-status');
            const button = event.target;
            
            const range = document.createRange();
            range.selectNodeContents(sig);
            const selection = window.getSelection();
            selection.removeAllRanges();
            selection.addRange(range);
            
            try {{
                document.execCommand('copy');
                selection.removeAllRanges();
                
                // Success feedback
                button.style.backgroundColor = '#14863a';
                button.innerHTML = '✓ COPIED!';
                statusDiv.style.backgroundColor = '#d4edda';
                statusDiv.style.color = '#155724';
                statusDiv.style.border = '1px solid #c3e6cb';
                statusDiv.innerHTML = '✅ Signature copied successfully! Now paste it in Outlook.';
                
                setTimeout(() => {{
                    button.style.backgroundColor = '#18a44a';
                    button.innerHTML = 'COPY SIGNATURE';
                    statusDiv.innerHTML = '';
                    statusDiv.style.backgroundColor = 'transparent';
                    statusDiv.style.border = 'none';
                }}, 3000);
            }} catch(err) {{
                // Error feedback
                statusDiv.style.backgroundColor = '#f8d7da';
                statusDiv.style.color = '#721c24';
                statusDiv.style.border = '1px solid #f5c6cb';
                statusDiv.innerHTML = '❌ Copy failed. Please select the signature manually and copy with Ctrl+C';
            }}
        }}
        </script>
        """
        
        st.components.v1.html(signature_copy_widget, height=550)