# MCP Server

A minimal, clean template for building Model Context Protocol (MCP) servers that integrate with external services. This template demonstrates the core patterns and structure without the complexity of actual service connections.

## 🎯 Purpose

This template shows:
- **MCP Server Structure**: How to organize an MCP server
- **Tool Creation**: How to build MCP tools with proper documentation
- **Integration Pattern**: Standard approach for external service integration
- **Error Handling**: Robust error handling and logging
- **Configuration**: How to manage service configuration

## 📁 What's Included

- **`mcp_server.py`** - Complete MCP server with one example tool
- **Example authentication flow** (simulated)
- **Proper error handling and validation**
- **Structured logging**
- **Clear documentation and comments**

## 🚀 Quick Start

### Prerequisites
```bash
pip install fastmcp
```

### Running the Server
```bash
python mcp_server.py
```

## 🔧 Customization

### 1. Update Configuration
Replace the example configuration with your service details:

```python
SERVICE_CONFIG = {
    "api_url": "https://your-actual-service.com/api",
    "username": "your_username",
    "api_key": "your_api_key",
    "timeout": 30
}
```

### 2. Implement Authentication
Replace the simulated authentication with your actual auth logic:

```python
async def authenticate_service():
    try:
        # Replace with actual API call
        response = requests.post(f"{SERVICE_CONFIG['api_url']}/auth", {
            "username": SERVICE_CONFIG["username"],
            "api_key": SERVICE_CONFIG["api_key"]
        })
        
        if response.status_code == 200:
            return {
                "success": True,
                "token": response.json()["access_token"]
            }
        else:
            return {"success": False, "error": "Auth failed"}
            
    except Exception as e:
        return {"success": False, "error": str(e)}
```

### 3. Replace the Example Tool
Modify `search_resources()` or create new tools for your use case:

```python
@mcp.tool()
async def your_custom_tool(param1: str, param2: int = 10) -> Dict[str, Any]:
    """
    Your custom tool description.
    
    Args:
        param1 (str): Description of parameter
        param2 (int): Description with default value
        
    Returns:
        Dict[str, Any]: Description of return value
    """
    try:
        # Your implementation here
        # 1. Authenticate if needed
        # 2. Validate parameters
        # 3. Make API calls
        # 4. Process results
        # 5. Return structured response
        
        return {"success": True, "data": "your_results"}
        
    except Exception as e:
        return {"error": str(e)}
```

### 4. Add Multiple Tools
You can add as many tools as needed:

```python
@mcp.tool()
async def create_resource(name: str, data: Dict[str, Any]) -> Dict[str, Any]:
    """Create a new resource."""
    # Implementation here
    pass

@mcp.tool()
async def update_resource(resource_id: str, updates: Dict[str, Any]) -> Dict[str, Any]:
    """Update an existing resource."""
    # Implementation here
    pass

@mcp.tool()
async def delete_resource(resource_id: str) -> Dict[str, Any]:
    """Delete a resource."""
    # Implementation here
    pass
```

## 🏗️ Integration Examples

### REST API Integration
```python
import requests

async def call_api(endpoint: str, method: str = "GET", data: Dict = None):
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.request(
        method, 
        f"{SERVICE_CONFIG['api_url']}{endpoint}",
        headers=headers,
        json=data
    )
    return response.json()
```

### Database Integration
```python
import asyncpg

async def query_database(query: str, params: list = None):
    conn = await asyncpg.connect(DATABASE_URL)
    try:
        result = await conn.fetch(query, *params if params else [])
        return [dict(row) for row in result]
    finally:
        await conn.close()
```

### GraphQL Integration
```python
import httpx

async def graphql_query(query: str, variables: Dict = None):
    async with httpx.AsyncClient() as client:
        response = await client.post(
            f"{SERVICE_CONFIG['api_url']}/graphql",
            json={"query": query, "variables": variables},
            headers={"Authorization": f"Bearer {token}"}
        )
        return response.json()
```

## 📋 Best Practices

### Error Handling
```python
try:
    # Your operation
    result = await external_service_call()
    return {"success": True, "data": result}
except ServiceAuthError:
    return {"error": "Authentication failed"}
except ServiceTimeoutError:
    return {"error": "Service timeout"}
except Exception as e:
    logger.error(f"Unexpected error: {e}")
    return {"error": "Internal server error"}
```

### Input Validation
```python
if not query or not query.strip():
    return {"error": "Query parameter is required"}

if limit <= 0 or limit > 1000:
    return {"error": "Limit must be between 1 and 1000"}

# Validate format
import re
if not re.match(r'^[a-zA-Z0-9\s]+$', query):
    return {"error": "Invalid query format"}
```

### Logging
```python
import logging

logger = logging.getLogger(__name__)

# Log important operations
logger.info(f"Processing request: {operation}")
logger.warning(f"Rate limit approaching: {current_usage}")
logger.error(f"Operation failed: {error_details}")
```

## 🧪 Testing Your Implementation

### Basic Test
```python
import asyncio

async def test_tool():
    result = await search_resources("test query", limit=5)
    print(f"Result: {result}")

if __name__ == "__main__":
    asyncio.run(test_tool())
```

### Integration Test
```python
async def test_integration():
    # Test authentication
    auth = await authenticate_service()
    assert auth["success"], f"Auth failed: {auth.get('error')}"
    
    # Test tool
    result = await search_resources("integration test")
    assert "error" not in result, f"Tool failed: {result.get('error')}"
    
    print("All tests passed!")
```

## 🔒 Security Considerations

- Store credentials securely (environment variables, key vault)
- Validate all input parameters
- Use HTTPS for all external communications
- Implement rate limiting if needed
- Log security events appropriately
- Handle sensitive data carefully

## 📚 Next Steps

1. **Copy this template** to start your project
2. **Update configuration** with your service details
3. **Implement authentication** for your specific service
4. **Replace example tool** with your business logic
5. **Add error handling** specific to your service
6. **Test thoroughly** with real data
7. **Add logging** for monitoring and debugging

This template provides a solid foundation for any MCP server integration. Focus on your business logic while following the established patterns for reliability and maintainability.