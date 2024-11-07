from flask import jsonify

# Task 6: Error Handling - Implement appropriate error handling mechanisms

def register_error_handlers(app):
    # Handle 400 Bad Request errors (invalid data)
    @app.errorhandler(400)
    def handle_invalid_data(error):
        response = jsonify({"error": "Invalid data", "message": error.description or "The input data is invalid."})
        response.status_code = 400
        return response

    # Handle 404 Not Found errors (resource not found)
    @app.errorhandler(404)
    def handle_not_found(error):
        response = jsonify({"error": "Not found", "message": error.description or "The requested resource was not found."})
        response.status_code = 404
        return response

    # Handle all other exceptions (generic server errors)
    @app.errorhandler(Exception)
    def handle_generic_error(error):
        response = jsonify({"error": "Internal Server Error", "message": "An unexpected error occurred."})
        response.status_code = 500
        return response
