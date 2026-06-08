import streamlit as st
import base64  

PAGE_TITLE = "John Nyirenda | Portfolio"
PAGE_ICON = "logo.webp"
PROFILE_IMAGE = "profile.png"
CV_FILE = "resume.pdf"
CONTACT_EMAIL = "jnyirenda971@gmail.com"

CUSTOM_CSS = """
<style>
    #MainMenu, #footer, #header { visibility: hidden; }

    @import url('https://fonts.googleapis.com/css2?family=Inter:wght=300;400;500;600;700&family=Poppins:wght=500;600;700&display=swap');

    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }

    h1, h2, h3, h4, h5, h6 {
        font-family: 'Poppins', sans-serif !important;
        color: #0f172a !important;
    }
    
    /* Adds a subtle drop shadow specifically to the main title name */
    h1 {
        text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.15);
    }
/* 🟢 NEW: Controls the OUTSIDE background color in LIGHT MODE */
    .stApp { 
        background-color: #fffff0 !important; /* Change this for Light Mode (e.g., Soft Off-White) */
    }

    /* Controls background colors in DARK MODE */
    @media (prefers-color-scheme: dark) {
        h1, h2, h3, h4, h5, h6 { color: #f8fafc !important; }
        .stApp { 
            background-color: #0f172a !important; /* Change this for Dark Mode (e.g., Deep Dark Blue) */
        }
    }

    /* Primary text/accent: Earth Copper */
    .copper-text { color: #b45309 !important; }

    .subtitle {
        font-size: 1.25rem;
        color: #0f172a;
        border-left: 4px solid #b45309; /* Earth Copper */
        padding-left: 1rem;
        margin-bottom: 2rem;
    }

    .card {
        background-color: rgba(255, 255, 255, 0.05);
        border: 1px solid #d97706; /* Subtle borders/cards: Sand Gold */
        border-radius: 10px;
        padding: 1.5rem;
        margin-bottom: 1rem;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
    }

    hr {
        border-color: #b45309; /* Earth Copper */
        border-width: 2px;
        max-width: 100px;
        margin-left: 0;
    }
    
    /* Update Streamlit progress bars to match the Earth Copper theme */
    .stProgress > div > div > div > div {
        background-color: #b45309 !important;
    }

    /* --- BACKGROUND IMAGE BANNER --- */
    .image-banner {
        position: absolute;
        top: -4rem; /* Starts at the very top of the page */
        left: 50%;
        transform: translateX(-50%);
        width: 100vw; /* Page wide */
        height: 40vh; /* Down 40% of the screen height */
        z-index: 0; /* Sits at the bottom layer of the layout */
        pointer-events: none; /* Prevents blocking clicks on the profile text/image */
        user-select: none;
        
        /* Image formatting */
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        opacity: 0.5; /* Adjust this to make the image darker or lighter */
    }

    /* Elevate the main content so it sits securely on top of the banner */
    [data-testid="block-container"] {
        position: relative;
        z-index: 1;
        padding-top: 2rem; 
    }
    
    /* Custom Styling for the Sidebar Menu */
    [data-testid="stSidebarNav"] {
        display: none; /* Hide default sidebar nav if any */
    }
    .css-1544g2n {
        padding-top: 2rem; /* Give sidebar elements breathing room */
    }
</style>
"""

PROJECTS = [
    {
        "title": "Landslide Susceptibility Mapping using GIS & Remote Sensing",
        "desc": "Developed a detailed landslide susceptibility model utilizing Geographic Information Systems (GIS) and remote sensing techniques for hazard assessment at T/A Mwalweni Area, Rumphi.",
        "tools": "ArcGIS, QGIS, Remote Sensing Data, Analytic Hierarchy Process (AHP)",
        "results": "Created a Landslide Susceptibility Index to produce susceptibility maps identifying high-risk zones. Evaluated key conditioning factors (slope, geology, land use, rainfall) supporting disaster mitigation."
    }
]

