#****************************** Code détection par caméra ***************************************** (décommenter si vous voulez tester avec la caméra  )
# from ultralytics import YOLO
# import cv2

# # Charger le modèle entraîné
# model = YOLO("C:/Users/lenovo/Desktop/resultat_modeleyolo/best.pt")  # changer le chemin si necessaire 


# # Ouvrir la caméra (0 = caméra par défaut)
# cap = cv2.VideoCapture(0)

# if not cap.isOpened():
#     print("❌ Impossible d'ouvrir la caméra.")
#     exit()

# while True:
#     ret, frame = cap.read()
#     if not ret:
#         print("❌ Impossible de lire la frame.")
#         break

#     # Détection avec le modèle
#     results = model.predict(source=frame, show=False, conf=0.3)

#     # Affichage avec boxes, labels etc.
#     annotated_frame = results[0].plot()

#     cv2.imshow("Détection en direct", annotated_frame)

#     # Appuyer sur 'q' pour quitter
#     if cv2.waitKey(1) & 0xFF == ord("q"):
#         break

# cap.release()
# cv2.destroyAllWindows()


#****************************** Code détection par vidéo *****************************************
import cv2
from ultralytics import YOLO
import os

# === 1. Charger le modèle YOLOv8 ===
model = YOLO("C:/Users/lenovo/Desktop/resultat_modeleyolo/best.pt")  # changer le chemin si necessaire 
# === 2. Charger la vidéo locale ===
video_path = "C:/Users/lenovo/Desktop/Forest_fires.mp4"   # changer le chemin si necessaire 
cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("❌ Erreur : Impossible de lire la vidéo.")
    exit()

# === 3. Configurer la sauvegarde de la vidéo avec détection ===
fps = cap.get(cv2.CAP_PROP_FPS)
width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter("video_detected.mp4", fourcc, fps, (width, height))

print("🚀 Traitement de la vidéo... Appuie sur Q pour quitter.")

# === 4. Traitement frame par frame ===
while True:
    ret, frame = cap.read()
    if not ret:
        break

    results = model.predict(source=frame, conf=0.5, save=False, verbose=False)
    annotated_frame = results[0].plot()

    cv2.imshow("YOLOv8 - Détection", annotated_frame)
    out.write(annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# === 5. Libération des ressources ===
cap.release()
out.release()
cv2.destroyAllWindows()
print("✅ Détection terminée. Résultat sauvegardé : video_detected.mp4")


