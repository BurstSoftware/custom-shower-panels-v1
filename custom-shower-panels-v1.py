import streamlit as st


def init():
    # App title
    st.set_page_config(page_title="Custom Shower Panels", layout="centered")

    # Sidebar for navigation
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Home", "Customize", "Quote Calculator", "Contact Us"])

    # Home page
    if page == "Home":
        st.title("Welcome to Custom Shower Panels")
        st.image("https://source.unsplash.com/600x400/?bathroom,shower", caption="Elegant Shower Panel")
        st.write("We offer premium custom shower panels tailored to your needs. Explore our customization options and get a quote today!")

    # Customize page
    elif page == "Customize":
        st.title("Customize Your Shower Panel")
        material = st.selectbox("Choose Material", ["Glass", "Acrylic", "Stone", "Metal"])
        height = st.slider("Select Panel Height (inches)", min_value=60, max_value=100, value=80)
        width = st.slider("Select Panel Width (inches)", min_value=20, max_value=60, value=36)
        features = st.multiselect("Select Additional Features", ["LED Lighting", "Hydro Jets", "Digital Controls", "Custom Print"])

        st.write("### Customization Summary")
        st.write(f"**Material:** {material}")
        st.write(f"**Dimensions:** {height} x {width} inches")
        st.write(f"**Features:** {', '.join(features) if features else 'None'}")

    # Quote Calculator page
    elif page == "Quote Calculator":
        st.title("Get a Quote")
        base_price = 500
        material_factor = st.selectbox("Material Type", {"Glass": 1.2, "Acrylic": 1.0, "Stone": 1.5, "Metal": 1.3})
        height = st.number_input("Height (inches)", min_value=60, max_value=100, value=80)
        width = st.number_input("Width (inches)", min_value=20, max_value=60, value=36)
        features_count = st.number_input("Number of Features", min_value=0, max_value=10, value=2)

        if st.button("Calculate Quote"):
            area = height * width
            feature_cost = features_count * 50
            total_cost = base_price * material_factor + (area * 0.5) + feature_cost
            st.success(f"Estimated Cost: ${total_cost:.2f}")

    # Contact Us page
    elif page == "Contact Us":
        st.title("Get in Touch")
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        message = st.text_area("Your Message")
        if st.button("Submit"):
            if name and email and message:
                st.success("Thank you for your message! We'll get back to you soon.")
            else:
                st.error("Please fill out all fields before submitting.")

    st.sidebar.info("Use the navigation menu to explore the app.")

    st.sidebar.markdown("---")
    st.sidebar.text("Custom Shower Panels App v1.0")


if __name__ == "__main__":
    init()")
    }
  ]
}
