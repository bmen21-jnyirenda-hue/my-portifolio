import streamlit as st
import base64
import requests  # Used to send the form data immediately via HTTP POST

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="John Nyirenda Portfolio",
    page_icon=":pick:",  
    layout="wide",
    initial_sidebar_state="collapsed"
)

# --- CUSTOM CSS (Tailwind-inspired Theme) ---
custom_css = """
<style>
    /* Hide Streamlit Default Menu and Footer */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* Global Font and Colors */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Poppins:wght@500;600;700&display=swap');
    
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
    }
    
    h1, h2, h3, h4, h5, h6 {
        font-family: 'Poppins', sans-serif !important;
        color: #0f172a !important; /* Dark Navy */
    }
    
    /* Dark Mode Overrides */
    @media (prefers-color-scheme: dark) {
        h1, h2, h3, h4, h5, h6 {
            color: #f8fafc !important; 
        }
        .stApp {
            background-color: #0f172a;
        }
    }

    /* Accents & Specifics */
    .gold-text {
        color: #eab308 !important; /* Gold Accent */
    }
    .subtitle {
        font-size: 1.25rem;
        color: #64748b;
        border-left: 4px solid #eab308;
        padding-left: 1rem;
        margin-bottom: 2rem;
    }
    .card {
        background-color: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 10px;
        padding: 1.5rem;
        margin-bottom: 1rem;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
    }
    hr {
        border-color: #eab308;
        border-width: 2px;
        max-width: 100px;
        margin-left: 0;
    }
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# --- DATA DICTIONARIES ---
projects = [
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

relevant_courses_left = [
    {"name": "Surface & Underground Mining Methods", "desc": "Techniques for extracting minerals from open pits and subterranean environments."},
    {"name": "Geotechnical Engineering & Rock Mechanics", "desc": "Analysis of rock and soil behavior to ensure safe mining excavations and slopes."},
    {"name": "Drilling and Blasting Engineering", "desc": "Design and optimization of explosive fragmentation for efficient ore extraction."},
    {"name": "Structural & Applied Geology", "desc": "Understanding rock structures and geological formations relevant to mineral exploration."},
    {"name": "Mineral Processing Methods", "desc": "Techniques for separating valuable minerals from waste rock efficiently."}
]

relevant_courses_right = [
    {"name": "Mine & Environmental Management", "desc": "Balancing extraction operations with ecological preservation and regulatory compliance."},
    {"name": "Mine Ventilation & Safety", "desc": "Designing airflow systems to maintain safe and healthy underground working conditions."},
    {"name": "Mineral Economics & Investment Evaluation", "desc": "Financial analysis, feasibility studies, and risk assessment for mining projects."},
    {"name": "Geo-Statistics & Spatial Analysis", "desc": "Applying statistical models and GIS tools for resource estimation and mapping."},
    {"name": "Numerical Methods in Geo-mechanics", "desc": "Computational modeling for complex structural and geotechnical mining problems."}
]

engineering_skills = { "GIS": 70, "Oasis Montaj": 60,"Exceel": 75,"Slide2": 50, "Python":40}
technical_skills = ["GIS Mapping", "Geology", "Drilling & Blasting", "Remote Sensing", "Spatial Analysis", "Geotechnical Analysis", "Organizational Effectiveness", "Training Assessment"]

# --- 1 & 2. HERO AND ABOUT ME SECTION ---
st.markdown("<br><br>", unsafe_allow_html=True)

main_col1, main_col2 = st.columns([1, 2.2])

with main_col1:
    try:
        st.image("profile.png", width=350)
    except FileNotFoundError:
        st.info("Place your profile.png image in this directory.")

with main_col2:
    st.markdown("<h1>John <span class='gold-text'>Nyirenda</span></h1>", unsafe_allow_html=True)
    st.markdown("<div class='subtitle'>Mining Engineering Student | Geotechnical Design, Drilling & Blasting | Geographic System Information GIS | Sustainable Mining Practices Advocate.</div>", unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    st.markdown("<h2>About <span class='gold-text'>Me</span></h2><hr>", unsafe_allow_html=True)
    
    inner_col1, inner_col2 = st.columns([2, 1])
    with inner_col1:
        st.write("""
        As a Mining Engineering student at the **Malawi University of Business and Applied Sciences (MUBAS)**, I am passionate about transforming the earth's resources into sustainable solutions. With a strong understanding of geology, drilling, blasting, and both surface and underground mining methods, I am building a solid foundation in modern mining practices.
        
        I thrive on learning, adapting, and solving complex challenges—especially those involving environmental and geotechnical aspects of mining. Outside academics, I enjoy reading, music, and movies. I am always ready for a new adventure or an opportunity to collaborate on something meaningful.
        """)
        st.write("**Core Values:** Discipline • Continuous Learning • Innovation • Professionalism")
    with inner_col2:
        st.markdown("""
        <div class='card'>
            <h4 style="margin-top: 0;">More</h4>
            <b>Home District:</b> Rumphi<br>
            <b>Trad. Authority:</b> Katumbi<br>
            <b>Location:</b> Blantyre, Malawi<br>
            <b>University:</b> MUBAS<br>
            <b>Major:</b> Mining Engineering<br>
            <b>Graduation:</b> Class of 2027
        </div>
        """, unsafe_allow_html=True)

st.markdown("---")

# --- 3. PROFESSIONAL EXPERIENCE ---
st.markdown("<h2>Professional <span class='gold-text'>Experience</span></h2><hr>", unsafe_allow_html=True)
exp_col1, exp_col2 = st.columns(2)

with exp_col1:
    st.markdown("""
    <div class='card'>
        <h4 style="margin-top: 0; color: #eab308;">Geological Survey Department</h4>
        <b>Intern</b><br>
        <i>Mzuzu, Northern Region, Malawi</i><br>
        <span style="color: #94a3b8;">July 2025 - October 2025</span>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")