RELEVANT_COURSES_LEFT = [
    {"name": "Surface & Underground Mining Methods", "desc": "Techniques for extracting minerals from open pits and subterranean environments."},
    {"name": "Geotechnical Engineering & Rock Mechanics", "desc": "Analysis of rock and soil behaviour to ensure safe mining excavations and slopes."},
    {"name": "Drilling and Blasting Engineering", "desc": "Design and optimization of explosive fragmentation for efficient ore extraction."},
    {"name": "Structural & Applied Geology", "desc": "Understanding rock structures and geological formations relevant to mineral exploration."},
    {"name": "Mineral Processing Methods", "desc": "Techniques for separating valuable minerals from waste rock efficiently."}
]

RELEVANT_COURSES_RIGHT = [
    {"name": "Mine & Environmental Management", "desc": "Balancing extraction operations with ecological preservation and regulatory compliance."},
    {"name": "Mine Ventilation & Safety", "desc": "Designing airflow systems to maintain safe and healthy underground working conditions."},
    {"name": "Mineral Economics & Investment Evaluation", "desc": "Financial analysis, feasibility studies, and risk assessment for mining projects."},
    {"name": "Geo-Statistics & Spatial Analysis", "desc": "Applying statistical models and GIS tools for resource estimation and mapping."},
    {"name": "Numerical Methods in Geo-mechanics", "desc": "Computational modelling for complex structural and geotechnical mining problems."}
]

ENGINEERING_SKILLS = {
    "QGIS & ArcGIS": 80,
    "Microsoft Office Suite (Excel, PPT, Word)": 85,
    "Oasis Montaj & PCI Geomatica": 65,
    "SPSS (Statistical Analysis)": 60,
    "AutoCAD": 55,
    "FLAC3D (Basics)": 35,
    "Python (Basics)": 40,
    "C++ (Basics)": 40,
}

TECHNICAL_SKILLS = [
    "Geospatial Analysis",
    "Rock Identification & Classifications",
    "Drilling & Blasting Optimization",
    "Remote Sensing",
    "Surveying & Field Research",
    "Geotechnical Engineering",
    "Environmental & Mine Management",
    "Technical Presentations",
]

