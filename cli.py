from hourly_timer import print_hourly_times
import argparse

def main():
    parser = argparse.ArgumentParser(description='Generate hourly time reports')
    parser.add_argument('--format', choices=['markdown', 'text'], default='markdown',
                       help='Output format (markdown or text)')
    args = parser.parse_args()
    
    print_hourly_times()

if __name__ == "__main__":
    main()