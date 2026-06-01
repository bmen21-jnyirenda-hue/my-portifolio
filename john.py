import requests
import streamlit as st
import base64  
from requests.exceptions import RequestException

PAGE_TITLE = "John Nyirenda Portfolio"
PAGE_ICON = "logo.webp"
PROFILE_IMAGE = "profile.png"
CV_FILE = "JOHN NYIRENDA TEMPLATE RESUME.pdf"
CONTACT_EMAIL = "jnyirenda971@gmail.com"

CUSTOM_CSS = """
<style>
    #MainMenu, #footer, #header { visibility: hidden; }

    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Poppins:wght@500;600;700&display=swap');

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

    @media (prefers-color-scheme: dark) {
        h1, h2, h3, h4, h5, h6 { color: #f8fafc !important; }
        .stApp { background-color: #0f172a; }
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
        opacity: 0.7; /* Adjust this to make the image darker or lighter */
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
        "title": "Landslide Susceptibility Mapping",
        "desc": "Comprehensive spatial analysis mapping potential landslide zones in high-risk areas using multi-criteria decision analysis.",
        "tools": "ArcGIS, QGIS, Remote Sensing Data",
        "results": "Developed a high-accuracy predictive map integrating topographical, geological, and hydrological parameters."
    },
    {
        "title": "Geotechnical Slope Stability Analysis",
        "desc": "Advanced simulation and analysis of open-pit mine slopes to determine factors of safety under various conditions.",
        "tools": "Slide2, Geotechnical Data, Excel",
        "results": "Provided actionable recommendations balancing safety with optimal ore extraction ratios."
    },
    {
        "title": "AHP and LSI Modelling Implementation",
        "desc": "Integrating Analytical Hierarchy Process (AHP) with Landslide Susceptibility Index (LSI) for precise terrain evaluation.",
        "tools": "QGIS, Python, Statistical Models",
        "results": "Successfully calibrated a weighted overlay model applicable to various mining environments in Malawi."
    },
    {
        "title": "Strategic Mine Planning Study",
        "desc": "Conceptual mine scheduling and block modeling for an underground ore deposit.",
        "tools": "Maptek Vulcan, MineSched",
        "results": "Produced a 5-year conceptual extraction schedule optimizing net present value (NPV)."
    }
]

RELEVANT_COURSES_LEFT = [
    {"name": "Surface & Underground Mining Methods", "desc": "Techniques for extracting minerals from open pits and subterranean environments."},
    {"name": "Geotechnical Engineering & Rock Mechanics", "desc": "Analysis of rock and soil behavior to ensure safe mining excavations and slopes."},
    {"name": "Drilling and Blasting Engineering", "desc": "Design and optimization of explosive fragmentation for efficient ore extraction."},
    {"name": "Structural & Applied Geology", "desc": "Understanding rock structures and geological formations relevant to mineral exploration."},
    {"name": "Mineral Processing Methods", "desc": "Techniques for separating valuable minerals from waste rock efficiently."}
]

RELEVANT_COURSES_RIGHT = [
    {"name": "Mine & Environmental Management", "desc": "Balancing extraction operations with ecological preservation and regulatory compliance."},
    {"name": "Mine Ventilation & Safety", "desc": "Designing airflow systems to maintain safe and healthy underground working conditions."},
    {"name": "Mineral Economics & Investment Evaluation", "desc": "Financial analysis, feasibility studies, and risk assessment for mining projects."},
    {"name": "Geo-Statistics & Spatial Analysis", "desc": "Applying statistical models and GIS tools for resource estimation and mapping."},
    {"name": "Numerical Methods in Geo-mechanics", "desc": "Computational modeling for complex structural and geotechnical mining problems."}
]

ENGINEERING_SKILLS = {
    "GIS": 70,
    "Oasis Montaj": 60,
    "Excel": 75,
    "Slide2": 50,
    "Python": 40,
}

TECHNICAL_SKILLS = [
    "GIS Mapping",
    "Geology",
    "Drilling & Blasting",
    "Remote Sensing",
    "Spatial Analysis",
    "Geotechnical Analysis",
    "Organizational Effectiveness",
    "Training Assessment",
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


def render_profile():
    # 1. Read the image and convert to base64 so HTML can display it
    try:
        with open("bgl.jpg", "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode()
            
        # 2. Inject the base64 image into the background-image CSS property
        bg_html = f"""
        <div class="image-banner" 
             style="background-image: url('data:image/webp;base64,{encoded_string}');">
        </div>
        """
        st.markdown(bg_html, unsafe_allow_html=True)
    except FileNotFoundError:
        st.warning("Background image 'bgl.jpg' not found. Please ensure it is in the same folder.")

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
                As a Mining Engineering student at the **Malawi University of Business and Applied Sciences (MUBAS)**, I am passionate about transforming the earth's resources into sustainable solutions. With a strong understanding of geology, drilling, blasting, and both surface and underground mining methods, I am building a solid foundation in modern mining practices.

                I thrive on learning, adapting, and solving complex challenges—especially those involving environmental and geotechnical aspects of mining. Outside academics, I enjoy reading, music, and movies. I am always ready for a new adventure or an opportunity to collaborate on something meaningful.
                """
            )
            st.write("**Core Values:** Discipline • Continuous Learning • Innovation • Professionalism")

        with col2:
            st.markdown(
                """
                <div class='card'>
                    <h4 style='margin-top: 0;'>More</h4>
                    <b>Home District:</b> Rumphi<br>
                    <b>Trad. Authority:</b> Katumbi<br>
                    <b>Location:</b> Blantyre, Malawi<br>
                    <b>University:</b> MUBAS<br>
                    <b>Major:</b> Mining Engineering<br>
                    <b>Graduation:</b> Class of 2027
                </div>
                """,
                unsafe_allow_html=True,
            )


