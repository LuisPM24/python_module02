def input_temperature(temp_str: str) -> int:
    return (int(temp_str))


def test_temperature() -> None:
    print("=== Garden Temperature ===\n")
    print("Input data is '25'")
    try:
        num1 = input_temperature('25')
        print(f"Temperature is now {num1}°C")
    except ValueError as e:
        print("Caught input_temperature error:", e)
    print("\nInput data is 'abc'")
    try:
        num1 = input_temperature('abc')
        print(f"Temperature is now {num1}°C")
    except ValueError as e:
        print("Caught input_temperature error:", e)
    print("\nAll tests completed - program didn't crash!")


def main() -> None:
    test_temperature()


if __name__ == "__main__":
    main()
