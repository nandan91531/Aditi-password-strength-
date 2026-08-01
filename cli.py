import sys
import argparse
import getpass
from checker.strength_evaluator import PasswordEvaluator
from checker.generator import PasswordGenerator

# ANSI Terminal Colors
COLOR_RESET = "\033[0m"
COLOR_BOLD = "\033[1m"
COLOR_CYAN = "\033[36m"
COLOR_GREEN = "\033[32m"
COLOR_YELLOW = "\033[33m"
COLOR_RED = "\033[31m"
COLOR_BLUE = "\033[34m"

def print_banner():
    banner = f"""
{COLOR_CYAN}{COLOR_BOLD}====================================================
     ADITI PASS CHECKER - EVALUATOR & GENERATOR 💖
===================================================={COLOR_RESET}
    """
    print(banner)

def print_evaluation(result: dict, password: str):
    score = result["score"]
    label = result["label"]
    crack_time = result["crack_time"]
    metrics = result["metrics"]

    # Choose badge color based on score
    if score >= 90:
        badge_color = COLOR_CYAN
    elif score >= 75:
        badge_color = COLOR_GREEN
    elif score >= 55:
        badge_color = COLOR_YELLOW
    else:
        badge_color = COLOR_RED

    print(f"\n{COLOR_BOLD}--- Evaluation Results ---{COLOR_RESET}")
    print(f"Overall Rating    : {badge_color}{COLOR_BOLD}{label}{COLOR_RESET} ({score}/100)")
    print(f"Est. Crack Time   : {COLOR_BOLD}{crack_time}{COLOR_RESET}")

    print(f"\n{COLOR_BOLD}Character Breakdown:{COLOR_RESET}")
    print(f"  * Length            : {metrics['length']['count']} chars [{COLOR_GREEN + 'OK' + COLOR_RESET if metrics['length']['status'] else COLOR_RED + 'X' + COLOR_RESET}]")
    print(f"  * Uppercase Letters : {metrics['uppercase']['count']} chars [{COLOR_GREEN + 'OK' + COLOR_RESET if metrics['uppercase']['status'] else COLOR_RED + 'X' + COLOR_RESET}]")
    print(f"  * Lowercase Letters : {metrics['lowercase']['count']} chars [{COLOR_GREEN + 'OK' + COLOR_RESET if metrics['lowercase']['status'] else COLOR_RED + 'X' + COLOR_RESET}]")
    print(f"  * Digits            : {metrics['digits']['count']} chars [{COLOR_GREEN + 'OK' + COLOR_RESET if metrics['digits']['status'] else COLOR_RED + 'X' + COLOR_RESET}]")
    print(f"  * Special Symbols   : {metrics['special']['count']} chars [{COLOR_GREEN + 'OK' + COLOR_RESET if metrics['special']['status'] else COLOR_RED + 'X' + COLOR_RESET}]")

    if result.get("has_patterns"):
        print(f"\n{COLOR_RED}{COLOR_BOLD}Pattern Warnings:{COLOR_RESET}")
        for warn in result["pattern_details"]:
            print(f"  ! {warn}")

    print(f"\n{COLOR_BOLD}Recommendations & Tips:{COLOR_RESET}")
    for tip in result["feedback"]:
        print(f"  -> {tip}")
    print("\n")

def interactive_mode():
    print_banner()
    while True:
        print(f"{COLOR_BOLD}Select an option:{COLOR_RESET}")
        print(" [1] Check password strength")
        print(" [2] Generate a strong password")
        print(" [3] Exit")
        choice = input(f"{COLOR_CYAN}> {COLOR_RESET}").strip()

        if choice == '1':
            pw = getpass.getpass("Enter password to evaluate (hidden): ").strip()
            if not pw:
                pw = input("Enter password (visible): ").strip()
            if pw:
                res = PasswordEvaluator.evaluate(pw)
                print_evaluation(res, pw)
        elif choice == '2':
            try:
                length_str = input("Enter password length (default 16): ").strip()
                length = int(length_str) if length_str else 16
            except ValueError:
                length = 16
            gen_pw = PasswordGenerator.generate(length=length)
            print(f"\n{COLOR_GREEN}{COLOR_BOLD}Generated Password:{COLOR_RESET} {gen_pw}")
            res = PasswordEvaluator.evaluate(gen_pw)
            print(f"Strength Rating: {COLOR_CYAN}{res['label']}{COLOR_RESET} ({res['score']}/100)\n")
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose 1, 2, or 3.\n")

def main():
    parser = argparse.ArgumentParser(description="Password Strength Evaluator & Secure Generator")
    parser.add_argument("-p", "--password", type=str, help="Password string to evaluate")
    parser.add_argument("-g", "--generate", action="store_true", help="Generate a strong password")
    parser.add_argument("-l", "--length", type=int, default=16, help="Length of generated password (default: 16)")

    args = parser.parse_args()

    if args.generate:
        print_banner()
        gen_pw = PasswordGenerator.generate(length=args.length)
        print(f"{COLOR_GREEN}{COLOR_BOLD}Generated Password:{COLOR_RESET} {gen_pw}")
        res = PasswordEvaluator.evaluate(gen_pw)
        print_evaluation(res, gen_pw)
    elif args.password:
        print_banner()
        res = PasswordEvaluator.evaluate(args.password)
        print_evaluation(res, args.password)
    else:
        interactive_mode()

if __name__ == "__main__":
    main()
