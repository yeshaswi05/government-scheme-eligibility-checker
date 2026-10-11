
import streamlit as st

st.set_page_config(
    page_title="Government Scheme Eligibility Checker",
    layout="centered"
)

st.title(" Government Scheme Eligibility Checker")
st.write("Enter your details and select the schemes you want to check.")

YES_NO = ["Choose an answer", "Yes", "No", "Not sure"]

# 1. PERSONAL INFORMATION

st.header("1. Personal Information")

age = st.number_input("Age", min_value=0, max_value=100, value=18, step=1)
annual_income = st.number_input("Annual family income (₹)", min_value=0, value=200000, step=10000)

gender = st.selectbox("Gender", ["Choose an answer", "Female", "Male", "Other"])
category = st.selectbox(
    "Category",
    ["Choose an answer", "General", "OBC", "SC", "ST", "EWS", "Minority"]
)

# 2. SELECT SCHEME CATEGORIES

st.header("2. Select Scheme Categories")

selected_categories = st.multiselect(
    "Which types of schemes would you like to check?",
    [
        "Education and Scholarships",
        "Business and Startups",
        "Healthcare",
        "Skills and Training",
        "Artisan Support"
    ]
)

# 3. EDUCATION AND SCHOLARSHIPS

if "Education and Scholarships" in selected_categories:
    st.header("3. Education and Scholarships")

    education_status = st.selectbox(
        "What is your current education status?",
        [
            "Choose an answer",
            "Not currently studying",
            "School",
            "College/University",
            "Planning to study abroad"
        ]
    )

    if education_status == "School":
        nmms_selected = st.selectbox(
            "Are you applying for the NMMS scholarship?", YES_NO
        )
        yasasvi_category = st.selectbox(
            "Do you belong to a category covered by PM YASASVI?", YES_NO
        )
        other_scholarship = st.selectbox(
            "Are you receiving another scholarship?", YES_NO
        )

    elif education_status == "College/University":
        aicte_approved = st.selectbox(
            "Is your institution AICTE-approved?", YES_NO
        )
        special_condition = st.selectbox(
            "Do you meet the special condition for the AICTE-Swanath scheme?", YES_NO
        )
        disability = st.selectbox(
            "Do you have a disability of 40% or more?", YES_NO
        )
        sc_student = st.selectbox(
            "Are you applying under the SC Post-Matric Scholarship?", YES_NO
        )
        yasasvi_category = st.selectbox(
            "Do you belong to a category covered by PM YASASVI?", YES_NO
        )
        top_marks = st.selectbox(
            "Were your Class 12 marks in the top 20% of your board?", YES_NO
        )
        other_scholarship = st.selectbox(
            "Are you receiving another scholarship?", YES_NO
        )

    elif education_status == "Planning to study abroad":
        overseas_category = st.selectbox(
            "Do you belong to a category covered by the National Overseas Scholarship?",
            YES_NO
        )
        overseas_marks = st.selectbox(
            "Do you meet the required academic marks?", YES_NO
        )
        foreign_offer = st.selectbox(
            "Do you have an admission offer from a foreign institution?", YES_NO
        )

# 4. BUSINESS AND STARTUPS

if "Business and Startups" in selected_categories:
    st.header("4. Business and Startups")

    business_status = st.selectbox(
        "Which describes your business?",
        [
            "Choose an answer",
            "Start a new business",
            "Already have a business",
            "I have an eligible startup"
        ]
    )

    business_type = st.selectbox(
        "Are you a woman entrepreneur or an SC/ST entrepreneur?", YES_NO
    )
    greenfield = st.selectbox(
        "Will this be your first-time (greenfield) business?", YES_NO
    )
    dpiit = st.selectbox(
        "Is your startup recognised by DPIIT?", YES_NO
    )
    tech_startup = st.selectbox(
        "Is your startup technology-based?", YES_NO
    )
    startup_age = st.number_input(
        "Age of startup in years", min_value=0, max_value=100, value=0, step=1
    )
    previous_support = st.selectbox(
        "Have you received government support for this startup?", YES_NO
    )
    promoter_share = st.selectbox(
        "Do Indian promoters hold at least 51% ownership?", YES_NO
    )
    street_vendor = st.selectbox(
        "Are you a street vendor?", YES_NO
    )
    loan_default = st.selectbox(
        "Have you defaulted on a loan?", YES_NO
    )
    npa = st.selectbox(
        "Is any of your loan account classified as an NPA?", YES_NO
    )

