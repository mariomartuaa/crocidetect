import sqlite3
import os

db_path = os.path.join("data", "predictions.db")

def init_db():
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute("""
    CREATE TABLE IF NOT EXISTS predictions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id TEXT,
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
        original_image BLOB,
        gradcam_image BLOB,
        predicted_class TEXT,
        confidence_table TEXT
    )
    """)
    conn.commit()
    conn.close()

def insert_prediction(user_id, original_image, gradcam_image, predicted_class, confidence_table):
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute("""
        INSERT INTO predictions (user_id, original_image, gradcam_image, predicted_class, confidence_table)
        VALUES (?, ?, ?, ?, ?)
    """, (user_id, original_image, gradcam_image, predicted_class, confidence_table))
    conn.commit()
    conn.close()

def get_predictions_by_user(user_id):
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute("""
        SELECT id, timestamp, original_image, gradcam_image, predicted_class, confidence_table
        FROM predictions WHERE user_id = ? ORDER BY timestamp DESC
    """, (user_id,))
    rows = c.fetchall()
    conn.close()
    return rows

def delete_prediction(prediction_id):
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute("DELETE FROM predictions WHERE id = ?", (prediction_id,))
    conn.commit()
    conn.close()

