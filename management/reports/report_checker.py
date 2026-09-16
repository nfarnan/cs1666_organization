import argparse
from dataclasses import dataclass
import tomllib

@dataclass
class Report:
	manager_username: str
	week: int
	commit_id: str
	team_members: dict[str, int]

	def __post_init__(self):
		if not isinstance(self.commit_id, str) or len(self.commit_id) != 40:
			raise ValueError(f"Invalid commit id: {self.commit_id}")

		if self.manager_username not in self.team_members:
			raise ValueError(f"Manager username {self.manager_username} not included in team_members list")

		if False in [ True if -2 <= score <= 2 else False for score in self.team_members.values() ]:
			raise ValueError(f"Invalid score given. Ensure all scores are between -2 and 2 (inclusive)")

def main():
	parser = argparse.ArgumentParser(description="sanity check a management week report YAML file")
	parser.add_argument("fname", help="file name to check")
	args = parser.parse_args()

	print("Checking...", end="", flush=True)

	try:
		try:
			fname_week = args.fname.split("_")[-3][2:]
			if len(fname_week) < 2:
				raise ValueError
			fname_week = int(fname_week)
		except Exception as e:
			raise ValueError("Could not parse week number from filename,\n\tbe sure the file name ends with 'wkXX_mgmt_report.toml',\n\tand use a 0 as the first digit for a week number under 10") from e

		with open(args.fname, "rb") as inf:
			report = tomllib.load(inf)
			report["week"] = fname_week
			report = Report(**report)

	except Exception as e:
		print("ERROR!\n")
		raise
	else:
		print("OK!")

if __name__ == "__main__":
	main()