# 5. HEALTHCARE

if "Healthcare" in selected_categories:
    st.header("5. Healthcare")

    pmjay_household = st.selectbox(
        "Is your household covered by PM-JAY eligibility criteria?", YES_NO
    )
    senior_health = st.selectbox(
        "Are you 70 years old or above?", YES_NO
    )
    central_employee = st.selectbox(
        "Are you a central government employee or pensioner?", YES_NO
    )
    cghs_member = st.selectbox(
        "Are you eligible for or enrolled in CGHS?", YES_NO
    )

# 6. SKILLS AND TRAINING

if "Skills and Training" in selected_categories:
    st.header("6. Skills and Training")

    apprenticeship = st.selectbox(
        "Are you interested in an apprenticeship?", YES_NO
    )
    skill_training = st.selectbox(
        "Are you interested in skill development training?", YES_NO
    )
    aadhaar = st.selectbox(
        "Do you have an Aadhaar card?", YES_NO
    )
    bank_linked = st.selectbox(
        "Is your bank account linked to Aadhaar?", YES_NO
    )

# 7. ARTISAN SUPPORT

if "Artisan Support" in selected_categories:
    st.header("7. Artisan Support")

    artisan = st.selectbox(
        "Do you work in a traditional trade or craft?", YES_NO
    )
    trade_included = st.selectbox(
        "Is your trade included in the PM Vishwakarma scheme?", YES_NO
    )
    family_member = st.selectbox(
        "Has a family member already received PM Vishwakarma benefits?", YES_NO
    )
    artisan_aadhaar = st.selectbox(
        "Do you have an Aadhaar card?", YES_NO
    )

# 8. CHECK ELIGIBILITY

