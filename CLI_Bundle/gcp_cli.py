import argparse

def main():
    parser = argparse.ArgumentParser(description="Genesis Recursive Code Protocol CLI")
    parser.add_argument("command", help="Command to run", choices=["init", "run", "full-run", "prompt", "audit", "export", "help"])
    parser.add_argument("--phase", type=int, help="Specify phase to run")
    parser.add_argument("--file", type=str, help="File to audit")
    parser.add_argument("--prompt", type=str, help="Your invention idea")
    
    args = parser.parse_args()

    if args.command == "init":
        print("📁 GCP session initialized.")
    elif args.command == "run" and args.phase:
        print(f"🚀 Running Phase {args.phase}")
        if args.phase == 1:
            from . import phase1
            phase1.main()
        elif args.phase == 6:
            from . import phase6
            phase6.main()
        else:
            print("⚠️ Phase not implemented yet.")
    elif args.command == "full-run":
        from . import full_run
        full_run.execute_full_run(args.prompt or "", "", "")
    elif args.command == "prompt" and args.prompt:
        from . import prompt_utils
        try:
            prompt_utils.run_prompt(args.prompt)
        except AttributeError:
            print("⚠️ Prompt utility not fully implemented.")
    elif args.command == "audit" and args.file:
        from . import audit_utils
        audit_utils.run_audit(args.file)
    elif args.command == "export":
        print("📄 Exporting session...")
    elif args.command == "help":
        parser.print_help()
    else:
        print("❗Invalid usage. Try `gcp help`")

if __name__ == "__main__":
    main()
