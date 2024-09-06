import streamlit as st
import subprocess

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
        # Run the speed test and capture the output
        result = subprocess.run(["speedtest-cli", "--share"], capture_output=True, text=True)
        output = result.stdout
        error = result.stderr

        # Debugging: Print stdout and stderr
        st.write("Debug - Command Output:", output)
        st.write("Debug - Command Error:", error)

        # Check if "results:" is in the output to prevent IndexError
        if "results:" in output:
            link = output.split("results:")[1].strip()
            st.image(link)
        else:
            st.error("Could not retrieve speed test results. Please try again.")

    except FileNotFoundError:
        st.error("Speedtest CLI tool is not installed. Please install it using `pip install speedtest-cli`.")
    except Exception as e:
        st.error(f"An error occurred: {e}")
