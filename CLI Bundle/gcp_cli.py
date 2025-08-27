import argparse
from phases import phase1, phase6, full_run
from utils import audit_utils, prompt_utils

def main():
    parser = argparse.ArgumentParser(description="Genesis Recursive Code Protocol CLI")
    parser.add_argument("command", help="Command to run", choices=["init", "run", "full-run", "prompt", "audit", "export", "help"])
    parser.add_argument("--phase", type=int, help="Specify phase to run")
    parser.add_argument("--version", type=str, help="Protocol version")
    parser.add_argument("--prompt", type=str, help="Your invention idea")
    
    args = parser.parse_args()

    if args.command == "init":
        print("📁 GCP session initialized.")
    elif args.command == "run" and args.phase:
        print(f"🚀 Running Phase {args.phase}")
        if args.phase == 1:
            phase1.run()
        elif args.phase == 6:
            phase6.run()
        else:
            print("⚠️ Phase not implemented yet.")
    elif args.command == "full-run":
        full_run.run_all()
    elif args.command == "prompt" and args.prompt:
        prompt_utils.run_prompt(args.prompt)
    elif args.command == "audit" and args.prompt and args.version:
        audit_utils.run_audit(args.prompt, args.version)
    elif args.command == "export":
        print("📄 Exporting session...")
    elif args.command == "help":
        parser.print_help()
    else:
        print("❗Invalid usage. Try `gcp help`")

if __name__ == "__main__":
    main()
