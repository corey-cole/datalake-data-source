"""Lambda function code"""
from typing import Any, Dict

def handler(event: Dict[str, Any], context: object) -> Dict[str, Any]:
    # If context isn't used, delete it
    del context
    return {
        'status': 200,
        'message': 'OK'
    }
