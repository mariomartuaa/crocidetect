import os
import json
from supabase import create_client, Client
import streamlit as st

SUPABASE_URL = st.secrets["SUPABASE_URL"]
SUPABASE_KEY = st.secrets["SUPABASE_KEY"]
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

STORAGE_BUCKET = "crocidetect"

def upload_image_to_storage(file_bytes, filename, folder):
    path = f"{folder}/{filename}"

    try:
        supabase.storage.from_(STORAGE_BUCKET).remove([path])
    except Exception:
        pass
        
    supabase.storage.from_(STORAGE_BUCKET).upload(path, file_bytes, {"content-type": "image/png"})

    public_url = f"{SUPABASE_URL}/storage/v1/object/public/{STORAGE_BUCKET}/{path}"
    return public_url


def insert_prediction(user_id, original_img_url, gradcam_img_url, predicted_class, confidence_table):
    data = {
        "user_id": user_id,
        "original_image": original_img_url,
        "gradcam_image": gradcam_img_url,
        "predicted_class": predicted_class,
        "confidence_table": json.dumps(confidence_table)
    }
    supabase.table("predictions").insert(data).execute()

def get_predictions_by_user(user_id):
    response = supabase.table("predictions") \
        .select("*") \
        .eq("user_id", user_id) \
        .order("timestamp", desc=True) \
        .execute()
    return response.data

def delete_prediction(prediction_id):
    response = supabase.table("predictions") \
        .select("original_image, gradcam_image") \
        .eq("id", prediction_id) \
        .single() \
        .execute()
    
    if response.data:
        def extract_path_from_url(url):
            return "/".join(url.split("/")[-2:])
        
        original_url = response.data["original_image"]
        gradcam_url = response.data["gradcam_image"]

        try:
            path1 = extract_path_from_url(original_url)
            path2 = extract_path_from_url(gradcam_url)
            supabase.storage.from_(STORAGE_BUCKET).remove([path1])
            supabase.storage.from_(STORAGE_BUCKET).remove([path2])
            
            print(original_url)
            print(path1)
            
        except Exception as e:
            print("Gagal menghapus gambar dari storage:", e)

    supabase.table("predictions").delete().eq("id", prediction_id).execute()
