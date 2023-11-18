import streamlit as st

def main():
    st.set_page_config(page_title="Big Mart Sales Prediction", page_icon=":bar_chart:")

    st.markdown(
        """
        <style>
            body {
                background: linear-gradient(to left, #667292 0%, #a2b9bc 100%);
                background-image: url("bigmart.jpg");
            }

            h1 {
                text-align: center;
                color: white;
            }

            .wrapper {
                margin-top: 50px;
                padding: 20px;
                background-color: rgba(255, 255, 255, 0.8);
                border-radius: 10px;
            }

            footer a {
                color: #fff;
            }

            footer a:hover {
                color: #fff;
            }

            .centerdiv {
                height: 15vh;
                display: flex;
                align-items: center;
            }

            .centerdiv a {
                height: 30px;
                width: 30px;
                background-color: #f5f6fa;
                border-radius: 50px;
                text-align: center;
                margin: 5px;
                line-height: 30px;
                position: relative;
                overflow: hidden;
            }

            .centerdiv a i {
                transition: all 0.3s linear;
            }

            .centerdiv a:hover i {
                transform: scale(1.5);
                color: #f5f6fa;
            }

            .centerdiv a:before {
                content: "";
                width: 120%;
                height: 120%;
                position: absolute;
                top: 90%;
                left: -50%;
                background-color: #00a8ff;
                transform: rotate(60deg);
            }

            .centerdiv a:hover:before {
                animation: socialicons 0.8s 1;
                animation-fill-mode: forwards;
            }

            @keyframes socialicons {
                0% {
                    top: 90%;
                    left: -50%;
                }

                50% {
                    top: -60%;
                    left: -10%;
                }

                100% {
                    top: -10%;
                    left: -10%
                }
            }

            .fa-facebook-f {
                color: #e84393;
            }

            .fa-instagram {
                color: #e84393;
            }

            .fa-github {
                color: #e84118;
            }

            .fa-linkedin {
                color: #0097e6;
            }

            .fa-twitter {
                color: #0097e6;
            }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.title("Big Mart Sales Prediction")
    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("<div class='wrapper'>", unsafe_allow_html=True)
    st.markdown("<div class='container my-5'>", unsafe_allow_html=True)
    st.markdown("<div class='row'>", unsafe_allow_html=True)
    st.markdown("<div class='col-md-6 col-sm-6 mx-auto'>", unsafe_allow_html=True)

    with st.form(key="prediction_form"):
        st.markdown("<div class='form-group'>", unsafe_allow_html=True)
        st.text_input("Enter Item Weight", key="item_weight")
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("<div class='form-group'>", unsafe_allow_html=True)
        st.selectbox("Item Fat Content", ["Low Fat", "Regular", "High Fat"], key="item_fat_content")
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("<div class='form-group'>", unsafe_allow_html=True)
        st.text_input("Enter Item Visibility", key="item_visibility")
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("<div class='form-group'>", unsafe_allow_html=True)
        st.selectbox("Item Type", ["Baking Goods", "Breads", "Breakfast", "Canned", "Dairy", "Frozen Foods",
                                   "Fruits and Vegetables", "Hard Drinks", "Health and Hygiene", "Household", "Meat",
                                   "Others", "Seafood", "Snack Foods", "Soft Drinks", "Starchy Foods"], key="item_type")
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("<div class='form-group'>", unsafe_allow_html=True)
        st.text_input("Enter Item MRP", key="item_mrp")
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("<div class='form-group'>", unsafe_allow_html=True)
        st.text_input("Outlet Establishment Year (YYYY)", key="outlet_establishment_year")
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("<div class='form-group'>", unsafe_allow_html=True)
        st.selectbox("Outlet Size", ["High", "Medium", "Small"], key="outlet_size")
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("<div class='form-group'>", unsafe_allow_html=True)
        st.selectbox("Outlet Location Type", ["Tier 1", "Tier 2", "Tier 3"], key="outlet_location_type")
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("<div class='form-group'>", unsafe_allow_html=True)
        st.selectbox("Outlet Type", ["Grocery Store", "Supermarket Type1", "Supermarket Type2", "Supermarket Type3"],
                     key="outlet_type")
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("<div class='form-group'>", unsafe_allow_html=True)
        st.form_submit_button("Submit")
        st.markdown("</div>", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
