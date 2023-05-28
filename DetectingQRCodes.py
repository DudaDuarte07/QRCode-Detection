import cv2
from pyzbar import pyzbar

# CONVERTE A IMAGEM PARA CINZA // TURNS THE IMAGE TO GRAY COLORS

def read_QRCode(frame):                        
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # DDETECTA O QRCODE // CODE DETECTING
    barcodes = pyzbar.decode(gray)

    # REFAZ OS QRCODES ENCONTRADOS // REDO THE QRCODE FOUND

    for barcode in barcodes:

        # EXTRAI SUAS COORDENADAS E DESENHA O RETANGULO AO REDOR DO CÓDIGO
        # GET THE POINTS AND DRAW A SQUARE AROUND EM THE QRCODE

        (x, y, w, h) = barcode.rect
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # DECODIFICAÇÃO // DECODING
        barcode_data = barcode.data.decode("utf-8")
        barcode_type = barcode.type

        # RESULTADO // RESULT
        cv2.putText(frame, f"{barcode_data} ({barcode_type})", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        # RETORNA O RESULTADO DO QRCODE // RETURN THE QRCODE RESULT
        return barcode_data

    # CASO NÃO SEJA ENCONTRADO QRCODE // IF NO QRCODE IS FOUND
    return None

# ABRE A CAMERA // OPEN THE CAMERA
capture = cv2.VideoCapture(0)

while True:

    # LEITURA DE FRAME // FRAME READER

    ret, frame = capture.read()
    QRCode_data = read_QRCode(frame)
    cv2.imshow("QR Code Reader", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()