def render_experience():
    render_section_title("Professional", "Experience")
    left, _ = st.columns(2)
    with left:
        st.markdown(
            """
            <div class='card'>
                <h4 style='margin-top: 0; color: #b45309;'>Geological Survey Department</h4>
                <b>Intern</b><br>
                <i>Mzuzu, Northern Region, Malawi</i><br>
                <span style='color: #94a3b8;'>July 2025 - October 2025</span>
            </div>
            """,
            unsafe_allow_html=True,
        )


def render_academic_background():
    render_section_title("Academic", "Background")
    left, right = st.columns(2)

    with left:
        st.subheader("Education")
        st.write("**Malawi University of Business and Applied Sciences (MUBAS)**")
        st.write("*Bachelor of Science in Mining and Mineral Engineering*")
        st.caption("January 2022 — September 2027 (Expected)")
        st.write("Comprehensive academic curriculum focusing on earth sciences, extraction methodologies, safety protocols, and modern computational engineering tools.")

        st.markdown("<br>**Kasungu CCAP Secondary School**", unsafe_allow_html=True)
        st.write("*Malawi School Certificate of Education (MSCE)*")
        st.caption("2021")

    with right:
        st.subheader("Certifications & Achievements")
        st.success("🏅 **Malawi Engineering Institution**")
        st.success("🏅 **Aspire Program**")
        st.success("🏅 **The Pan-African Case Study Challenge 2025**")
        st.success("🏅 **Strategies to Learn and Upskill More Effectively**")


def render_courses():
    render_section_title("Relevant", "Courses")
    st.write("A selection of core modules from the Bachelor of Mining Engineering (Honours) curriculum:")
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
            with st.expander(f"🗺️ {project['title']}", expanded=True):
                st.write(f"**Description:** {project['desc']}")
                st.write(f"**Outcome:** {project['results']}")
                st.caption(f"**Tools Used:** {project['tools']}")


def render_skills():
    render_section_title("Technical", "Skills")
    left, right = st.columns(2)

    with left:
        st.subheader("Engineering Software")
        for skill, level in ENGINEERING_SKILLS.items():
            st.write(f"**{skill}**")
            st.progress(level)

    with right:
        st.subheader("Core Competencies")
        st.write(" • ".join(TECHNICAL_SKILLS))
        st.write("")
        st.subheader("Computer Skills")
        st.write("Microsoft Office Suite • Data Analysis • Presentation Design • Report Formatting • Technical Troubleshooting")


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


def send_contact_form(name: str, email: str, message: str) -> bool:
    url = f"https://formsubmit.co/ajax/{CONTACT_EMAIL}"
    payload = {
        "name": name,
        "email": email,
        "message": message,
        "_subject": f"{name} - Portfolio Message",
    }
    try:
        response = requests.post(url, data=payload, timeout=10)
        return response.ok
    except RequestException:
        return False


def render_contact():
    render_section_title("Get In", "Touch")
    left, right = st.columns(2)

    with left:
        st.write("Open to networking, research collaborations, and early-career opportunities in the mining and earth sciences sectors.")
        st.write("📧 **Email:** bmen21-jnyirenda@mubas.ac.mw")
        st.write(f"📧 **Email:** {CONTACT_EMAIL}")
        st.write("📞 **Phone:** +265 99 057 0007")
        st.write("📞 **Phone:** +265 88 802 1422")
        st.write("📍 **Location:** Blantyre, Malawi")
        st.write("🔗 **LinkedIn:** [linkedin.com/in/john-nyirenda](https://www.linkedin.com/in/john-nyirenda)")

    with right:
        with st.form("contact_form", clear_on_submit=True):
            st.write("**Send a Direct Message**")
            name = st.text_input("Full Name")
            sender_email = st.text_input("Email Address")
            message = st.text_area("Your Message", height=150)
            submitted = st.form_submit_button("Submit Message")

            if submitted:
                if not (name.strip() and sender_email.strip() and message.strip()):
                    st.warning("Please fill out all fields before submitting.")
                    return

                with st.spinner("Sending email immediately..."):
                    if send_contact_form(name.strip(), sender_email.strip(), message.strip()):
                        st.success("Message sent successfully! John will get back to you soon.")
                    else:
                        st.error("Network error. Could not connect to the email server.")


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
            st.warning(f"Place {CV_FILE} in the same folder to enable CV download.")


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
        "🖼️ Gallery"
    ]
)

st.sidebar.markdown("---")

# 2. Render content based on sidebar selection
if menu_selection == "🏠 Home":
    render_profile()
    st.markdown("---")
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

elif menu_selection == "🖼️ Gallery":
    render_gallery()
