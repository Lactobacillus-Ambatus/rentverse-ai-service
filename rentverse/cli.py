import uvicorn


def dev():
    """Run the development server with hot reload."""
    uvicorn.run(
        "rentverse.main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )


def start():
    """Run the production server."""
    uvicorn.run(
        "rentverse.main:app",
        host="0.0.0.0",
        port=8000,
        log_level="info"
    )


if __name__ == "__main__":
    dev()
