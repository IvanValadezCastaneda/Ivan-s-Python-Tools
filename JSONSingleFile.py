import psycopg2
import json

# Establish a connection to the PostgreSQL database
conn = psycopg2.connect(
    host="your_host",
    port="your_port",
    database="your_database",
    user="your_username",
    password="your_password"
)

# Create a cursor object to interact with the database
cursor = conn.cursor()

# Define the JSON payload
json_payload = {
  "dispositivo": "Device123",
  "estacion": "StationXYZ",
  "fecha": "2023-05-17T10:15:00",
  "tipo": 1,
  "evento": "EventABC"
}

# Convert the JSON payload to a string
json_string = json.dumps(json_payload)

# Execute the INSERT statement to insert the JSON payload into the table
cursor.execute("INSERT INTO public.para_scada1 (dispositivo, estacion, fecha, tipo, evento) VALUES (%s, %s, %s, %s, %s)",
               (json_string['dispositivo'], json_string['estacion'], json_string['fecha'], json_string['tipo'], json_string['evento']))

# Commit the transaction
conn.commit()

# Close the cursor and the connection
cursor.close()
conn.close()
