from src.data.schema import create_tables

#Testing if the database has been created
if __name__ == "__main__":
    create_tables()
    print("Database + tables created successfully ✅")
