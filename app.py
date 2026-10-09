
import streamlit as st

st.set_page_config(page_title="Government Scheme Eligibility Checker", layout="wide")

st.title("Government Scheme Eligibility Checker")
st.write(
    "Enter your details to find government schemes that may suit you. "
    "Results are preliminary and must be verified with official scheme guidelines."
)

YES_NO = ["Yes", "No", "Not sure"]

# =====================================================
# SECTION 1: PERSONAL INFORMATION
# =====================================================

st.header("1. Personal Information")

col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Your age", min_value=0, max_value=120, value=18)
    income = st.number_input(
        "Annual family income (₹)", min_value=0, value=200000, step=10000
    )
    gender = st.selectbox("Gender", ["Female", "Male", "Other"])

with col2:
    category = st.selectbox(
        "Social category", ["General", "SC", "ST", "OBC", "EWS", "DNT"]
    )
    special_condition = st.selectbox(
        "Do you meet a special circumstance required by a scholarship, "
        "such as being an orphan or a ward of a deceased/martyred parent?",
        YES_NO
    )

# =====================================================
# SECTION 2: EDUCATION DETAILS
# =====================================================

st.header("2. Education Details")

education = st.selectbox(
    "Current education status",
    [
        "Not currently studying",
        "School",
        "Post-matric education",
        "College/University",
        "Higher education abroad"
    ]
)

col1, col2 = st.columns(2)

with col1:
    aicte_institution = st.selectbox(
        "Are you studying in an AICTE-approved institution?", YES_NO
    )
    disability = st.selectbox(
        "Do you have a certified disability of 40% or more?", YES_NO
    )
    csss_merit = st.selectbox(
        "Did you score among the top 20% of successful students "
        "in your Class 12 board?", YES_NO
    )
    nmms_selected = st.selectbox(
        "Have you qualified for the NMMS scholarship selection?", YES_NO
    )

with col2:
    marks_60 = st.selectbox(
        "Do you have at least 60% marks in the qualifying examination?", YES_NO
    )
    admission_offer = st.selectbox(
        "Do you have an admission offer from a foreign institution?", YES_NO
    )
    other_scholarship = st.selectbox(
        "Are you receiving another scholarship that may not be allowed "
        "under the scheme?", YES_NO
    )
    yasasvi_category = st.selectbox(
        "Do you belong to a category eligible under PM YASASVI?",
        YES_NO
    )

# =====================================================
# SECTION 3: SPECIAL ELIGIBILITY CONDITIONS
# =====================================================

st.header("3. Special Eligibility Conditions")

col1, col2 = st.columns(2)

with col1:
    pmjay_beneficiary = st.selectbox(
        "Do you belong to a household eligible under PM-JAY?",
        YES_NO
    )
    eligible_overseas_category = st.selectbox(
        "Do you meet the eligible category requirements for the "
        "National Overseas Scholarship?", YES_NO
    )

with col2:
    pmjay_verification = st.selectbox(
        "Have you checked your PM-JAY beneficiary status?", YES_NO
    )
    artisan = st.selectbox(
        "Do you practise a traditional trade covered by PM Vishwakarma?",
        YES_NO
    )

# =====================================================
# SECTION 4: BUSINESS AND STARTUP DETAILS
# =====================================================

st.header("4. Business and Startup Details")

business_status = st.selectbox(
    "Which option describes you?",
    [
        "No business and not planning one",
        "Planning a new business",
        "Already running a business",
        "Running a startup"
    ]
)

col1, col2 = st.columns(2)

with col1:
    business_activity = st.selectbox(
        "Is your proposed or existing business an eligible income-generating "
        "activity?", YES_NO
    )
    greenfield = st.selectbox(
        "Is this a new business venture rather than an expansion of an "
        "existing business?", YES_NO
    )
    dpiit = st.selectbox(
        "Does your startup have DPIIT recognition?", YES_NO
    )
    technology_based = st.selectbox(
        "Is your startup based on technology or innovation?", YES_NO
    )

