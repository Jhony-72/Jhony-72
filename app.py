from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route("/", methods=["GET"])
def inicio():
    return "Servidor del Bot de Likes de WhatsApp Activo"

@app.route("/api/whatsapp", methods=["POST"])
def recibir_mensaje():
    data = request.get_json()
    
    try:
        # El código lee el mensaje que entra desde Green-API en WhatsApp
        if data.get("typeWebhook") == "incomingMessageReceived":
            message_data = data.get("messageData", {})
            
            if message_data.get("typeMessage") == "textMessage":
                texto = message_data.get("textMessageData", {}).get("textMessage", "").strip()
                
                # Detecta si el usuario escribió el comando: /like 3091263541
                if texto.startswith("/like"):
                    partes = texto.split(" ")
                    if len(partes) >= 2:
                        player_id = partes[1]
                        
                        # Verifica que el ID de Free Fire sean solo números
                        if player_id.isdigit():
                            
                            # ========================================================
                            # AQUÍ VA TU LÓGICA MÁGICA PARA DAR LOS LIKES REALES.
                            # Por ahora, el bot le responderá al usuario en WhatsApp:
                            # ========================================================
                            mensaje_respuesta = f"✅ ¡Petición recibida! Enviando likes gratis al ID de Free Fire: {player_id}. Por favor, espera unos minutos en el juego."
                            
                            return jsonify({
                                "reply": mensaje_respuesta
                            }), 200
                        else:
                            return jsonify({"reply": "⚠️ El ID de Free Fire debe contener solo números."}), 200
                    else:
                        return jsonify({"reply": "💡 Modo de uso correcto: /like [Tu_ID]\nEjemplo: /like 3091263541"}), 200
                        
    except Exception as e:
        print(f"Error procesando el mensaje de WhatsApp: {e}")
        
    return jsonify({"status": "ignored"}), 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
