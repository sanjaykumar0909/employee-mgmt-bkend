import random
from datetime import datetime, timedelta

def generate_dates(start_year=1960, end_year=2004):
    # Define the start and end dates
    start_date = datetime(start_year, 1, 1)
    end_date = datetime(end_year, 12, 31)

    # Calculate the total number of days between start and end dates
    total_days = (end_date - start_date).days

    # Generate a random number of days to add to the start date
    random_days = random.randint(0, total_days)

    # Add the random number of days to the start date
    random_date = start_date + timedelta(days=random_days)

    return random_date.strftime("%Y-%m-%d")