with col2:
    startup_age = st.number_input(
        "Age of your startup in years", min_value=0, max_value=100, value=0
    )
    previous_support = st.number_input(
        "Government support already received by your startup (₹)",
        min_value=0, value=0, step=100000
    )
    indian_promoter = st.selectbox(
        "Do Indian promoters hold at least 51% ownership in your startup?",
        YES_NO
    )
    loan_default = st.selectbox(
        "Have you defaulted on a loan?", YES_NO
    )
    npa = st.selectbox(
        "Has your loan account been classified as a Non-Performing Asset (NPA)?",
        YES_NO
    )

# =====================================================
# SECTION 5: HEALTH AND GOVERNMENT EMPLOYMENT
# =====================================================

st.header("5. Health and Government Employment")

col1, col2 = st.columns(2)

with col1:
    central_employee = st.selectbox(
        "Are you a Central Government employee or pensioner?", YES_NO
    )
    senior_healthcare = st.selectbox(
        "Are you aged 60 or above and seeking elderly healthcare services?",
        YES_NO
    )

with col2:
    ayushman_senior = st.selectbox(
        "Are you aged 70 or above?", YES_NO
    )
    cg_health_need = st.selectbox(
        "Are you seeking healthcare coverage through CGHS?", YES_NO
    )

# =====================================================
# SECTION 6: SKILLS AND TRAINING
# =====================================================

st.header("6. Skills and Training")

col1, col2 = st.columns(2)

with col1:
    apprentice = st.selectbox(
        "Are you applying for or undertaking an apprenticeship?", YES_NO
    )
    apprenticeship_contract = st.selectbox(
        "Do you have an apprenticeship contract with an employer?",
        YES_NO
    )
    self_employed = st.selectbox(
        "Are you self-employed in your traditional trade?", YES_NO
    )

with col2:
    aadhaar = st.selectbox("Do you have Aadhaar?", YES_NO)
    linked_bank = st.selectbox(
        "Do you have a bank account linked to Aadhaar?", YES_NO
    )
    skill_india = st.selectbox(
        "Are you registered on the Skill India Digital Hub, if required?",
        YES_NO
    )

# =====================================================
# SECTION 7: DOCUMENTS AND OTHER REQUIREMENTS
# =====================================================

st.header("7. Documents and Other Requirements")

col1, col2 = st.columns(2)

with col1:
    family_trade_condition = st.selectbox(
        "Do you meet the family and trade conditions applicable to "
        "PM Vishwakarma?", YES_NO
    )
    business_documents = st.selectbox(
        "Can you provide the required business and identity documents?",
        YES_NO
    )

with col2:
    pmjay_documents = st.selectbox(
        "Can you provide documents needed to verify your PM-JAY eligibility?",
        YES_NO
    )
    scheme_documents = st.selectbox(
        "Can you provide the income, category and education documents "
        "required for the relevant scheme?", YES_NO
    )

# =====================================================
# ELIGIBILITY CHECK
# =====================================================

