import cv2
import easyocr
import numpy as np
import sys

# Initialize ocr reader in spanish.
reader = easyocr.Reader(['es'])

# Arrays for accepted names and IDs.
nombres = ["OCTAVIO SEBASTIÁN HERNÁNDEZ GALINDO", "GAEL CASTILLO ZEPEDA"]
matriculas = ["A01638638", "A01638993"]

# Function for image processing.
def procesado_imagen(nombre_archivo):
    imagen = cv2.imread(nombre_archivo)
    imagen_gray = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
    
    # Alpha is used for contrast, while beta is used for brightness
    imagen_con_contraste = cv2.convertScaleAbs(imagen_gray, 
                                               alpha=1.75, 
                                               beta=-300)
    
    cv2.imwrite(f"{nombre_archivo}_contraste.png", imagen_con_contraste)
    kernel= np.array([[-1,-1,-1],
                      [-1,9,-1],
                      [-1,-1,-1]])
    imagen_con_sharpness=cv2.filter2D(imagen_con_contraste,-1,kernel)
    cv2.imwrite(f"{nombre_archivo}_sharpening.png", imagen_con_sharpness)

    # Using easyocr to detect characters in images
    # If 'detail=0', then only the text is returned
    results=reader.readtext(imagen_con_sharpness, detail=0)
    detected_text = " ".join(results).upper()
    return detected_text


def main():
    if len(sys.argv)<2:
        print("Error trata usando: python script.py nombre_imagen.jpg")
        return
    archivo=sys.argv[1]
    resultado=procesado_imagen(archivo)
    
    # Filtrado por nombre y matricula
    matricula_aprobada=[matricula for matricula in matriculas if 
                        matricula in resultado]
    if matricula_aprobada:
        # Si se confirma que la matricula concuerda checas el nombre 
        # del alumno
        nombre_aprobado=[nombre for nombre in nombres if nombre in resultado]
        if nombre_aprobado:
            print(f"Entrada exitosa, Bienvenido: {nombre_aprobado[0]}")
        else:
            print("Entrada fallida, el nombre de la matricula no concuerda")
    else:
        print("Entrada fallida, la matricula no concuerda")

if __name__ == "__main__":
    main()