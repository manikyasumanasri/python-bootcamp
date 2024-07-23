mr_x_height = 150  # Example height for Mr. X in cm
mr_x_weight = 70   # Example weight for Mr. X in kg

mr_y_height = 130  # Example height for Mr. Y in cm
mr_y_weight = 3    # Example weight for Mr. Y in kg (number of medals factor)

mr_z_games = 14        # Total games Mr. Z participated in
mr_z_success_rate = 65  # Success rate of Mr. Z

# Calculate Mr. Z's number of medals
mr_z_medals = round(mr_z_games * (mr_z_success_rate / 100))

# Check Mr. X's selection criteria for Badminton
if mr_x_height >= 140:
    if mr_x_weight % 2 == 0:
        mr_x_selected = True
    else:
        mr_x_selected = False
else:
    mr_x_selected = False

# Check Mr. Y's selection criteria for Table Tennis
if 118 <= mr_y_height <= 148:
    if mr_y_weight % mr_z_medals == 0:
        mr_y_selected = True
    else:
        mr_y_selected = False
else:
    mr_y_selected = False

# Check if Mr. X and Mr. Y will travel with Mr. Z
if mr_x_selected and mr_y_selected:
    print("Mr. X and Mr. Y will travel with Mr. Z to the Olympics.")
else:
    print("Mr. X and Mr. Y will not travel with Mr z.olympics)