import streamlit as st
import pandas as pd
import plotly 
import plotly.express as px

st.set_page_config(page_title="Football", 
                   layout="wide")

position_select = st.sidebar.selectbox(
    "Select the Player Position:",
    options= ["QB","RB","WR","TE"]
)

df = pd.read_csv('/Users/michaelwalter/Documents/CodeProjects/Fantasy Football/NFL-Data/NFL-data-Players/2023/'+position_select+'_season.csv')


#st.sidebar.header("Please Filter Here:")
PlayerName = st.sidebar.multiselect(
    "Select the Player Name:",
    options=df["PlayerName"].unique(),
)

stat_selections = st.sidebar.multiselect(
    "Select the Statistics to view:",
    options=df.columns,
    default=df.columns[0],
)

df_selection = df.query(
    "PlayerName == @PlayerName"
)

#
# movie_select_pie_format = pd.melt(movie_select_pie_format, id_vars=["presenter", "movie_name", "average_vote", "genre_name"], value_vars=["amount_wertvoll_1","amount_gut_2" ,"amount_okay_3", "amount_schlecht_4", "amount_grottig_5"], var_name="vote" ,value_name="value")
print(PlayerName)
print(stat_selections)
st.dataframe(df_selection.loc[:, stat_selections])




# fig = px.pie(df_selection, values='RushingYDS', names='PlayerName', title='Scoring Breakdown')
# st.plotly_chart(fig, theme=None)

# passing_yds = int(df_selection["PassingYDS"])
# passing_td = int(df_selection["PassingTD"])
# rushing_td= ":star:" * int(df_selection["RushingTD"])
# total_points = int(df_selection["TotalPoints"])

# left_column, middle_column, right_column = st.columns(3)
# with left_column:
#     st.subheader("Total Points:")
#     st.subheader(f"{total_points:,}")
# with middle_column:
#     st.subheader("Passing Yards:")
#     st.subheader(f"{passing_yds}")
# with right_column:
#     st.subheader("Passing Touchdowns:")
#     st.subheader(f"{passing_td}")

# st.markdown("""---""")
