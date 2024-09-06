import streamlit as st
import speedtest

# Set the page configuration
st.set_page_config(
    page_title="Speedify",
    page_icon="icon.png",
    menu_items={
        "About": "Speedify offers a quick and accurate way to measure your internet speed. Test your download, upload, and ping speeds with ease!"
    }
)

# Title of the app
st.write("<h2 style='color:#6CB3FF;'>Test Your Internet Speed Instantly</h2>", unsafe_allow_html=True)

# Button to test speed
btn = st.button("Test Speed")

if btn:
    try:
        # Create a Speedtest object and run the test
        st.write("Running speed test. Please wait...")
        speed_test = speedtest.Speedtest()
        speed_test.get_best_server()
        download_speed = speed_test.download() / 1_000_000  # Convert to Mbps
        upload_speed = speed_test.upload() / 1_000_000  # Convert to Mbps
        ping = speed_test.results.ping

        # Display the results
        st.write(f"**Download Speed:** {download_speed:.2f} Mbps")
        st.write(f"**Upload Speed:** {upload_speed:.2f} Mbps")
        st.write(f"**Ping:** {ping:.2f} ms")
    except Exception as e:
        st.error(f"An error occurred: {e}")