if st.button("Check Eligible Schemes", type="primary"):

    eligible = []
    not_met = []

    if not selected_categories:
        st.warning("Please select at least one scheme category.")

    else:

        # EDUCATION SCHEMES

        if "Education and Scholarships" in selected_categories:

            if education_status == "School":

                if (
                    nmms_selected == "Yes"
                    and age <= 18
                    and annual_income <= 350000
                ):
                    eligible.append("National Means-cum-Merit Scholarship (NMMS)")
                else:
                    not_met.append("National Means-cum-Merit Scholarship (NMMS)")

                if (
                    yasasvi_category == "Yes"
                    and annual_income <= 250000
                    and other_scholarship == "No"
                ):
                    eligible.append("PM YASASVI")
                else:
                    not_met.append("PM YASASVI")

            elif education_status == "College/University":

                if (
                    aicte_approved == "Yes"
                    and special_condition == "Yes"
                    and annual_income <= 800000
                    and other_scholarship == "No"
                ):
                    eligible.append("AICTE-Swanath Scholarship")
                else:
                    not_met.append("AICTE-Swanath Scholarship")

                if (
                    disability == "Yes"
                    and annual_income <= 250000
                    and other_scholarship == "No"
                ):
                    eligible.append("Post-Matric Scholarship for Students with Disabilities")
                else:
                    not_met.append("Post-Matric Scholarship for Students with Disabilities")

                if (
                    sc_student == "Yes"
                    and category == "SC"
                    and annual_income <= 250000
                    and other_scholarship == "No"
                ):
                    eligible.append("Post-Matric Scholarship for SC Students")
                else:
                    not_met.append("Post-Matric Scholarship for SC Students")

                if (
                    yasasvi_category == "Yes"
                    and annual_income <= 250000
                    and other_scholarship == "No"
                ):
                    eligible.append("PM YASASVI")
                else:
                    not_met.append("PM YASASVI")

                if (
                    top_marks == "Yes"
                    and annual_income <= 450000
                    and other_scholarship == "No"
                ):
                    eligible.append("Central Sector Scholarship Scheme")
                else:
                    not_met.append("Central Sector Scholarship Scheme")

            elif education_status == "Planning to study abroad":

                if (
                    overseas_category == "Yes"
                    and overseas_marks == "Yes"
                    and foreign_offer == "Yes"
                ):
                    eligible.append("National Overseas Scholarship")
                else:
                    not_met.append("National Overseas Scholarship")

        # BUSINESS SCHEMES

        if "Business and Startups" in selected_categories:

            if (
                business_status in ["Start a new business", "Already have a business"]
                and loan_default == "No"
                and npa == "No"
            ):
                eligible.append("Pradhan Mantri MUDRA Yojana")
            else:
                not_met.append("Pradhan Mantri MUDRA Yojana")

            if (
                age >= 18
                and business_status in ["Start a new business", "Already have a business"]
                and greenfield == "Yes"
                and loan_default == "No"
                and npa == "No"
            ):
                eligible.append("Prime Minister's Employment Generation Programme (PMEGP)")
            else:
                not_met.append("Prime Minister's Employment Generation Programme (PMEGP)")

            if (
                age >= 18
                and business_type == "Yes"
                and greenfield == "Yes"
                and loan_default == "No"
                and npa == "No"
            ):
                eligible.append("Stand-Up India")
            else:
                not_met.append("Stand-Up India")

            if (
                business_status == "I have an eligible startup"
                and dpiit == "Yes"
                and tech_startup == "Yes"
                and startup_age <= 2
                and previous_support == "No"
            ):
                eligible.append("Startup India Seed Fund Scheme")
            else:
                not_met.append("Startup India Seed Fund Scheme")

            if street_vendor == "Yes":
                eligible.append("PM Street Vendor's AtmaNirbhar Nidhi (PM SVANidhi)")
            else:
                not_met.append("PM Street Vendor's AtmaNirbhar Nidhi (PM SVANidhi)")

            if (
                business_status == "I have an eligible startup"
                and dpiit == "Yes"
                and tech_startup == "Yes"
                and promoter_share == "Yes"
                and loan_default == "No"
                and npa == "No"
            ):
                eligible.append("Credit Guarantee Scheme for Startups")
            else:
                not_met.append("Credit Guarantee Scheme for Startups")

        # HEALTHCARE SCHEMES

        if "Healthcare" in selected_categories:

            if pmjay_household == "Yes":
                eligible.append("Ayushman Bharat PM-JAY")
            else:
                not_met.append("Ayushman Bharat PM-JAY")

            if age >= 70 or senior_health == "Yes":
                eligible.append("Ayushman Bharat for Senior Citizens")
            else:
                not_met.append("Ayushman Bharat for Senior Citizens")

            if central_employee == "Yes" and cghs_member == "Yes":
                eligible.append("Central Government Health Scheme (CGHS)")
            else:
                not_met.append("Central Government Health Scheme (CGHS)")

            if age >= 60:
                eligible.append("National Programme for Health Care of the Elderly (NPHCE)")
            else:
                not_met.append("National Programme for Health Care of the Elderly (NPHCE)")

        # SKILL DEVELOPMENT SCHEMES

        if "Skills and Training" in selected_categories:

            if (
                apprenticeship == "Yes"
                and aadhaar == "Yes"
                and bank_linked == "Yes"
            ):
                eligible.append("National Apprenticeship Promotion Scheme (NAPS)")
            else:
                not_met.append("National Apprenticeship Promotion Scheme (NAPS)")

            if (
                skill_training == "Yes"
                and aadhaar == "Yes"
                and age >= 18
                and age <= 45
                and category in ["OBC", "EWS"]
                and annual_income <= 300000
                and bank_linked == "Yes"
            ):
                eligible.append("PM-DAKSH")
            else:
                not_met.append("PM-DAKSH")

        # ARTISAN SCHEME

        if "Artisan Support" in selected_categories:

            if (
                artisan == "Yes"
                and trade_included == "Yes"
                and family_member == "No"
                and artisan_aadhaar == "Yes"
            ):
                eligible.append("PM Vishwakarma")
            else:
                not_met.append("PM Vishwakarma")

        # DISPLAY RESULTS

        st.header("Eligible Schemes")

        if eligible:
            for scheme in eligible:
                st.success(scheme)
        else:
            st.info("No schemes matched the answers entered.")

        st.header("Schemes You May Not Be Eligible For")

        if not_met:
            for scheme in not_met:
                st.write("- " + scheme)
        else:
            st.success("No unmatched schemes in the selected categories.")

        st.caption(
            "This is an academic prototype. Check official scheme guidelines "
            "and application portals before applying."
        )
