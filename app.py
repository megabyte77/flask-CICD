from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/devops', methods=['GET'])
def devops_info():
    return jsonify({
        "message": "Welcome to the DevOps API!",
        "tools": ["Docker", "Kubernetes", "Terraform", "Jenkins", "Ansible"],
        "status": "running"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
