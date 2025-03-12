import time
import webbrowser

# Open the URL in the default browser
url = "https://singingfiles.com/show.php?l=0&u=2346217&id=68712"
webbrowser.open(url)

# Wait for the page to load
time.sleep(5)  # Adjust this if the page needs more time to load

# Delay for 0.5 seconds before starting the clicks
time.sleep(0.5)

# Simulate 500 mouse clicks
for _ in range(500):
    time.sleep(0.1)  # Adding a small delay between clicks to avoid overloading

print("500 clicks simulated.")
