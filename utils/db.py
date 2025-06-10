import os
import json
from supabase import create_client, Client

# Supabase Credentials
SUPABASE_URL = "https://xxzegimecgqwmcuchvaz.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6Inh4emVnaW1lY2dxd21jdWNodmF6Iiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc0OTM4ODAwNSwiZXhwIjoyMDY0OTY0MDA1fQ.6E7rGQ7fi7zNJJcf1dBKSbjq0SBpmjFPHfZPgb_GEi8"
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

STORAGE_BUCKET = "crocidetect"
DATABASE_TABLE = "predictions"

def upload_image_to_storage(file_bytes, filename, folder):
    path = f"{folder}/{filename}"
    bucket = supabase.storage.from_(STORAGE_BUCKET)

    # Hapus file jika sudah ada
    try:
        bucket.remove([path])
    except Exception:
        pass  # Abaikan jika file tidak ada

    # Upload ulang file
    bucket.upload(path, file_bytes, {"content-type": "image/png"})

    # Bangun URL publik
    return f"{SUPABASE_URL}/storage/v1/object/public/{STORAGE_BUCKET}/{path}"



def insert_prediction(user_id, original_img_url, gradcam_img_url, predicted_class, confidence_table):
    data = {
        "user_id": user_id,
        "original_image": original_img_url,
        "gradcam_image": gradcam_img_url,
        "predicted_class": predicted_class,
        "confidence_table": json.dumps(confidence_table)
    }
    supabase.table(DATABASE_TABLE).insert(data).execute()

def get_predictions_by_user(user_id):
    response = (
        supabase.table(DATABASE_TABLE)
        .select("*")
        .eq("user_id", user_id)
        .order("timestamp", desc=True)
        .execute()
    )
    return response.data

def delete_prediction(prediction_id):
    # Ambil data prediksi berdasarkan ID
    response = (
        supabase.table(DATABASE_TABLE)
        .select("original_image, gradcam_image")
        .eq("id", prediction_id)
        .single()
        .execute()
    )
    
    if response.data:
        def extract_path_from_url(url):
            return "/".join(url.split("/")[-2:])
        
        original_url = response.data["original_image"]
        gradcam_url = response.data["gradcam_image"]

        path1 = extract_path_from_url(original_url)
        path2 = extract_path_from_url(gradcam_url)
        supabase.storage.from_(STORAGE_BUCKET).remove([path1])
        supabase.storage.from_(STORAGE_BUCKET).remove([path2])

    # Hapus record dari database
    supabase.table(DATABASE_TABLE).delete().eq("id", prediction_id).execute()
