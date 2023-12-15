from uvicorn import run

from app.app import app


# "192.168.1.119"
def main():
    run(app, host="192.168.1.107", port=80)


if __name__ == "__main__":
    main()

# {
# "pyres":[{"item":["EC",777]},{"item":["TDS",666]}],
# "query_key":"1"
# }
