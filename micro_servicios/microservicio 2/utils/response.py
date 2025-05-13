


def response(success: bool, message: str, data: dict = None) -> dict:
    
    if(data!=None): return {
        "success": success,
        "message": message,
        "data": data
    }
    return {
        "success": success,
        "message": message
    }