from volumecalculator import parse_args, calculate_vol

if __name__ == '__main__':
    args = parse_args()
    print (calculate_vol(args.radius, args.height))