st.set_page_config(
    page_title=PAGE_TITLE,
    page_icon=PAGE_ICON,
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown(CUSTOM_CSS, unsafe_allow_html=True)


def render_section_title(title, accent=None):
    accent_markup = f" <span class='copper-text'>{accent}</span>" if accent else ""
    st.markdown(f"<h2>{title}{accent_markup}</h2><hr>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)


def render_profile():
    # 1. Read the image and convert to base64 so HTML can display it
    try:
        with open("bgl.jpg", "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode()
            
        # 2. Inject the base64 image into the background-image CSS property
        bg_html = f"""
        <div class="image-banner" 
             style="background-image: url('data:image/jpeg;base64,{encoded_string}');">
        </div>
        """
        st.markdown(bg_html, unsafe_allow_html=True)
    except FileNotFoundError:
        pass # Image banner skipped if missing

    # --- Proceed with normal profile layout ---
    left, right = st.columns([1, 2.2])
    with left:
        try:
            st.image(PROFILE_IMAGE, width=350)
        except FileNotFoundError:
            st.info(f"Place {PROFILE_IMAGE} in the project folder to display your photo.")

    with right:
        st.markdown("<h1>John <span class='copper-text'>Nyirenda</span></h1>", unsafe_allow_html=True)
        st.markdown(
            "<div class='subtitle'>Mining Engineering Student | Geotechnical Design | Drilling & Blasting | GIS | Sustainable Mining Practices Advocate.</div>",
            unsafe_allow_html=True,
        )

        st.markdown("<br>", unsafe_allow_html=True)
        st.markdown("<h2>About <span class='copper-text'>Me</span></h2><hr>", unsafe_allow_html=True)

        col1, col2 = st.columns([2, 1])
        with col1:
            st.write(
                """
                As a Mining Engineering student at the **Malawi University of Business and Applied Sciences (MUBAS)**, I am passionate about transforming the earth's resources using sustainable solutions. With a strong understanding of geology, drilling, blasting, together with both surface and underground mining methods, I am building a solid understanding of modern mining practices. 

                I thrive on learning, adapting, and solving complex challenges, especially those involving environmental and geotechnical aspects of mining. I am an efficient, hardworking, accountable, and result-oriented person who desires to produce excellent products and services to meet organizational objectives.
                """
            )
        
        with col2:
            st.markdown(
                """
                <div class='card'>
                    <h4 style='margin-top: 0;'>Quick Facts</h4>
                    <b>Nationality:</b> Malawian<br>
                    <b>Location:</b> Blantyre, Malawi<br>
                    <b>Languages:</b> English, Chichewa, Tumbuka<br>
                    <b>University:</b> MUBAS<br>
                    <b>Degree:</b> BSc in Mining Engineering<br>
                    <b>Graduation:</b> Class of 2027
                </div>
                """,
                unsafe_allow_html=True,
            )
        st.markdown("<h2>Professional <span class='copper-text'>Objective:</span></h2><hr>", unsafe_allow_html=True)

        col1, col2 = st.columns([2, 1])
        with col1:
            st.write(
                """
                To become associated with an organization where I can utilize my skills and gain further experience while enhancing the organization’s productivity and commitment to sustainable resource extraction.
                """
            )
            st.write("**Core Attributes:** Efficient • Hardworking • Accountable • Result-Oriented")

def render_experience():
    render_section_title("Professional", "Experience")
    left, right = st.columns([1, 1.5])
    with left:
        st.markdown(
            """
            <div class='card'>
                <h4 style='margin-top: 0; color: #b45309;'>Geological Survey Department (GSD)</h4>
                <b>Academic Attachment (Intern)</b><br>
                <span style='color: #94a3b8;'>July 2025 - October 2025</span>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with right:
        st.write("### Key Responsibilities:")
        st.write("""
        - Conducted detailed data analysis and synthesized field findings.
        - Assisted in surveying and technical field research.
        - Utilized GIS software for map-making and spatial data interpretation.
        - Performed rock identification and geological classifications.
        - Prepared and delivered comprehensive PowerPoint presentations on project progress and findings.
        """)

def render_academic_background():
    render_section_title("Academic", "Background")
    left, right = st.columns(2)

    with left:
        st.subheader("Education")
        st.write("**Malawi University of Business and Applied Sciences (MUBAS)**")
        st.write("*Bachelor of Science in Mining Engineering (Hons)*")
        st.caption("2022 — 2027 (Expected)")
        st.write("Comprehensive academic curriculum focusing on earth sciences, extraction methodologies, safety protocols, and modern computational engineering tools.")

        st.markdown("<br>**Kasungu CCAP Private Secondary School**", unsafe_allow_html=True)
        st.write("*Malawi School Certificate of Education (MSCE)*")
        st.caption("Graduated: 2021")

    with right:
        st.subheader("Certifications & Achievements")
        st.success("🏅 **Student Engineer** – Malawi Engineering Institution (MEI) (2025)")
        st.success("🏅 **Aspire Leaders Program** – Aspire Institute (October 2025)")
        st.success("🏅 **The Pan-African Case Study Challenge** – SMAD Initiative (July 2025)")


def render_courses():
    render_section_title("Relevant", "Courses")
    st.write("A selection of core modules from the Bachelor of Science in Mining Engineering curriculum:")
    left, right = st.columns(2)

    with left:
        for course in RELEVANT_COURSES_LEFT:
            st.info(f"📚 **{course['name']}**\n\n_{course['desc']}_")

    with right:
        for course in RELEVANT_COURSES_RIGHT:
            st.info(f"📚 **{course['name']}**\n\n_{course['desc']}_")


def render_projects():
    render_section_title("Projects &", "Research")
    left, right = st.columns(2)
    for index, project in enumerate(PROJECTS):
        column = left if index % 2 == 0 else right
        with column:
            with st.expander(f"🗺️ {project['title']} (2026)", expanded=True):
                st.write(f"**Description:** {project['desc']}")
                st.write(f"**Outcome:** {project['results']}")
                st.caption(f"**Tools Used:** {project['tools']}")


def render_skills():
    render_section_title("Technical", "Skills")
    left, right = st.columns(2)

    with left:
        st.subheader("Engineering & IT Software")
        for skill, level in ENGINEERING_SKILLS.items():
            st.write(f"**{skill}**")
            st.progress(level)

    with right:
        st.subheader("Core Competencies")
        st.write(" • ".join(TECHNICAL_SKILLS))
        st.write("")
        st.subheader("Computer Skills")
        st.write("Microsoft Office Suite • Presentation Design • Report Formatting • Technical Troubleshooting")

def render_referees():
    render_section_title("Professional", "Referees")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown(
            """
            <div class='card'>
                <h4 style='margin-top: 0; color: #b45309;'>Mr. Harrison Mtumbuka</h4>
                <b>Regional Geologist</b><br>
                <i>Geological Survey Department of Malawi</i><br><br>
                📍 P/Bag 9, Mzuzu<br>
                📞 +265 999 08 82 66<br>
                📞 +265 883 24 01 05<br>
                📧 mtumbukaharris@gmail.com
            </div>
            """, unsafe_allow_html=True
        )
    with col2:
        st.markdown(
            """
            <div class='card'>
                <h4 style='margin-top: 0; color: #b45309;'>Dr. T. S. Banda</h4>
                <b>Mechanical Engineering Faculty</b><br>
                <i>Malawi University of Business and Applied Sciences</i><br><br>
                📍 P/Bag 303 Chichiri, Blantyre 3<br>
                📞 Via MUBAS Department<br><br>
                📧 tbanda@mubas.ac.mw
            </div>
            """, unsafe_allow_html=True
        )
    with col3:
        st.markdown(
            """
            <div class='card'>
                <h4 style='margin-top: 0; color: #b45309;'>Mr. Daniel Moyo</h4>
                <b>Geologist</b><br>
                <i>Geological Survey Department of Malawi</i><br><br>
                📍 P/Bag 9, Mzuzu<br>
                📞 +265 998 49 10 32<br>
                📞 +265 883 07 57 71<br>
                📧 moyodanj@gmail.com
            </div>
            """, unsafe_allow_html=True
        )

def render_gallery():
    render_section_title("Portfolio", "Gallery")
    columns = st.columns(3)
    gallery_items = [
        "GIS Map Output",
        "Slope Stability Model",
        "Fieldwork Photography",
        "Research Poster",
        "AHP Overlay Chart",
        "Mine Block Model",
    ]

    for column, item in zip(columns * 2, gallery_items):
        with column:
            st.info(f"🖼️ [ Image Placeholder ]\n\n**{item}**")


def render_contact():
    render_section_title("Get In", "Touch")
    left, right = st.columns(2)

    with left:
        st.write("Open to networking, research collaborations, and early-career opportunities in the mining and earth sciences sectors.")
        st.write("📧 **Email:** bmen21-jnyirenda@mubas.ac.mw")
        st.write(f"📧 **Email:** {CONTACT_EMAIL}")
        st.write("📞 **Phone:** +265 990 570 007")
        st.write("📞 **Phone:** +265 888 021 422")
        st.write("📍 **Location:** Malawi University of Business and Applied Sciences, P/Bag 303. Chichiri, Blantyre")
        st.write("🔗 **LinkedIn:** [linkedin.com/in/john-nyirenda](https://www.linkedin.com/in/john-nyirenda)")

    with right:
        # ALL HTML tags are pushed to the absolute left margin to prevent Markdown code-block rendering
        contact_form_html = f"""
<form action="https://formsubmit.co/{CONTACT_EMAIL}" method="POST" style="background-color: rgba(255, 255, 255, 0.05); padding: 1.5rem; border-radius: 10px; border: 1px solid #d97706; box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);">
<input type="hidden" name="_subject" value="New Portfolio Message!">
<input type="hidden" name="_honeypot" style="display:none">
<label style="font-weight: 500; display: block; margin-bottom: 0.4rem; color: #b45309;">Full Name</label>
<input type="text" name="name" required style="width: 100%; padding: 0.5rem; margin-bottom: 1rem; border-radius: 6px; border: 1px solid #d97706; background: transparent; color: inherit;">
<label style="font-weight: 500; display: block; margin-bottom: 0.4rem; color: #b45309;">Email Address</label>
<input type="email" name="email" required style="width: 100%; padding: 0.5rem; margin-bottom: 1rem; border-radius: 6px; border: 1px solid #d97706; background: transparent; color: inherit;">
<label style="font-weight: 500; display: block; margin-bottom: 0.4rem; color: #b45309;">Your Message</label>
<textarea name="message" required style="width: 100%; height: 120px; padding: 0.5rem; margin-bottom: 1.2rem; border-radius: 6px; border: 1px solid #d97706; background: transparent; color: inherit; resize: vertical;"></textarea>
<button type="submit" style="background-color: #b45309; color: white; padding: 0.6rem 1.5rem; border: none; border-radius: 6px; cursor: pointer; width: 100%; font-weight: 600;">Submit Message</button>
</form>
"""
        st.markdown(contact_form_html, unsafe_allow_html=True)


def render_cv_download():
    st.markdown("<br>", unsafe_allow_html=True)
    _, center, _ = st.columns([1, 2, 1])
    with center:
        st.markdown("<h3 style='text-align: center;'>Want to learn more?</h3>", unsafe_allow_html=True)
        try:
            with open(CV_FILE, "rb") as pdf_file:
                st.download_button(
                    label="📄 Download Full Resume",
                    data=pdf_file,
                    file_name=CV_FILE,
                    mime="application/pdf",
                    use_container_width=True,
                )
        except FileNotFoundError:
            st.warning(f"Place '{CV_FILE}' in the same folder to enable resume download.")


def render_footer():
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown(
        "<div style='text-align: center; color: #64748b; padding-bottom: 3rem;'>© 2026 John Nyirenda. All rights reserved. | Mining Engineering Portfolio</div>",
        unsafe_allow_html=True,
    )


# ==========================================
# EXECUTE APPLICATION (SIDEBAR LAYOUT)
# ==========================================

# 1. Create the Sidebar Navigation Menu
st.sidebar.markdown(f"<h2 style='text-align: center; color: #b45309;'>Menu</h2>", unsafe_allow_html=True)
st.sidebar.markdown("---")

menu_selection = st.sidebar.radio(
    "Go to Section:",
    [
        "🏠 Home", 
        "💼 Experience", 
        "🎓 Education", 
        "📚 Courses", 
        "🔬 Projects", 
        "⚙️ Skills", 
        "👥 Referees",
        "🖼️ Gallery"
    ]
)

st.sidebar.markdown("---")

# 2. Render content based on sidebar selection
if menu_selection == "🏠 Home":
    render_profile()
    st.markdown(" ")
    render_contact()
    st.markdown("---")
    render_cv_download()
    render_footer()

elif menu_selection == "💼 Experience":
    render_experience()

elif menu_selection == "🎓 Education":
    render_academic_background()

elif menu_selection == "📚 Courses":
    render_courses()

elif menu_selection == "🔬 Projects":
    render_projects()

elif menu_selection == "⚙️ Skills":
    render_skills()
    
elif menu_selection == "👥 Referees":
    render_referees()

elif menu_selection == "🖼️ Gallery":
    render_gallery()
