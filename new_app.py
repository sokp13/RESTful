from crypt import methods
from flask import Flask,jsonify, request
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)

SWAGGER_URL="/swagger"
API_URL="/static/swagger.json"

swagger_ui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': 'Access API'
    }
)
app.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URL)

methods = []

@app.route("/",methods=["GET"])
def home():
    return jsonify({
        "Message": "app up and running successfully"
    })

@app.route("/access",methods=["POST"])
def access():
    data = request.get_json()
    name = data.get("name", "dipto")
    server = data.get("server","server1")

    message = f"User {name} received access to server {server}"

    return jsonify({
        "Message": message
    })

@app.route("/access/<string:name>/<string:server>", methods=["PUT"])
def put(name, server):
    data = request.get_json()

    if not name or not server:
        return jsonify({"error": "Missing attributes"}), 400

    for access in methods:
        if access["name"] == name and access["server"] == server:
            access.update(data)
            u_access = access 
            break 
    else:
        return jsonify({"error": "Access not found"}), 404

    message = f"Access for '{name}' on '{server}' updated successfully"
           
    return jsonify({"message": message, "access": u_access})

@app.route("/delete/<string:name>/<string:server>", methods=["DELETE"])
def revoke(name, server):

    for access in methods:
        if access["name"] == name and access["server"] == server:
            methods.remove(access)
            return jsonify({
                "message": f"Access for {name} on {server} revoked"  
            })

    return jsonify({"error": "Access not found"}), 404

if __name__=="__main__":
    app.run(debug=True,host="0.0.0.0",port=8080)
