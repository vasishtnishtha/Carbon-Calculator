import streamlit as st

EMISSION_FACTORS = {
    'India': {
        "Transportation": 0.14,  # kg CO2/km
        "Electricity": 0.82,  # kg CO2/kwh
        "Diet": 1.25,  # kg CO2/meals
        "Waste": 0.12,  # kg CO2/kg
    },
    'Canada': {
        "Transportation": 0.14,  # kg CO2/km
        "Electricity": 0.82,  # kg CO2/kwh
        "Diet": 1.25,  # kg CO2/meals
        "Waste": 0.12,  # kg CO2/kg
    }
}

st.set_page_config(
    layout="wide",
    page_title="Carbon Calculator",
    page_icon="images/icons8-world-32.png"
)

st.title('Carbon Calculator')
# user inputs

st.subheader("🌍 Your Country")
country = st.selectbox("Select your country", ['India', 'Canada'])

col1, col2 = st.columns(2)
with col1:
    st.subheader("🚗 Daily Commpute Distance (in km)")
    distance = st.slider("Distance", 0.0, 100.0, key="distance_input")

    st.subheader("💡 Monthly Electricity Consumption (in kwh)")
    electricity = st.slider("Electricity", 0.0, 1000.0, key="electricity_input")

with col2:
    st.subheader("🗑️ Waste Generated per Week (in kg)")
    waste = st.slider("Waste", 0.0, 100.0, key="waste_input")

    st.subheader("🍔 No. of Meals per Day")
    meals = st.number_input("Meals", 0, key="meals_input")

if distance > 0:
    distance = distance * 365

if electricity > 0:
    electricity = electricity * 12

if meals > 0:
    meals = meals * 365

if waste > 0:
    waste = waste * 52

# cal carbon emission
transportation_emissions = EMISSION_FACTORS[country]['Transportation'] * distance
electricity_emissions = EMISSION_FACTORS[country]['Electricity'] * electricity
meals_emissions = EMISSION_FACTORS[country]['Diet'] * meals
waste_emissions = EMISSION_FACTORS[country]['Waste'] * waste

transportation_emissions = round(transportation_emissions / 1000, 2)
electricity_emissions = round(electricity_emissions / 1000, 2)
meals_emissions = round(meals_emissions / 1000, 2)
waste_emissions = round(waste_emissions / 1000, 2)

# convert emission to tons
total_emissions = round(transportation_emissions + electricity_emissions
                        + meals_emissions + waste_emissions, 2)

if st.button("Calculate CO2 Emission"):
    st.header("Results")

col3, col4 = st.columns(2)

with col3:
    st.subheader("Carbon Emissions By Categories")
    st.info(f"🚗 Transportation: {transportation_emissions} tonnes CO2 per year")
    st.info(f"💡 Electricity: {electricity_emissions} tonnes CO2 per year")
    st.info(f"🍔 Meals: {meals_emissions} tonnes CO2 per year")
    st.info(f"🗑️ Waste: {waste_emissions} tonnes CO2 per year")

with col4:
    st.subheader("Total Carbon Footprints")
    st.info(f"🌍 Your Total Carbon Footprints: {total_emissions} tonnes CO2 per year")
    st.warning(
        "In 2021, CO2 emissions per capita for India was 1.9 tons of CO2 per capita. Between 1972 and 2021, CO2 emissions per capita of India grew substantially from 0.39 to 1.9 tons of CO2 per capita rising at an increasing annual rate that reached a maximum of 9.41% in 2021.")
