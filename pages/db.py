import firebase_admin
from firebase_admin import credentials, firestore
import datetime
import base64
import io
import uuid

# Inisialisasi Firebase hanya sekali
if not firebase_admin._apps:
    cred = credentials.Certificate("firebase_key.json")
    firebase_admin.initialize_app(cred)

db = firestore.client()

# Firestore tidak perlu init_db, jadi fungsi ini dikosongkan
def init_db():
    pass

# Simpan prediksi
def insert_prediction(user_id, original_image, gradcam_image, predicted_class, confidence_table):
    # Encode gambar jadi base64 string
    orig_img_b64 = base64.b64encode(original_image).decode("utf-8")
    gradcam_img_b64 = base64.b64encode(gradcam_image).decode("utf-8")

    doc_id = str(uuid.uuid4())
    doc_ref = db.collection("predictions").document(doc_id)
    doc_ref.set({
        "user_id": user_id,
        "timestamp": firestore.SERVER_TIMESTAMP,
        "original_image": orig_img_b64,
        "gradcam_image": gradcam_img_b64,
        "predicted_class": predicted_class,
        "confidence_table": confidence_table
    })

# Ambil prediksi berdasarkan user_id
def get_predictions_by_user(user_id):
    docs = db.collection("predictions") \
             .where("user_id", "==", user_id) \
             .order_by("timestamp", direction=firestore.Query.DESCENDING) \
             .stream()

    records = []
    for doc in docs:
        data = doc.to_dict()
        records.append((
            doc.id,
            data.get("timestamp"),
            base64.b64decode(data.get("original_image")),
            base64.b64decode(data.get("gradcam_image")),
            data.get("predicted_class"),
            data.get("confidence_table")
        ))
    return records

# Hapus dokumen berdasarkan ID
def delete_prediction(prediction_id):
    db.collection("predictions").document(prediction_id).delete()
