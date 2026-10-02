import argparse

parser = argparse.ArgumentParser(description="포트와 룰을 받습니다")
parser.add_argument("--port", type=int, default=5000, help="열어 둘 포트 번호")

parser.add_argument(
    "--rule",
    default="brute_force",
    help="보낼 룰 이름"
)

args = parser.parse_args()

print(f"포트 {args.port} · 룰 {args.rule}")
