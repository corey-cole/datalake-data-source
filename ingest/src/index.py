"""Lambda function code"""
from typing import Any, Dict

def handler(event: Dict[str, Any], context: object) -> Dict[str, Any]:
    return {
        'status': 200,
        'message': 'OK'
    }
