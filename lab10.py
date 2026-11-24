import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Lab 10 | Data Story", layout="wide")

# ---------------------------------------------------------------
# DATA (fictional practice values)
# Assignment step 2: I changed ONE rating -> "Chart selection"
# went from 3.2 to 2.1, so it is now the lowest average.
# The highlight, title and takeaway below update automatically,
# so they always stay consistent with the data.
# ---------------------------------------------------------------
skills = ["Data storytelling", "Python", "Chart selection",
          "Color and labels", "Data cleaning"]
ratings = [2.4, 3.0, 2.1, 3.7, 4.1]
df = pd.DataFrame({"Skill": skills, "Average rating": ratings})

# Position cue: sort so the weakest skill sits at the top
df = df.sort_values("Average rating").reset_index(drop=True)
lowest_skill = df.loc[0, "Skill"]
lowest_value = df.loc[0, "Average rating"]

# ---------------------------------------------------------------
# AUDIENCE FRAMING (assignment step 1)
# Original audience : students planning a workshop
# New audience      : the workshop INSTRUCTOR, who must decide
#                     which topic to teach first.
# ---------------------------------------------------------------
st.title(f"Start the Workshop with {lowest_skill}")
st.write(
    "**For the workshop instructor:** students rated their own data "
    "visualization skills. Use this to decide which topic gets the most teaching time."
)
st.write(
    f"**Takeaway:** {lowest_skill.lower()} has the lowest average "
    f"self-rating ({lowest_value:.1f} out of 5), so teach it first."
)

fig, ax = plt.subplots(figsize=(8, 4.5))

# One pre-attentive feature: contrasting colour on the lowest bar only
bar_colors = ["#E07A3F"] + ["#4C78A8"] * (len(df) - 1)
bars = ax.barh(df["Skill"], df["Average rating"], color=bar_colors)

ax.set_xlim(0, 5.6)            # a little room for the annotation text
ax.set_xticks(range(0, 6))     # zero baseline kept for honest bar lengths
ax.set_xlabel("Average self-rating of all students "
              "(1 = beginner, 5 = confident)")
ax.set_title(f"{lowest_skill} received the lowest average rating",
             loc="left", fontweight="bold")
ax.invert_yaxis()

# REMOVED detail: vertical grid lines. Every bar already has a value
# label, so the grid only added visual noise.
ax.spines["top"].set_visible(False)
ax.spines["right"].set_visible(False)

# Value labels
for bar, value in zip(bars, df["Average rating"]):
    ax.text(value + 0.05, bar.get_y() + bar.get_height() / 2,
            f"{value:.1f}", va="center")

# Text annotation (assignment step 2): explains WHY the orange bar matters
ax.annotate(
    "Lowest average:\nmost support needed",
    xy=(lowest_value + 0.35, 0),
    xytext=(3.4, 0.9),
    fontsize=10, color="#B4541A", fontweight="bold",
    arrowprops=dict(arrowstyle="->", color="#B4541A"),
)

fig.tight_layout()
st.pyplot(fig, clear_figure=True)

# Change made after classmate feedback: added the reading-direction hint
# ("longer bar = more confident") because the reader was unsure whether
# a long bar was good or bad.
st.caption(
    "Longer bar = higher self-confidence. "
    "Each bar is a group average, not one student's score. "
    "Fictional practice values, 1-5 scale."
)
