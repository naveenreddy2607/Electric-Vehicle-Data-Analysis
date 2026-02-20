def greet(name):
    """
    A basic function that returns a greeting message.
    
    Args:
        name (str): The name to greet
        
    Returns:
        str: A greeting message
    """
    response = f"Hello, {name}! Welcome to the Electric Vehicle Data Analysis project."
    return response


def get_status():
    """
    A basic function that returns the status of the application.
    
    Returns:
        dict: Status information
    """
    return {
        "status": "running",
        "message": "Application is working correctly",
        "code": 200
    }


if __name__ == "__main__":
    # Test the greet function
    print(greet("User"))
    
    # Test the get_status function
    status = get_status()
    print(f"\nStatus: {status}")
