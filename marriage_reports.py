"""
Description:
 Generates a CSV reports containing all married couples in
 the Social Network database.

Usage:
 python marriage_report.py
"""
import os
import sqlite3
import pandas as pd
from datetime import datetime

# Determine the path of the database
db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'social_network.db')

def main():
    # Query DB for list of married couples
    married_couples = get_married_couples()

    # Save all married couples to CSV file
    today = datetime.now().strftime('%Y-%m-%d')
    csv_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), f'married_couples_{today}.csv')
    save_married_couples_csv(married_couples, csv_path)

def get_married_couples():
    """Queries the Social Network database for all married couples.

    Returns:
        list: (name1, name2, start_date) of married couples 
    """
    con = sqlite3.connect(db_path)
    cur = con.cursor()

    query = """
    SELECT p1.person_name, p2.person_name, r.start_date 
    FROM relationships AS r 
    INNER JOIN persons p1 ON p1.person_id = r.person1_id 
    INNER JOIN persons p2 ON p2.person_id = r.person2_id 
    WHERE r.relationship_type='spouse'
    """
    cur.execute(query)
    couples = cur.fetchall()
    return couples

def save_married_couples_csv(married_couples, csv_path):
    """Saves list of married couples to a CSV file, including both people's 
    names and their wedding anniversary date  

    Args:
        married_couples (list): (name1, name2, start_date) of married couples
        csv_path (str): Path of CSV file
    """
    df = pd.DataFrame(married_couples, columns=['Person1', 'Person2', 'Anniversary Date'])
    df.to_csv(csv_path, index=False)

if __name__ == '__main__':
   main()