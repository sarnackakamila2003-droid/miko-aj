import matplotlib.pyplot as plt
import matplotlib.patches as patches
import streamlit as st

def draw_santa(suit_color, beard_width):
    """
    Draws a simple Santa Claus figure with interactive parameters 
    using Matplotlib patches and returns the figure.
    """
    fig, ax = plt.subplots(figsize=(8, 10))
    ax.set_aspect('equal')
    ax.set_xlim(-5, 5)
    ax.set_ylim(-5, 5)

    # Body (uses the interactive suit_color)
    body = patches.Ellipse((0, -2), 3, 4, color=suit_color)
    ax.add_patch(body)

    # Head (skin color)
    head = patches.Circle((0, 1), 0.8, color='#FFDBAC') # Skin tone
    ax.add_patch(head)

    # Hat (uses the interactive suit_color for the main parts)
    hat_base = patches.Rectangle((-0.8, 1.5), 1.6, 0.5, color=suit_color, zorder=2)
    ax.add_patch(hat_base)
    hat_top = patches.Polygon([(0.8, 2), (0.2, 3.5), (-0.8, 2)], color=suit_color, zorder=2)
    ax.add_patch(hat_top)
    hat_trim = patches.Ellipse((0, 1.5), 2.2, 0.4, color='white', zorder=3) # White trim
    ax.add_patch(hat_trim)
    hat_pompom = patches.Circle((0.2, 3.5), 0.3, color='white', zorder=4) # Pompom
    ax.add_patch(hat_pompom)

    # Beard (uses the interactive beard_width)
    beard = patches.Ellipse((0, 0), beard_width, 2, angle=0, color='white', zorder=1)
    ax.add_patch(beard)

    # Face details
    # Eyes
    ax.add_patch(patches.Circle((-0.3, 1.2), 0.1, color='black', zorder=5))
    ax.add_patch(patches.Circle((0.3, 1.2), 0.1, color='black', zorder=5))
    # Nose
    ax.add_patch(patches.Circle((0, 0.8), 0.15, color='brown', zorder=5))

    # Arms (uses the interactive suit_color)
    left_arm = patches.Rectangle((-1.7, -1.5), 1.5, 0.7, angle=-20, color=suit_color, zorder=2)
    ax.add_patch(left_arm)
    right_arm = patches.Rectangle((0.2, -1.5), 1.5, 0.7, angle=20, color=suit_color, zorder=2)
    ax.add_patch(right_arm)

    # Hands (skin color)
    left_hand = patches.Circle((-2.5, -2.0), 0.3, color='#FFDBAC', zorder=2)
    ax.add_patch(left_hand)
    right_hand = patches.Circle((2.5, -2.0), 0.3, color='#FFDBAC', zorder=2)
    ax.add_patch(right_hand)

    # Legs (uses the interactive suit_color)
    left_leg = patches.Rectangle((-0.8, -4), 0.6, 1.5, color=suit_color, zorder=0)
    ax.add_patch(left_leg)
    right_leg = patches.Rectangle((0.2, -4), 0.6, 1.5, color=suit_color, zorder=0)
    ax.add_patch(right_leg)

    # Boots (black)
    left_boot = patches.Rectangle((-1, -4.5), 0.9, 0.5, color='black', zorder=0)
    ax.add_patch(left_boot)
    right_boot = patches.Rectangle((0.1, -4.5), 0.9, 0.5, color='black', zorder=0)
    ax.add_patch(right_boot)

    ax.set_title('Santa Claus')
    ax.axis('off') # Hide axes
    
    # Return the figure object
    return fig

# --- Streamlit Application Logic (Interactive) ---
st.title("🎨 Interactive Matplotlib Santa Claus")
st.sidebar.header("Santa Customizer")

# 1. Create interactive widgets in the sidebar
suit_color_choice = st.sidebar.color_picker(
    'Choose Suit Color', 
    '#FF0000' # Default to Red
)

beard_width_choice = st.sidebar.slider(
    'Adjust Beard Width', 
    min_value=1.5, 
    max_value=4.0, 
    value=2.5, # Default value
    step=0.1
)

# 2. Call the function with the chosen interactive parameters
santa_fig = draw_santa(suit_color_choice, beard_width_choice)

# 3. Use st.pyplot() to display the figure
st.pyplot(santa_fig)
