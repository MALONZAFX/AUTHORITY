import psycopg2
from psycopg2 import sql

# Replace with your actual database URL
DATABASE_URL = "postgresql://postgres:UqUaguBlEWaQahOaEzJnkoSJwdqQhmSs@autorack.proxy.rlwy.net:58829/railway"

# Connect to PostgreSQL
conn = psycopg2.connect(DATABASE_URL)
cur = conn.cursor()

# SQL Insert Query
insert_query = """
INSERT INTO auth_user (password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
"""

# User records to be inserted
users = [
    ("pbkdf2_sha256$600000$5iIwJ85RLcqHEjOPyiNamB$ahmPxdREnJdlSzw7vjYYh0TonQlSS0QmB+hBQvzt02U=", "2024-06-25T13:11:03.112Z", True, "willy", "", "", "", True, True, "2024-06-24T00:37:11.102Z"),
    ("pbkdf2_sha256$600000$qYqm1JYLkj2UWCfhXdkcYP$zxkN+SD/BGqVB+C1kwu5OL2l0Z4dBczcTXRHGxU8K6I=", "2024-08-21T10:47:46.418Z", True, "mesh", "", "", "", True, True, "2024-08-21T10:25:21.922Z"),
    ("pbkdf2_sha256$600000$V1fSebAsU2zLvYJXIx171B$UVR1LsBHwCnMIQE7MQI0/fgfS8srgkUpM8m2A8sIftQ=", "2024-08-21T11:53:05.466Z", True, "Wawuda", "Trizer", "Mwanyika", "vwawuda@privatisation.go.ke", True, True, "2024-08-21T11:48:31.000Z"),
    ("pbkdf2_sha256$600000$izdmqf66HdcwAvcSaKJIrh$uSPE2WUQhwuaUCyCaK02ctFgjW2cNtW++QkMNs2bui4=", "2024-08-21T11:53:19.000Z", False, "vcheruiyot", "Victor", "Cheruiyot", "vcheruiyot@privatisation.go.ke", True, True, "2024-08-21T11:51:38.000Z"),
    ("pbkdf2_sha256$600000$O9kulkijqEBYlOaSmZ0PbR$W1w1ZW1w86ZmWJBFYki79ERnq8nKmu1TwAfXhbakLIw=", "2024-08-21T11:54:47.000Z", False, "Veronica", "Veronica", "Muchiri", "vmuchiri@privatisation.go.ke", True, True, "2024-08-21T11:43:58.000Z"),
    ("pbkdf2_sha256$600000$yupxulUCfwVqheM1KaE2T1$s5ArlU8nN2hUpxgHtVS0NMZjDxHqLiv1H21mGKWRVP0=", None, True, "Bryan", "", "", "", True, True, "2024-08-21T12:04:24.000Z")
]

# Insert users
try:
    for user in users:
        cur.execute(insert_query, user)
    conn.commit()  # Save changes
    print("Users inserted successfully.")
except Exception as e:
    conn.rollback()  # Rollback in case of error
    print("Failed to insert users:", e)

# Close the connection
cur.close()
conn.close()
