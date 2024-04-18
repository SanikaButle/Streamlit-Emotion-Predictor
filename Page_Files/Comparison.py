import streamlit as st


def run():
   
    # Title
    st.markdown(
        """
        <div style='border: 4px solid #447ECC; border-radius: 15px; padding: 20px; margin-bottom: 30px; background-color:#1B1F31 ;'>
            <h1 style='text-align: center; color: #E8D9CF;'>Comparative Study</h1>
        </div>
        """,
        unsafe_allow_html=True
    )
    # Define image paths and captions
    graph_info = [
        {"path": "Visualizations/Fig25.png", "caption": "Fig 1.Accuracy of all models", "description": "Description "},
        {"path": "Visualizations/Fig26.png", "caption": "Fig 2.Precision of all models", "description": "Description "},
        {"path": "Visualizations/Fig27.png", "caption": "Fig 3.F1 score of all models", "description": "Description"},
        {"path": "Visualizations/Fig28.png", "caption": "Fig 4.Recall of all models", "description": "Description"}
    ]

    # Display images and descriptions
    for info in graph_info:
        col1, col2 = st.columns([5, 3])  # Divide the layout into 3/4 and 1/4 columns
        with col1:
            st.image(info["path"], caption=info["caption"], width=None, use_column_width="auto")
            st.markdown("<style>img {border-radius: 10px;}</style>", unsafe_allow_html=True)
        with col2:
            st.write(info["description"])

    # Conclusion box
    st.markdown(
        """
        <div style='border: 4px solid #447ECC; border-radius: 15px; padding: 20px; margin-top: 30px; background-color:#1B1F31 ;'>
            <h2 style='text-align: left; color:#E8D9CF ;'>Conclusion</h2>
            <p style='color: #656B79; padding-left: 20px;'>Hence , we conclude that........</p>
        </div>
        """,
        unsafe_allow_html=True
    )