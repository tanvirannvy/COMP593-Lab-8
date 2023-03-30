"""
Description:
 Creates the relationships table in the Social Network database
 and populates it with 100 fake relationships.

Usage:
 python create_relationships.py
"""
import os
import sqlite3
import random
from datetime import datetime
from datetime import timedelta

# Store the path of the database
db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'social_network.db')

def main():
    create_relationships_table()
    populate_relationships_table()

def create_relationships_table():
    """Creates the relationships table in the DB"""
    # Connect to the database
    con = sqlite3.connect(db_path)
    cur = con.cursor()

    # Create table
    query = """
    CREATE TABLE IF NOT EXISTS relationships (
    	person1_id INTEGER,
    	relationship_type TEXT,
	    person2_id INTEGER,
	    start_date TEXT,
    	FOREIGN KEY (person1_id) REFERENCES persons(person_id),
    	FOREIGN KEY (person2_id) REFERENCES persons(person_id)
    )
    """
    cur.execute(query)
    con.commit()

def populate_relationships_table():
    """Adds 100 random relationships to the DB"""
    con = sqlite3.connect(db_path)
    cur = con.cursor()

    # Inserting 100 fake entries
    num_entries = 100
    relationship_types = ['spouse', 'parent', 'friend', 'colleague']
    for _ in range(num_entries):
        # Generate random relationship info
        person1_id = random.randint(1, 1000)
        person2_id = random.randint(1, 1000)
        relationship_type = random.choice(relationship_types)
        # Generate random start_date from one year ago
        start_date = (datetime.now() - timedelta(days=365))
        start_date = start_date.strftime('%Y-%m-%d')
        
        # Construct query for inserting data
        query = """
            INSERT INTO relationships 
            (person1_id, relationship_type, person2_id, start_date)
            VALUES (?, ?, ?, ?)
        """
        cur.execute(query, (person1_id, relationship_type, person2_id, start_date))
        con.commit()


if __name__ == '__main__':
   main()
