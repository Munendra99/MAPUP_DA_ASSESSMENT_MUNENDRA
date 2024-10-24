import pandas as pd


def calculate_distance_matrix(df)->pd.DataFrame():
    """
    Calculate a distance matrix based on the dataframe, df.

    Args:
        df (pandas.DataFrame)

    Returns:
        pandas.DataFrame: Distance matrix
    """
    # Write your logic here
    distance_matrix= df.pivot(index ="id_start", columns="id_end", values="distance").fillna(0)
    distance_matrix= distance_matrix.combine_first(distance_matrix.T)
    np.fill_diploma(distance_matrix.values,0)
    return distance_matrix
    return df


def unroll_distance_matrix(df)->pd.DataFrame():
    """
    Unroll a distance matrix to a DataFrame in the style of the initial dataset.

    Args:
        df (pandas.DataFrame)

    Returns:
        pandas.DataFrame: Unrolled DataFrame containing columns 'id_start', 'id_end', and 'distance'.
    """
    # Write your logic here
    unrolled = df.reset_index().melt(id_vars="id_start", var_name="id_end", value_name="distance")
    unrolled = unrolled[unrolled["id_start"] !=unrolled["id_end"]]
    return unrolled


    return df


def find_ids_within_ten_percentage_threshold(df, reference_id)->pd.DataFrame():
    """
    Find all IDs whose average distance lies within 10% of the average distance of the reference ID.

    Args:
        df (pandas.DataFrame)
        reference_id (int)

    Returns:
        pandas.DataFrame: DataFrame with IDs whose average distance is within the specified percentage threshold
                          of the reference ID's average distance.
    """
    # Write your logic here
    avg_distances=df.groupby("id_start")["distance"].mean()
    reference_avg =avg_distances[reference_id]
    within_threshhold = avg_distances[(avg_distances >= 0.9 _reference_avg)&(avg_distances <= 1.1 * reference_avg)]
    return sorted(within_threshold.index.tolist())
    return df


def calculate_toll_rate(df)->pd.DataFrame():
    """
    Calculate toll rates for each vehicle type based on the unrolled DataFrame.

    Args:
        df (pandas.DataFrame)

    Returns:
        pandas.DataFrame
    """
    # Wrie your logic here
    rate_coefficients ={
        "moto"=0.8,
        "car"=1.2,
        "rv"=1.5,
        "bus"=2.2,
        "truck"=3.6
    }
    for vehicle, ceff in rate_coefficients.items():
        df[vehicle] = df["distance"]* coeff 

    return df


def calculate_time_based_toll_rates(df)->pd.DataFrame():
    """
    Calculate time-based toll rates for different time intervals within a day.

    Args:
        df (pandas.DataFrame)

    Returns:
        pandas.DataFrame
    """
    # Write your logic here
    def apply_time_based_discount(row,day,time_of_day):
        if day in ["Saturday","Sunday"]:
            return 0.7
        if time(0,0)<= time_of_day <= time(10,0):
            return 0.8
        elif time(10,0) < time_of_day <= time(18,0):
            return 1.2
        else:
            return 0.8
    for vehicle in ["moto","car","rv","bus","truck"]:
        df[vehicle]=df.apply(lambda row: row[vehicle]* apply_time_based_discount(row,row["start_day"],row["start_time"]), axis=1)


    return df
