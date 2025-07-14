from flask import Flask
from ariadne import load_schema_from_path, make_executable_schema, graphql_sync
from ariadne.explorer import ExplorerGraphiQL
from flask import request, jsonify
from models import db
from resolvers import query, mutation
import psycopg2

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://andrew_music:Gamelol225@localhost:5432/music_app"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)
type_defs = load_schema_from_path("schema.graphql")
schema = make_executable_schema(type_defs, query, mutation)

@app.route("/graphql", methods=["GET"])
def graphql_playground():
    return ExplorerGraphiQL().html(None), 200

@app.route("/graphql", methods=["POST"])
def graphql_server():
    data = request.get_json()
    success, result = graphql_sync(
        schema,
        data,
        context_value={"request": request}
    )
    status_code = 200 if success else 400
    return jsonify(result), status_code

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)