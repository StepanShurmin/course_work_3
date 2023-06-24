from src.functions import load_data, get_last_executed_operations, print_transactions


def main():
    data = load_data()
    transactions_sorted = get_last_executed_operations(data)
    print_transactions(transactions_sorted)


if __name__ == "__main__":
    main()