# --- 4. ACADEMIC BACKGROUND & CERTIFICATIONS ---
st.markdown("<h2>Academic <span class='gold-text'>Background</span></h2><hr>", unsafe_allow_html=True)
acad_col1, acad_col2 = st.columns(2)

with acad_col1:
    st.subheader("Education")
    st.write("**Malawi University of Business and Applied Sciences (MUBAS)**")
    st.write("*Bachelor of Science in Mining and Mineral Engineering*")
    st.caption("January 2022 — September 2027 (Expected)")
    st.write("Comprehensive academic curriculum focusing on earth sciences, extraction methodologies, safety protocols, and modern computational engineering tools.")
    
    st.write("<br>**Kasungu CCAP Secondary School**", unsafe_allow_html=True)
    st.write("*Malawi School Certificate of Education (MSCE)*")
    st.caption("2021")

with acad_col2:
    st.subheader("Certifications & Achievements")
    st.success("🏅 **Malawi Engineering Institution**")
    st.success("🏅 **The Pan-African Case Study Challenge 2025**")
    st.success("🏅 **Strategies to Learn and Upskill More Effectively**")
    st.success("🏅 **Aspire Program**")

st.markdown("---")

# --- 5. RELEVANT COURSES ---
st.markdown("<h2>Relevant <span class='gold-text'>Courses</span></h2><hr>", unsafe_allow_html=True)
st.write("A selection of core modules from the Bachelor of Mining Engineering (Honours) curriculum:")

course_col1, course_col2 = st.columns(2)

with course_col1:
    for course in relevant_courses_left:
        st.info(f"📚 **{course['name']}**\n\n_{course['desc']}_")

with course_col2:
    for course in relevant_courses_right:
        st.info(f"📚 **{course['name']}**\n\n_{course['desc']}_")

st.markdown("---")

# --- 6. PROJECTS & RESEARCH ---
st.markdown("<h2>Projects & <span class='gold-text'>Research</span></h2><hr>", unsafe_allow_html=True)
p_col1, p_col2 = st.columns(2)

for i, proj in enumerate(projects):
    target_col = p_col1 if i % 2 == 0 else p_col2
    with target_col:
        with st.expander(f"🗺️ {proj['title']}", expanded=True):
            st.write(f"**Description:** {proj['desc']}")
            st.write(f"**Outcome:** {proj['results']}")
            st.caption(f"**Tools Used:** {proj['tools']}")

st.markdown("---")

# --- 7. TECHNICAL SKILLS ---
st.markdown("<h2>Technical <span class='gold-text'>Skills</span></h2><hr>", unsafe_allow_html=True)
skill_col1, skill_col2 = st.columns(2)

with skill_col1:
    st.subheader("Engineering Software")
    for skill, level in engineering_skills.items():
        st.write(f"**{skill}**")
        st.progress(level)