if st.button("Check Eligibility", type="primary"):

    eligible = []
    not_eligible = []
    verification = []

    # -------------------------------------------------
    # 1. AICTE-SWANATH SCHOLARSHIP
    # -------------------------------------------------

    reasons = []

    if education not in ["Post-matric education", "College/University"]:
        reasons.append("You must be pursuing eligible higher education.")
    if aicte_institution != "Yes":
        reasons.append("AICTE-approved institution status is not confirmed.")
    if special_condition != "Yes":
        reasons.append("The required special circumstance is not confirmed.")
    if income > 800000:
        reasons.append("Family income exceeds ₹8 lakh.")
    if other_scholarship == "Yes":
        reasons.append("Another scholarship may not be permitted.")

    if not reasons:
        eligible.append(("AICTE-Swanath Scholarship",
                         "Potential support for eligible students facing specified special circumstances."))
    elif "Not sure" in [aicte_institution, special_condition, other_scholarship]:
        verification.append(("AICTE-Swanath Scholarship", reasons))
    else:
        not_eligible.append(("AICTE-Swanath Scholarship", reasons))

    # -------------------------------------------------
    # 2. POST-MATRIC SCHOLARSHIP FOR STUDENTS WITH DISABILITIES
    # -------------------------------------------------

    reasons = []

    if education not in ["Post-matric education", "College/University"]:
        reasons.append("Post-matric education is required.")
    if disability != "Yes":
        reasons.append("A certified disability of at least 40% is not confirmed.")
    if income > 250000:
        reasons.append("Family income exceeds ₹2.5 lakh.")
    if other_scholarship == "Yes":
        reasons.append("Another scholarship may not be permitted.")

    if not reasons:
        eligible.append(("Post-Matric Scholarship for Students with Disabilities",
                         "Scholarship support for eligible students with disabilities."))
    elif "Not sure" in [disability, other_scholarship]:
        verification.append(("Post-Matric Scholarship for Students with Disabilities", reasons))
    else:
        not_eligible.append(("Post-Matric Scholarship for Students with Disabilities", reasons))

    # -------------------------------------------------
    # 3. POST-MATRIC SCHOLARSHIP FOR SC STUDENTS
    # -------------------------------------------------

    reasons = []

    if category != "SC":
        reasons.append("The scheme is for eligible SC students.")
    if education not in ["Post-matric education", "College/University"]:
        reasons.append("Post-matric education is required.")
    if income > 250000:
        reasons.append("Family income exceeds ₹2.5 lakh.")

    if not reasons:
        eligible.append(("Post-Matric Scholarship for SC Students",
                         "Scholarship support for eligible SC students."))
    else:
        not_eligible.append(("Post-Matric Scholarship for SC Students", reasons))

    # -------------------------------------------------
    # 4. PM YASASVI SCHOLARSHIP
    # -------------------------------------------------

    reasons = []

    if education not in ["Post-matric education", "College/University", "School"]:
        reasons.append("Eligible school or post-matric study is required.")
    if yasasvi_category != "Yes":
        reasons.append("Eligible social category is not confirmed.")
    if income > 250000:
        reasons.append("Family income exceeds the simplified screening limit of ₹2.5 lakh.")

    if not reasons:
        eligible.append(("PM YASASVI Scholarship",
                         "Potential scholarship support for eligible students."))
    elif yasasvi_category == "Not sure":
        verification.append(("PM YASASVI Scholarship", reasons))
    else:
        not_eligible.append(("PM YASASVI Scholarship", reasons))

    # -------------------------------------------------
    # 5. CENTRAL SECTOR SCHOLARSHIP (CSSS)
    # -------------------------------------------------

    reasons = []

    if education != "College/University":
        reasons.append("You must be studying at college or university.")
    if csss_merit != "Yes":
        reasons.append("Top-20-percentile Class 12 performance is not confirmed.")
    if income > 450000:
        reasons.append("Family income exceeds ₹4.5 lakh.")

    if not reasons:
        eligible.append(("Central Sector Scheme of Scholarship",
                         "Potential merit-based scholarship for eligible college students."))
    elif csss_merit == "Not sure":
        verification.append(("Central Sector Scheme of Scholarship", reasons))
    else:
        not_eligible.append(("Central Sector Scheme of Scholarship", reasons))

    # -------------------------------------------------
    # 6. NATIONAL MEANS-CUM-MERIT SCHOLARSHIP
    # -------------------------------------------------

    reasons = []

    if education != "School":
        reasons.append("This scheme is for eligible school students.")
    if nmms_selected != "Yes":
        reasons.append("NMMS selection is not confirmed.")
    if income > 350000:
        reasons.append("Family income exceeds the simplified screening limit of ₹3.5 lakh.")

    if not reasons:
        eligible.append(("National Means-cum-Merit Scholarship Scheme",
                         "Scholarship support for eligible school students."))
    elif nmms_selected == "Not sure":
        verification.append(("National Means-cum-Merit Scholarship Scheme", reasons))
    else:
        not_eligible.append(("National Means-cum-Merit Scholarship Scheme", reasons))

    # -------------------------------------------------
    # 7. NATIONAL OVERSEAS SCHOLARSHIP
    # -------------------------------------------------

    reasons = []

    if eligible_overseas_category != "Yes":
        reasons.append("Eligible category requirements are not confirmed.")
    if education != "Higher education abroad":
        reasons.append("You must be pursuing eligible higher education abroad.")
    if marks_60 != "Yes":
        reasons.append("At least 60% marks are not confirmed.")
    if admission_offer != "Yes":
        reasons.append("A foreign institution admission offer is not confirmed.")
    if age > 35:
        reasons.append("Age exceeds the simplified screening limit of 35.")
    if income > 800000:
        reasons.append("Family income exceeds ₹8 lakh.")

    if not reasons:
        eligible.append(("National Overseas Scholarship",
                         "Potential financial support for eligible overseas study."))
    elif "Not sure" in [eligible_overseas_category, marks_60, admission_offer]:
        verification.append(("National Overseas Scholarship", reasons))
    else:
        not_eligible.append(("National Overseas Scholarship", reasons))

    # -------------------------------------------------
    # 8. PRADHAN MANTRI MUDRA YOJANA
    # -------------------------------------------------

    reasons = []

    if business_status == "No business and not planning one":
        reasons.append("You are not planning or running a business.")
    if business_activity != "Yes":
        reasons.append("An eligible income-generating business activity is not confirmed.")
    if business_documents != "Yes":
        reasons.append("Required business documents are not confirmed.")

    if not reasons:
        eligible.append(("Pradhan Mantri MUDRA Yojana",
                         "Business loan options may be available through eligible lenders."))
    elif "Not sure" in [business_activity, business_documents]:
        verification.append(("Pradhan Mantri MUDRA Yojana", reasons))
    else:
        not_eligible.append(("Pradhan Mantri MUDRA Yojana", reasons))

    # -------------------------------------------------
    # 9. PRIME MINISTER'S EMPLOYMENT GENERATION PROGRAMME
    # -------------------------------------------------

    reasons = []

    if age < 18:
        reasons.append("You must be at least 18 years old.")
    if business_status != "Planning a new business":
        reasons.append("This screening is for applicants planning a new business.")
    if business_activity != "Yes":
        reasons.append("An eligible business activity is not confirmed.")
    if business_documents != "Yes":
        reasons.append("Required business documents are not confirmed.")

    if not reasons:
        eligible.append(("Prime Minister's Employment Generation Programme (PMEGP)",
                         "Potential support for eligible new micro-enterprises."))
    elif "Not sure" in [business_activity, business_documents]:
        verification.append(("PMEGP", reasons))
    else:
        not_eligible.append(("PMEGP", reasons))

    # -------------------------------------------------
    # 10. STAND-UP INDIA
    # -------------------------------------------------

    reasons = []

    if age < 18:
        reasons.append("You must be at least 18 years old.")
    if gender != "Female" and category not in ["SC", "ST"]:
        reasons.append("The scheme targets women or SC/ST entrepreneurs.")
    if business_status != "Planning a new business":
        reasons.append("You must be planning a new business.")
    if greenfield != "Yes":
        reasons.append("The venture must meet the greenfield requirement.")
    if business_documents != "Yes":
        reasons.append("Required business documents are not confirmed.")

    if not reasons:
        eligible.append(("Stand-Up India",
                         "Potential loan support for eligible women or SC/ST entrepreneurs."))
    elif "Not sure" in [greenfield, business_documents]:
        verification.append(("Stand-Up India", reasons))
    else:
        not_eligible.append(("Stand-Up India", reasons))

    # -------------------------------------------------
    # 11. STARTUP INDIA SEED FUND SCHEME
    # -------------------------------------------------

    reasons = []

    if business_status != "Running a startup":
        reasons.append("You must have a startup.")
    if dpiit != "Yes":
        reasons.append("DPIIT recognition is not confirmed.")
    if startup_age > 2:
        reasons.append("Startup age exceeds the simplified two-year screening limit.")
    if technology_based != "Yes":
        reasons.append("A technology-based or innovative business is not confirmed.")
    if previous_support > 1000000:
        reasons.append("Previous government support exceeds ₹10 lakh.")
    if indian_promoter != "Yes":
        reasons.append("At least 51% Indian promoter ownership is not confirmed.")

    if not reasons:
        eligible.append(("Startup India Seed Fund Scheme",
                         "Potential support for eligible startups; scheme conditions must be checked."))
    elif "Not sure" in [dpiit, technology_based, indian_promoter]:
        verification.append(("Startup India Seed Fund Scheme", reasons))
    else:
        not_eligible.append(("Startup India Seed Fund Scheme", reasons))

    # -------------------------------------------------
    # 12. CREDIT GUARANTEE SCHEME FOR STARTUPS
    # -------------------------------------------------

    reasons = []

    if business_status != "Running a startup":
        reasons.append("You must have a startup.")
    if dpiit != "Yes":
        reasons.append("DPIIT recognition is not confirmed.")
    if loan_default != "No":
        reasons.append("A loan default must be ruled out.")
    if npa != "No":
        reasons.append("NPA status must be ruled out.")

    if not reasons:
        eligible.append(("Credit Guarantee Scheme for Startups",
                         "Eligible startups may seek credit through participating lenders."))
    elif "Not sure" in [dpiit, loan_default, npa]:
        verification.append(("Credit Guarantee Scheme for Startups", reasons))
    else:
        not_eligible.append(("Credit Guarantee Scheme for Startups", reasons))

    # -------------------------------------------------
    # 13. AYUSHMAN BHARAT PM-JAY
    # -------------------------------------------------

    reasons = []

    if pmjay_beneficiary != "Yes":
        reasons.append("Eligible beneficiary household status is not confirmed.")
    if pmjay_documents != "Yes":
        reasons.append("Documents for beneficiary verification are not confirmed.")

    if not reasons:
        eligible.append(("Ayushman Bharat PM-JAY",
                         "Health coverage may be available if your beneficiary status is verified."))
    elif "Not sure" in [pmjay_beneficiary, pmjay_documents]:
        verification.append(("Ayushman Bharat PM-JAY", reasons))
    else:
        not_eligible.append(("Ayushman Bharat PM-JAY", reasons))

    # -------------------------------------------------
    # 14. AYUSHMAN BHARAT FOR SENIOR CITIZENS
    # -------------------------------------------------

    reasons = []

    if age < 70:
        reasons.append("You must be aged 70 or above.")

    if not reasons:
        eligible.append(("Ayushman Bharat for Senior Citizens",
                         "Potential health coverage for eligible people aged 70 and above."))
    else:
        not_eligible.append(("Ayushman Bharat for Senior Citizens", reasons))

    # -------------------------------------------------
    # 15. CENTRAL GOVERNMENT HEALTH SCHEME
    # -------------------------------------------------

    reasons = []

    if central_employee != "Yes":
        reasons.append("Central Government employee or pensioner status is not confirmed.")
    if cg_health_need != "Yes":
        reasons.append("CGHS coverage requirement is not confirmed.")

    if not reasons:
        eligible.append(("Central Government Health Scheme (CGHS)",
                         "Healthcare services may be available to eligible beneficiaries."))
    elif "Not sure" in [central_employee, cg_health_need]:
        verification.append(("Central Government Health Scheme (CGHS)", reasons))
    else:
        not_eligible.append(("Central Government Health Scheme (CGHS)", reasons))

    # -------------------------------------------------
    # 16. NATIONAL PROGRAMME FOR HEALTH CARE OF THE ELDERLY
    # -------------------------------------------------

    reasons = []

    if age < 60:
        reasons.append("This programme focuses on people aged 60 and above.")
    if senior_healthcare != "Yes":
        reasons.append("The stated elderly healthcare need is not confirmed.")

    if not reasons:
        eligible.append(("National Programme for Health Care of the Elderly",
                         "Elderly healthcare services may be available through participating facilities."))
    elif senior_healthcare == "Not sure":
        verification.append(("National Programme for Health Care of the Elderly", reasons))
    else:
        not_eligible.append(("National Programme for Health Care of the Elderly", reasons))

    # -------------------------------------------------
    # 17. PM-DAKSH
    # -------------------------------------------------

    reasons = []

    if age < 18 or age > 45:
        reasons.append("The simplified age range is 18–45 years.")
    if category not in ["SC", "ST", "OBC", "EWS"]:
        reasons.append("The selected category is outside this prototype's screening categories.")
    if category in ["OBC", "EWS"] and income > 300000:
        reasons.append("For this screening, OBC/EWS family income must not exceed ₹3 lakh.")
    if aadhaar != "Yes":
        reasons.append("Aadhaar is not confirmed.")
    if linked_bank != "Yes":
        reasons.append("An Aadhaar-linked bank account is not confirmed.")
    if skill_india != "Yes":
        reasons.append("Skill India Digital Hub registration is not confirmed.")

    if not reasons:
        eligible.append(("PM-DAKSH",
                         "Potential skill-development and training support for eligible applicants."))
    elif "Not sure" in [aadhaar, linked_bank, skill_india]:
        verification.append(("PM-DAKSH", reasons))
    else:
        not_eligible.append(("PM-DAKSH", reasons))

    # -------------------------------------------------
    # 18. NATIONAL APPRENTICESHIP PROMOTION SCHEME
    # -------------------------------------------------

    reasons = []

    if age < 14:
        reasons.append("You must be at least 14 years old; some trades have higher age requirements.")
    if apprentice != "Yes":
        reasons.append("Apprenticeship participation is not confirmed.")
    if apprenticeship_contract != "Yes":
        reasons.append("An apprenticeship contract is not confirmed.")

    if not reasons:
        eligible.append(("National Apprenticeship Promotion Scheme",
                         "Apprenticeship training support may be available if all conditions are met."))
    elif "Not sure" in [apprentice, apprenticeship_contract]:
        verification.append(("National Apprenticeship Promotion Scheme", reasons))
    else:
        not_eligible.append(("National Apprenticeship Promotion Scheme", reasons))

    # -------------------------------------------------
    # 19. PM VISHWAKARMA
    # -------------------------------------------------

    reasons = []

    if age < 18:
        reasons.append("You must be at least 18 years old.")
    if artisan != "Yes":
        reasons.append("A covered traditional trade is not confirmed.")
    if self_employed != "Yes":
        reasons.append("Self-employment in the traditional trade is not confirmed.")
    if family_trade_condition != "Yes":
        reasons.append("Family and trade conditions are not confirmed.")

    if not reasons:
        eligible.append(("PM Vishwakarma",
                         "Potential training, toolkit and other support for eligible traditional artisans."))
    elif "Not sure" in [artisan, self_employed, family_trade_condition]:
        verification.append(("PM Vishwakarma", reasons))
    else:
        not_eligible.append(("PM Vishwakarma", reasons))

    # =================================================
    # DISPLAY RESULTS
    # =================================================

    st.divider()
    st.header("Your Results")

    st.subheader("Eligible Based on Your Answers")

    if eligible:
        for name, description in eligible:
            st.write("**" + name + "**")
            st.write(description)
    else:
        st.write("No schemes met all the screening conditions based on your answers.")

    st.subheader("Conditions Not Met")

    if not_eligible:
        for name, reasons in not_eligible:
            st.write("**" + name + "**")
            for reason in reasons:
                st.write("- " + reason)
    else:
        st.write("No schemes were placed in this category.")

    st.subheader("Needs Verification")

    if verification:
        for name, reasons in verification:
            st.write("**" + name + "**")
            for reason in reasons:
                st.write("- " + reason)
            st.write("Please confirm the requirements using official scheme guidelines.")
    else:
        st.write("No schemes were placed in this category.")

    st.info(
        "This is a college-project screening tool, not an official eligibility decision. "
        "Some scheme rules are simplified for demonstration. Always confirm current "
        "criteria, income limits, documents and application rules with the official scheme."
    )
