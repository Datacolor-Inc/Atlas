"""
Simple MCP Server Template

This is a minimal template for building a Model Context Protocol (MCP) server.
It demonstrates the basic structure and patterns for creating MCP tools that can
integrate with any external service or API.

This template shows:
- How to structure an MCP server
- How to create tools with proper documentation
- How to handle configuration
- How to implement error handling
- How to add logging

Replace the example tool with your own business logic and external service connections.
"""

import logging
from typing import Dict, Any
from mcp.server.fastmcp import FastMCP

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)

# Initialize FastMCP server
mcp = FastMCP("simple-mcp-server")

# Example configuration - Replace with your service configuration
SERVICE_CONFIG = {
    "api_url": "https://your-service-api.com",
    "username": "your_username",
    "api_key": "your_api_key",
    "timeout": 30
}


async def authenticate_service():
    """
    Example authentication function.
    Replace this with your actual service authentication logic.
    
    Returns:
        Dict[str, Any]: Authentication result or error information
    """
    try:
        # Simulate authentication logic
        # In real implementation, this would call your service's auth endpoint
        logger.info("Authenticating with external service...")
        
        # Example: Make API call to get token
        # response = requests.post(f"{SERVICE_CONFIG['api_url']}/auth", ...)
        
        # Simulated successful authentication
        return {
            "success": True,
            "token": "simulated_auth_token_12345",
            "expires_in": 3600
        }
        
    except Exception as e:
        logger.error(f"Authentication failed: {e}")
        return {
            "success": False,
            "error": str(e)
        }


@mcp.tool()
async def search_resources(query: str, limit: int = 10) -> Dict[str, Any]:
    """
    Example tool that demonstrates how to search for resources in an external service.
    
    This is a template tool that shows the proper structure for MCP tools.
    Replace this with your actual business logic and external service calls.

    Args:
        query (str): The search query to find resources
        limit (int): Maximum number of results to return (default: 10)
        
    Returns:
        Dict[str, Any]: Search results or error information
    """
    try:
        logger.info(f"Searching for resources with query: '{query}', limit: {limit}")
        
        # Step 1: Authenticate with the service (if needed)
        auth_result = await authenticate_service()
        if not auth_result.get("success"):
            return {
                "error": f"Authentication failed: {auth_result.get('error', 'Unknown error')}"
            }
        
        # Step 2: Validate input parameters
        if not query or not query.strip():
            return {
                "error": "Query parameter cannot be empty"
            }
        
        if limit <= 0 or limit > 100:
            return {
                "error": "Limit must be between 1 and 100"
            }
        
        # Step 3: Make API call to external service
        # In a real implementation, this would be something like:
        # headers = {"Authorization": f"Bearer {auth_result['token']}"}
        # response = requests.get(f"{SERVICE_CONFIG['api_url']}/search", 
        #                        params={"q": query, "limit": limit}, 
        #                        headers=headers)
        
        # Step 4: Simulate service response (replace with actual API call)
        simulated_results = [
            {
                "id": f"resource_{i}",
                "name": f"Example Resource {i}",
                "description": f"This is a sample resource matching '{query}'",
                "type": "document" if i % 2 == 0 else "dataset",
                "created_date": "2024-01-15",
                "owner": f"user_{i}@example.com",
                "tags": ["example", "template", query.lower()],
                "url": f"https://your-service.com/resource_{i}"
            }
            for i in range(1, min(limit + 1, 6))  # Return up to 5 sample results
        ]
        
        # Step 5: Process and format the results
        result = {
            "success": True,
            "query": query,
            "total_found": len(simulated_results),
            "limit": limit,
            "resources": simulated_results,
            "metadata": {
                "search_time_ms": 142,
                "service": "Example Service API v1.0",
                "timestamp": "2024-08-25T10:30:00Z"
            }
        }
        
        logger.info(f"Search completed successfully. Found {len(simulated_results)} resources.")
        return result
        
    except Exception as e:
        logger.error(f"Search failed with error: {e}")
        return {
            "success": False,
            "error": f"Search operation failed: {str(e)}",
            "query": query
        }


@mcp.prompt()
def get_system_prompt() -> Dict[str, str]:
    """
    System prompt that provides instructions for using this MCP server.
    
    Returns:
        Dict[str, str]: The system prompt configuration
    """
    return {
        "role": "assistant",
        "content": """# Simple MCP Server Instructions

## Overview
This MCP server demonstrates how to integrate with external services and APIs.
It provides a template for building your own MCP tools.

## Available Tool

### search_resources(query, limit=10)
Search for resources in the external service.

**Parameters:**
- `query` (str): Search term or phrase
- `limit` (int): Maximum results to return (1-100, default: 10)

**Returns:**
- List of matching resources with metadata
- Each resource includes: id, name, description, type, owner, tags, URL

**Example Usage:**
```
search_resources("data governance")
search_resources("sales reports", limit=5)
```

## Response Format
Results are returned as structured data with:
- `success`: Boolean indicating if the operation succeeded
- `resources`: Array of matching resources
- `metadata`: Additional information about the search
- `error`: Error message if operation failed

## Integration Pattern
This server demonstrates the standard pattern for MCP service integration:

1. **Authentication**: Authenticate with the external service
2. **Validation**: Validate input parameters
3. **API Call**: Make requests to the external service
4. **Processing**: Format and structure the response
5. **Error Handling**: Handle and report errors gracefully

## Customization
To adapt this template for your service:

1. Update `SERVICE_CONFIG` with your service details
2. Modify `authenticate_service()` with your auth logic
3. Replace the simulated API call in `search_resources()` with real service calls
4. Add additional tools as needed using the `@mcp.tool()` decorator
5. Update this prompt with your specific instructions

## Error Handling
All tools include comprehensive error handling and return structured error information when operations fail.
"""
    }


if __name__ == "__main__":
    logger.info("Simple MCP server starting...")
    print("🚀 Simple MCP Server Template")
    print("This is a demonstration of MCP server structure")
    print("Replace the example tool with your actual service integration")
    mcp.run(transport='stdio')