with skill_col2:
    st.subheader("Core Competencies")
    st.write(" • ".join(technical_skills))
    st.write("")
    st.subheader("Computer Skills")
    st.write("Microsoft Office Suite • Data Analysis • Presentation Design • Report Formatting • Technical Troubleshooting")

st.markdown("---")

# --- 8. PORTFOLIO GALLERY ---
st.markdown("<h2>Portfolio <span class='gold-text'>Gallery</span></h2><hr>", unsafe_allow_html=True)
gal_col1, gal_col2, gal_col3 = st.columns(3)

galleries = ["GIS Map Output", "Slope Stability Model", "Fieldwork Photography", "Research Poster", "AHP Overlay Chart", "Mine Block Model"]
cols = [gal_col1, gal_col2, gal_col3, gal_col1, gal_col2, gal_col3]

for col, item in zip(cols, galleries):
    with col:
        st.info(f"🖼️ [ Image Placeholder ]\n\n**{item}**")

st.markdown("---")

# --- 9. CONTACT SECTION (IMMEDIATE SENDING - NO PASSWORDS) ---
st.markdown("<h2>Get In <span class='gold-text'>Touch</span></h2><hr>", unsafe_allow_html=True)
contact_col1, contact_col2 = st.columns([1, 1])

with contact_col1:
    st.write("Open to networking, research collaborations, and early-career opportunities in the mining and earth sciences sectors.")
    st.write("📧 **Email:** bmen21-jnyirenda@mubas.ac.mw")
    st.write("📧 **Email:** jnyirenda971@gmail.com")
    st.write("📞 **Phone:** +265 99 057 0007")
    st.write("📞 **Phone:** +265 88 802 1422")
    st.write("📍 **Location:** Blantyre, Malawi")
    st.write("🔗 **LinkedIn:** [linkedin.com/in/john-nyirenda](https://www.linkedin.com/in/john-nyirenda)")
    
with contact_col2:
    with st.form("contact_form", clear_on_submit=True):
        st.write("**Send a Direct Message**")
        name = st.text_input("Full Name")
        sender_email = st.text_input("Email Address")
        message = st.text_area("Your Message", height=150)
        submitted = st.form_submit_button("Submit Message")
        
        if submitted:
            # Check to make sure the user didn't leave fields blank
            if name.strip() and sender_email.strip() and message.strip():
                
                # Updated directly to your Gmail AJAX endpoint
                url = "https://formsubmit.co/ajax/jnyirenda971@gmail.com"
                
                payload = {
                    "name": name,
                    "email": sender_email,
                    "message": message,
                    "_subject": f"{name} - Portifolio Message"
                }
                
                with st.spinner("Sending email immediately..."):
                    try:
                        # Sending a proper POST request with data
                        response = requests.post(url, data=payload)
                        
                        if response.status_code == 200:
                            st.success("Message sent successfully! John will get back to you soon.")
                        else:
                            st.error(f"FormSubmit rejected the message (Error Code: {response.status_code}).")
                    except Exception as e:
                        st.error("Network error. Could not connect to the email server.")
            else:
                st.warning("Please fill out all fields before submitting.")

st.markdown("---")

# --- 10. CV DOWNLOAD SECTION ---
st.markdown("<br>", unsafe_allow_html=True)
cv_col1, cv_col2, cv_col3 = st.columns([1, 2, 1])

with cv_col2:
    st.markdown("<h3 style='text-align: center;'>Want to learn more?</h3>", unsafe_allow_html=True)
    
    try:
        with open("Profile.pdf", "rb") as pdf_file:
            pdf_bytes = pdf_file.read()
            st.download_button(
                label="📄 Download Full CV",
                data=pdf_bytes,
                file_name="John_Nyirenda_CV.pdf",
                mime="application/pdf",
                use_container_width=True 
            )
    except FileNotFoundError:
        st.download_button(
            label="📄 Download Full CV",
            data=b"Please place Profile.pdf in the same folder",
            file_name="John_Nyirenda_CV.pdf",
            mime="application/pdf",
            use_container_width=True 
        )

st.markdown("<br><br>", unsafe_allow_html=True)

# --- FOOTER ---
st.markdown("<div style='text-align: center; color: #64748b;'>© 2026 John Nyirenda. All rights reserved. | Mining Engineering Portfolio</div>", unsafe_allow_html=True)