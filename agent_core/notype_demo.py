import argparse

parser = argparse.ArgumentParser()

parser.add_argument("--port", default="5000")

args = parser.parse_args()

print(args.port + "1")
