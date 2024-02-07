from flask import Flask, request, jsonify
app = Flask(__name__)

todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]

@app.route('/todos', methods=['GET'])
def hello_world():

    json_text = jsonify(todos)
    return json_text

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json

    todos.append(request_body)
    resp = jsonify(todos)
    resp.status_code = 200
    return resp

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    if position < len(todos):
        del todos[position]
        return jsonify(todos), 200
    else:
        return jsonify({"msg": "Position does not exist"}), 404


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)