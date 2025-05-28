import streamlit as st

def calculate_bmi(weight, height_cm):
    height_m = height_cm / 100  # Convert cm to meters
    bmi = weight / (height_m ** 2)
    return round(bmi, 2)

def get_bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def main():
    st.title("BMI Calculator")
    st.write("Calculate your Body Mass Index (BMI) and understand your health category.")

    unit = st.radio("Select Height Unit:", ["Centimeters (cm)", "Feet & Inches"])

    weight = st.number_input("Enter your weight (kg):", min_value=1.0, step=0.1)

    if unit == "Centimeters (cm)":
        height_cm = st.number_input("Enter your height (cm):", min_value=50.0, step=0.1)
    else:
        feet = st.number_input("Feet:", min_value=0, step=1)
        inches = st.number_input("Inches:", min_value=0, step=1)
        height_cm = (feet * 30.48) + (inches * 2.54)

    if st.button("Calculate BMI"):
        if weight and height_cm:
            bmi = calculate_bmi(weight, height_cm)
            category = get_bmi_category(bmi)
            st.success(f"Your BMI is **{bmi}**")
            st.info(f"Category: **{category}**")
        else:
            st.warning("Please enter valid weight and height.")

if __name__ == "__main__":
    main()
