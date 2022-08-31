"""Unit tests for Lambda function"""
from index import handler

def test_handler():
    result = handler({}, {})
    assert 'status' in result
    assert result['status'] == 200
    assert 'message' in result
    assert result['message'] == 'OK'
